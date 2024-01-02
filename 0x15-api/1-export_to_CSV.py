#!/usr/bin/python3
"""
Gather data from an API and export to CSV

Usage:
    python3 1-export_to_CSV.py <employee_id>
"""

import requests
import sys
import csv

def export_to_csv(employee_id):
    # Fetch user information
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    user_info = requests.get(user_url).json()

    if 'id' not in user_info:
        print(f"Error: Unable to fetch user data for ID {employee_id}")
        sys.exit(1)

    # Fetch user's tasks
    todos_url = f'https://jsonplaceholder.typicode.com/todos'
    todos = requests.get(todos_url, params={'userId': employee_id}).json()

    # Prepare data for CSV
    csv_data = [
        [user_info['id'], user_info['username'], str(task['completed']),
            task['title']]
        for task in todos
    ]

    # Write to CSV
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
            "TASK_TITLE"])
        csv_writer.writerows(csv_data)

    print(f"Number of tasks in CSV: {len(csv_data)}")
    print(f"Data exported to {csv_filename}")

if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_csv(employee_id)
