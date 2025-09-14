def print_string(string):
    if type(string) is str:
        print(string)
    else:
        raise TypeError("Data for print_string must be of type str")

def analyze_string(string):
    if type(string) is not str:
        raise TypeError("Data for analyze_string must be of type str")
    else:
        if string.isupper():
            print(f"String {string} in uppercase")
        elif string.islower():
            print(f"String {string} in lowercase")
        else:
            print(f"String {string} is mixed")


def to_uppercase(string):
    if type(string) is not str:
        raise TypeError("Data for analyze_string must be of type str")
    else:
        return string.upper()