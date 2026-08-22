#  Phase 1 — Topic 2: Strings

Strings are important for AI/ML because a **huge amount of data is text**: documents, prompts, labels, usernames, reviews, datasets, etc.

We don't need to go deep into Python's string implementation. Just become comfortable manipulating text.

---

## 1. Creating Strings

You can use single or double quotes:

```python
name = "Annu"
language = 'Python'
```

You can also use triple quotes for multiline text:

```python
text = """This is
a multiline
string."""
```

For our purposes, you'll mostly use `"..."`.

---

# 2. String Indexing

A string is a sequence of characters.

```python
name = "Annu"
```

Think of it as:

```text
 A   n   n   u
 0   1   2   3
```

So:

```python
print(name[0])  # A
print(name[1])  # n
print(name[3])  # u
```

Python starts counting from **0**.

You can also count from the end:

```python
print(name[-1])  # u
print(name[-2])  # n
```

This is worth remembering because indexing appears everywhere in Python and later in NumPy.

---

# 3. String Slicing

Slicing lets you take a portion of a string.

```python
text = "Artificial Intelligence"
```

```python
print(text[0:10])
```

The important rule:

```text
[start : stop]
```

The `start` position is included.

The `stop` position is **not included**.

For example:

```python
text = "Python"

print(text[0:2])
```

Output:

```text
Py
```

Because indexes `0` and `1` are included, but `2` isn't.

You can omit either side:

```python
text[:3]    # first 3 characters
text[3:]    # from index 3 onward
text[:]     # entire string
```

You can also use a step:

```python
text[::2]
```

That takes every second character.

---

# 4. Strings Are Immutable

You can read characters:

```python
name = "Annu"

print(name[0])
```

But you can't directly change one:

```python
name[0] = "A"
```

That produces an error.

Instead, create a new string.

You don't need to memorize the underlying reason yet. Just remember:

> **Python strings are immutable.**

---

# 5. Useful String Methods

You'll use these frequently.

### `.lower()`

```python
text = "HELLO"

print(text.lower())
```

Output:

```text
hello
```

### `.upper()`

```python
text = "hello"

print(text.upper())
```

Output:

```text
HELLO
```

### `.strip()`

Removes whitespace at the beginning and end:

```python
text = "   hello   "

print(text.strip())
```

Output:

```text
hello
```

This is particularly useful when cleaning datasets.

---

### `.replace()`

```python
text = "I like Java"

text = text.replace("Java", "Python")

print(text)
```

Output:

```text
I like Python
```

---

### `.split()`

This one is **very important for text processing**.

```python
sentence = "I am learning Python"

words = sentence.split()

print(words)
```

Output:

```python
["I", "am", "learning", "Python"]
```

You just converted one string into a list of words.

Later, you'll encounter much more sophisticated tokenization techniques in NLP.

---

### `"separator".join()`

The opposite direction:

```python
words = ["I", "am", "learning", "Python"]

sentence = " ".join(words)

print(sentence)
```

Output:

```text
I am learning Python
```

---

# 6. `len()`

Get the number of characters:

```python
text = "Python"

print(len(text))
```

Output:

```text
6
```

Remember that spaces count too:

```python
text = "Hello world"

print(len(text))
```

---

# 7. Checking Text

You can check whether something exists inside a string:

```python
text = "I am learning Python"

print("Python" in text)
```

Output:

```text
True
```

And:

```python
print("Java" in text)
```

Output:

```text
False
```

This becomes useful when filtering data.

---

# 8. f-Strings

You'll use these **all the time**.

```python
name = "Annu"
age = 20

print(f"My name is {name} and I am {age} years old.")
```

Output:

```text
My name is Annu and I am 20 years old.
```

You can also put expressions inside:

```python
a = 10
b = 20

print(f"The total is {a + b}")
```

Output:

```text
The total is 30
```

---

# Exercises

### Exercise 1 — Indexing

Given:

```python
language = "Python"
```

Print:

* First character
* Last character
* Third character

---

### Exercise 2 — Slicing

Given:

```python
text = "Artificial Intelligence"
```

Try to print:

* `"Artificial"`
* `"Intelligence"`
* The first 5 characters
* The last 5 characters

---

### Exercise 3 — Cleaning text

Given:

```python
text = "   MACHINE LEARNING IS FUN   "
```

Create a new variable that:

1. Removes the extra spaces.
2. Converts everything to lowercase.

Expected result:

```text
machine learning is fun
```

---

### Exercise 4 — Text processing

Given:

```python
sentence = "Python is powerful for AI"
```

Convert it into a list of words using `.split()`.

Then print the number of words.

Expected:

```text
["Python", "is", "powerful", "for", "AI"]
5
```

---

### Exercise 5 — f-string

Create:

```python
name = "Annu"
field = "AI/ML"
```

Print a sentence using an f-string:

```text
My name is Annu and I am learning AI/ML.
```

