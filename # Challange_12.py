# Challange_12

def recursive_sum(n):
    # Base case n = 1, so it would just be 1
    if n == 1:
        return 1
    # Recursive case: "if n is more than 1,
    # add n to the sum of all the integers from 1 to n - 1"
    else:
        return n + recursive_sum(n - 1)
        
# Test # change to any number
test_number = 700
print(f"The sum of numbers from 1 to {test_number} is...{recursive_sum(test_number)}")
