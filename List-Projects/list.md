#  Phase 1 — Topic 3: Lists

Lists are one of the most important Python data structures to revise before moving into **NumPy**.

A list stores multiple values:

```python
numbers = [10, 20, 30, 40]
```

You can also store different types:

```python
data = [10, "Annu", 5.2, True]
```

For AI/ML, you'll more commonly see lists like:

```python
features = [25, 170, 65]
labels = ["cat", "dog", "cat"]
```

---

## 1. Indexing

Just like strings, lists start at index `0`.

```python
numbers = [10, 20, 30, 40]

print(numbers[0])   # 10
print(numbers[2])   # 30
print(numbers[-1])  # 40
```

---

## 2. Slicing

```python
numbers = [10, 20, 30, 40, 50]

print(numbers[1:4])
```

Output:

```python
[20, 30, 40]
```

Remember: the ending index is **not included**.

---

# 3. Updating Elements

Unlike strings, lists are **mutable**.

```python
numbers = [10, 20, 30]

numbers[1] = 99

print(numbers)
```

Output:

```python
[10, 99, 30]
```

---

# 4. Adding Elements

### `append()`

Adds **one item** to the end.

```python
numbers = [1, 2, 3]

numbers.append(4)

print(numbers)
```

Result:

```python
[1, 2, 3, 4]
```

### `extend()`

Adds multiple elements from another iterable.

```python
numbers = [1, 2, 3]

numbers.extend([4, 5, 6])

print(numbers)
```

Result:

```python
[1, 2, 3, 4, 5, 6]
```

Important difference:

```python
numbers.append([4, 5])
```

Produces:

```python
[1, 2, 3, [4, 5]]
```

But:

```python
numbers.extend([4, 5])
```

Produces:

```python
[1, 2, 3, 4, 5]
```

This distinction is worth remembering.

---

# 5. `insert()`

Add an item at a specific index.

```python
numbers = [10, 20, 40]

numbers.insert(2, 30)

print(numbers)
```

Output:

```python
[10, 20, 30, 40]
```

The pattern is:

```python
list.insert(index, value)
```

---

# 6. Removing Elements

### `remove()`

Removes by **value**:

```python
numbers = [10, 20, 30]

numbers.remove(20)

print(numbers)
```

Result:

```python
[10, 30]
```

### `pop()`

Removes by **index** and returns the removed value:

```python
numbers = [10, 20, 30]

removed = numbers.pop(1)

print(removed)
print(numbers)
```

Output:

```python
20
[10, 30]
```

If you don't give an index:

```python
numbers.pop()
```

It removes the last item.

---

# 7. `len()`

```python
numbers = [10, 20, 30]

print(len(numbers))
```

Output:

```text
3
```

---

# 8. Sorting

### `.sort()`

Changes the original list:

```python
numbers = [5, 2, 8, 1]

numbers.sort()

print(numbers)
```

Output:

```python
[1, 2, 5, 8]
```

### `sorted()`

Returns a new sorted list:

```python
numbers = [5, 2, 8, 1]

new_numbers = sorted(numbers)

print(new_numbers)
print(numbers)
```

The original list remains unchanged.

---

# 9. Looping Through a List

```python
numbers = [10, 20, 30]

for number in numbers:
    print(number)
```

This will become very natural when processing datasets.

---

# 10. List Comprehension

Very common in Python and useful to understand before NumPy.

Suppose:

```python
numbers = [1, 2, 3, 4]
```

You want the square of every number.

Normal approach:

```python
squares = []

for number in numbers:
    squares.append(number ** 2)
```

List comprehension:

```python
squares = [number ** 2 for number in numbers]
```

Result:

```python
[1, 4, 9, 16]
```

You can also add conditions:

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [n for n in numbers if n % 2 == 0]
```

Result:

```python
[2, 4, 6]
```

---

#  Exercises

### Exercise 1 — Indexing and Updating

```python
models = ["Linear Regression", "Decision Tree", "Neural Network"]
```

1. Print `"Decision Tree"`.
2. Change `"Decision Tree"` to `"Random Forest"`.
3. Print the updated list.

---

### Exercise 2 — Adding Elements

Start with:

```python
numbers = [1, 2, 3]
```

1. Add `4` using `append()`.
2. Add `[5, 6, 7]` using `extend()`.

What should the final list be?

---

### Exercise 3 — Removing Elements

```python
data = [10, 20, 30, 40, 50]
```

1. Remove `20` using `remove()`.
2. Remove the last element using `pop()`.
3. Print the final list.

---

### Exercise 4 — Sorting

```python
scores = [87, 45, 92, 60, 78]
```

Create a **new sorted list** without changing the original list.

Print both lists.

---

### Exercise 5 — List Comprehension

Given:

```python
numbers = [1, 2, 3, 4, 5]
```

Use a list comprehension to create:

```python
[1, 4, 9, 16, 25]
```


