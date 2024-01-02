Project 0x15 - API

Project Description
This project focuses on leveraging Python to interact with a REST API, retrieve employee data, and organize/export it into various data structures. In contrast to traditional Bash scripting, this project embraces the versatility of Python for efficient data manipulation.

Background
In the evolving landscape of system administration, there has been a discernible shift from the conventional Bash-centric approach to a more comprehensive skill set, particularly among the new generation known as Site Reliability Engineers (SREs). SREs, distinct from their predecessors, possess a broader understanding of various programming languages in addition to managing systems.

APIs serve as a prevalent method for exposing applications and datasets, acting as the public-facing interfaces for websites and microservices. They enable external entities to interact with and modify data. This project focuses on accessing employee data through an API, analyzing it, and exporting it into different data structures using Python scripts.

Project Tasks
Gather data from an API (Task 0 - Mandatory):

Write a Python script utilizing the provided REST API.
Accept an employee ID as a parameter.
Display the employee's TODO list progress in a specific format on the standard output.
Export to CSV (Task 1 - Mandatory):

Extend the script from Task 0 to export data in CSV format.
Record tasks owned by the specified employee.
Format: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE".
File name: USER_ID.csv.
Export to JSON (Task 2 - Mandatory):

Extend the script from Task 0 to export data in JSON format.
Record tasks owned by the specified employee.
Format: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}.
File name: USER_ID.json.
Dictionary of list of dictionaries (Task 3 - Mandatory):

Extend the script from Task 0 to export data in JSON format.
Record tasks from all employees.
Format: { "USER_ID": [{"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS"}, ... ], ... }.
File name: todo_all_employees.json.
