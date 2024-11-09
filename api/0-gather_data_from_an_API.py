#!/usr/bin/python3
"""Module for gathering data from an API."""
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
        employee_name = user_data.get("name")

        # Fetch todo list for the employee
        todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
        response = requests.get(todos_url)
        todos = response.json()

        # Count total and completed tasks
        total_tasks = len(todos)
        completed_tasks = [task for task in todos if task["completed"]]
        total_completed_tasks = len(completed_tasks)

        # Display todo progress
        print(f"Employee {employee_name} is done with tasks(" +
              f"{total_completed_tasks}/{total_tasks}):")

        for task in completed_tasks:
            print(f"\t {task['title']}")
