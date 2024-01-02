#!/usr/bin/python3
"""
Gather data from an API

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>
"""

import requests
import sys


def gather_data(employee_id):
    """
    Retrieve and display TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    response_employee = requests.get(api_url)
    response_todos = requests.get(todos_url)

    if response_employee.status_code != 200 or response_todos.status_code != 200:
        print("Error: Unable to fetch data from the API.")
        sys.exit(1)

    employee_info = response_employee.json()
    todos = response_todos.json()

    completed_tasks = [task for task in todos if task['completed']]
    total_tasks = len(todos)

    print(f"Employee {employee_info['name']} is done with tasks"
          f"({len(completed_tasks)}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t{task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    gather_data(employee_id)

