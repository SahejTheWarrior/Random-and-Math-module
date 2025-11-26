import random
playing=True
number=str(random.randint(10,20))
print("I will generate a number from 0 to 9, ad you have to guess the number one digit at a time")
print("the game ends when you get one")
while playing:
    guess = input("give me your best guess \n")
    if number==guess:
        print("you with te game")
        print("the number was",number)
        break
    else:
        print("your guess is not quite right please try again")