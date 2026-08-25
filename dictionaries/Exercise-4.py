# Exercise 4 — Looping

# Given:

# config = {
#     "batch_size": 32,
#     "epochs": 10,
#     "learning_rate": 0.001
# }

# Use a for loop with .items() to print every key and value.


config = {
    "batch_size": 32,
    "epochs": 10,
    "learning_rate": 0.001
}

for key, value in config.items():
    print(key, value)
