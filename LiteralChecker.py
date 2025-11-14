from decInt import state0

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