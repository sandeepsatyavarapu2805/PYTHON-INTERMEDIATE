import sys
import random, math
from my_modules import find_index as fi, test as t
#import my_modules as mm then we can use mm.find_index()
print(sys.path)

courses = ['History','Math','Physics','Chemistry']
index = fi(courses,'Math')
print(index,t)

random_course = random.choice(courses)
print('\n'+random_course)

radian = math.radians(90)
print(radian)