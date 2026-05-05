import math, random

courses = ['History','Math','Physics','Chemistry']

radian = math.radians(90)
print(radian)
print(math.sin(radian))

random_course = random.choice(courses) # prints a random choice from the sequence
print('\n'+random_course)
random.shuffle(courses) # suffles the origiinal sequence , it is in-place
print(courses)