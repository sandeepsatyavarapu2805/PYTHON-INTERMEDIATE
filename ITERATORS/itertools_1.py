# it contains iterators which will run infinitely
# count, cycler, repeater,starmap 

import itertools

counter = itertools.count(start=5, step=2) # it is a generator
print(next(counter))
print(next(counter))

data = [100, 200, 300, 400]
ordered_data = dict(zip(itertools.count(), data)) # so the zip calls next for the count which starts from 0
print(ordered_data)

elonged_data = list(itertools.zip_longest(range(10), data)) # this takes the data until the last value of range , if no data then 'None' is the placeholder
print(elonged_data)

cycler = itertools.cycle(data) # this is an itertool where it spans over and over the data
print(next(cycler))
print(next(cycler))
print(next(cycler))
print(next(cycler))
print(next(cycler))

repeater = itertools.repeat(data, times=2) # this repeats the arguement again and again until the given number of times if it crosses the limit then StopIteration Error
print(next(repeater))
print(next(repeater))

squares = list(map(pow, range(5), itertools.repeat(2)))
print(squares)

# itertools.starmap does the same thing but it takes the arguements as list[tuples]
star_squares = itertools.starmap(pow, [(0,2), (1,2), (2,2)])
print(next(star_squares))