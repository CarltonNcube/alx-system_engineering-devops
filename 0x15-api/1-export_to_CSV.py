#!/usr/bin/python3
"""
Gather data from an API and export to CSV

Usage:
    python3 1-export_to_CSV.py <employee_id>
"""

import requests
import sys
import csv

if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    user_info = requests.get(url).json()

    if 'id' not in user_info:
        print(f"Error: Unable to fetch user data for ID {employee_id}")
        sys.exit(1)

    todos_url = f'https://jsonplaceholder.typicode.com/todos'
    todos = requests.get(todos_url, params={'userId': employee_id}).json()

    completed_tasks = [
        [user_info['id'], user_info['name'], str(task['completed']),
            task['title']]
        for task in todos
    ]

    csv_filename = f"{user_info['id']}.csv"

    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
            "TASK_TITLE"])
        csv_writer.writerows(completed_tasks)

    print(f"Data exported to {csv_filename}")
