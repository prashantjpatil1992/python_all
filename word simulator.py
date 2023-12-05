import random
word_list = ["ram","arm","cat","act","dog","god","khan","hank","bat","tab","avinash","vinasha","car","arc","thar","rath"]
score = 0
while True:    
    for i in range(3):
        letters = list(random.choice(word_list))
        dupli="".join(letters)
        print("letters :", "".join(letters))
        user_word = input("Enter Correct Word Either You can ('quit') : ")
        if user_word == "quit":
            break
        if dupli!=user_word:
            valid = True
            for letter in user_word:
                if letter in letters:
                    letters.remove(letter)
                else:
                    valid = False
                    break

            if valid and user_word in word_list:
                score+=len(user_word)
                print(f"Correct Word And You Got {score} cores")
                break
            else:
                print("In-Correct")
        else:
             print("Bro ! You Enter Same Word ('Logic Lagao')")
    if user_word == "quit":
        break
    else:
        score-=len(user_word)
        print(f"Sorry To Say But We reduce Your {score} scores")
print("Thank You For Playing With Us")

   
        
    
    
