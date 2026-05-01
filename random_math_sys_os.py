import sys, os
import random, math
from my_modules import find_index as fi, test as t
#import my_modules as mm then we can use mm.find_index()

print(sys.path)

print(os.__file__)
print(os.getcwd()) # prints the path of currently running directory

courses = ['History','Math','Physics','Chemistry']
index = fi(courses,'Math')
print(index,t)

random_course = random.choice(courses) # prints a random choice from the sequence
print('\n'+random_course)
print(random.shuffle(courses))

radian = math.radians(90)
print(radian)
print(math.sin(radian))