import os
import requests
import json
from datetime import datetime
import argparse
from dotenv import load_dotenv
from base64 import b64decode, b64encode

# Argument parser for checking the --test-local flag
parser = argparse.ArgumentParser(description="Update the Hall of Fame")
parser.add_argument('--test-local', action='store_true', help="Output Hall of Fame to TEST_README.md instead of updating GitHub")
args = parser.parse_args()

# Load environment variables from .env file if --test-local is specified
if args.test_local:
    load_dotenv()

# Environment variables for API keys, tokens, etc.
HACKERONE_API_USERNAME = os.getenv("HACKERONE_API_USERNAME")
HACKERONE_API_KEY = os.getenv("HACKERONE_API_KEY")
GITHUB_TOKEN = os.getenv("X_GITHUB_TOKEN")
GITHUB_REPO = os.getenv("X_GITHUB_REPOSITORY")  # format: "username/repo"

# Headers for GitHub and HackerOne API requests
HACKERONE_HEADERS = {
    'Accept': 'application/json'
}

GITHUB_HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

# HackerOne API endpoint for reports data
HACKERONE_API_URL = "https://api.hackerone.com/v1/reports"

# Dictionary to correctly map months to their respective numbers for sorting
MONTH_ORDER = {
    "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
    "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
}

def fetch_hackerone_data():
    # Define the programs you want to filter by
    programs = ['six-group-private', 'six-group']
    
    # Construct the URL with the filter parameters
    params = {
        'filter[program][]': programs,  # Filter for the specified programs
        'filter[bounty_awarded_at__null]': 'false'  # Filter for reports with awarded bounties
    }

    # Fetching data from HackerOne with basic authentication
    response = requests.get(
        HACKERONE_API_URL,
        auth=(HACKERONE_API_USERNAME, HACKERONE_API_KEY),
        headers=HACKERONE_HEADERS,
        params=params
    )
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data from HackerOne API: {response.status_code}, {response.text}")

def format_hall_of_fame(data):
    hall_of_fame = {}

    for report in data.get('data', []):
        # Extract relevant report information
        report_created_at = report['attributes']['created_at']
        created_date = datetime.strptime(report_created_at, "%Y-%m-%dT%H:%M:%S.%fZ")
        year = created_date.year
        month = created_date.strftime("%B")

        # Initialize the year and month structure if not present
        if year not in hall_of_fame:
            hall_of_fame[year] = {}
        if month not in hall_of_fame[year]:
            hall_of_fame[year][month] = []

        # Extract the hacker information
        hacker_data = report['relationships']['reporter']['data']['attributes']
        hacker_username = hacker_data['username']
        profile_picture_url = hacker_data['profile_picture']['62x62']  # Using the 62x62 size
        hacker_profile_url = f"https://hackerone.com/{hacker_username}"

        # Check if this hacker is already in the hall of fame for this month to avoid duplication
        if not any(entry['hacker_username'] == hacker_username for entry in hall_of_fame[year][month]):
            # Append the hacker information to the hall of fame structure if not a duplicate
            hall_of_fame[year][month].append({
                "hacker_username": hacker_username,
                "profile_picture_url": profile_picture_url,
                "hacker_profile_url": hacker_profile_url
            })
    
    return hall_of_fame

def write_to_test_readme(hall_of_fame):
    test_readme_file = "TEST_README.md"

    # Begin with an empty string to build the content
    readme_content = "# Test Hall of Fame\n\n"

    # Sort the hall_of_fame dictionary by year descending and month order
    for year in sorted(hall_of_fame.keys(), reverse=True):
        # Sort months using the MONTH_ORDER dictionary
        sorted_months = sorted(hall_of_fame[year].keys(), key=lambda m: MONTH_ORDER[m], reverse=True)

        for month in sorted_months:
            reports = hall_of_fame[year][month]

            if reports:
                # Add the month-year heading
                readme_content += f"### {month} {year}\n\n"

                # Create table header
                readme_content += "| Profile | Hacker |\n"
                readme_content += "|---------|--------|\n"

                # Add each report as a row in the table
                for report in reports:
                    # Using inline HTML to set fixed width and height (50x50) for the profile picture
                    profile_picture = f'<img src="{report["profile_picture_url"]}" width="50" height="50" style="border-radius:50%"/>'
                    hacker_link = f"[{report['hacker_username']}]({report['hacker_profile_url']})"
                    readme_content += f"| {profile_picture} | {hacker_link} |\n"

                # Add some space after each table
                readme_content += "\n"

    # Write content to TEST_README.md
    with open(test_readme_file, 'w') as f:
        f.write(readme_content)
    
    print(f"{test_readme_file} has been created/updated with the Hall of Fame.")

