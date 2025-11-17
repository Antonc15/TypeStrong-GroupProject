octalDigits = ["0", "1", "2", "3", "4", "5", "6", "7"]

#Method for starting state.
def state11(word, index):
    # Checks if the given input has no more characters left.
    if index >= len(word):
        # Since state 11 isn't an accepting state, return False.
        return False

    # Gets the character of input at the specified index.
    char = word[index]

    #Checks if given character is a 0.
    if char == "0":
        return state12(word, index + 1)

    return False

def state12(word, index):
    # Checks if the given input has no more characters left.
    if index >= len(word):
        # Since state 12 isn't an accepting state, return False.
        return False

    # Gets the character of input at the specified index.
    char = word[index]

    # Checks if the given character is o or O.
    if char == "o" or char == "O":
        return state13(word, index + 1)

    return False

def state13(word, index):
    # Checks if the given input has no more characters left.
    if index >= len(word):
        # Since state 13 isn't an accepting state, return False.
        return False

    # Gets the character of input at the specified index.
    char = word[index]

    # Checks if the given character is in octalDigits.
    if char in octalDigits:
        return state14(word, index + 1)
    # Checks if the given character is a underscore.
    elif char == "_":
        return state15(word, index + 1)

    return False

#Method for accepting state.
def state14(word, index):
    # Checks if the given input has no more characters left.
    if index >= len(word):
        # Since state 14 is an accepting state, return True.
        return True

    # Gets the character of input at the specified index.
    char = word[index]

    # Checks if the given character is in octalDigits.
    if char in octalDigits:
        return state14(word, index + 1)

    # Checks if the given character is a underscore..
    elif char == "_":
        return state15(word, index + 1)

    return False

def state15(word, index):
    # Checks if the given input has no more characters left.
    if index >= len(word):
        # Since state 15 isn't an accepting state, return False.
        return False

    # Gets the character of input at the specified index.
    char = word[index]

    #Checks if given character is in octalDigits.
    if char in octalDigits:
        return state14(word, index + 1)

    return False