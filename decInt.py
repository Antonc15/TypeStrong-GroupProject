#Make an array for the allowed characters that are in decimal integers in Python (0-9)
nonZeroDigits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

#Method for starting state.
def state1(word, index):
    #Checks if the given input has no more characters left.
    if index >= len(word):
        # Since state 0 isn't an accepting statement, return False.
        return False

    #Gets the character of input at the specified index.
    char = word[index]

    #Checks if the given character is in the array of allowed characters.
    if char == '0':
        return state2(word, index + 1)
    if char in nonZeroDigits:
        #If the char is in the allowed characters it will go into the next state (state2).
        return state4(word, index + 1)

    #If there are no valid characters it will be rejected and return False.
    return False

def state2(word, index):
    #Checks if the given input has no more characters left.
    if index >= len(word):
        # Since state 0 isn't an accepting statement, return False.
        return True

    #Gets the character of input at the specified index.
    char = word[index]

    #Checks if the given character is in the array of allowed characters.
    if char == '0':
        #If the char is in the allowed characters it will go into the next state (state2).
        return state2(word, index + 1)
    if char == '_':
        return state3(word, index + 1)

    #If there are no valid characters it will be rejected and return False.
    return False

def state3(word, index):
    #Checks if the given input has no more characters left.
    if index >= len(word):
        # Since state 0 isn't an accepting statement, return False.
        return False

    #Gets the character of input at the specified index.
    char = word[index]

    #Checks if the given character is in the array of allowed characters.
    if char == '0':
        #If the char is in the allowed characters it will go into the next state (state2).
        return state2(word, index + 1)

    #If there are no valid characters it will be rejected and return False.
    return False

#Method for accepting state.
def state4(word, index):
    #Checks if given input has no characters left.
    if index >= len(word):
        # Since state 1 is an accepting statement, return True
        return True

    #Gets the character of input at the specified index.
    char = word[index]

    #Checks if the given character is in the array of allowed characters.
    if char in nonZeroDigits or char  == '0':
        #If the char is in the allowed characters it will stay in state2.
        return state4(word, index + 1)

    #Checks if the given character is an underscore.
    elif char == "_":
        #If the char is an underscore it will go back to state1.
        return state5(word, index + 1)

    #If there is no valid characters it will be rejected and return false.
    return False

def state5(word, index):
    #Checks if the given input has no more characters left.
    if index >= len(word):
        # Since state 0 isn't an accepting statement, return False.
        return False

    #Gets the character of input at the specified index.
    char = word[index]

    #Checks if the given character is in the array of allowed characters.
    if char in nonZeroDigits or char  == '0':
        #If the char is in the allowed characters it will go into the next state (state2).
        return state4(word, index + 1)

    #If there are no valid characters it will be rejected and return False.
    return False