def decorator_function(original_function):

    def wrapper(*args,**kwargs):
        print("before function")

        original_function(*args,**kwargs)

        print("after function")

    return wrapper

# you can use anything but decorator functions are seen more often while class decorators are clean
class decorator_class:
    def __init__(self,f):
        self.f = f

    def __call__(self, *args, **kwargs):
        print(f'call constructor is called before the {self.f.__name__}')
        return self.f(*args,*kwargs), print('finish')

@decorator_function # this is equivalent to 'display = decorator_function(display)' so then 'display = wrapper' will be done 
def display(name, age):
    print(f"display function triggered by {name} : {age} years")

display('S.Sandeep',18)