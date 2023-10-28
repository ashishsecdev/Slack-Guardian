
![Slack_Guardian](https://github.com/ashishsecdev/Slack-Guardian/assets/49029528/2fe1b806-c974-4aa7-b313-2f85e2567820)


# Slack-Guardian
[![python](https://img.shields.io/badge/Python-3.9-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)  [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) 

Slack Guardian is a proactive security suite that utilizes Python, Regex and Slack API to safeguard sensitive data posted on Slack Channels, ensuring seamless secure collaboration within Slack.

# Your trusted partner in securing "Sensitive Conversations"!

In today's professional landscape, both small businesses and large enterprises heavily utilize Slack as their primary internal communication tool. Consequently, safeguarding sensitive information within this collaborative platform has become absolutely crucial.

Elevate your team's security posture with Slack Guardian and say goodbye to data breaches and hello to secure collaboration!

Enter the world of Slack Guardian, a Slack Bot designed to safeguard your team's confidential conversations on Slack by using Regex pattern provided in .CSV file that also generates the real-time report of the violations.


# Features

- **Real-time Monitoring:** Slack Guardian continuously scans messages for sensitive information, such as personal data or financial details.

- **Automated Responses:** In case policy violations, Slack Guardian takes immediate action by deleting the message, notifying the user and also keeping the deleted record for audits.

- **Violation Audit Reporting:** Gain insights into potential breaches and data leaks with comprehensive customizable audit report that provides `User ID, Channel ID, Thread ID, Message Time, Deleted Message` as output fields.
  
- **Customizable Patterns:** Fine tune the detection patterns by adding regex under "Pattern.csv".

- **Threaded Conversations:** Slack Guardian seamlessly integrates into threads, ensuring the security of your entire discussion.
  

# Installation
To be updated! :-P

# Achitecture
![Slack_Guardian_architecture](https://github.com/ashishsecdev/Slack-Guardian/assets/49029528/c39526f6-c7e1-4d49-bc8f-0c274a0482a2)

1. Listens to Slack events via Slack API and Flask APP for handling incoming requests. `/slack/events` route is the endpoint where Slack events are received and further processing happens.
2. Detection happens on the incoming `events` using detection patterns present in `Slack_Guardian_Detections.csv`. 
3. Detected violation logs are appended into `violation-audit-report.csv` with Slack fields like `User ID` Starts from 'U',`Channel ID` Starts from 'C', `Thread ID` 10 digit number, `Message Time` Epoch format, `Deleted Message` Raw format. 
4. `User with violation is tagged into Slack message thread` and notified on the violation.
5. Automatic `deletion of violation` is performed.

# Contribution
Please create a new branch and raise it as a PR for consideration.


# License
Source code for this project is released under the [GNU General Public Licence V3.0.](https://www.gnu.org/licenses/licenses.html) \
Slack Guardian is an independent project that doesn't have any affiliations with Slack Technologies or Salesforce.


# Curated By 
Ashishsecdev \
https://ashishsecdev.medium.com \
Ashishsecdev@gmail.com
