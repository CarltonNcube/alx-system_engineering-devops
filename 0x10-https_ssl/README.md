HTTPS SSL Configuration
This project focuses on enhancing website security by implementing HTTPS SSL configuration using HAProxy. 
The tasks involve configuring domain zones, SSL termination on HAProxy, and enforcing HTTPS traffic.

Table of Contents
0. World Wide Web
Tasks
Configure Domain Zone
Bash Script
1. HAProxy SSL Termination
2. No loophole in your website traffic (Advanced)
0. World Wide Web
Tasks
Configure Domain Zone
Add the subdomains www, lb-01, web-01, and web-02 to the specified domain, pointing them to their respective IPs.
Bash Script
Write a Bash script named 0-world_wide_web that:

Accepts domain and subdomain parameters.
Displays information about subdomains based on the provided criteria.
Utilizes awk and at least one Bash function.
Ignores shellcheck case SC2086.
1. HAProxy SSL Termination
Tasks
SSL Termination Configuration
Create a certificate using certbot.
Configure HAProxy to listen on port TCP 443 and accept SSL traffic.
HAProxy must serve encrypted traffic returning the / of your web server.
The root page must contain "Holberton School".
Answer File
Share your HAProxy config as an answer file at /etc/haproxy/haproxy.cfg.
The file 1-haproxy_ssl_termination must be your HAProxy configuration file.
Requirements
Install HAProxy 1.5 or higher, as SSL termination is not available before v1.5.
2. No loophole in your website traffic (Advanced)
Advanced Task
Enforce HTTPS traffic to eliminate unencrypted traffic. Configure HAProxy to:

Automatically redirect HTTP traffic to HTTPS.
Return a 301 for the redirect.
Answer File
Share your HAProxy config as an answer file at /etc/haproxy/haproxy.cfg.
The file 100-redirect_http_to_https must be your HAProxy configuration file.
