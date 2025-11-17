floatDigits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def state16(word, index):
    if index >= len(word):
        return False

    char = word[index]

    if char in floatDigits:
        return state17(word, index + 1)
    elif char == ".":
        return state19(word, index + 1)

    return False

def state17(word, index):
    if index >= len(word):
        return False

    char = word[index]

    if char in floatDigits:
        return state17(word, index + 1)
    elif char == "_":
        return state18(word, index + 1)
    elif char == ".":
        return state19(word, index + 1)
    elif char == "e" or char == "E":
        return state21(word, index + 1)

    return False

def state18(word, index):
    if index >= len(word):
        return False

    char = word[index]

    if char in floatDigits:
        return state17(word, index + 1)

    return False

def state19(word, index):
    if index >= len(word):
        return True

    char = word[index]

    if char in floatDigits:
        return state19(word, index + 1)
    elif char == "_":
        return state20(word, index + 1)
    elif char == "e" or char == "E":
        return state21(word, index + 1)

    return False

def state20(word, index):
    if index >= len(word):
        return False

    char = word[index]

    if char in floatDigits:
        return state19(word, index + 1)

    return False

def state21(word, index):
    if index >= len(word):
        return False

    char = word[index]

    if char in floatDigits:
        return state22(word, index + 1)
    elif char == "-" or char == "+":
        return state24(word, index + 1)

    return False

def state22(word, index):
    if index >= len(word):
        return True

    char = word[index]

    if char in floatDigits:
        return state22(word, index + 1)
    elif char == "_":
        return state23(word, index + 1)

    return False

def state23(word, index):
    if index >= len(word):
        return False

    char = word[index]

    if char in floatDigits:
        return state22(word, index + 1)

    return False


def state24(word, index):
    if index >= len(word):
        return False

    char = word[index]

    if char in floatDigits:
        return state22(word, index + 1)

    return False

