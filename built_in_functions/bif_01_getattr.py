'''
The getattr() method returns the value of the named
attribute of an object. If not found, it returns the
default value provided to the function.
'''


class Student:
    marks: int = 88
    name: str = 'Sheeran'


person = Student()

name = getattr(person, 'name')
print(name)
print(person.name)

marks = getattr(person, 'marks')
print(marks)
print(person.marks)


# if the object has not the specified attribute
# it returns the default value given to it
sex = getattr(person, 'sex', 'Male')
print(sex)


