Project 0x17. Web Stack Debugging #3

Project Description
When debugging, logs may not provide sufficient information, especially when the software breaks unexpectedly or doesn't log the error. In such cases, it becomes necessary to dive deeper into the stack, a skill that Holberton students are well-equipped to handle.

WordPress is a widely used tool, powering 26% of the web for various purposes like blogs, portfolios, e-commerce, and company websites. It is typically run on the LAMP stack, consisting of Linux, Apache, MySQL, and PHP.

The web stack being debugged in this project is a WordPress website running on a LAMP stack.

Task 0. Strace is your friend (Mandatory)
The primary objective of this task is to utilize strace to identify the root cause of the 500 error being returned by Apache. Strace is a powerful tool that allows you to trace system calls and signals, providing insights into the interactions between a process and the operating system.

Once the issue is identified using strace, the next step is to implement a fix for the problem. In contrast to the previous approach using Bash scripts, this project emphasizes the use of Puppet for automation. Puppet is a configuration management tool that allows for the automated provisioning and management of infrastructure.

Requirements:

Your 0-strace_is_your_friend.pp file must contain Puppet code.
Use Puppet resource types to implement the fix for the identified issue.
