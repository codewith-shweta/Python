#membership operator = 1 in 2 not in
# i really dont know what the heck is this  


word = "CART"
letter = input("Guess a letter in the word: ")

if letter in word:
    print(f"There is a {letter}")

else:
    print(f"{letter} was not found")