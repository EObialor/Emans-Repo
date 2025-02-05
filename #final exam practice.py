#final exam practice

#$9ilovepizza '1 = OR 1' $18




# Try lists, is a letter, is digit,
def sanitize(un_str):
san_str = '[$9ilovepizza, '1 = OR 1', '$', '18']
           
for char in un_str:
        if char.isalpha() and char.islower():
            san_str.append(char)
            #print(char, end="")
        else:
            print("", end="")
            print(str(san_str))    
        pass



# This fucntion will store the user name in a dictionary
def database():
    
    
    pass


#if __name__ == "__main__":
    
    unsanitized_string = input("Enter a string with special characters and numbers: ")
    sanitize(unsanitized_string)
    
    
    #return the dictionary and prnt it to the screen with the new user name
    pass
    
    
    
    
numbers = [3, 1, 4, 1, 5, 9]

# sort() and sorted()
numbers.sort()
print(numbers)  # [1, 1, 3, 4, 5, 9]

numbers_reversed = sorted(numbers, reverse=True)
print(numbers_reversed)  # [9, 5, 4, 3, 1, 1]

# reverse()
numbers.reverse()
print(numbers)  # [9, 5, 4, 3, 1, 1]

# append(), insert(), and remove()
numbers.append(10)
print(numbers)  # [9, 5, 4, 3, 1, 1, 10]

numbers.insert(2, 7)
print(numbers)  # [9, 5, 7, 4, 3, 1, 1, 10]

numbers.remove(1)
print(numbers)  # [9, 5, 7, 4, 3, 1, 10]
    