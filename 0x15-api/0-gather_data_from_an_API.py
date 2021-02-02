#!/usr/bin/python3
'''
using this REST API, for a given employee ID,
returns information about his/her TODO list progress
'''

if __name__ == "__main__":
    from requests import get
    from sys import argv

    id = argv[1]
    api_users = "https://jsonplaceholder.typicode.com/users/{}"
    api_todos = "https://jsonplaceholder.typicode.com/users/{}/todos"
    msg_title = "Employee {name} is done with tasks({done}/{total}):"
    msg_body = "\t {}"

    data = {
        "name": "",
        "done": 0,
        "total": 0,
        "tasks": []
    }
    data["name"] = get(api_users.format(id)).json().get("name")

    for r in get(api_todos.format(id)).json():
        data["total"] += 1
        if r.get("completed"):
            data["done"] += 1
            data["tasks"].append(r.get("title"))
    print(msg_title.format(**data))
    for task in data["tasks"]:
        print(msg_body.format(task))
