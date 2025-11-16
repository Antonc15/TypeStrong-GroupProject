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

choice = input("Do you want to: " + "\n (1) Enter a File \n (2) Enter a single string \n")
if choice == "1":
    fileName = input("Enter file name: ")
    # Opens and takes content from file.
    try:
        with open(fileName, "r") as file:
            # Reads the lines in a file and converts to an array.
            words = file.read().splitlines()
    except FileNotFoundError:
        print("File not found")

    # Iterates through array and checks if the input is accepted or rejected.
    for line in words:
        word = line.split(" ")
        if state0(word[0], 0):
            print(f"Accepted {word[0]}")
        else:
            print(f"Rejected {word[0]}")

elif choice == "2":
    string = input("Enter string to check: ")
    if state0(string, 0):
        print(f"Accepted {string}")
    else:
        print(f"Rejected {string}")

else:
    print("Enter a valid choice")