num = int(input('enter a number: '))
if num != 0:
    is_prime = True
else:
    is_prime = False
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break
if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")