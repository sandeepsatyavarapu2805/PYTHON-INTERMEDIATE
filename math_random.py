import math, random # for random for every run the output is not same it is random

courses = ['History','Math','Physics','Chemistry']
greetings = ['Hi','Hello!','Good Morning','Hey','Hola']
colors = ['Red','Black','Green']
deck = range(1,53)

radian = math.radians(90)
print(radian)
print(math.sin(radian))

random_course = random.choice(courses) # prints a random choice from the sequence
print('\n'+random_course)

random.shuffle(courses) # suffles the origiinal sequence , it is in-place
print(courses)

value = random.random() # it returns a value between [0,1)
print(value)

range_value_float = random.uniform(1,10) # it returns a floating value between the given arguements
# Get a random number in the range [a, b) or [a, b] depending on rounding.
print(range_value_float)

range_value_int = random.randint(1,10) # it returns a integer value between the given arguements [a,b]
print(range_value_int)

random_greeting = random.choice(greetings) # it returns a random element in a non empty sequence
print(random_greeting, 'Sandeep!')

random_colors = random.choices(colors, k= 10) # it returns a list of 10 times - random elements from colors with even chances of picking
print(random_colors)

random_colors_roulette = random.choices(colors, weights=[18, 18 ,2], k= 10)
# it returns a list of 10 times - random elements from colors but now they have defined probabilities
print(random_colors_roulette)

hand = random.sample(deck,k=5) # it picks random elements from the sequence for the number of times mentioned
print(hand)