def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Test 
my_list = [1, 2, 2, 3, 4, 2, 3, 1, 2]
result = remove_duplicates(my_list)
print ("List without duplicates:",result)