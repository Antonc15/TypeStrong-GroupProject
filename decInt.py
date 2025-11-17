# Make an array for the nonzero characters that are in decimal integers in Python (1-9)
nonZeroDigits = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# Method for starting state.
def state1(word, index):
    # Checks if the given input has no more characters left.
    if index >= len(word):
        # Since state 1 isn't an accepting state, return False.
        return False

    # Gets the character of input at the specified index.
    char = word[index]

    # Checks if the given character is 0.
    if char == '0':
        return state2(word, index + 1)
    # Checks if the given character is in nonZeroDigits.
    if char in nonZeroDigits:
        return state4(word, index + 1)

    # If there are no valid characters it will be rejected and return False.
    return False

#Method accepting state.
def state2(word, index):
    # Checks if the given input has no more characters left.
    if index >= len(word):
        # Since state 2 is an accepting state, return True.
        return True

    # Gets the character of input at the specified index.
    char = word[index]

    # Checks if the given character is 0.
    if char == '0':
        return state2(word, index + 1)
    # Checks if the given character is an underscore.
    if char == '_':
        return state3(word, index + 1)

    # If there are no valid characters it will be rejected and return False.
    return False

def state3(word, index):
    # Checks if the given input has no more characters left.
    if index >= len(word):
        # Since state 3 isn't an accepting state, return False.
        return False

    # Gets the character of input at the specified index.
    char = word[index]

    # Checks if the given character is 0.
    if char == '0':
        return state2(word, index + 1)

    # If there are no valid characters it will be rejected and return False.
    return False

# Method for accepting state.
def state4(word, index):
    # Checks if given input has no characters left.
    if index >= len(word):
        # Since state 4 is an accepting state, return True
        return True

    # Gets the character of input at the specified index.
    char = word[index]

    # Checks if the given character is in nonZeroDigits or if the given character is 0.
    if char in nonZeroDigits or char  == '0':
        return state4(word, index + 1)

    # Checks if the given character is an underscore.
    elif char == "_":
        return state5(word, index + 1)

    # If there is no valid characters it will be rejected and return false.
    return False

def state5(word, index):
    #Checks if the given input has no more characters left.
    if index >= len(word):
        # Since state 5 isn't an accepting state, return False.
        return False

    #Gets the character of input at the specified index.
    char = word[index]

    # Checks if the given character is in nonZeroDigits or if the given character is 0.
    if char in nonZeroDigits or char  == '0':
        return state4(word, index + 1)

    #If there are no valid characters it will be rejected and return False.
    return False