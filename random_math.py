import random, math

courses = ['History','Math','Physics','Chemistry']

random_course = random.choice(courses) # prints a random choice from the sequence
print('\n'+random_course)
print(random.shuffle(courses))

radian = math.radians(90)
print(radian)
print(math.sin(radian))