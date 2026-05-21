# When you call repr(variable), Python looks up that object's class definition, executes the code inside its __repr__ method, and returns that exact string.

a = [1, 2, 3, 4]
b = 'sample string'

#  repr helps us to know the exact type of the variable
print(str(a))
print(repr(a))

print(str(b))
print(repr(b))