#Make an array for the allowed characters that are in decimal integers in Python (0-9)
allowedChars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#Method for starting state.
def state0(word, index):
    #Checks if the given input has no more characters left.
    if index >= len(word):
        # Since state 0 isn't an accepting statement, return False.
        return False

    #Gets the character of input at the specified index.
    char = word[index]

    #Checks if the given character is in the array of allowed characters.
    if char in allowedChars:
        #If the char is in the allowed characters it will go into the next state (state1).
        return state1(word, index + 1)

    #If there are no valid characters it will be rejected and return False.
    return False

#Method for accepting state.
def state1(word, index):
    #Checks if given input has no characters left.
    if index >= len(word):
        # Since state 1 is an accepting statement, return True
        return True

    #Gets the character of input at the specified index.
    char = word[index]

    #Checks if the given character is in the array of allowed characters.
    if char in allowedChars:
        #If the char is in the allowed characters it will stay in state1.
        return state1(word, index + 1)

    #Checks if the given character is an underscore.
    elif char == "_":
        #If the char is an underscore it will go back to state0.
        return state0(word, index + 1)

    #If there is no valid characters it will be rejected and return false.
    return False