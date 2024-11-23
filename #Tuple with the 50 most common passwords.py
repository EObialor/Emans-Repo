#Tuple with the 50 most common passwords
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
    # Check if the password is part of the common passwords tuple
    if checkPass in list_of_common_passwords:
        index = list_of_common_passwords.index(checkPass)
        return (f"Your password is too obvious bro. Please consider changing it. I found it in the index {index}.")
    else:
        return "You have a tough password."

def UserPass():
    username = input("Create a username: ")
    userPass = input("Create a password: ")
    
    result = StoredPasswords(userPass)
    print(result)

def main():
    UserPass()

if __name__ == '__main__':
    main()