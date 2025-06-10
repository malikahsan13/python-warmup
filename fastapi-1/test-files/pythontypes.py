class Person:
    def __init__(self, name: str):
        self.name = name

    
def get_person_name(one_person: Person):
    return one_person.name.capitalize()

p1 = Person("test")
print(get_person_name(p1))
        