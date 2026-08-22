#  Phase 1 — Topic 4: Tuples

Tuples are similar to lists, but there is one major difference:

> **Lists are mutable; tuples are immutable.**

Since this is a revision for AI/ML, we only need the practical parts.

---

## 1. Creating a Tuple

```python
coordinates = (10, 20)
```

You can have multiple values:

```python
data = ("Annu", 20, "AI/ML")
```

You can check its type:

```python
print(type(data))
```

Output:

```text
<class 'tuple'>
```

---

## 2. Indexing

Tuples work like lists when accessing elements:

```python
data = ("Annu", 20, "AI/ML")

print(data[0])
print(data[1])
print(data[-1])
```

Output:

```text
Annu
20
AI/ML
```

---

## 3. Slicing

Also just like lists:

```python
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
```

Output:

```text
(20, 30, 40)
```

---

## 4. Tuples Are Immutable

This is the important part.

You **cannot** do:

```python
data = ("Annu", 20)

data[1] = 21
```

That produces an error.

If you need to modify the collection, you'd generally create a new tuple.

```python
data = ("Annu", 21)
```

Don't worry about the deeper implementation yet.

---

## 5. Why Use Tuples?

Tuples are useful when you have a collection of values that shouldn't be changed.

For example:

```python
image_size = (224, 224)
```

This is something you'll actually encounter in computer vision.

Another example:

```python
coordinates = (10, 20)
```

---

# 6. Tuple Unpacking

This is worth learning because you'll see it frequently in Python and ML code.

```python
data = ("Annu", 20, "AI/ML")

name, age, field = data

print(name)
print(age)
print(field)
```

Python assigns the values in order:

```text
name  → "Annu"
age   → 20
field → "AI/ML"
```

You can also do:

```python
x, y = (10, 20)
```

Very convenient.

---

## 7. One-Element Tuple

There's a small Python gotcha:

```python
x = (10)
```

That's just an integer.

```python
type(x)
```

gives:

```text
int
```

For a one-element tuple, you need the comma:

```python
x = (10,)
```

Now:

```python
type(x)
```

is:

```text
tuple
```

You don't need to memorize this deeply, but it's a useful Python detail.

---

#  Exercises

### Exercise 1

Create a tuple containing:

```text
Python
NumPy
Pandas
PyTorch
```

Print the tuple and its type.

### Exercise 2

Given:

```python
dimensions = (1920, 1080)
```

Print:

* Width
* Height

using indexing.

### Exercise 3

Given:

```python
model_info = ("Neural Network", 10, 0.95)
```

Use **tuple unpacking** to store these into:

```text
model
epochs
accuracy
```

Then print all three.

### Exercise 4

What happens when you run:

```python
data = ("AI", "ML")
data[0] = "Python"
```

You don't need to reproduce the entire error message. Just tell me **why** it happens.

