from pathlib import Path
import json


def get_stored_name(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def new_user(path):
    username = input("Enter your name: ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    path = Path('username.json')
    username = get_stored_name(path)
    if username:
        print(f"Hello {username.title()}, welcome back!")
    else:
        username = new_user(path)
        print(f"We will remember you {username.title()}!")

greet_user()
