#!/usr/bin/python3
"""
Fetches and displays an employee's TODO list progress using a REST API.
"""

import sys
import urllib.request
import json

def fetch_todo_progress(employee_id):
    """Fetch and display the TODO progress for a given employee ID."""
    base_url = "https://jsonplaceholder.typicode.com/users/"
    user_url = f"{base_url}{employee_id}"
    todos_url = f"{user_url}/todos"
    
    try:
        # Fetch user data
        with urllib.request.urlopen(user_url) as response:
            user_data = json.load(response)
            employee_name = user_data.get("name")
        
        # Fetch TODO list data
        with urllib.request.urlopen(todos_url) as response:
            todos_data = json.load(response)
        
        total_tasks = len(todos_data)
        done_tasks = [task["title"] for task in todos_data if task.get("completed")]
        number_of_done_tasks = len(done_tasks)
        
        # Print employee progress
        print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
        for task_title in done_tasks:
            print(f"\t {task_title}")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        fetch_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)

