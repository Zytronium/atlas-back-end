#!/usr/bin/python3
"""Module for gathering data from an API and exporting to CSV."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    # Check if an employee ID argument is passed
    if len(argv) < 2:
        print("No employee ID provided")
    elif not argv[1].isdigit():
        print("Employee ID must be an integer")
    else:
        employee_id = int(argv[1])

        # Fetch employee data
        user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        response = requests.get(user_url)
        if response.status_code != 200:
            print(f"Employee with ID {employee_id} not found")
            exit()
        user_data = response.json()
        employee_name = user_data.get("username")

        # Fetch todo list for the employee
        todos_url = ("https://jsonplaceholder.typicode.com/todos?userId={e_id}"
                     .format(e_id=employee_id))
        response = requests.get(todos_url)
        todos = response.json()

        # Write JSON data to file
        tasks = [{
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_name
        } for task in todos]

        data = {str(employee_id): tasks}

        json_filename = f"{employee_id}.json"
        with open(json_filename, "w") as json_file:
            json.dump(data, json_file)

        print(f"Data exported to {json_filename}.")
