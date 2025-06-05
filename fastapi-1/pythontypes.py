def add(firstname : str | list[int], lastname: str = None):
    return firstname+" "+lastname


fname = "Bill"
lname = "Gates"

name = add(fname)
print(name)


def showNumbers(numberList : list[int, int, bool]):
    for i in numserList:
        print(i)

showNumbers([True, True, 3])