# this is an iterato class
class Sentence:
    def __init__(self, text: str):
        self.words: list[str] = text.split(' ')
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        
        if self.index >= len(self.words):
            raise StopIteration
        word = self.words[self.index]
        
        self.index += 1
        return word

# this is a generator function
def word(sentence: str):

    for word in sentence.split(' '):
        yield word

my_sentence = Sentence('This is a test')
# you can also use my_sentence = word('This is a test')

print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))
print(next(my_sentence))