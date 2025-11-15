allowedChars = ["0", "1", "2", "3", "4", "5", "6", "7"]

def state8(word, index):
    if index >= len(word):
        return False

    char = word[index]

    if char == "0":
        return state9(word, index + 1)

    return False

def state9(word, index):
    if index >= len(word):
        return False

    char = word[index]

    if char == "o":
        return state10(word, index + 1)

    return False

def state10(word, index):
    if index >= len(word):
        return False

    char = word[index]

    if char in allowedChars:
        return state11(word, index + 1)
    elif char == "_":
        return state12(word, index + 1)

    return False

def state11(word, index):
    if index >= len(word):
        return True

    char = word[index]

    if char in allowedChars:
        return state11(word, index + 1)
    elif char == "_":
        return state12(word, index + 1)

    return False

def state12(word, index):
    if index >= len(word):
        return False

    char = word[index]

    if char in allowedChars:
        return state11(word, index + 1)

    return False