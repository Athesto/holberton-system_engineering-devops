#!/usr/bin/python3
'''export into json'''
from json import dumps
from requests import get
from sys import argv

if __name__ == '__main__':
    api_users = "https://jsonplaceholder.typicode.com/users/{id}"
    api_todos = "https://jsonplaceholder.typicode.com/users/{id}/todos"
    data = {
        "id": argv[1],
        "username": "",
    }
    json_obj = {
        data.get('id'): []
    }

    info = get(api_users.format(**data)).json()
    data.update(username=info.get('username'))
    info = get(api_todos.format(**data)).json()
    for element in info:
        json_obj[data.get('id')].append(
            {
                'username': data.get('username'),
                'completed': element.get('completed'),
                'title': element.get('title')
            })
    with open('{id}.json'.format(**data), 'w') as f:
        print(dumps(json_obj), file=f)
