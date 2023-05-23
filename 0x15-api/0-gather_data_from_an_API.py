#!/usr/bin/python3

"""This is a program to receive and display api get calls
   @author: Oke Oladunsi Samuel
   CreatedOn: 5/23/2023

"""

from requests import get
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    #cert_path = "usr/lib/ssl/certs/mycert.pem"
    # getting user personal info   
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = get(url) #verify=cert_path)
    """Employee_name = response.json()['name']

    # getting todo data
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    response = get(url)
    todo_list_info = response.json()
    completed_tasks = []
    count = 0

    for task in todo_list_info:
        if task['completed'] == True:
            count += 1
            completed_tasks.append(task['title'])
    # printing out the outcome
    print("Employee {} is done with tasks({}/{}):"
            .format(Employee_name, count, len(todo_list_info)))

    for compl_task in completed_tasks:
        print("\t {}".format(compl_task))"""
    print(response)
