print('Importing my_module....')

test = 'test string'

def find_index(search, target):
    '''Find the index of a value in a sequence'''
    for i,value in enumerate(search):
        if value==target:
            return i

    return -1