import requests
import json
import argparse

# Parse arguments
parser = argparse.ArgumentParser(description="Create users in XNAT and add them to a project")
parser.add_argument("--url", required=True, help="XNAT Server URL")
parser.add_argument("--username", required=True, help="Username")
parser.add_argument("--password", required=True, help="Password")
parser.add_argument("--project", required=True, help="XNAT Project ID")
args = parser.parse_args()

# XNAT Server details
XNAT_URL = args.url
USERNAME = args.username
PASSWORD = args.password
PROJECT_ID = args.project

# API Endpoints
CREATE_USER_ENDPOINT = f"{XNAT_URL}/xapi/users"
ADD_USER_TO_PROJECT_ENDPOINT = f"{XNAT_URL}/REST/projects/{PROJECT_ID}/users/{PROJECT_ID}_member/"

# Create a session
session = requests.Session()
session.auth = (USERNAME, PASSWORD)

# Function to create a user
def create_user(username, email, firstname, lastname, password="defaultPassword"):
    user_data = {
        "username": username,
        "email": email,
        "enabled": True,
        "firstName": firstname,
        "lastName": lastname,
        "password": password
    }
    response = session.post(CREATE_USER_ENDPOINT, json=user_data)
    if response.status_code == 200:
        print(f"User {username} created successfully.")
    else:
        print(f"Failed to create user {username}: {response.text}")
    
    # Ensure the function is executed even if user already exists
    add_user_to_project(username)

# Function to add a user to the project
def add_user_to_project(username, role="member"):
    print(f"Adding user {username} to project {PROJECT_ID}...")  # Debug print
    response = session.put(f"{ADD_USER_TO_PROJECT_ENDPOINT}{username}")
    if response.status_code == 200:
        print(f"User {username} added to project {PROJECT_ID} successfully.")
    else:
        print(f"Failed to add user {username} to project {PROJECT_ID}: {response.text}")

# Generate 100 users
for i in range(101, 500):
    username = f"mrjamesdickson{i}"
    email = f"mrjamesdickson+{i}@gmail.com"
    firstname = f"Test{i}"
    lastname = "User"
    create_user(username, email, firstname, lastname)

print("User creation and assignment process completed.")
