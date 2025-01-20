import argparse 
from argparse import Namespace
import requests

def parser_func() -> Namespace:
    parser = argparse.ArgumentParser(description = "Fetch the GitHub username from CLI")
    parser.add_argument('user_name', type = str, help = "The GitHub username to fetch user activity")

    args : Namespace = parser.parse_args()
    return args.user_name

def fetch_api(username : str) -> list[dict]:
    url = f'https://api.github.com/users/{username}/events'
    response = requests.get(url)
    if (response.status_code == 200):
        events : list[dict] = response.json()
        return events
    elif (response.status_code == 404):
        print(f"Username {username} not found")
    else:
        print("unable to fetch data")

def event_type(events : list[dict]):
    for event in events:
        event_type : str = event['type']
        repo : str= event['repo']['name']
        if(event_type == 'PushEvent'):
            print(f"Pushed {event['payload']['size']} commits into {repo}")
        elif(event_type == 'CreateEvent'):
            print(f"Created a new {event['payload']['ref_type']} in {repo}")
        elif(event_type == 'ForkEvent'):
            print(f"Forked from {event['payload']['forkee']}")
        elif event_type == 'WatchEvent':
            print(f"Starred {repo}")
        else:
            print(f"other event {event_type} in {repo}")

def main() -> None:
    username : str = parser_func()
    events : list[dict] = fetch_api(username)
    event_type(events)
    
if __name__ == '__main__':
    main()