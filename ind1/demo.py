from string_operations import *
from generator import even_odd_generator

print_string("Hello")

analyze_string("hello")
analyze_string("HELLO")
analyze_string("Hello")

print(to_uppercase("smogtether"))

gen = even_odd_generator()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))