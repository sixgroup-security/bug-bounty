<!-- DOCUMENT Hero -->
<div align="center">
  <!-- Use the SVG as the hero -->
  <a href="https://hackerone.com/six-group">
    <img src="/assets/header.svg" alt="Logo" width="600" />
  </a>

  <h3 align="center">Bug Bounty 🐛 | SIX Group AG</h3>

  <p align="center">
    Join our bug bounty program and help improve our system security!
  </p>

  <!-- SVG Buttons for Public and Private Programs -->
  <div>
  <table border="0" width="100%" cellspacing="20">
    <tr>
      <td align="center" width="50%">
        <a href="https://hackerone.com/six-group">
          <img src="/assets/buttons/public-program-button.svg" alt="Public Bug Bounty Program" width="200" />
        </a>
      </td>
      <td align="center" width="50%">
        <a href="https://hackerone.com/six-group-private">
          <img src="/assets/buttons/private-program-button.svg" alt="Private Bug Bounty Program" width="200" />
        </a>
      </td>
    </tr>
  </table>
  </div>

  <!-- Hero Menu with Emojis -->
  <div align="center" style="font-size: 18px;">
    📖 <a href="#-introduction" style="text-decoration: none; padding: 10px;">Introduction</a>
    ·
    💰 <a href="#-rewards" style="text-decoration: none; padding: 10px;">Rewards</a>
    ·
    🏆 <a href="#-hall-of-fame" style="text-decoration: none; padding: 10px;">Hall of Fame</a>
    ·
    🤝 <a href="#-eligibility-guidelines" style="text-decoration: none; padding: 10px;">Guidelines</a>
    ·
    🛡️ <a href="#-safe-harbor" style="text-decoration: none; padding: 10px;">Safe Harbor</a>
  </div>
</div>

---

## 📖 Introduction

SIX Group AG is committed to improving the security of its internet-facing applications. We have partnered with HackerOne, the leading bug bounty platform, to invite ethical hackers to identify and report vulnerabilities in our systems.

The public program is open to all security researchers, while the private program is invite-only for selected experts. Both programs provide round-the-clock vulnerability detection and reward researchers based on the criticality of their findings.

<div align="center">
  <div align="center" style="margin-top: 20px;">
    <a href="https://hackerone.com/six-group/reports/new?type=team&report_type=vulnerability">
      <img src="/assets/buttons/submit-report-button.svg" alt="Submit Report" width="250" />
    </a>
  </div>
</div>

---

## 💰 Rewards

| 🟢 Low | 🟡 Medium | 🟠 High | 🔴 Critical |
| :----: | :-------: | :-----: | :---------: |
|  $200–$500 |  $750–$1,500   | $1,500–$3,000  |   $5,000–$7,500   |

For more details on our reward structure, visit the _[public bug bounty program page ⤴](https://hackerone.com/six-group)_.

---

## 🏆 Hall of Fame

We acknowledge the contributions of top researchers. Below are those who have earned their place in the Hall of Fame:

<div align="center">
  <!-- tba -->
</div>

Check out the leaderboard _[here ⤴](https://hackerone.com/six-group/thanks)_.

---

## 🤝 Eligibility Guidelines

### 📃 General Rules

- You agree and adhere to the Program Rules and Legal terms as stated in this policy.
- Do not engage in any activity that can potentially or actually cause harm to SIX, our customers, or our employees.
- Do not engage in any activity that can potentially or actually stop or degrade SIX services or assets.
- Social engineering (e.g. physical, phishing, vishing, smishing) is prohibited.
- Testing and/or research must be on in-scope systems only. If you’re not sure whether a system is in scope, please ask.
- Security researchers should refrain from disclosing issues publicly prior to a mutually agreed upon disclosure date.
- Do not store, share, compromise or destroy SIX or customer data. If Personally Identifiable Information (PII) is encountered, you should immediately halt your activity, purge related data from your system, and immediately contact SIX. This step protects any potentially vulnerable data, and you.
- SIX employees and third-party assets employees are not eligible for participation in this program.

### 👤 Accounts and Tooling

- Interact only with accounts you own or those provided by the program team. Brute-force attacks are not allowed.
- Use exploits only to confirm the presence of a vulnerability. Do not exploit further or pivot to other systems.
- Append the string "bugbounty" to your user agent for all HTTP/HTTPS traffic.
- Automated scans (e.g., via Burp Suite, SqlMap) are prohibited on SIX assets.

### 🚫 Scope Exclusions

Some core findings are out of scope and won’t be rewarded:

- Clickjacking on pages with no sensitive actions.
- Cross-Site Request Forgery (CSRF) on unauthenticated forms or forms with no sensitive actions.
- Attacks requiring MITM or physical access or control over a user's device.
- Cross-domain referer leakage (except there is an actual impact like disclosure of authenticated session cookies).
- Cross-domain script inclusions.
- Previously known vulnerable libraries without a working Proof of Concept.
- Missing best practices in SSL/TLS configuration.
- Rate limiting.
- Brute force attacks, as long as user enumeration isn’t possible.
- Denial of service attacks (DDOS/DOS).
- Missing cookies security flags (e.g., HttpOnly or Secure).
- Missing email best practices (Invalid, incomplete or missing SPF/DKIM/DMARC records, etc.).
- Missing DNS resource record for Certificate Authority Authorization (CAA).
- Vulnerabilities only affecting users of outdated or unpatched browsers (less than 2 stable versions behind the latest released stable version).
- Information disclosure vulnerabilities like software version disclosure / internal path disclosure issues / banner identification issues / descriptive error messages or headers (e.g. stack traces, application or server errors) (except there is an actual impact like disclosure of sensitive information).
- Zero-days or known vulnerabilities disclosed publicly within the past 30 days.
- Vulnerabilities solely based on Open Source Intelligence (OSINT) investigations, without a technical exploit.
- Broken links or URL inconsistencies without an associated security vulnerability or demonstrable impact on system security.
- Web links that point to non-existing web pages.
- Unconfirmed reports from automated vulnerability scanners.
- General low severity issues reported by automated scanners.

### 📝 Submission / Reporting Criteria

- Please provide detailed reports with reproducible steps. If the report is not detailed enough to reproduce the issue, the issue may not be marked as triaged.
- Submit one vulnerability per report, unless you need to chain vulnerabilities to provide impact.
- You are the first to submit a sufficiently reproducible report for an issue in order to be eligible for a bounty.
- You are available to supply additional information, as needed by our team, to reproduce and triage the issue.
- Multiple vulnerabilities caused by one underlying issue will be treated as one valid report.
- In case that a reported vulnerability was already known to the company from our own tests, it will be flagged as a duplicate.
- If applicable, provide information about necessary cleanup steps (e.g., removal of uploaded files) to establish the targets initial state prior to testing.

_[Learn more about exclusions ⤴](https://hackerone.com/six-group)_

---

## 🛡️ Safe Harbor

Any activities conducted in a manner consistent with this policy will be considered authorized conduct, and SIX Group will not initiate legal action against you. If legal action is initiated by a third party against you in connection with activities conducted under this policy, we will take steps to ensure that your actions were in compliance with this policy.
