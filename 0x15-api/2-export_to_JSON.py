#!/usr/bin/python3
"""
Export to JSON

Usage:
    python3 2-export_to_JSON.py <employee_id>
"""

import requests
import json
import sys


def export_to_json(employee_id):
    """
    Retrieve and export TODO list progress for a given employee 
    ID in JSON format.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    response_employee = requests.get(api_url)
    response_todos = requests.get(todos_url)

    if (
        response_employee.status_code != 200
        or response_todos.status_code != 200
    ):
        print("Error: Unable to fetch data from the API.")
        sys.exit(1)

    employee_info = response_employee.json()
    todos = response_todos.json()

    data = {str(employee_id): []}

    for task in todos:
        data[str(employee_id)].append(
            {
                "task": task["title"],
                "completed": task["completed"],
                "username": employee_info["username"],
            }
        )

    filename = f"{employee_id}.json"
    with open(filename, "w") as file:
        json.dump(data, file)

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_json(employee_id)
