import argparse 
from argparse import Namespace

def parser_func() -> Namespace:
    parser = argparse.ArgumentParser(description = "Fetch the GitHub username from CLI")
    parser.add_argument('user_name', type = str, help = "The GitHub username to fetch user activity")

    args : Namespace = parser.parse_args()
    return args

def main() -> None:
    args : Namespace = parser_func()
    
if __name__ == '__main__':
    main()