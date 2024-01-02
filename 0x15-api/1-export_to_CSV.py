#!/usr/bin/python3
import requests
import csv
import sys

def export_to_csv(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch user information
    user_info = requests.get(user_url).json()
    username = user_info.get("username")

    # Fetch user's todos
    todos = requests.get(todos_url).json()

    # Prepare and write to CSV
    filename = f"{employee_id}.csv"
    with open(filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
            "TASK_TITLE"])

        for task in todos:
            csv_writer.writerow([employee_id, username, 
                str(task["completed"]), task["title"]])

    print(f"Data exported to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    export_to_csv(employee_id)

