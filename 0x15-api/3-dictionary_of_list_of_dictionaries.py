#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com to return information about all
employee's todo list progress
"""

import json
import requests

if __name__ == '__main__':
    users = requests.get("https://jsonplaceholder.typicode.com/users",
                         verify=False).json()
    userdict = {}
    usernamedict = {}
    for user in users:
        uid = user.get("id")
        userdict[uid] = []
        usernamedict[uid] = user.get("username")
    todo = requests.get("https://jsonplaceholder.typicode.com/todos",
                        verify=False).json()
    for task in todo:
        taskdict = {}
        uid = task.get("userId")
        taskdict["task"] = task.get('title')
        taskdict["completed"] = task.get('completed')
        taskdict["username"] = usernamedict.get(uid)
        userdict.get(uid).append(taskdict)
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(userdict, jsonfile)
