# generator exprssions can be used to yield by next so it does not hold any memory in it and without us saying next it won't execute

def squared(nums):
    for num in nums:
        yield num**2 # in generators we use yield as checkpoints which provide the info of last line running inside a fun/loop etc

nums = [1,2,3,4,5]
square_nums = squared(nums)

print(square_nums) # this gives us the loaction of generator not the values because they do not hold memory

# next(square_nums) we should use next to get to the yield occurence in this case its the first yield occurence
# we get an STOPITERATION error when the generator is exhausted of yield

# so we use loops for this
for square in square_nums:
    print(square)

# now we can use the generator expression by comprehension too
my_nums = (x*x for x in nums)
# since we used () this becomes a generator which should be accessed by next as you know

print(my_nums)