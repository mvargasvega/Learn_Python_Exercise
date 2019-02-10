types_of_people = 10
# a string with embeded variable of types_of_people
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
# assigns a string to y with embeded variables
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
# printing a string with variable y
print(f"I also said: '{y}'")

# assign the boolean value of false to hilarious
hilarious = False
# assigns a string with an empty curly brace, which allows us to print something in
joke_evaluation = "Isn't that joke so funny?! {}"

# prints thet variable joke_evaluation and plugs in False into the two curlry braces
print(joke_evaluation.format(hilarious))

# a variable that stores a string
w = "This is the left side of..."
# a variable that stores a string
e = "a string with a right side."
# Conncatintes two variables that are holding strings
print(w + e)
