import argparse 
from argparse import Namespace
import requests
import json

def parser_func() -> Namespace:
    parser = argparse.ArgumentParser(description = "Fetch the GitHub username from CLI")
    parser.add_argument('user_name', type = str, help = "The GitHub username to fetch user activity")

    args : Namespace = parser.parse_args()
    return args.user_name

def fetch_api(username : str) -> list[dict]:
    try:
        url = f'https://api.github.com/users/{username}/events'
        response = requests.get(url)
        if (response.status_code == 200):
            events : list[dict] = response.json()
            return events
        elif (response.status_code == 404):
            print(f"Username {username} not found")
        else:
            print("unable to fetch data")
    except:
        print("Error fetching the data")

def event_type(events : list[dict]):
    if not events:
        print("No events available")
        return
    
    event_types = {
        'PushEvent' : lambda event : print(f"Pushed {event['payload']['size']} commits into {event['repo']['name']}"),
        'CreateEvent' : lambda event : print(f"Created a new {event['payload']['ref_type']} in {event['repo']['name']}"),
        'ForkEvent' : lambda event : print(f"Forked from {event['payload']['forkee']}"),
        'WatchEvent' : lambda event : print(f"Starred {event['repo']['name']}")
    }

    for event in events:
        event_type = event['type']
        handler = event_types.get(event_type)

        if handler:
            handler(event)
        else:
            print(f"other event {event_type} in {event['repo']['name']}")


def main() -> None:
    username : str = parser_func()
    events : list[dict] = fetch_api(username)
    event_type(events)
    

if __name__ == '__main__':
    main()