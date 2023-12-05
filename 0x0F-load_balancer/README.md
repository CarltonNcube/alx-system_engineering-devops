Project README
This project involves configuring web servers and a load balancer to efficiently distribute traffic. The tasks include setting up servers, installing and configuring HAproxy for load balancing, and automating the addition of a custom HTTP header using both Bash and Puppet scripts.

Task 0: Double the number of webservers
Tasks
Double the number of webservers (mandatory)
Configure web-02 to be identical to web-01 using the provided Bash script (0-custom_http_response_header).
Add a custom Nginx response header:
Header Name: X-Served-By
Header Value: Hostname of the server Nginx is running on
Write a Bash script (0-custom_http_response_header) to configure a new Ubuntu machine to meet the specified requirements.
Ignore SC2154 for shellcheck.
Task 1: Install your load balancer
Tasks
Install your load balancer (mandatory)
Install and configure HAproxy on lb-01.
Configure HAproxy to send traffic to web-01 and web-02 using a round-robin algorithm.
Ensure HAproxy can be managed via an init script.
Make sure servers are configured with the correct hostnames: [STUDENT_ID]-web-01 and [STUDENT_ID]-web-02.
Write a Bash script to configure a new Ubuntu machine to meet the specified requirements.
Task 2: Add a custom HTTP header with Puppet
Add a custom HTTP header with Puppet (advanced)
Automate the creation of a custom HTTP header using Puppet.
Header Name: X-Served-By
Header Value: Hostname of the server Nginx is running on.
Write a Puppet script (2-puppet_custom_http_response_header.pp) to configure a new Ubuntu machine according to the specified requirements.
Feel free to adapt the placeholders such as [STUDENT_ID], [IP_ADDRESS], and [STATE] with the actual values for your project.
