# this file has dropwhile, takewhile, accumulation, groupby, tee

import itertools
import operator

people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]

numbers = [0, 1, 2, 3, 0, 1, 2]
# Condition (predicate): Is the number less than 2? it will start to store values from false state
numbers_dropwhile = list(itertools.dropwhile(lambda x: x < 2, numbers))
print(numbers_dropwhile)

numbers_extended = [0, 1, 2, 3, 0, 1, 2]
# Condition (predicate): Is the number less than 2? it will start to store values from true and will stop when it gets to the first false
result = list(itertools.takewhile(lambda x: x < 2, numbers_extended))
print(result)

numbers = [1, 2, 3, 4]
# Default - Addition its like accumulating a certain operation along the list
running_sum = list(itertools.accumulate(numbers))
print(running_sum) # Output: [1, 3, 6, 10]

# Example B: Custom running product (Multiplication)
running_product = list(itertools.accumulate(numbers, operator.mul))
print(running_product) # Output: [1, 2, 6, 24]

people_sorted = sorted(people, key=lambda x: x['state'])
grouped_data = itertools.groupby(people_sorted, lambda x: x['state']) # so it groups same data and returns by which we sorted as key and other things as continuation

for key, group in grouped_data:
    print(f"State: {key} -> Members: {list(group)}")

letters = ['a', 'b', 'c']
# Create two independent iterators from one list
iter1, iter2 = itertools.tee(letters, 2)
# this helps us to make multiple iterators which we will use in different ways
print("Iter1:", list(iter1))
print("Iter2:", list(iter2))