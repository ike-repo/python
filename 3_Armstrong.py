input_num = input("Enter a positive integer value: ")
digits = len(input_num)
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'] 
flag = False #I thought isdigit() cannot differentiate the int and float or negative numbers.
for char in range(digits):
    if input_num[char] not in nums:
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
        flag = True
        break
if not flag:
    arm_num = 0
    int_num = int(input_num)
    rem_num = int_num
    for i in range(digits):
        remainder = rem_num % 10
        rem_num = rem_num // 10
        arm_num = arm_num + remainder ** digits
    if arm_num == int_num:
        print(f"{int_num} is an Armstrong number")
    else:
        print(int_num, "is not an Armstrong number")