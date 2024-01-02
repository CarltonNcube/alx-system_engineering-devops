#!/usr/bin/python3
"""
Export TODO list progress to JSON format.

Usage:
    python3 2-export_to_JSON.py <employee_id>
"""

import requests
import json
import sys


def export_to_json(employee_id):
    """
    Retrieve and export TODO list progress for a given 
    employee ID in JSON format.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    api_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    try:
        response_employee = requests.get(api_url)
        response_todos = requests.get(todos_url)
        response_employee.raise_for_status()
        response_todos.raise_for_status()
    except requests.RequestException as e:
        print(f"Error: Unable to fetch data from the API. {e}")
        sys.exit(1)

    employee_info = response_employee.json()
    todos = response_todos.json()

    data = {str(employee_id): []}

    for task in todos:
        data[str(employee_id)].append({
            "task": task['title'],
            "completed": task['completed'],
            "username": employee_info['username']
        })

    filename = f"{employee_id}.json"
    with open(filename, 'w') as file:
        json.dump(data, file)

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 2-export_to_JSON.py <employee_id>
                (employee_id should be a positive integer)")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_json(employee_id)
