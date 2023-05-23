#!/usr/bin/python
"""program to receive and display api get calls
   @author: Oke Oladunsi Samuel
   CreatedOn: 5/23/2023

"""

from requests import get
from sys import argv
import csv

if __name__ == "__main__":
    user_id = argv[1]
    #cert_path = "usr/lib/ssl/certs/mycert.pem"
    # getting user personal info
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = get(url) #verify=cert_path)
    Employee_name = response.json()['name']

    # getting todo data
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    response = get(url)
    todo_list_info = response.json()
    tasks = {}
    tmp = []
    c = 0
    with open('{}.csv'.format(user_id), 'w') as file:
            for task in todo_list_info:
                file.write('"{}","{}","{}","{}"\n'.format(user_id, Employee_name, task['completed'], task['title']))
