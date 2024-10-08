# Bug Bounty 🐛 | SIX Group AG

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

  <!-- Hero Menu with Emojis -->
  <div align="center" style="font-size: 18px;">
    <a href="#introduction" style="text-decoration: none; padding: 10px;">📖 Introduction</a>
    ·
    <a href="#scopes-public-program" style="text-decoration: none; padding: 10px;">🎯 Scopes</a>
    ·
    <a href="#rewards" style="text-decoration: none; padding: 10px;">💰 Rewards</a>
    ·
    <a href="#hall-of-fame" style="text-decoration: none; padding: 10px;">🏆 Hall of Fame</a>
    ·
    <a href="#eligibility-guidelines" style="text-decoration: none; padding: 10px;">🤝 Participation</a>
  </div>
</div>

---

## 📖 Introduction

SIX Group AG is committed to improving the security of its internet-facing applications. We have partnered with HackerOne, the leading bug bounty platform, to invite ethical hackers to identify and report vulnerabilities in our systems.

The public program is open to all security researchers, while the private program is invite-only for selected experts. Both programs provide round-the-clock vulnerability detection and reward researchers based on the criticality of their findings.

---

## 🎯 Scopes (Public Program)

| Asset Name        | Type     | Coverage     | Max Severity | Bounty        |
| ----------------- | -------- | ------------ | ------------ | ------------- |
| www.six-group.com | Domain   | In scope     | 🔴 Critical  | 💰 Eligible   |
| \*.six-group.com  | Wildcard | Out of scope | 🔵 None      | 🚫 Ineligible |

---

## 💰 Rewards

| 🟢 Low | 🟡 Medium | 🟠 High | 🔴 Critical |
| :----: | :-------: | :-----: | :---------: |
|  $500  |  $1,000   | $5,000  |   $10,000   |

For more details on our reward structure, visit the _[public bug bounty program page ⤴](https://hackerone.com/six-group)_.

---

## 🏆 Hall of Fame

We acknowledge the contributions of top researchers and feature them in our **Hall of Fame**. Earn your spot by consistently reporting critical vulnerabilities. Check out the leaderboard _[here ⤴](https://hackerone.com/six-group/thanks)_.

---

## 🤝 Eligibility Guidelines

### 📃 General Rules

1. Adhere to the _[Program Rules ⤴](https://hackerone.com/six-group/program)_ and legal terms as stated in this policy.
2. Do not engage in any activity that can potentially cause harm to SIX, its customers, or employees.
3. Do not degrade or disrupt SIX services or assets.
4. Social engineering (e.g., phishing, vishing, smishing) is strictly prohibited.
5. Testing must only be conducted on **in-scope systems**. If unsure, please ask.
6. Security researchers must refrain from publicly disclosing issues prior to an agreed-upon disclosure date.
7. Do not store, share, or destroy SIX or customer data. If Personally Identifiable Information (PII) is encountered, halt activity immediately and contact SIX.

### 👤 Accounts and Tooling

- Interact only with accounts you own or those provided by the program team. Brute-force attacks are not allowed.
- Use exploits only to confirm the presence of a vulnerability. Do not exploit further or pivot to other systems.
- Append the string "bugbounty" to your user agent for all HTTP/HTTPS traffic.
- Automated scans (e.g., via Burp Suite, SqlMap) are prohibited on SIX assets.

### 🚫 Scope Exclusions

Some core findings are out of scope and won’t be rewarded:

- Clickjacking on pages with no sensitive actions
- CSRF on unauthenticated forms or forms with no sensitive actions
- Vulnerabilities requiring MITM or physical access
- Missing cookies security flags (e.g., HttpOnly or Secure)
- Denial of service (DDoS) attacks
- Rate limiting
- Vulnerabilities affecting users of outdated/unpatched browsers
- Information disclosure (e.g., version info or error messages without sensitive data)

_[Learn more about exclusions ⤴](https://hackerone.com/six-group)_

---

## 🛡️ Safe Harbor

Any activities conducted in a manner consistent with this policy will be considered authorized conduct, and SIX Group will not initiate legal action against you. If legal action is initiated by a third party against you in connection with activities conducted under this policy, we will take steps to ensure that your actions were in compliance with this policy.
