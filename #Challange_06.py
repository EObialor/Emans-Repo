#Challange_06
import random

def create_file(user_numbers):
    with open("emmanuelsfile.txt", "w") as file:  
        for _ in range(user_numbers):
            rand_num = random.randint(1, 500)
            file.write(f"{rand_num}\n") 
    print(f"{user_numbers} random numbers written to my file 'emmanuelsfile.txt'.")

def get_user_input():
    while True:
        user_input = input("Enter any positive random number (must be a positive): ")
        try:
            user_numbers = int(user_input)  
            if user_numbers > 0:  
                return user_numbers 
            else:
                print("The number has to be a positive. Try again.")
        except ValueError:
            print("You did not enter a positive number. Try again.")

def main():
    user_numbers = get_user_input() 
    create_file(user_numbers) 

if __name__ == "__main__":
    main()
