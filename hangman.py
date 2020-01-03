import random
#Writing a set of words for the computer to pick
secret_word=["istanbul","mugla","santorini","dubai","la"]
#storing the random word in secret
secret = random.choice(secret_word)
#I gave the user 10 tires
tries=10
#I am multiplying dashes with the number of letters in the word so they both have the same number
dashes="_"*len(secret)
#This is the function that updates the dashes with the letters
def update_dashes(secret_word, dashes, user_guess):
    #Runs for the duration of the length of the word
    for i in range (len(secret_word)):
        #if user_guess is in any index of i of the secret_word ,
        if secret_word[i]==user_guess:
            #update dashes so the letter is now inserted within the dashes.
            dashes=dashes[:i]+user_guess+dashes[i+1:]
    #return the new set of dashes/letters
    return dashes

"""
for letter in secret:
    dashes.append("_")
"""
#I am giving the user
print ("This is a city")
print dashes
#I will be asking the user to enter a letter until they use all of their tries
while tries !=0:
    #asking the user to enter a number and I make it lowercase
    user_guess=input("Enter a Letter: ").lower()
    #If the user enter more than more letters I dont accept it
    if len(user_guess)!=1:
        print "No more than 1 letter"
    #if the letter is not in the random word i reduce tries by one
    if user_guess not in secret:
        tries=tries-1
        print ("Unfortunately wrong you have "+str(tries)+" tries left")
    #if the tires are equal to zero I the game is over
    if tries==0:
        print("Game over and there is nothing you could do about it")
    # if the letter user entered is in the word i will update the dashes with the function i made
    if user_guess in secret:
        print ("Correct you got it right")
        dashes=update_dashes(secret,dashes ,user_guess)
        print dashes
    #After all the letters are in and the dashes is equivalent with the secret word the user wins the game
    if dashes == secret:
        print("You Won!!!")
        print("The correct word is ")+str(dashes)
        break