def update_readme(hall_of_fame):
    repo_url = f"https://api.github.com/repos/{GITHUB_REPO}/contents/README.md"
    
    # Get the README file from the repository
    response = requests.get(repo_url, headers=GITHUB_HEADERS)
    if response.status_code != 200:
        raise Exception(f"Failed to get README.md: {response.status_code}, {response.text}")
    
    readme_data = response.json()
    readme_content = b64decode(readme_data['content']).decode("utf-8")  # Decode the README.md content
    
    # Build the new Hall of Fame content (the tables with hacker profiles)
    hall_of_fame_str = ""

    # Sort the hall_of_fame dictionary by year descending and month order
    for year in sorted(hall_of_fame.keys(), reverse=True):
        sorted_months = sorted(hall_of_fame[year].keys(), key=lambda m: MONTH_ORDER[m], reverse=True)

        for month in sorted_months:
            reports = hall_of_fame[year][month]

            if reports:
                # Add the month-year heading
                hall_of_fame_str += f"### {month} {year}\n\n"

                # Create table header
                hall_of_fame_str += "| Profile | Hacker |\n"
                hall_of_fame_str += "|---------|--------|\n"

                # Add each report as a row in the table
                for report in reports:
                    profile_picture = f'<img src="{report["profile_picture_url"]}" width="50" height="50" style="border-radius:50%"/>'
                    hacker_link = f"[{report['hacker_username']}]({report['hacker_profile_url']})"
                    hall_of_fame_str += f"| {profile_picture} | {hacker_link} |\n"

                # Add some space after each table
                hall_of_fame_str += "\n"

    # The specific text to search for
    insertion_point_text = "We acknowledge the contributions of top researchers. Below are those who have earned their place in the Hall of Fame:"

    # Find where this specific text occurs in the README.md file
    if insertion_point_text in readme_content:
        # Insert the tables directly after this specific text
        updated_content = readme_content.replace(insertion_point_text, insertion_point_text + "\n\n" + hall_of_fame_str)
    else:
        # Append Hall of Fame if the specific text is not found (fallback behavior)
        updated_content = readme_content + "\n\n## Hall of Fame\n" + hall_of_fame_str
    
    # Encode the content back to Base64
    updated_content_encoded = b64encode(updated_content.encode("utf-8")).decode("utf-8")

    # Update the README file
    update_payload = {
        "message": "Automated update of Hall of Fame",
        "content": updated_content_encoded,
        "sha": readme_data['sha']  # Required to update the file
    }

    update_response = requests.put(repo_url, headers=GITHUB_HEADERS, json=update_payload)
    if update_response.status_code != 200:
        raise Exception(f"Failed to update README.md: {update_response.status_code}, {update_response.text}")
    
    print("README.md updated successfully.")

if __name__ == "__main__":
    # Step 1: Fetch data from HackerOne
    hackerone_data = fetch_hackerone_data()

    # Step 2: Format the data for the Hall of Fame section
    hall_of_fame = format_hall_of_fame(hackerone_data)

    # Step 3: Check if --test-local flag is set, write output to TEST_README.md
    if args.test_local:
        write_to_test_readme(hall_of_fame)
    else:
        # Step 4: Update the README.md file on GitHub
        update_readme(hall_of_fame)
