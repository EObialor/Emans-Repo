#Emmanuel_Obialor_Challange_03

counter = 0
# Ask the user if they want to play
print('Welcome to my escape room, answer correctly to get out!')
#print('You need to get at least 3 out of 5 questions to escape!')
user_choice = input("Do you wish to play? (yes/no): ")
while user_choice.lower() == "yes" :
    counter = 0
    print('Okay, first question!')

    #First question
    print('What can you hold in your right hand, but never in your left hand?')
    correct_answer = 'your left hand'
    user_answer = input("Your answer: ")
    if user_answer.lower() == correct_answer:
        print('Correct, 1 point!')
        counter += 1
        print('Next question!')
    else:
        print('Sorry, that is not right. The answer is Your left hand!')
        print('Next question')    
       
    #Second question
    print("What gets wet while drying? ")
    correct_answer_two = 'a towel'
    user_answer_two = input('your answer: ')
    if user_answer_two.lower() == correct_answer_two:
            print('Correct again! 1 point!')
            counter += 1
            print('Next Question, youre doing great!')
    else:
        print('Sorry, that is not right. The answer is A towel!')
        print('Next Question')
        
    #Third question
    print("What kind of band never plays music?")
    correct_answer_three = 'a rubber band'
    user_answer_three = input('your answer: ')
    if user_answer_three.lower() == correct_answer_three:
        print('Correct, you are on a roll!')
        counter += 1
        print('Next Question!')   
    else:
        print('Sorry, that is not right! The answer is A rubber band.')
        print('Next Question')
        
    #fourth question
    print("What is the end of everything?")
    correct_answer_four = 'g'
    user_answer_four = input('your answer: ')
    if user_answer_four.lower() == correct_answer_four:
        print('You are about to escape, keep going!')
        counter += 1
        print('Next question!')
    else:
     print('sorry, thats wrong. The answer is the letter g!')
     print('Next question!')
     
    #fifth question
    print("When is a door no longer a door?")
    correct_answer_five = 'ajar'
    user_answer_five = input('your answer: ')
    if user_answer_five.lower() == correct_answer_five:
      print('That is correct.')
      counter += 1                           
    else:  
     print('Sorry, thats Incorrect. The answer is Ajar!')
     
     #Loop time
     
    if counter == 5:
      print(f'Congratulations, you perfectly escaped the room of many riddles with {counter}/5 correct answers!')
      break
    else:
        print(f'Unfortunately, you did not escape the room of many riddles. You only got {counter}/5 correct.')
    user_choice = input('Would you like to try again? (yes/no): ')
    if user_choice != "yes" :
        print('Thanks for playing, GAME OVER!')
        break
        
if user_choice != "yes" :
    print('You chose to stop.')   