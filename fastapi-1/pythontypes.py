def add(firstname : str | list, lastname: str = None):
    return firstname+" "+lastname


fname = "Bill"
lname = "Gates"

name = add(fname)
print(name)