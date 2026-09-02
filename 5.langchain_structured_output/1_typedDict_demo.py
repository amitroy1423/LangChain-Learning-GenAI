from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

new_person1: Person = { 'name': "Amit", 'age': 20 }
new_person2: Person = { 'name': "Bob", 'age': "21" }#--> print inspiteof type error


print(new_person1)
print(new_person2)#-->not give error at runtime, but will give error in type checking tools like mypy or pyright