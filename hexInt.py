hexDigits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F"]

#Method for starting state.
def state6(word, index):
    #Checks if the given input has no more characters left.
    if index >= len(word):
        # Since state 6 isn't an accepting statement, return False.
        return False

    # Gets the character of input at the specified index.
    char = word[index]

    # Checks if the given character is a 0.
    if char == "0":
        return state7(word, index + 1)

    return False

def state7(word, index):
    #Checks if the given input has no more characters left.
    if index >= len(word):
        # Since state 7 isn't an accepting statement, return False.
        return False

    # Gets the character of input at the specified index.
    char = word[index]
    # Checks if the given character is an x or X.
    if char == "x" or char == "X":
        return state8(word, index + 1)

    return False

def state8(word, index):
    #Checks if the given input has no more characters left.
    if index >= len(word):
        # Since state 8 isn't an accepting statement, return False.
        return False

    # Gets the character of input at the specified index.
    char = word[index]
    # Checks if the given character is in hexDigits.
    if char in hexDigits:
        return state9(word, index + 1)
    # Checks if the given character is an underscore.
    elif char == "_":
        return state10(word, index + 1)

    return False

#Method for accepting state.
def state9(word, index):
    #Checks if the given input has no more characters left.
    if index >= len(word):
        # Since state 9 is an accepting state, return True.
        return True

    # Gets the character of input at the specified index.
    char = word[index]

    # Checks if the given character is in hexDigits.
    if char in hexDigits:
        return state9(word, index + 1)
    # Checks if the given character is an underscore.
    elif char == "_":
        return state10(word, index + 1)

    return False

#Method for if given character is an underscore.
def state10(word, index):
    #Checks if the given input has no more characters left.
    if index >= len(word):
        # Since state 10 isn't an accepting statement, return False.
        return False

    # Gets the character of input at the specified index.
    char = word[index]

    # Checks if the given character is in hexDigits.
    if char in hexDigits:
        return state9(word, index + 1)

    return False

