# fibonacci numbers is a sequence that 
# each number is the sum of the two preceding ones, starting from 0 and 1
fibo = list(range(11))
for i in range(2,11):
    fibo[i] = fibo[i-1]+fibo[i-2]
print(fibo)
