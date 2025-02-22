import argparse
import requests
from requests.auth import HTTPBasicAuth
import json

# Function to create the project
def create_project(xnat_url, admin_username, admin_password, project_id, project_name, project_description):
    # Prepare the payload with the project information
    project_data = {
        "project": {
            "name": project_name,
            "id": project_id,
            "description": project_description
        }
    }

    # Set the API endpoint for creating a project
    endpoint = f"{xnat_url}/data/projects/{project_id}"

    # Make the POST request to create the project
    response = requests.put(
        endpoint,
        data=json.dumps(project_data),
        headers={"Content-Type": "application/json"},
        auth=HTTPBasicAuth(admin_username, admin_password)
    )

    # Check the response status
    if response.status_code == 200:
        print(f"Project '{project_name}' created successfully!")
    else:
        print(f"Failed to create project. Status code: {response.status_code}")
        print(response.text)

# Main function to parse arguments and call create_project
def main():
    # Create the parser
    parser = argparse.ArgumentParser(description="Create a new project in XNAT.")

    # Add arguments
    parser.add_argument("--xnat-url", required=True, help="URL of the XNAT instance")
    parser.add_argument("--username", required=True, help="XNAT admin username")
    parser.add_argument("--password", required=True, help="XNAT admin password")
    parser.add_argument("--project-id", required=True, help="Unique identifier for the new project")
    parser.add_argument("--project-name", required=True, help="Name of the new project")
    parser.add_argument("--project-description", default="", help="Description of the new project (optional)")

    # Parse the arguments
    args = parser.parse_args()

    # Call the function to create the project with parsed arguments
    create_project(
        args.xnat_url,
        args.username,
        args.password,
        args.project_id,
        args.project_name,
        args.project_description
    )

# Entry point
if __name__ == "__main__":
    main()
