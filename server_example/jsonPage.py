#!/usr/bin/python3

import json  # JSON serialisointi ja deserialisointi
from json import JSONEncoder


class Person():
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName


class PersonEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


print("Content-type: application/json\n")

people = []
people.append(Person("Michael", "Jordan"))
people.append(Person("Scottie", "Pippen"))

jsonData = json.dumps(people, indent=2, cls=PersonEncoder)

print(jsonData)
