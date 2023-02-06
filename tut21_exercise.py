# find a particular number
num=10

num_of_guesses=1
print("You have only 5 changes to guess the number")
while (num_of_guesses<=5):
    guess_num=int(input("Enter the Number of Guess:"))

    if (guess_num<num):
        print("you entered the less number.\n")
    elif(guess_num>num):
        print("you entered the greater number\n")
    else:
        print("Congrats !! you won\n")
        print(num_of_guesses, "no., of guesses you took to finish")
        break;
    print(5-num_of_guesses,"no, of guesses left")
    num_of_guesses=num_of_guesses+1

if (num_of_guesses>5):
    print("Game Over....")