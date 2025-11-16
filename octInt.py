octalDigits = ["0", "1", "2", "3", "4", "5", "6", "7"]

def state11(word, index):
    if index >= len(word):
        return False

    char = word[index]

    if char == "0":
        return state12(word, index + 1)

    return False

def state12(word, index):
    if index >= len(word):
        return False

    char = word[index]

    if char == "o":
        return state13(word, index + 1)

    return False

def state13(word, index):
    if index >= len(word):
        return False

    char = word[index]

    if char in octalDigits:
        return state14(word, index + 1)
    elif char == "_":
        return state15(word, index + 1)

    return False

def state14(word, index):
    if index >= len(word):
        return True

    char = word[index]

    if char in octalDigits:
        return state14(word, index + 1)
    elif char == "_":
        return state15(word, index + 1)

    return False

def state15(word, index):
    if index >= len(word):
        return False

    char = word[index]

    if char in octalDigits:
        return state14(word, index + 1)

    return False