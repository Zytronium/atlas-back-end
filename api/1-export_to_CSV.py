#!/usr/bin/python3
"""Module for gathering data from an API and exporting to CSV."""
import csv
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
        todos_url = ("https://jsonplaceholder.typicode.com/todos?userId={e_id}"
                     .format(e_id=employee_id))
        response = requests.get(todos_url)
        todos = response.json()

        # Write tasks to CSV
        csv_filename = f"{employee_id}.csv"
        with open(csv_filename, mode="w", newline="") as csv_file:
            writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            for task in todos:
                writer.writerow([
                    employee_id,
                    employee_name,
                    task["completed"],
                    task["title"]
                ])

        print(f"Data exported to {csv_filename}")
