# fibonacci numbers is a sequence that 
# each number is the sum of the two preceding ones, starting from 0 and 1
l = list(range(11))
for i in range(2,11):
    l[i] = l[i-1]+l[i-2]
print(l)
