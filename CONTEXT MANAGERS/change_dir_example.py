import os
from contextlib import contextmanager

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@contextmanager
def change_dir(destination):
    try:
        folder_path = os.path.join(BASE_DIR, destination)
        cwd = os.getcwd()
        os.chdir(folder_path)
        yield
    finally:
        os.chdir(cwd)

with change_dir('Sample-dir'):
    print(os.getcwd())
    print(os.listdir())

print(os.getcwd())