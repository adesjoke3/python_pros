def count_vowels(input_string):
    vowels = 'aeiou'
    count = 0
    for char in input_string:
        if char.lower() in vowels:
            count += 1  
    return count

sentence = "Bob is the best he ate icecream at bobs icecream place YAY"
#call the funtion
x = count_vowels(sentence)
print(x)