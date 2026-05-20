import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Open_File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(os.path.join(BASE_DIR, self.filename), self.mode)
        return self.file

    def __exit__(self, exc_type, exc, tb):
        self.file.close()

        if exc_type is not None:
            print(f"[Error Logged]")
            print(f"Type: {exc_type.__name__}")
            print(f"Message: {exc}")

            if exc_type is TypeError:
                print("Handled TypeError Safely. Program will continue")
                return True
            
        return False

with Open_File('sample.txt', 'w') as f:
    f.write('Testing Context Manager using Classes')
    f.write(123)