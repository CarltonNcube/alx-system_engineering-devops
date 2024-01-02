#!/usr/bin/python3
"""
Gather data from an API

Usage:
    python3 0-gather_data_from_an_API.py <employee_id>
"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    user_info = requests.get(url).json()

    if 'id' not in user_info:
        print(f"Error: Unable to fetch user data for ID {employee_id}")
        sys.exit(1)

    todos_url = f'https://jsonplaceholder.typicode.com/todos'
    todos = requests.get(todos_url, params={'userId': employee_id}).json()

    completed_tasks = [task['title'] for task in todos if task['completed']]

    print(f"Employee {user_info['name']} is done with tasks"
          f"({len(completed_tasks)}/{len(todos)}):")

    for task in completed_tasks:
        print(f"\t {task}")
