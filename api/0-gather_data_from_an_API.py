import requests
import sys

def fetch_employee_todos(employee_id):
    # Endpoint for fetching employee's TODO list
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    
    # Send GET request to fetch TODO list
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error: Unable to fetch data for employee with ID {employee_id}")
        sys.exit(1)
    
    todos = response.json()
    
    # Filter completed tasks
    completed_tasks = [task for task in todos if task['completed']]
    total_tasks = len(todos)
    num_completed = len(completed_tasks)
    
    # Extract employee's name (it will also be in the user endpoint)
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_response = requests.get(employee_url)
    
    if employee_response.status_code != 200:
        print(f"Error: Unable to fetch employee details for ID {employee_id}")
        sys.exit(1)
    
    employee = employee_response.json()
    employee_name = employee['name']
    
    # Print results
    print(f"Employee {employee_name} is done with tasks({num_completed}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    # Get employee ID from command line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    fetch_employee_todos(employee_id)
