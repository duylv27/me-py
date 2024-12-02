# Creating a dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}

# Access value
print(person["name"])  # 'Alice'

# Add a new key-value pair
person["job"] = "Engineer"
person["name"] = "Duy"
print(person)  # {'name': 'Alice', 'age': 25, 'city': 'New York', 'job': 'Engineer'}

# Modify a value
person["age"] = 26

# Remove a key
del person["city"]
print(person)  # {'name': 'Alice', 'age': 26, 'job': 'Engineer'}

# Iterate
for key, value in person.items():
    print(f"{key}: {value}")