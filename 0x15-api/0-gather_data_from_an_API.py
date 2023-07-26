#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


if __name__ == "__main__":
    the_url = "https://jsonplaceholder.typicode.com/"
    tasks_com = []

    user = '{}users/{}'.format(the_url, sys.argv[1])
    requesting = requests.get(user)
    be_json = requesting.json()

    print("Employee {} is done with tasks".format(be_json['name']), end="")

    todos = '{}todos?userId={}'.format(the_url, sys.argv[1])
    requesting_todos = requests.get(todos)
    be_jsonTodos = requesting_todos.json()

    for x in be_jsonTodos:
        if x['completed'] is True:
            tasks_com.append(x['completed'])

    print("({}/{}):".format(len(tasks_com), len(be_jsonTodos)))

    for y in be_jsonTodos:
        print("\t {}".format(y['title']))
