import requests
import json

#This is the json web token generated from your developer.clashroyale.com account
file = open("token.txt", "r")

token = file.read().strip('\n')

file.close()

base_url = "https://api.clashroyale.com/v1"
# This is an example of enpoint of the reqest, for more check the documentation
endpoint = "/cards"

# Correct Authorization header looks like this: "Authorization: Bearer API_TOKEN".
query = {"Authorization": f"Bearer {token}"}

# Send the GET request
response = requests.get(base_url+endpoint, params=query)

# Save the jsonresponse in json file
with open("example_response.json", "w") as response_file:
    r : dict = response.json()
    
    # For pretty output
    p : str= json.dumps(r, indent=4)
    response_file.write(p)
