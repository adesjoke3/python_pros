def multiplication_table(number):
    table = ""
    i = 1
    while i <= 100:
        result = number * i
        table += f"{number} times {i} = {result}\n"
        i += 1
    return table


# Test
num = 100
result = multiplication_table(num)
print(f"multiplication table for {num}:\n{result}")

        
        