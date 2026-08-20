# Exercise 4 — Small AI-flavored example

# Imagine a model gives a prediction score:

# score = 0.87

# Create a variable called is_confident that is True when the score is at least 0.80.


# score =  0.87
# is_confident = True

# predicted_score = score < 0.80 and is_confident
# print(predicted_score)

# wrong


score = 0.87

is_confident = score >= 0.80

print(is_confident)
