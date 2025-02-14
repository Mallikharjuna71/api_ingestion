import requests

url = 'https://api.restful-api.dev/objects'

headers = {
    'Authorization': 'Bearer <your_access_token>', 
    'Content-Type': 'application/json',  
    'Accept': 'application/json', 
    'User-Agent': 'MyApp/1.0',  
    'X-API-Key': '<your_api_key>',  
    'Accept-Encoding': 'gzip, deflate',  
    'Cache-Control': 'no-cache',  
}

def get_data(url, headers):
    try:
        response = requests.get(url, headers)
        if response.status_code == 200:
            data = response.json()  
            print(data)
        else:
            print(f"Request failed with status code {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")


get_data(url, headers)


def post_data(url, headers, body):
    response = requests.post(url, headers=headers, json=body)

# Handle the response
    if response.status_code == 200:
        print("User created successfully.")
        print("Response Data:", response.json())  
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