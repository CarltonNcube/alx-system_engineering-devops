#!/usr/bin/python3
"""Exports to-do list information of all employees to JSON format."""
import json
import requests


def fetch_todos(user_id):
    return requests.get(f"https://jsonplaceholder.typicode.com/todos",
                        params={"userId": user_id}).json()


def export_to_json(users):
    todo_data = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        todos = fetch_todos(user_id)

        todo_data[user_id] = [
            {
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": username
            }
            for todo in todos
        ]

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(todo_data, jsonfile)


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(f"{url}users").json()

    export_to_json(users)

