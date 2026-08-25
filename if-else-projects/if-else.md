#  Phase 1 — Topic 7: `if / elif / else`

This is a **quick revision**. The main goal is to get comfortable writing conditions, because you'll use them constantly in normal Python and data-processing code.

## 1. Basic `if`

```python
age = 20

if age >= 18:
    print("Adult")
```

The code inside the `if` runs only when the condition is `True`.

---

## 2. `if / else`

```python
score = 0.75

if score >= 0.80:
    print("Confident")
else:
    print("Not confident")
```

Since `0.75 >= 0.80` is `False`, the output is:

```text
Not confident
```

---

## 3. `if / elif / else`

Use `elif` when there are multiple conditions.

```python
accuracy = 0.88

if accuracy >= 0.90:
    print("Excellent")
elif accuracy >= 0.75:
    print("Good")
else:
    print("Needs improvement")
```

Python checks from **top to bottom** and stops when it finds the first true condition.

For example, with `accuracy = 0.95`:

```text
accuracy >= 0.90  → True
```

So Python prints `"Excellent"` and doesn't check the remaining branches.

---

## 4. Logical operators

You already revised these, but here they are in conditions:

### `and`

Both conditions must be `True`.

```python
age = 20
has_access = True

if age >= 18 and has_access:
    print("Allowed")
```

### `or`

At least one condition must be `True`.

```python
is_admin = False
is_owner = True

if is_admin or is_owner:
    print("Access granted")
```

### `not`

Reverses a Boolean value.

```python
is_training = False

if not is_training:
    print("Model is not training")
```

---

# AI/ML-style example

Imagine a binary classifier:

```python
probability = 0.87
threshold = 0.80

if probability >= threshold:
    prediction = "Positive"
else:
    prediction = "Negative"

print(prediction)
```

This is a simplified example of turning a numerical score into a decision.

---

#  Exercises

### Exercise 1

```python
age = 20
```

Print:

* `"Adult"` if age is `18` or greater.
* Otherwise print `"Minor"`.

---

### Exercise 2

```python
score = 85
```

Print:

* `"Excellent"` if score is `90` or above.
* `"Good"` if score is `70` or above.
* `"Needs Improvement"` otherwise.

---

### Exercise 3

```python
temperature = 35
is_raining = False
```

Print `"Good weather"` only if:

* temperature is greater than `25`
* **and** it is not raining

Otherwise print `"Not ideal"`.

---

### Exercise 4 — AI/ML style

```python
probability = 0.62
threshold = 0.50
```

Create a variable called `prediction`.

* If probability is greater than or equal to the threshold → `"Positive"`
* Otherwise → `"Negative"`

Then print `prediction`.
