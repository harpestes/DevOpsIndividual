def print_string(string):
    print(string)

def analyze_string(string):
    if string.isupper():
        print(f"String {string} in uppercase")
    elif string.islower():
        print(f"String {string} in lowercase")
    else:
        print(f"String {string} is mixed")
