nums = [1, 2, 3, 4]

iter_nums = nums.__iter__()
# or you can use iter_nums = iter(nums) which returns an iterable on the object

print(dir(iter_nums)) # iter_nums is an iterator since it has __next__ and __iter__
print(next(iter_nums), end=' ') # it raises a StopIteration Error if there is nothing next i.e it has reached the end

# the finctionality of a for loop
while True:
    try:
        item = next(iter_nums)
        print(item, end=' ')
    except StopIteration:
        break

print()
# creating a iterator class
class MyRange:

    def __init__(self, start, end):
        self.value = start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value += 1

        return current
    
# creating a iterator function
def my_range(start, end):
    value = start

    while value < end:
        yield value
        value += 1
    else:
        raise StopIteration

class_nums = my_range(1, 10)

# since class_nums is an iterator so we use next on it
print(next(class_nums))