import pandas as pd  # Common convention

data = pd.Series([10, 20, 30, 40])
print(data)

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Tokyo"]
}
df = pd.DataFrame(data)
print(df)