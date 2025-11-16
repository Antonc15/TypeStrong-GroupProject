from decInt import state1
from hexInt import state6
from octInt import state11
from float import state16

def state0(word, index):
    if state1(word, index):
        return True
    elif state6(word, index):
        return True
    elif state11(word, index):
        return True
    elif state16(word, index):
        return True
    return False

#Opens and takes content from file.
try:
    with open("in_ans.txt", "r") as file:
        #Reads the lines in a file and converts to an array.
        words = file.read().splitlines()
except FileNotFoundError:
    print("File not found")

#Iterates through array and checks if the input is accepted or rejected.
for word in words:
    if state0(word, 0):
        print(f"Accepted {word}")
    else:
        print(f"Rejected {word}")