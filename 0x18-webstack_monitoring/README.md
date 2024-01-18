Project 0x18. Webstack Monitoring

Project Overview
The project revolves around the crucial practice of web stack monitoring, emphasizing the significance of keeping a vigilant eye on system performance. Understanding and implementing effective monitoring strategies are essential for ensuring the reliability and optimal functioning of software systems. The project specifically addresses two main areas of web stack monitoring: application monitoring, which focuses on the behavior of running software, and server monitoring, which ensures the health and performance of virtual or physical servers.

Tasks
Task 0: Sign up for Datadog and Install Datadog-agent (Mandatory)
Begin the project by signing up for a Datadog account and installing the Datadog agent on the web-01 server. The goal is to integrate Datadog's monitoring capabilities into the server environment.

Requirements:

Use the US region (US1) for Datadog.
Install the Datadog agent on the web-01 server.
Create and paste the DataDog API key and application key in your Intranet user profile.
Ensure visibility of web-01 in Datadog under the hostname XX-web-01.
Task 1: Monitor Some Metrics (Mandatory)
Implement monitoring measures by setting up monitors in the Datadog dashboard. Create monitors to track the number of read and write requests issued to the device per second.

Requirements:

Set up a monitor for read requests per second.
Set up a monitor for write requests per second.
Task 2: Create a Dashboard (Mandatory)
Develop a new Datadog dashboard featuring at least four widgets of various types. These widgets should monitor different metrics, providing diverse visualizations for effective analysis.

Requirements:

Create a new dashboard.
Add at least four widgets to the dashboard, monitoring a range of metrics.
Update the answer file 2-setup_datadog with the dashboard_id on the first line.
