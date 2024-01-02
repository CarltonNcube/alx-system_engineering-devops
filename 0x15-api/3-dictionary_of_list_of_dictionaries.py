#!/usr/bin/python3
"""
Dictionary of List of Dictionaries

Usage:
    python3 3-dictionary_of_list_of_dictionaries.py
"""

import requests
import json


def export_all_to_json():
    """
    Retrieve and export TODO list progress for all employees in JSON format.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com/users/"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    all_data = {}

    response = requests.get(base_url)
    if response.status_code != 200:
        print(f"Error: Unable to fetch user data. Status code:
                {response.status_code}")
        return

    users = response.json()

    for user in users:
        user_id = user["id"]
        user_info = user

        response_todos = requests.get(f"{todos_url}?userId={user_id}")
        if response_todos.status_code != 200:
            print(f"Error: Unable to fetch TODO data for user {user_id}.
                    Status code: {response_todos.status_code}")
            continue

        todos = response_todos.json()

        all_data[str(user_id)] = [
            {
                "username": user_info["username"],
                "task": task["title"],
                "completed": task["completed"]
            } for task in todos
        ]

    filename = "todo_all_employees.json"
    with open(filename, 'w') as file:
        json.dump(all_data, file)

    print(f"Data exported to {filename}")


if __name__ == "__main__":
    export_all_to_json()

