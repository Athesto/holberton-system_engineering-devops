#!/usr/bin/python3
'''
using this REST API, for a given employee ID,
returns information about his/her TODO list progress
'''


def main():
    '''main file'''
    getinfo("urllib")
    # getinfo("requests")


def getinfo(option):
    '''get info'''
    from sys import argv
    methods = {'urllib': urllib_method, 'requests': requests_method}
    api_users = "https://jsonplaceholder.typicode.com/users/{id}"
    api_todos = "https://jsonplaceholder.typicode.com/users/{id}/todos"
    msg_title = "Employee {name} is done with tasks({done}/{total}):"
    msg_body = "\t {}"
    data = {
        "id": argv[1],
        "name": "",
        "done": 0,
        "total": 0,
        "tasks": []
    }
    info = methods[option](api_users, data)
    data.update(name=info.get("name"))
    info = methods[option](api_todos, data)
    for r in info:
        data["total"] += 1
        if r.get("completed"):
            data["done"] += 1
            data["tasks"].append(r.get("title"))
    print(msg_title.format(**data))
    for task in data["tasks"]:
        print(msg_body.format(task))


def requests_method(url, data):
    '''this options works with requests module'''
    from requests import get

    return get(url.format(**data)).json()


def urllib_method(url, data):
    '''this option use urllib'''
    from json import loads
    from urllib import request

    with request.urlopen(url.format(**data)) as r:
        info = loads(r.read().decode())
    return info


if __name__ == "__main__":
    main()
