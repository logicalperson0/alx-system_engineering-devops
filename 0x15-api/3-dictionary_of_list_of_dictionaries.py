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
    dicts_Id = {}

    user = '{}users/'.format(the_url)
    requesting = requests.get(user)
    be_json = requesting.json()
    # name = be_json['username']

    for y in be_json:
        name = y['username']
        user_Id = y['id']

        todos = '{}todos?userId={}'.format(the_url, user_Id)
        requesting_todos = requests.get(todos)
        be_jsonTodos = requesting_todos.json()

        for x in be_jsonTodos:
            dict_t = {"task": x['title'], "completed": x['completed'],
                      "username": name}
            tasks_com.append(dict_t)
        # print(tasks_com)

        dicts_Id[str(user_Id)] = tasks_com

        with open("todo_all_employees.json", "w") as outfile:
            json.dump(dicts_Id, outfile)
