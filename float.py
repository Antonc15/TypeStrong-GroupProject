# Make an array for allowed characters that are in floats in python (0-9).
floatDigits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

#Method for starting state
def state16(word, index):
    # Checks if the given input has no more characters left.
    if index >= len(word):
        # Since state 16 isn't an accepting state, return False.
        return False
    # Gets the character of input at the specified index.
    char = word[index]

    # Checks if given character is in floatDigits.
    if char in floatDigits:
        return state17(word, index + 1)
    # Checks if the given character is a period.
    elif char == ".":
        return state19(word, index + 1)

    return False

def state17(word, index):
    # Checks if the given input has no more characters left.
    if index >= len(word):
        # Since state 17 isn't an accepting state, return False.
        return False

    # Gets the character of input at the specified index.
    char = word[index]

    # Checks if given character is in floatDigits.
    if char in floatDigits:
        return state17(word, index + 1)
    # Checks if the given character is an underscore.
    elif char == "_":
        return state18(word, index + 1)
    # Checks if the given character is a period.
    elif char == ".":
        return state19(word, index + 1)
    # Checks if the given character is either e or E.
    elif char == "e" or char == "E":
        return state21(word, index + 1)

    return False

def state18(word, index):
    # Checks if the given input has no more characters left.
    if index >= len(word):
        # Since state 16 isn't an accepting state, return False.
        return False

    # Gets the character of input at the specified index.
    char = word[index]

    # Checks if given character is in floatDigits.
    if char in floatDigits:
        return state17(word, index + 1)

    return False

#Method for accepting state.
def state19(word, index):
    # Checks if the given input has no more characters left.
    if index >= len(word):
        # Since state 19 is an accepting state, return True.
        return True

    # Gets the character of input at the specified index.
    char = word[index]

    # Checks if given character is in floatDigits.
    if char in floatDigits:
        return state19(word, index + 1)
    # Checks if the given character is an underscore.
    elif char == "_":
        return state20(word, index + 1)
    # Checks if the given character is e or E.
    elif char == "e" or char == "E":
        return state21(word, index + 1)

    return False

def state20(word, index):
    # Checks if the given input has no more characters left.
    if index >= len(word):
        # Since state 20 isn't an accepting state, return False.
        return False

    # Gets the character of input at the specified index.
    char = word[index]

    # Checks if given character is in floatDigits.
    if char in floatDigits:
        return state19(word, index + 1)

    return False

def state21(word, index):
    # Checks if the given input has no more characters left.
    if index >= len(word):
        # Since state 16 isn't an accepting state, return False.
        return False

    # Gets the character of input at the specified index.
    char = word[index]

    # Checks if given character is in floatDigits.
    if char in floatDigits:
        return state22(word, index + 1)
    # Checks if the given character is a + or -.
    elif char == "-" or char == "+":
        return state24(word, index + 1)

    return False

#Method for accepting state
def state22(word, index):
    # Checks if the given input has no more characters left.
    if index >= len(word):
        # Since state 22 is an accepting state, return True.
        return True

    # Gets the character of input at the specified index.
    char = word[index]

    # Checks if given character is in floatDigits.
    if char in floatDigits:
        return state22(word, index + 1)
    # Checks if the given character is an underscore.
    elif char == "_":
        return state23(word, index + 1)

    return False

def state23(word, index):
    # Checks if the given input has no more characters left.
    if index >= len(word):
        # Since state 23 isn't an accepting state, return False.
        return False

    # Gets the character of input at the specified index.
    char = word[index]

    # Checks if given character is in floatDigits.
    if char in floatDigits:
        return state22(word, index + 1)

    return False


def state24(word, index):
    # Checks if the given input has no more characters left.
    if index >= len(word):
        # Since state 24 isn't an accepting state, return False.
        return False

    # Gets the character of input at the specified index.
    char = word[index]

    # Checks if given character is in floatDigits.
    if char in floatDigits:
        return state22(word, index + 1)

    return False

