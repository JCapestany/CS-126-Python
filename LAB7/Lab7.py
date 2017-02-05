'''
Cameron Meier & Jose Capestany
3/25/16
CS 126L-4
'''

# Import random for the play_game function
import random


# This function acts as the main menu and presents three options
def main_menu():
    print("Welcome to Who Wants to be a Fake Millionare!")
    print("Win fake millions!")
    print("What do you want to do?")
    choice = input("Play, Credits, or Quit: ").lower()
    print("")
    if choice == "play":
        play_game()
    elif choice == "credits":
        view_credits()
    elif choice == "quit":
        quit_game()
    else:
        main_menu()


# This function displays the credits and returns to the main menu
def view_credits():
    print("\nGame Designers: Cameron Meier & Jose Capestany\n")
    main_menu()


# We thank the user and end the program
def quit_game():
    print("\nThank you for playing our game!")

# Randomly asks the user questions based on our list and keeps a running total
def play_game():
    random.shuffle(question_list)
    prize = 0
    for question_dict in question_list:
        ans = 0
        print(question_dict['question'])
        for i, choice in enumerate(question_dict["answers"]):
            print(str(i + 1) + ". " + choice)
        while ans == 0:
            list = []
            answer = input("Choose an answer: 1-%d:" %
                           (len(question_dict["answers"])))
            for z in range(len(question_dict["answers"])):
                list.append(str(z+1))
            if answer in list:
                ans = 1
        if answer == question_dict["correct"]:
            prize += 1000000
            print("\nGood job, you won $1000000!")
            print("You have $%d!\n" % (prize))
        else:
            print("\nFailure! You get nothing!")
            print("You have $%d!\n" % (prize))
    print("Thanks for playing with us today!\nCome back again!\n")
    main_menu()

# The question list
question_list = [{"question": "Who is Luke Skywalker's father?", "answers":
                 ["Darth Vader", "Yoda", "Obi Wan", "Jar Jar Binks"],
                  "correct": "1"},
                 {"question": "What is not a liquid?", "answers":
                 ["Water", "Juice", "Soda", "Chicken"], "correct": "4"},
                 {"question": "What is not a primary color?", "answers":
                 ["Red", "Blue", "Brown"], "correct": "3"},
                 {"question": "Is water wet?", "answers":
                 ["Yes", "No"], "correct": "1"},
                 {"question": "What is not a state of matter?", "answers":
                 ["Solid", "Fluid", "Liquid", "Gas"], "correct": "2"},
                 {"question": "Who is the 16th president?", "answers":
                 ["Reagan", "Putin", "Lincoln", "Jackson"], "correct": "3"},
                 {"question": "What school is Harry Potter in?", "answers":
                 ["Oxford", "Harvard", "Hogwarts"], "correct": "3"},
                 {"question": "Which is not a US state?", "answers":
                 ["Hawaii", "Cuba", "Delaware", "Texas"], "correct": "2"},
                 {"question": "Which is a mammal?", "answers":
                 ["Ostrich", "Chicken", "Whale"], "correct": "3"},
                 {"question": "What is (1+1*1/1-1)^1?", "answers":
                 ["5", "1", "3", "2", "4"], "correct": "2"}]

# Running the program
main_menu()
