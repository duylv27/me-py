# Creating a list
fruits = ["apple", "banana", "cherry"]

# Access elements
print(fruits[1])  # 'banana'

# Modify elements
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']

# Add elements
fruits.append("date")
print(fruits)  # ['apple', 'blueberry', 'cherry', 'date']

# Remove elements
fruits.append("blueberry")
fruits.remove("blueberry")
print(fruits)  # ['apple', 'cherry', 'date']

# Slicing
print(fruits[:2])  # ['apple', 'cherry']
