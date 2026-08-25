#  Phase 1 — Topic 5: Sets

Sets are simpler than lists and tuples. For your AI/ML revision, focus on one core idea:

> **A set stores unique values.**

---

## 1. Creating a Set

```python
numbers = {1, 2, 3, 4}
```

You can also create one using `set()`:

```python
numbers = set([1, 2, 3, 4])
```

---

## 2. Duplicate Values

Sets automatically remove duplicates.

```python
numbers = {1, 2, 2, 3, 3, 3, 4}

print(numbers)
```

Output:

```text
{1, 2, 3, 4}
```

This is one of the main reasons to use sets.

For example, imagine dataset labels:

```python
labels = ["cat", "dog", "cat", "bird", "dog"]

unique_labels = set(labels)

print(unique_labels)
```

Result contains:

```text
cat, dog, bird
```

**Note:** Sets are unordered, so don't depend on the printed order.

---

# 3. Adding Elements

Use `.add()`:

```python
models = {"Linear Regression", "Decision Tree"}

models.add("Neural Network")

print(models)
```

---

# 4. Removing Elements

### `remove()`

```python
models = {"Linear Regression", "Decision Tree"}

models.remove("Decision Tree")
```

If the item doesn't exist, `remove()` raises an error.

### `discard()`

```python
models.discard("Decision Tree")
```

If the item doesn't exist, no error occurs.

For revision, just remember:

* `remove()` → errors if missing
* `discard()` → safely does nothing if missing

---

# 5. Set Operations

This is the most interesting part.

Suppose:

```python
python_skills = {"Python", "NumPy", "Pandas"}
ml_skills = {"Python", "PyTorch", "NumPy"}
```

### Union

All unique elements from both:

```python
all_skills = python_skills | ml_skills
```

You can also use:

```python
all_skills = python_skills.union(ml_skills)
```

---

### Intersection

Elements present in **both**:

```python
common_skills = python_skills & ml_skills
```

Result:

```text
{"Python", "NumPy"}
```

---

### Difference

Elements in the first set but not the second:

```python
only_python = python_skills - ml_skills
```

Result:

```text
{"Pandas"}
```

---

# 6. Checking Membership

```python
skills = {"Python", "NumPy", "PyTorch"}

print("Python" in skills)
print("Java" in skills)
```

Output:

```text
True
False
```

---

# 7. Empty Set Gotcha

This:

```python
data = {}
```

creates an **empty dictionary**, not a set.

To create an empty set:

```python
data = set()
```

Worth remembering because it's a common mistake.

---

#  Exercises

### Exercise 1 — Remove Duplicates

```python
numbers = [1, 2, 2, 3, 4, 4, 5, 5]
```

Convert this into a set and print the result.

---

### Exercise 2 — Adding

```python
skills = {"Python", "NumPy"}
```

Add `"PyTorch"`.

---

### Exercise 3 — Union

```python
set_a = {"Python", "NumPy", "Pandas"}

set_b = {"NumPy", "PyTorch", "TensorFlow"}
```

Create a new set containing all unique elements.

---

### Exercise 4 — Intersection

Using the same sets, find the elements that exist in both.

---

### Exercise 5 — Difference

Using the same sets, find the elements that exist in `set_a` but **not** in `set_b`.

