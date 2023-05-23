#!/usr/bin/python3

"""
   @author: Oke Oladunsi Samuel
   CreatedOn: 5/23/2023

   Python script to export in the Json format.

   Requirements:

   Records all tasks that are owned by this employee
   Format must be: { "USER_ID":
                     [{"task": "TASK_TITLE", 
                       "completed": TASK_COMPLETED_STATUS,
                       "username": "USERNAME"},
                     {"task": "TASK_TITLE",
                      "completed": TASK_COMPLETED_STATUS,
                      "username": "USERNAME"}, ... ]}
   File name must be: USER_ID.csv
"""

from requests import get
from sys import argv
from json import dump

if __name__ == "__main__":
    user_id = argv[1]
    # getting user personal info
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = get(url)
    Employee_name = response.json()['name']

    # getting todo data
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    response = get(url)
    todo_list_info = response.json()
    dump_dict = {user_id:  []}
    for task in todo_list_info:
        dump_dict[user_id].append({
                                   "task": task['title'],
                                   "completed": task['completed'],
                                   "username": Employee_name})

    with open('{}.json'.format(user_id), 'w') as file:
        dump(dump_dict, file)
