import os
from contextlib import contextmanager

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# the context manager decorator makes the function behave as __enter__ and __exit__ class
@contextmanager
def open_file(file, mode):
    file_path = os.path.join(BASE_DIR, file)
    try:
        f = open(file_path, mode)
        yield f
    except TypeError as e:
        print(f"{e} is caught by the except and is suppressed")
    finally:
        f.close()

with open_file('sample.txt', 'w') as f:
    f.write('Testing Context Manager using Functions')
    f.write(123)

print(f.closed) # checks if the file is closed or not