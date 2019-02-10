# sys is module or library
from sys import argv
#read the WYSS section for how to run this
# argv is the argument variable. This variable holds the arguments you pass to your python script when you run it
# script, first, second, third = argv
#
# print("The script is called:", script)
# print("Your first variable is:", first)
# print("Your second variable is:", second)
# print("Your third variable is:", third)


# creating a component
script, component, css = argv
name = input("What is your name:")
print("The component name is:",component)
print("The CSS file is called:",css)
print(f"What is your name {name}")
