#!/usr/bin/python3
"""Script to export data in the CSV format"""
import csv
import requests as r
import sys


def export_to_csv(user_id):
    url = "https://jsonplaceholder.typicode.com/"
    user_info = r.get(url + "users/{}".format(user_id)).json()
    username = user_info.get("username")
    todos = r.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        writer.writerow([
            user_id, username, elm.get("completed"), elm.get("title")
        ] for elm in todos)


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 script.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    export_to_csv(user_id)

