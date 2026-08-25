#  Phase 1 — Topic 6: Dictionaries

Dictionaries are **very important** for AI/ML because they store data as **key → value** pairs.

For example:

```python
model_config = {
    "learning_rate": 0.001,
    "batch_size": 32,
    "epochs": 10
}
```

Think of it like:

```text
"learning_rate" → 0.001
"batch_size"    → 32
"epochs"        → 10
```

---

## 1. Creating a Dictionary

```python
student = {
    "name": "Annu",
    "age": 20,
    "field": "AI/ML"
}

print(student)
```

Each item has:

```text
key : value
```

For example:

```python
"name": "Annu"
```

* `"name"` → key
* `"Annu"` → value

---

## 2. Accessing Values

Use the key:

```python
student = {
    "name": "Annu",
    "age": 20
}

print(student["name"])
print(student["age"])
```

Output:

```text
Annu
20
```

Unlike lists, you generally don't access dictionaries using positions like `[0]`.

---

## 3. Updating a Value

```python
student = {
    "name": "Annu",
    "age": 20
}

student["age"] = 21

print(student)
```

The value for `"age"` is updated.

---

## 4. Adding a New Key-Value Pair

```python
student = {
    "name": "Annu"
}

student["field"] = "AI/ML"

print(student)
```

Now the dictionary contains:

```python
{
    "name": "Annu",
    "field": "AI/ML"
}
```

---

## 5. Removing Items

### `pop()`

```python
student = {
    "name": "Annu",
    "age": 20
}

student.pop("age")

print(student)
```

This removes the `"age"` key and its value.

---

### `del`

```python
del student["age"]
```

Also removes the item.

For now, just remember both exist.

---

# 6. `.keys()`, `.values()`, `.items()`

Given:

```python
model = {
    "name": "Neural Network",
    "epochs": 10,
    "accuracy": 0.95
}
```

### Keys

```python
print(model.keys())
```

Gives the keys.

### Values

```python
print(model.values())
```

Gives the values.

### Items

```python
print(model.items())
```

Gives key-value pairs.

You'll often loop through `.items()`:

```python
for key, value in model.items():
    print(key, value)
```

Output conceptually:

```text
name Neural Network
epochs 10
accuracy 0.95
```

---

# 7. Checking Whether a Key Exists

```python
model = {
    "learning_rate": 0.001,
    "batch_size": 32
}

print("learning_rate" in model)
print("epochs" in model)
```

Output:

```text
True
False
```

---

# 8. `.get()` — Useful and Safer

Normally:

```python
print(model["epochs"])
```

If `"epochs"` doesn't exist, Python raises an error.

Instead:

```python
print(model.get("epochs"))
```

This returns:

```text
None
```

You can also provide a default:

```python
epochs = model.get("epochs", 10)

print(epochs)
```

If `"epochs"` doesn't exist, it uses `10`.

This is useful when dealing with messy JSON/API/dataset data.

---

# 9. Nested Dictionaries

You'll encounter these in configuration files and API responses.

```python
experiment = {
    "model": {
        "name": "Neural Network",
        "layers": 3
    },
    "training": {
        "epochs": 10,
        "learning_rate": 0.001
    }
}
```

Access nested values like:

```python
print(experiment["model"]["name"])
```

Output:

```text
Neural Network
```

---

#  Exercises

### Exercise 1 — Accessing

```python
model = {
    "name": "Random Forest",
    "accuracy": 0.92,
    "epochs": 50
}
```

Print:

* Model name
* Accuracy

---

### Exercise 2 — Update

Using the same dictionary, change:

```text
accuracy → 0.95
```

Then print the dictionary.

---

### Exercise 3 — Add

Add:

```text
learning_rate → 0.01
```

Then print the dictionary.

---

### Exercise 4 — Looping

Given:

```python
config = {
    "batch_size": 32,
    "epochs": 10,
    "learning_rate": 0.001
}
```

Use a `for` loop with `.items()` to print every key and value.

---

### Exercise 5 — Nested Dictionary

Given:

```python
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
```

Print:

1. The model name.
2. The number of layers.
3. The batch size.
