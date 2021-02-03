#!/usr/bin/python3
'''export into json'''
from json import dumps
from requests import get
from sys import argv

if __name__ == '__main__':
    api_users = "https://jsonplaceholder.typicode.com/users"
    api_todos = "https://jsonplaceholder.typicode.com/todos"
    user_data = {}
    json_obj = {}

    info = get(api_users).json()
    for element in info:
        tmp = {}
        tmp['id'] = element.get('id')
        tmp['username'] = element.get('username')
        user_data[element.get('id')] = tmp
        json_obj[element.get('id')] = []

    print(dumps(user_data, indent=2))

    info = get(api_todos).json()
    for element in info:
        my_id = element.get('userId')
        json_obj[my_id].append(
            {
                'username': user_data.get(my_id).get('username'),
                'completed': element.get('completed'),
                'task': element.get('title')
            })
    print(dumps(json_obj, indent=2))
    with open('todo_all_employees.json', 'w') as f:
        print(dumps(json_obj), file=f)
