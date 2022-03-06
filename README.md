# Clash Royale official API usage example
The Clash Royale API provides near real time access to game related data. In order to access the API, you need a developer account and a key for your application. In this example, I sent an HTTP GET request to https://api.clashroyale.com/v1/cards to get the information about all the cards in the game.

All requests must have the API key as a argument:
```python
    ...
    
    api_key = {"Authorization": f"Bearer {token}"}
    request = requests.get("https://api.clashroyale.com/v1" + endpoint, api_key)
    
    ...
```
## Instructions <br>
In order to use the Clash Royale API you must:
1. Create account in https://developer.clashroyale.com and login to your account
2. Go to My account section at the top right
3. Click *Create New Key* 
4. Fill in the form

## Requirements
- Python 3.x (that I used)
- requests
- git

## Installation
For running this example:
    
    $ sudo apt update 
    $ sudo apt install python3 python3-pip
    $ git clone https://github.com/anthonyraf/clash-royale-api-example.git
    $ cd clash-royale-api-example
    $ pip install -r requirements.txt
    $ python3 main.py

> Go to : https://developer.clashroyale.com/#/getting-started for more information
