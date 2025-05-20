# What will be the output?
x = 10
y = "10"
print(x + int(y))

fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i + 1}: {fruit}")

person = {"name": "Alice", "age": 30}
print(person.get("name"))