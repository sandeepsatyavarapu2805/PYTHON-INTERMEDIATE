# it contains permutations and combinations iterators which run certain times according to the data
# also has chain, islice, compress, filterfalse

import itertools

letters = ['a', 'b', 'c', 'd']
numbers = [0, 1, 2, 3]
names = ['Corey', 'Nicole']

letter_combinations = list(itertools.combinations(letters, 3)) # it gives tuples of groups that are possible according to the 2nd arg which is !> len(data)
print(letter_combinations)

letter_permutations = list(itertools.permutations(letters, 2)) # it give the tuples of all possible ordered permutations where the len(tuples) is !> len(data)
print(letter_permutations)

numbers_reapeated_combinations = list(itertools.combinations_with_replacement(numbers, 2)) # it allows repetition and gives combinations tuples of group of len(2nd arg)
print(numbers_reapeated_combinations) # (1,1,2) == (1,2,1) or (1,0) == (0,1)

numbers_product = list(itertools.product(numbers, repeat=2)) # it allows repetations and give all permutations as a tuple groups of len(repeat)
print(numbers_product) # (1,1,2) != (1,2,1) or (1,0) != (0,1)

combined = letters + numbers + names # this creates a new list adding all of the lists which is not reliable for large data
print(type(combined))

combined_chained = list(itertools.chain(letters, numbers, names)) # this does not store everything in the memory and iterates in an order
print(combined_chained)

sliced_result = list(itertools.islice(letters, 1, 3)) # it stops when it reaches, index / number == 2nd arg which is same for start
print(sliced_result)

selectors = [True, True, False, True]
letters_compress = list(itertools.compress(letters, selectors)) # it returns the values of the data according to the selectors
print(letters_compress)

numbers_filter = list(itertools.filterfalse(lambda x: x < 2, numbers)) # it returns data which are false but takes func as 1st arg and data as 2nd arg
print(numbers_filter)