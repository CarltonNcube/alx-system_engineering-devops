#!/usr/bin/python3
"""
Export to CSV

Usage:
    python3 1-export_to_CSV.py <employee_id>
"""

import requests
import csv
import sys


def export_to_csv(employee_id):
    """
    Retrieve and export TODO list progress for a given employee ID in CSV format.

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

    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todos:
            writer.writerow([employee_id, employee_info['username'],
                             str(task['completed']), task['title']])

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_csv(employee_id)

