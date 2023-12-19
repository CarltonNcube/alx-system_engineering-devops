Web Stack Debugging #2


Task 0: Run Software as Another User
The root user in Linux has extensive privileges, making it crucial to avoid direct 
use whenever possible. Running processes as less privileged users enhances security. 
To achieve this, a Bash script is created to run the whoami command under a specified user.

Task 1: Run Nginx as Nginx
To enhance security, it is recommended to run web servers like Nginx as a less 
privileged user, such as nginx. The provided Bash script configures Nginx to run 
as the nginx user and listen on all active IPs on port 8080.

After debugging, the Nginx processes are shown to be running as the nginx user,
and the server is successfully listening on port 8080.

Task 2: Short and Sweet
A concise Bash script is crafted to accomplish the configuration task from Task #1, 
adhering to specified requirements. The script is kept within 7 lines, ensuring 
simplicity and efficiency.
