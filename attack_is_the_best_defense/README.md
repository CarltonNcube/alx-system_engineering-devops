Project: Attack is the Best Defense
Overview
Dive into advanced DevOps, scripting, and hacking concepts with this optional project. It offers an opportunity to enhance your skills and understanding of network security, Docker, and hacking techniques. The project involves two tasks, each focusing on specific aspects of cybersecurity.

Tasks
Task 0: Sniffing Unencrypted Traffic
Objective: Use tcpdump to sniff unencrypted traffic and extract information.

Execute the user_authenticating_into_server script locally on your Ubuntu machine.
Use tcpdump to sniff the network and find the password used in the authentication process.
Paste the found password in your answer file.
Task 1: Dictionary Attack
Objective: Perform a dictionary attack on an SSH account within a Docker container.

Install Docker on your Ubuntu machine.
Run the Docker image sylvainkalache/264-1.
Use hydra to brute force the account sylvain via SSH.
The password is 11 characters long. Once found, share it in your answer file.
Resources
Read about:

Network sniffing
ARP spoofing
Connect to SendGrid’s SMTP relay using telnet
What is Docker and why is it popular?
Dictionary attack
Commands:

tcpdump
hydra
telnet
docker
Disclaimer
During Task 0, you might see "Authentication failed: Bad username / password" in the tcpdump trace. This is expected, as the user has been deleted from the SendGrid account. Verification via SendGrid is not possible; only the correction system can validate it.
