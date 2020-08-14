def prime_Num(num):
    prime_list, count = [], 0
    for i in range(2, num + 1):
        for k in range(1, i + 1):
            if i % k == 0:
                count += 1
                # in order to make it run faster, checking if the count is over 2 or not
                if count > 2:  
                    break
        if not count > 2:
            prime_list.append(i)
        count = 0
    return prime_list

print(prime_Num(100))
