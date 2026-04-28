from my_modules import find_index as fi
#import my_modules as mm then we can use mm.find_index()

courses = ['History','Math','Physics','Chemistry']

index = fi(courses,'Math')
print(index)