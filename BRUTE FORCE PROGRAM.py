#Brute Force program 
#Tuple with the 50 most common passwords
import time
import itertools
import string

# List of 50 common passwords
list_of_common_passwords = ("123456", "123456789", "12345", "qwerty", "password",
    "12345678", "111111", "123123", "1234567890", "1234567",
    "qwerty123", "000000", "1q2w3e", "aa12345678", "abc123",
    "password1", "1234", "qwertyuiop", "123321", "password123",
    "1q2w3e4r5t", "iloveyou", "654321", "666666", "987654321",
    "123", "123456a", "qwe123", "1q2w3e4r", "7777777",
    "1qaz2wsx", "123qwe", "zxcvbnm", "121212", "asdasd",
    "a123456", "555555", "dragon", "112233", "123123123",
    "monkey", "11111111", "qazwsx", "159753", "asdfghjkl",
    "222222", "1234qwer", "qwerty1", "123654", "123abcdef")

def StoredPasswords(checkPass):
    # creating a function to check if the password is part of the common passwords tuple with if/else structure
    if checkPass in list_of_common_passwords:
        index = list_of_common_passwords.index(checkPass)
        return (f"Your password is too obvious bro. Please consider changing it. I found it in the index {index}.")
    else:
        return "You have a tough password."

def brute_force_crack(target_password, num_characters):
    # Creating a function to test different charcaters and combinations(lowercase, uppercase, digits, and symbols)
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    combinations_checked = 0
    
    start_time = time.time()  # Start timing
    
    # Brute force all combinations of the specified length
    for password_tuple in itertools.product(chars, repeat=num_characters):
        password_candidate = ''.join(password_tuple)
        combinations_checked += 1
        
        # Check if the generated password matches the target
        if password_candidate == target_password:
            end_time = time.time()  # End timing
            time_taken = end_time - start_time
            return time_taken, combinations_checked, password_candidate
    
    return None, None, None  # In case we fail to crack it (very unlikely here)

def UserPass():
    username = input("Create a username: ")
    userPass = input("Create a password: ")

    # First, check if the password is part of common passwords
    result = StoredPasswords(userPass)
    print(result)

    # Now, perform a brute-force cracking if it's not a common password
    if result == "You have a tough password.":
        print("Attempting to crack your password...")
        
        num_characters = len(userPass)
        time_taken, combinations_checked, cracked_password = brute_force_crack(userPass, num_characters)
        
        if cracked_password:
            print(f"Password cracked! It took {time_taken:.6f} seconds and {combinations_checked} combinations to crack it.")
        else:
            print("Failed to crack the password.")

def main():
    UserPass()

if __name__ == '__main__':
    main()

