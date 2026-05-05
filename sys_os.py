import sys, os
from my_modules import find_index as fi, test as t
#import my_modules as mm then we can use mm.find_index()

print(sys.path)

print(os.__file__)
print(os.getcwd()) # prints the path of currently running directory

courses = ['History','Math','Physics','Chemistry']
index = fi(courses,'Math')
print(index,t) # t is the test string