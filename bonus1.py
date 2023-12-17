# A long funtion to calculate statistics for a list of numbers
def calculate_statistics(numbers):
    # Step 1: calculate the total number of elements in the list
    count = len(numbers)

    # Step 2: calculate the sum of all elements in the list
    total = sum(numbers)

    # Step 3: calculate the mean (average) of the numbers
    mean = total / count if count > 0 else 0

    # Step 4: sort the list in ascending order
    sorted_numbers = sorted(numbers)

    #step 5: Check if the count of numbers are even or odd
    if count % 2 == 0: #if count is even
        # Calculate the median for odd count
        median = (sorted_numbers[count // 2 - 1] + sorted_numbers[count // 2]) / 2
    else: #if count is odd
        # calculate the median for odd count
        median = sorted_numbers[count // 2]

        # Step 6: Find the minimum and maximum values in the list
        minimum = min(numbers)if count > 0 else 0
        maximum = max(numbers)if count > 0 else 0

        #step 7: print or return the calculated statistics
        print("Total count:", count)
        print("sum:",total)
        print("mean(average):",mean)
        print("Median:",median)
        print("Minimum:",minimum)
        print("Maximum:",maximum)

# Example usage of the calculate_statistics funtion
numbers_list =  [7,12,5,21,8,10,15]
calculate_statistics(numbers_list)