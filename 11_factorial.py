def my_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact
print(my_fact(5))