#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""
import requests
import sys
import csv


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
        tasks_com.append([sys.argv[1], name, x['completed'], x['title']])

    with open("{}.csv".format(sys.argv[1]), 'w') as file:
        writing = csv.writer(file, quoting=csv.QUOTE_ALL)

        for y in tasks_com:
            writing.writerow(y)
