import requests

url = 'https://api.restful-api.dev/objects'

headers = {
    'Authorization': 'Bearer <your_access_token>',  # Bearer token for authentication
    'Content-Type': 'application/json',  # The body content is JSON
    'Accept': 'application/json',  # The expected response format
    'User-Agent': 'MyApp/1.0',  # Identifying the client
    'X-API-Key': '<your_api_key>',  # Custom API Key authentication (if needed)
    'Accept-Encoding': 'gzip, deflate',  # Supports compressed responses
    'Cache-Control': 'no-cache',  # Ensuring the response is not cached
}

def get_data(url, headers):
    try:
        response = requests.get(url, headers)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()  # Parse the JSON data from the response
            print(data)  # Print or use the data
        else:
            print(f"Request failed with status code {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


get_data(url, headers)


def post_data(url, headers, body):
    response = requests.post(url, headers=headers, json=body)

# Handle the response
    if response.status_code == 200:
        print("User created successfully.")
        print("Response Data:", response.json())  # Print the server's response data (if applicable)
    elif response.status_code == 400:
        print("Bad request. Check the data sent.")
        print("Response:", response.text)
    elif response.status_code == 401:
        print("Unauthorized. Check your authentication credentials.")
    else:
        print(f"Failed to create user. Status Code: {response.status_code}")
        print("Response:", response.text)



body = {
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}

post_data(url, headers, body)