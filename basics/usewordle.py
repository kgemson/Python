from wordle import WordCheck
import random

guess_list = []
counter = 1
max_guesses = 6
answer = random.choice(["fussy","happy","drums","sugar","wield","potty","bears","venus","plant"])

# loop round until word found or max guesses exhausted or user quits
while(True):
    guess = input("Enter a guess \n")
    guess = guess.lower()

    guess_list.append(guess)

    myWordCheck = WordCheck()

    if guess == 'q':
        break
    elif counter == max_guesses:
        print("You've had " + str(counter) + " guesses - nae luck")
        break
    else:
        check_value = myWordCheck.check_guess(guess, answer)

        if check_value == 'XXXXX':
            print("Congratulations! Answer was indeed " + answer)
            break
        else:
            print(check_value)
            counter = counter + 1