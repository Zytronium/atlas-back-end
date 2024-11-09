#!/usr/bin/python3
"""Module for gathering data from an API and exporting to CSV."""
import json
import requests


if __name__ == "__main__":
    # Fetch all users
    users_url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(users_url)
    if response.status_code != 200:
        print("Failed to fetch user data.")
        exit()
    users = response.json()

    # Dictionary to store data for all users
    all_tasks = {}

    # Loop through each user and fetch their tasks
    for user in users:
        user_id = user["id"]
        username = user["username"]

        # Fetch todo list for the user
        todos_url = ("https://jsonplaceholder.typicode.com/todos?userId={uid}"
                     .format(uid=user_id))
        response = requests.get(todos_url)

        if response.status_code != 200:
            print(f"Failed to fetch tasks for user ID {user_id}")
            continue
        todos = response.json()

        # Process and structure each user's tasks
        tasks = [{
            "task": task["title"],
            "completed": task["completed"],
            "username": username
        } for task in todos]

        # Store the user's tasks under their user ID
        all_tasks[str(user_id)] = tasks

    # Write all tasks to a JSON file
    json_filename = "todo_all_employees.json"
    with open(json_filename, "w") as json_file:
        json.dump(all_tasks, json_file)

    print(f"All employee data exported to {json_filename}.")
