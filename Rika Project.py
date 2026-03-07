char = input("Please Enter a Single Alphabet character: ")

if char.isalpha() and len(char)==1:
    print("The character is an alphabet.")
else:
    print("The character is not an alphabet.")