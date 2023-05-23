#!/usr/bin/python3

"""
   @author: Oke Oladunsi Samuel
   CreatedOn: 5/23/2023

   Python script to export data in the CSV format.

   Requirements:

   Records all tasks that are owned by this employee
   Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
   File name must be: USER_ID.csv
"""

from requests import get
from sys import argv
import csv

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
    with open('{}.csv'.format(user_id), 'w') as file:
        for task in todo_list_info:
            file.write('"{}","{}","{}","{}"\n'
                       .format(user_id, Employee_name, task['completed'], \n
                               task['title']))
