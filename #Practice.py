#Practice


#Create a file on desktop
def Create_file():
    
    #Create file
    users_file = input('Please enter a path and file name. Example: users/emmanuel/desktop/test.txt:')
    with open(users_file, 'w') as file:
        file.write('Python is cool.')



#check to see if file exists
def does_file_exist():
    
    user_file = input("Enter the file path")
    #get an exception handler in case it doesnt exist
    while True:
        try:
            file = open(user_file, 'r')
            result = file.read()
            break
            print(result)
            break
        
        except FileNotFoundError:
          print('file not found')
          break

if __name__ == "main":
    Create_file()
    does_file_exist()