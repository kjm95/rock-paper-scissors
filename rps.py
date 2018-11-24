import random


play = True

max_streak = 0
curr_streak = 0

while play == True:

    user_choice = input('What is your choice: ').lower()

    choices = ['rock', 'paper', 'scissors']

    cpu_choice = choices[random.randint(0,2)]

    lose = 'You chose '+ user_choice + '\n CPU chose ' + cpu_choice + '\n You lose!'
    win = 'You chose '+ user_choice + '\n CPU chose ' + cpu_choice + '\n You win!'
    tie = 'You chose '+ user_choice + '\n CPU chose ' + cpu_choice + "\n It's a tie!"

    if user_choice in choices:
        if user_choice == 'rock':
            if cpu_choice == 'rock':
                print (tie)
            elif cpu_choice == 'paper':
                print (lose)
                max_streak = max(max_streak, curr_streak)
                curr_streak = 0
            else:
                print (win)
                curr_streak += 1
        elif user_choice == 'paper':
            if cpu_choice == 'paper':
                print (tie)
            elif cpu_choice == 'scissors':
                print (lose)
                max_streak = max(max_streak, curr_streak)
                curr_streak = 0
            else:
                print (win)
                curr_streak += 1
        else:
            if cpu_choice == 'scissors':
                print (tie)
            elif cpu_choice == 'rock':
                print (lose)
                max_streak = max(max_streak, curr_streak)
                curr_streak = 0
            else:
                print (win)
                curr_streak += 1
    elif user_choice == 'score':
        print ('Your current streak is ', str(curr_streak), '\n The highest streak is ', str(max_streak))
    elif user_choice == 'reset':
        max_streak = curr_streak = 0
        print ('Streaks have been reset!')
    elif user_choice == 'stop':
        play = False
    else:
        print ("I didn't quite understand that. Please make another choice.")
