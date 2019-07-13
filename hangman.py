#definitions
def show_word():
    for i in range (N):
        if word[i] not in all_guesses:
            print ("_ ", end="")
        else:
            print (word[i], end=" ")
    print()

def have_i_won():
    for i in range (N):
        if word[i] not in all_guesses:
            return False
    print ("Congratulations you have won!")
    return True
            
        
#Hangman
finished=False
word=input("Please enter a word: ")
N = len(word)
lives = 10
all_guesses = []
for counter in range (50):
    print()
#print (len(word))
#for i in range (N):
#    print ("_ ", end="")
show_word()
#change condition of while loop
while lives > 0 and finished==False :
    guess = input("Please enter a letter: ")
    if guess in all_guesses:
        print ("You've already tried that letter :( ")
    else:
        #record what was guessed
        all_guesses.append (guess)
        print("You have guessed these letters:",all_guesses)
        if guess in word:
            #print (guess)
            #print word with spaces
            show_word()
            finished = have_i_won()
        else:
            print ("Sorry, the letter is not in the word!")
            lives = lives - 1
            show_word()
            print ("You have" ,lives , "lives left.")
            if lives == 0:
                print()
                print ("GAME OVER.")
                finished=True

        
        
