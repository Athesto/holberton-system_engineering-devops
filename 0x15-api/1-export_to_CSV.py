#!/usr/bin/python3
'''save into csv'''
from requests import get
from sys import argv

api_users = "https://jsonplaceholder.typicode.com/users/{id}"
api_todos = "https://jsonplaceholder.typicode.com/users/{id}/todos"
csv_format = ['"{id}","{name}",', '"{completed}","{title}"']
data = {
    "id": argv[1],
    "name": "",
    "tasks": []
}
info = get(api_users.format(**data)).json()
data.update(name=info.get('name'))
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
