#!/usr/bin/python3
"""Script to export data in the CSV format"""
import csv
import requests as r
import sys


def export_to_csv(user_id):
    url = "https://jsonplaceholder.typicode.com/"
    user_info = r.get(f"{url}users/{user_id}").json()
    username = user_info.get("username")
    todos = r.get(f"{url}todos", params={"userId": user_id}).json()

    with open(f"{user_id}.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for elm in todos:
            writer.writerow(
                [user_id, username, elm.get("completed"), elm.get("title")]
            )


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 script.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    export_to_csv(user_id)
