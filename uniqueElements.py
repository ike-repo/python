# Write a Python function that takes a list and returns a 
# new list with unique elements of the first list. Don't use set

def uni(my_list):
    a = []
    for i in my_list:
        if i not in a:
            a.append(i)
    return a   

print(uni([1,2,3,4,4,4,5,6,7,8,9,8,8,10]))