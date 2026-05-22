print(f'Importing {__name__}....')
# in this file if run print we get __main__ as output

def main():
    print(__name__)

test = 'test string'

def find_index(search, target):
    '''Find the index of a value in a sequence'''
    for i,value in enumerate(search):
        if value==target:
            return i

    return -1

# so this line executes only if the file is running directly if its being imported the code below this line does not run
if __name__ == '__main__' :
    main()