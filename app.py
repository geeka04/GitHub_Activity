import argparse 
from argparse import Namespace
import requests
import json

def parser_func() -> Namespace:
    parser = argparse.ArgumentParser(description = "Fetch the GitHub username from CLI")
    parser.add_argument('user_name', type = str, help = "The GitHub username to fetch user activity")

    args : Namespace = parser.parse_args()
    return args.user_name

def fetch_api(username : str):
    url = f'https://api.github.com/users/{username}/events'
    response = requests.get(url)
    events = response.json()
    return events

def main() -> None:
    username : str = parser_func()
    event = fetch_api(username)
    print(event)

if __name__ == '__main__':
    main()