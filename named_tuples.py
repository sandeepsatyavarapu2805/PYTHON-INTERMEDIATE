# namedtuples are beneficial for code readability and reusability
from collections import namedtuple

Color = namedtuple('Color',['red','green','blue']) # this is a named tuple where Color is the naming and [..] - are the values

color = Color(55,155,255) # a Color named tuple where the values are defined as red, green, blue above
# we can also write like this --> Color(red=55,green=155,blue=255)
white = Color(255,255,255)

print(color.red)