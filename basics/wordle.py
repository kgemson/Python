
class WordCheck:
   
   def check_guess(self, my_guess, answer):
        return_value_list = list("?????")
        checked_list = list("?????")
        
        # check each letter
        # first, check for matching letters and mark those that do
        for i in range(0,len(answer)):
            if my_guess[i] == answer[i]:
                return_value_list[i] = "X"
        
        checked_list = return_value_list.copy()

        # then, check each letter not already matched to see if it exists in the word
        for j in range(0,len(answer)):
            if return_value_list[j] != 'X':
                # scroll through the answer to see if letter exists and drop out after first match
                for k in range(0,len(answer)):
                    if my_guess[j] == answer[k] and checked_list[k] == '?':
                        return_value_list[j] = '@'
                        checked_list[k] = 'c'
                        break
                
        return "".join(return_value_list)