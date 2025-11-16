hexDigits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "A", "B", "C", "D", "E", "F"]

def state6(word, index):
    if index >= len(word):
        return False

    char = word[index]

    if char == "0":
        return state7(word, index + 1)

    return False

def state7(word, index):
    if index >= len(word):
        return False

    char = word[index]

    if char == "x":
        return state8(word, index + 1)

    return False

def state8(word, index):
    if index >= len(word):
        return False

    char = word[index]

    if char in hexDigits:
        return state9(word, index + 1)
    elif char == "_":
        return state10(word, index + 1)

    return False

def state9(word, index):
    if index >= len(word):
        return True

    char = word[index]

    if char in hexDigits:
        return state9(word, index + 1)
    elif char == "_":
        return state10(word, index + 1)

    return False

def state10(word, index):
    if index >= len(word):
        return False

    char = word[index]

    if char in hexDigits:
        return state9(word, index + 1)

    return False


