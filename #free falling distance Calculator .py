#Free_Falling Distance Calculator
#constant
GRAVITY = 9.8

#Calculate distance
def distance_Calculator(time):
    distance = 0.5 * GRAVITY * time ** 2
    return distance

#user input
def user_input():
    user_time = int(input('Enter any seconds (positive only): '))
    while user_time < 1:
        print('It has to be postive!')
        user_time = int(input('Enter your time, and it has to be positive!: '))
    
    return user_time

#Calculating all seconds
def user_distance(all_seconds):
    for t in range(1, all_seconds + 1): 
        distance = distance_Calculator(t) 
        print(f"After {t} second/s, the object fell {distance:.2f} meters.")

# Main Program
if __name__ == "__main__":
    user_time = user_input() 
    user_distance(user_time) 
