# print(101+101+28+75+69)
# print("How old are you?", end = ' ')
# age = input()
# print("How tall are you?", end=' ')
# height = input()
# print("How much do you weigh?", end = ' ')
# weight = input()
#
# print(f"So, you're {age} old, {height} tall and {weight} heavy.")


# sleep calculator
# what time to I sleep, am|pm


print("Is it morning (Y | N)", end = " ")
morning = input()
print("Hour : ", end = " ")
sleep_time_hours = int(input())#10
print("Min : ", end = " ")
sleep_time_min = int(input()) #30

if morning == 'Y':
    time = "am"
else:
    time= "pm"

print(f"You slept at {sleep_time_hours}:{sleep_time_min} {time}")

# calculate sleep sleep time

print("How many hours do you want to sleep?", end = " ")
hours_to_sleep = int(input())

wake_up_calculator = sleep_time_hours + hours_to_sleep

if wake_up_calculator > 12:
    wake_up_calculator = wake_up_calculator - 12

if time == "am":
    time = "pm"
else:
    time = "am"

print (f"You should wake up at {wake_up_calculator}:{sleep_time_min} {time} ")



# sleep_cycle = 90/60
# wake_up_calculator = 4
# for x in range(1,7):
#     Hour_Slept = x * sleep_cycle
#     wake_up_time = wake_up_calculator + Hour_Slept
#
#     if wake_up_time > 12:
#         wake_up_time = wake_up_time - 12
#
#     print(wake_up_time)
#
#     print (f"Number of Sleep Cycles {x}\nHours slept {Hour_Slept}")
#     print(f"You should wake up at {wake_up_time} am\n")
