 #!/usr/bin/python3
"""Script that gets user data (Todo list) from API
and then export the result to a JSON file."""

import json
import requests


def main():
    """Main function"""

    # Fetch all todos
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    todos = requests.get(todo_url).json()

    # Fetch all users in one request
    users_url = 'https://jsonplaceholder.typicode.com/users'
    users = requests.get(users_url).json()

    # Create a dictionary of userId to username
    user_dict = {user["id"]: user["username"] for user in users}

    output = {}

    for todo in todos:
        user_id = todo['userId']
        username = user_dict[user_id]  # Get username from pre-fetched data

        if user_id not in output:
            output[user_id] = []

        output[user_id].append({
            "username": username,
            "task": todo["title"],
            "completed": todo["completed"]
        })

    # Save the output to a JSON file
    with open("todo_all_employees.json", "w") as file:
        json.dump(output, file, indent=4)


if __name__ == '__main__':
    main()

