
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age


    # To make the Person work well in data structures like dictionaries,
    # the hash of the class should remain immutable. To do it,
    # you can make the age attribute of the Person class a read-only
    @property
    def age(self):
        return self._age

    """
    If a class overrides the __eq__ method,
    the objects of the class become unhashable
    """
    def __eq__(self, other):
        return isinstance(other, Person) and self.age == other.age

    def __hash__(self):
        return hash(self.age)


p1 =  Person("Subhranil", 23)
p2 =  Person("Towasum", 22)


# hash() method returns the hash value of an integer.
print(hash(p1))
print(hash(p2))

print(p1 == p2)
