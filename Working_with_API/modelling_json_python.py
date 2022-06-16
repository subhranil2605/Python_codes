import json


# Student class
class Student:
    def __init__(self, id_, name, phone):
        self.id_ = id_
        self.name = name
        self.phone = phone


    # convert a string that generated from json to a Student instance 
    @staticmethod
    def from_json_to_class(json):
        return Student(json["id"], json["name"], json["phone_number"])


    # convert a Student instance into a python dictionary that can be used in JSON
    def from_student_to_json(self):
        return {"id": self.id_, "name": self.name, "phone_number": self.phone}



# returns a list of Student instance
def student_from_json(s: str):
    return list(map(Student.from_json_to_class, s))
    

# returns a list of dictionary
def student_to_json(s):
    return list(map(Student.from_student_to_json, s))




"""
This data can be coming from an API
So, it simulates a data created by API
=--------------------data.json--------------------=
[
    {
        "id": 1,
        "name": "Subhranil Sarkar",
        "phone_number": "6294769160"
    },
    {
        "id": 2,
        "name": "Ashik Mamun",
        "phone_number": "7477575205"
    },
    {
        "id": 3,
        "name": "Chinmoy Biswas",
        "phone_number": "9474595912"
    }
]
"""

# reading the json file in python and stored the data
with open("data.json", 'r') as f:
    data = json.load(f)



student_class_list = student_from_json(data)

student_json = student_to_json(student_class_list)

print(student_json)








    

