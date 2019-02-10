# use argv to get a filename
from sys import argv

script, filename = argv
# command to open filename and assign it to txt
txt = open(filename)

# Print out filename that was given & reads/prints what was in that file
print(f"Here's your file {filename}:")
print(txt.read())

# # Ask for user to retype file they would like to open
# print("Type the filename again:")
# # Assigns input from user to type out file name, no assitance from terminals
# file_again = input("> ")
#
# # opens file that was given
# txt_again = open(file_again)
# # reads and prints out the information on txt_given
# print(txt_again.read())
