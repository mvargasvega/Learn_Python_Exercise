from sys import argv

script, user_name= argv
prompt = 'Type stuff here ---> '

print(f"Hi {user_name}, I'm the {script} script")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)


print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")

print("Okay can I ask you more questions? (Yes|No)")
more_questions = input(prompt)
if more_questions == "Yes":
    print("Great, what do you want to do in life")
    life_goal = input(prompt)
    print(f"That is amazing, you want to {life_goal} in life")
    print("You are awesome")
else:
    print("Aww that is so sad")

print("Thank you for playing")
