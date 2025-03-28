<<<<<<< HEAD
#!/usr/bin/python3
"""
Python script that exports data in the JSON format
"""
import json
import requests


def get_all_users():
    """
    Get the list of all users
    """
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    return response.json()


def get_user_todos(user_id):
    """
    Get the TODO list for a given user ID
    """
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params={"userId": user_id})
    return response.json()


def export_all_todos_to_json(users):
    """
    Export all users' TODO lists to a JSON file
    """
    data = {
        user["id"]: [
            {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": user["username"]
            } for todo in get_user_todos(user["id"])
        ] for user in users
    }
    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(data, jsonfile)


def main():
    """
    Main function to fetch users and their TODO lists, then export to JSON
    """
    users = get_all_users()
    export_all_todos_to_json(users)

if __name__ == "__main__":
    main()
=======
#!/usr/bin/python3
"""Exports data in the JSON format"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    todoAll = {}

    for user in users:
        taskList = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        todoAll[user.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todoAll, f)
>>>>>>> 2e0e743a0dd2aefc721d02f9ae7d2583cdc33a6b
