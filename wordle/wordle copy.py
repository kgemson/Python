import random

class WordCheck:
    answer = random.choice(["fussy","happy","drums","sugar","wield","potty","bears","venus","plant"])
    #answer = "potty"
    guess_list = []
    counter = 1
    max_guesses = 6

    def check_guess(self, my_guess):
        return_value_list = list("?????")
        checked_list = list("?????")
        
        # check each letter
        # first, check for matching letters and mark those that do
        for i in range(0,len(self.answer)):
            if my_guess[i] == self.answer[i]:
                return_value_list[i] = "X"
        
        checked_list = return_value_list.copy()

        # then, check each letter not already matched to see if it exists in the word
        for j in range(0,len(self.answer)):
            if return_value_list[j] != 'X':
                # scroll through the answer to see if letter exists and drop out after first match
                for k in range(0,len(self.answer)):
                    if my_guess[j] == self.answer[k] and checked_list[k] == '?':
                        return_value_list[j] = '@'
                        checked_list[k] = 'c'
                        break
                
        print(checked_list)

        return "".join(return_value_list)

    # loop round until word found or max guesses exhausted or user quits
    while(True):
        guess = input("Enter a guess \n")
        guess = guess.lower()

        guess_list.append(guess)

        if guess == 'q':
            break
        elif counter == max_guesses:
            print("You've had " + str(counter) + " guesses - nae luck")
            break
        else:
            check_value = check_guess(guess)

            if check_value == 'XXXXX':
                print("Congratulations! Answer was indeed " + answer)
                break
            else:
                print(check_value)
                counter = counter + 1