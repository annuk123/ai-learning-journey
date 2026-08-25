# Exercise 2 — Update

# Using the same dictionary, change:

# accuracy → 0.95

# Then print the dictionary.

model = {
    "name": "Random Forest",
    "accuracy": 0.92,
    "epochs": 50
}

model["accuracy"] = 0.95

print(model["accuracy"])