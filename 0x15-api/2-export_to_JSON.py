#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""
import csv
import json
import requests
import sys


if __name__ == "__main__":
    the_url = "https://jsonplaceholder.typicode.com/"
    tasks_com = []

    user = '{}users/{}'.format(the_url, sys.argv[1])
    requesting = requests.get(user)
    be_json = requesting.json()
    name = be_json['username']

    todos = '{}todos?userId={}'.format(the_url, sys.argv[1])
    requesting_todos = requests.get(todos)
    be_jsonTodos = requesting_todos.json()

    for x in be_jsonTodos:
        # print("{}, {}, {}, {}".format(sys.argv[1], name,
        # x['completed'], x['title']))
        dict_t = {"task": x['title'], "completed": x['completed'],
                  "username": name}
        tasks_com.append(dict_t)

    dicts_Id = {str(sys.argv[1]): tasks_com}

    # with open("sample.json", "w") as outfile:
    # json.dump(dictionary, outfile)

    with open('{}.json'.format(sys.argv[1]), "w") as outfile:
        json.dump(dicts_Id, outfile)
