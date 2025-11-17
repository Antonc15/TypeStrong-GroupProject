from decInt import state1
from hexInt import state6
from octInt import state11
from float import state16

#Method to combine all decimal, hexadecimal, octal, and float methods(NFAs) into one singular method(NFA).
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

with open("out.txt", "w") as outputFile:
    while True:
        #Asks users what input they want to enter.
        choice = input("Do you want to: " + "\n (1) Enter a File \n (2) Enter a single string " +
            "\n (3) Exit the program. \n")

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
                    if word[1] == "accept":
                        print(f"Accepted {word[0]}")
                        print(f"Accepted {word[0]}", file=outputFile)
                    else:
                        print(f"Accepted {word[0]} (Rejected)")
                        print(f"Accepted {word[0]} (Rejected)", file=outputFile)
                else:
                    if word[1] == "reject":
                        print(f"Rejected {word[0]}")
                        print(f"Rejected {word[0]}", file=outputFile)
                    else:
                        print(f"Rejected {word[0]} (Accepted)")
                        print(f"Rejected {word[0]} (Accepted)", file=outputFile)

        elif choice == "2":
            #Asks users what type of literal they would like to check.
            choice2 = input("Do you want to check if:  " + "\n (1) String is a decimal integer literal." +
                            "\n (2) String is a hexadecimal integer literal." + "\n (3) String is a octal integer literal." +
                            "\n (4) String is a float literal." + "\n (5) Any python Literal. \n")

            #Asks users to enter a string to check.
            string = input("Enter string to check: ")

            #Decimal Literal
            if choice2 == "1":
                if state1(string, 0):
                    print(f"Accepted decimal literal {string}")
                else:
                    print(f"Rejected decimal literal {string}")
            #Hexadecimal Literal
            elif choice2 == "2":
                if state6(string, 0):
                    print(f"Accepted hexadecimal literal {string}")
                else:
                    print(f"Rejected hexadecimal literal {string}")
            #Octal Literal
            elif choice2 == "3":
                if state11(string, 0):
                    print(f"Accepted octal literal {string}")
                else:
                    print(f"Rejected octal literal {string}")
            #Float Literal
            elif choice2 == "4":
                if state16(string, 0):
                    print(f"Accepted float literal {string}")
                else:
                    print(f"Rejected float literal {string}")
            #Any literal.
            elif choice2 == "5":
                if state0(string, 0):
                    print(f"Accepted literal {string}")
                else:
                    print(f"Rejected literal {string}")
            else:
                print("Invalid input")
        elif choice == "3":
            break
        else:
            print("Enter a valid choice")

        print("-----")