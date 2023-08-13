#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import json
import requests
import sys


if __name__ == "__main__":
    the_url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users'.format(the_url)
    requesting = requests.get(user)
    be_json = requesting.json()

    dicts_all = {}

    for y in be_json:
        name = y.get('username')
        user_Id = y.get('id')

        todos = '{}todos?userId={}'.format(the_url, user_Id)
        resquesting_Todos = requests.get(todos)
        tasks = resquesting_Todos.json()
        list_task = []

        for x in tasks:
            dict_tasks = {"username": name,
                          "task": x.get('title'),
                          "completed": x.get('completed')}
            list_task.append(dict_tasks)

        dicts_all[str(user_Id)] = list_task

    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as f:
        json.dump(dicts_all, f)
