def most_freq(given_list):
    max_count = 0
    for i in given_list:
        num = max(given_list, key = given_list.count )
    return num
print(most_freq([1,1,2,2,3,3,5,6,8]))