#  Phase 1 — Core Python

### Goal

By the end, you should be able to comfortably read and write Python code used in:

* NumPy
* Pandas
* scikit-learn
* PyTorch
* Jupyter notebooks
* ML experiments

We'll go **topic by topic**, with a short explanation → examples → small exercises.

---

## Topic 1 — Variables & Data Types

Python variables are names used to refer to values.

```python
name = "Anniee"
age = 21
height = 5.2
learning_ai = True
```

Python automatically determines the type.

The four basic types you'll use constantly:

| Type    | Example    | Use             |
| ------- | ---------- | --------------- |
| `int`   | `21`       | Integers        |
| `float` | `5.2`      | Decimal numbers |
| `str`   | `"Python"` | Text            |
| `bool`  | `True`     | True/False      |

Check a type with:

```python
print(type(age))
print(type(height))
```

### Type conversion

You'll frequently need this when processing datasets.

```python
x = "100"

x = int(x)

print(x)
print(type(x))
```

Other common conversions:

```python
int()
float()
str()
bool()
```

Example:

```python
price = "99.5"

price = float(price)
```

---

## Basic operators

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.333...
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

The ones worth remembering:

* `/` → division
* `//` → floor division
* `%` → remainder
* `**` → exponent

---

## Comparison operators

```python
x = 10

x == 10
x != 5
x > 5
x < 20
x >= 10
x <= 10
```

These produce a Boolean:

```python
True
False
```

You'll use these heavily in data filtering and ML preprocessing.

---

## Logical operators

```python
age = 25
has_degree = True

age > 18 and has_degree
```

Three important operators:

```python
and
or
not
```

---

#  Revision Exercise

Don't just look at the answers—write the code yourself.

### Exercise 1

Create variables for:

* your name
* your age
* your height
* whether you're learning AI/ML

Print their values and types.

### Exercise 2

Given:

```python
a = 15
b = 4
```

Print:

* addition
* subtraction
* multiplication
* division
* floor division
* remainder
* exponent

### Exercise 3

Given:

```python
temperature = 32
```

Create a Boolean variable that checks whether the temperature is greater than `30`.

### Exercise 4 — Small AI-flavored example

Imagine a model gives a prediction score:

```python
score = 0.87
```

Create a variable called `is_confident` that is `True` when the score is at least `0.80`.
