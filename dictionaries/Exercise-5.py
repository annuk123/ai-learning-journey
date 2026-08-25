# Exercise 5 — Nested Dictionary

# Given:

# experiment = {
#     "model": {
#         "name": "CNN",
#         "layers": 5
#     },
#     "training": {
#         "epochs": 20,
#         "batch_size": 32
#     }
# }

# Print:

# The model name.
# The number of layers.
# The batch size.



experiment = {
    "model": {
        "name": "CNN",
        "layers": 5
    },
    "training": {
        "epochs": 20,
        "batch_size": 32
    }
}

print(experiment["model"]["name"])
print(experiment["model"]["layers"])
print(experiment["training"]["batch_size"])