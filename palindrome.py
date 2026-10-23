import sys

def is_palindrome(string):
    return string == string[:: -1]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: Python palindrome.py ")
        sys.exit(1)

    string = sys.argv[1]

    if is_palindrome:
        print(f"{string} is palindrome")
    else:
        print(f"{string} is not a Palindrome")