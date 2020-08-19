# Write a Python program to filter a list of integers using Lambda.
evens = tuple(filter(lambda x: x % 2 == 0, range(1,11)))
odds = set(filter(lambda x: x % 2 != 0, nums))
print(evens)
print(odds)