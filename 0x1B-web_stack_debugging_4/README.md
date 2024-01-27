Project 0x1B. Web Stack Debugging #4
This project revolves around the critical tasks of debugging and optimizing the performance of a web server stack featuring Nginx. The challenges involve identifying and resolving issues under high traffic conditions using ApacheBench, a popular benchmarking tool. The primary focus is on achieving optimal performance and reliability.

Task 0: Sky is the limit, let's bring that limit higher (Mandatory)
Understand the intricacies of the Nginx web server's behavior under pressure by conducting benchmark tests with ApacheBench. The task involves analyzing the results, identifying bottlenecks, and implementing necessary fixes using Puppet scripting. The goal is to eliminate failed requests and enhance the overall responsiveness of the web server.

Steps:
Benchmark the current Nginx setup using ApacheBench:

bash
Copy code
ab -c 100 -n 2000 localhost/
Analyze the benchmark results to determine the number of failed requests.

Create a Puppet script (0-the_sky_is_the_limit_not.pp) to address issues in the Nginx configuration.

Apply the Puppet script to implement the fixes:

bash
Copy code
puppet apply 0-the_sky_is_the_limit_not.pp
Re-run the ApacheBench to validate the improvements.

Task 1: User limit (Advanced)
Tackle an advanced challenge involving the modification of the OS configuration to enable smooth login for the holberton user, eliminating any error messages when opening files. This task requires in-depth debugging and system configuration to ensure a seamless user experience.

Steps:
Identify the obstacles preventing successful login for the holberton user.

Adjust the OS configuration to facilitate error-free login and file operations for the holberton user.

The project aims to not only resolve immediate performance issues but also to enhance the overall user experience and system stability under varying conditions.
