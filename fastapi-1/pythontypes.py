def add (firstname: str, lastname: str):
    return firstname.capitalize()+" "+lastname.capitalize()


fname = "bill"
lname = "test"

name = add(fname, lname)
print(name)