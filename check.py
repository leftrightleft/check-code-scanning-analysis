import json
import requests

# Open the 'repo-list.json' file
with open('repo-list.json') as f:
    # Parse the JSON data into a Python object
    data = json.load(f)

# Loop through each item in the array
for item in data:
    # Extract the value of the 'nameWithOwner' key
    name_with_owner = item['nameWithOwner']
    
    # Construct the API endpoint URL using the extracted value
    url = f'https://api.github.com/repos/{name_with_owner}/code-scanning/analyses'
    
    # Set the required headers
    headers = {
        'Accept': 'application/vnd.github+json',
        'Authorization': 'Bearer <YOUR TOKEN HERE>',
        'X-GitHub-Api-Version': '2022-11-28'
    }
    
    # Make a GET request to the API endpoint URL with the headers
    response = requests.get(url, headers=headers)
    
# Handle the response as needed
    if response.status_code == 200:
        json_data = response.json()
        for item in json_data:
            error = item.get('error', '')
            if error != '':
                print(f'{name_with_owner}: {error}')
            # print(f'{name_with_owner}: {error}')
    else:
        print(f'{name_with_owner}: {response.status_code} - {response.text}')
