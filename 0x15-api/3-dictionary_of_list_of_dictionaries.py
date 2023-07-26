#!/usr/bin/python3
import csv
import json
import requests
import sys

"""
Python script to export data in the JSON format
"""

"""
if __name__ == "__main__":
    the_url = "https://jsonplaceholder.typicode.com/"
    tasks_com = []
    dicts_Id = {}
    # dicts_all = {}
    # tasks_all = []

    user = '{}users'.format(the_url)
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
            dict_t = {"username": name, "task": x['title'],
                      "completed": x['completed']}
            tasks_com.append(dict_t)
        # print(tasks_com)

        dicts_Id[str(user_Id)] = tasks_com

        # tasks_all.append(dicts_Id)

        # dicts_all[str(user_Id)] = tasks_all

        with open("todo_all_employees.json", "w") as outfile:
            json.dump(dicts_Id, outfile)
"""
if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = '{}users'.format(url)
    res = requests.get(user)
    json_o = res.json()
    d_task = {}
    for user in json_o:
        name = user.get('username')
        userid = user.get('id')
        todos = '{}todos?userId={}'.format(url, userid)
        res = requests.get(todos)
        tasks = res.json()
        l_task = []
        for task in tasks:
            dict_task = {"username": name,
                         "task": task.get('title'),
                         "completed": task.get('completed')}
            l_task.append(dict_task)

        d_task[str(userid)] = l_task
    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as f:
        json.dump(d_task, f)
