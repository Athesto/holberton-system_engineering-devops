#!/usr/bin/python3
'''save into csv'''
from requests import get
from sys import argv

if __name__ == '__main__':
    api_users = "https://jsonplaceholder.typicode.com/users/{id}"
    api_todos = "https://jsonplaceholder.typicode.com/users/{id}/todos"
    csv_format = ['"{id}","{username}",', '"{completed}","{title}"']
    data = {
        "id": argv[1],
        "username": "",
        "tasks": []
    }
    info = get(api_users.format(**data)).json()
    data.update(username=info.get('username'))
    info = get(api_todos.format(**data)).json()
    for element in info:
        data['tasks'].append(
            {
                'completed': element.get('completed'),
                'title': element.get('title')
            })
    with open('{id}.csv'.format(**data), 'w') as f:
        a = csv_format[0].format(**data)
        for element in data["tasks"]:
            b = csv_format[1].format(**element)
            print(a+b, file=f)
