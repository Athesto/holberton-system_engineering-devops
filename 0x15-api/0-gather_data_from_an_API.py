#!/usr/bin/python3
'''
using this REST API, for a given employee ID,
returns information about his/her TODO list progress
'''

if __name__ == "__main__":
    from requests import get
    from sys import argv

    id = argv[1]
    api_name = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    api_todo = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)

    data = {
        "name": "",
        "done": 0,
        "total": 0,
        "tasks": []
    }
    response = get(api_name)
    data["name"] = response.json().get("name")

    responses = get(api_todo)
    for r in responses.json():
        data["total"] += 1
        if r.get("completed"):
            data["done"] += 1
            data["tasks"].append(r.get("title"))
    msg = "Employee {name} is done with tasks({done}/{total}):"
    print(msg.format(**data))
    for task in data["tasks"]:
        print("\t {}".format(task))
