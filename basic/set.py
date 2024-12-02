# Creating a set
numbers = {1, 2, 3, 4}

# Add elements
numbers.add(5)
print(numbers)  # {1, 2, 3, 4, 5}

# Remove elements
numbers.discard(3)  # Safe: Does not raise an error if element doesn't exist
print(numbers)  # {1, 2, 4, 5}

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1.union(set2))        # {1, 2, 3, 4, 5}
print(set1.intersection(set2)) # {3}
print(set1.difference(set2))   # {1, 2}