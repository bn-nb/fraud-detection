# Testing the API, run from another script

import requests

# Example input data
input_data = {
    "amount": 987895.45,
    "toMerc": False,
    "oldOrg": 100,
    "newOrg": 100,
    "oldDst": 100,
    "newDst": 78548500,
}

# Send POST request to your FastAPI app
# Copy Public NGROK url here before running
response = requests.post("", json=input_data)

# Print the prediction returned by the API
print(response.json())
