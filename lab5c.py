 #!/usr/bin/env python3
# Author ID: [seneca_id]

def add(number1, number2):
    try:
        # Try converting both to integers if they are strings representing numbers
        number1 = int(number1) if isinstance(number1, str) else number1
        number2 = int(number2) if isinstance(number2, str) else number2
        
        return number1 + number2
    except (TypeError, ValueError):
        return 'error: could not add numbers'

def read_file(filename):
    try:
        # Attempt to open the file and read all lines
        with open(filename, 'r') as f:
            return f.readlines()
    except (FileNotFoundError, PermissionError, IsADirectoryError):
        return 'error: could not read file'

if __name__ == '__main__':
    # Test the add function
    print(add(10, 5))                     # works
    print(add('10', 5))                   # works
    print(add('abc', 5))                  # exception
    print(add('hello', 'world'))          # exception

    # Test the read_file function
    print(read_file('seneca2.txt'))       # works
    print(read_file('file10000.txt'))     # exception

