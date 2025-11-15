allowedChars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def state13(word, index):
    if index >= len(word):
        return False

    char = word[index]

    if char in allowedChars:
        return state14(word, index + 1)
    elif char == ".":
        return state16(word, index + 1)

    return False

def state14(word, index):
    if index >= len(word):
        return False

    char = word[index]

    if char in allowedChars:
        return state14(word, index + 1)
    elif char == "_":
        return state15(word, index + 1)
    elif char == ".":
        return state16(word, index + 1)
    elif char == "e" or char == "E":
        return state18(word, index + 1)

    return False

def state15(word, index):
    if index >= len(word):
        return False

    char = word[index]

    if char in allowedChars:
        return state14(word, index + 1)

    return False

def state16(word, index):
    if index >= len(word):
        return True

    char = word[index]

    if char in allowedChars:
        return state16(word, index + 1)
    elif char == "_":
        return state17(word, index + 1)
    elif char == "e" or char == "E":
        return state18(word, index + 1)

    return False

def state17(word, index):
    if index >= len(word):
        return False

    char = word[index]

    if char in allowedChars:
        return state16(word, index + 1)

    return False

def state18(word, index):
    if index >= len(word):
        return False

    char = word[index]

    if char in allowedChars:
        return state19(word, index + 1)
    elif char == "-" or char == "+":
        return state21(word, index + 1)

    return False

def state19(word, index):
    if index >= len(word):
        return True

    char = word[index]

    if char in allowedChars:
        return state19(word, index + 1)
    elif char == "_":
        return state20(word, index + 1)

    return False

def state20(word, index):
    if index >= len(word):
        return False

    char = word[index]

    if char in allowedChars:
        return state19(word, index + 1)

    return False


def state21(word, index):
    if index >= len(word):
        return False

    char = word[index]

    if char in allowedChars:
        return state19(word, index + 1)

    return False

