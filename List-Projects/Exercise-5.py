# Exercise 5 — List Comprehension

# Given:

# numbers = [1, 2, 3, 4, 5]

# Use a list comprehension to create:

# [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers]
print(squares)
# for number in numbers:
#    squares.append(number ** 2)

