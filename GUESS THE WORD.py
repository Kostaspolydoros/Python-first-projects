import random
Words =["dog", "microwave", "phone", "bedroom", "plate", "jacket"]
word = random.choice(Words)
print("Let's play <<GUESS THE WORD>>")
choice = input("If you want to play type yes ")

if choice == "yes":
    print("The word has", len(word), "letters")
    if word == "dog":
        print("It is a pet and has often been described as a man's best friend.")
        print("You have 3 guesses")
        for x in range(1, 4):
            guess = input("Guess the word: ")
            if guess == "dog":
                 print("Correct")
                 break
            else:
                 y = 3 - int(x)
                 print("Incorrect, you have", y, "more guesses")
if word == "microwave":
    print("It is a piece of kitchen equipment used to heat food")
    print("You have 3 guesses")
    for x in range(1, 4):
        guess = input("Guess the word: ")
        if guess == "microwave":
            print("Correct")
            break
        else:
            y = 3 - int(x)
            print("Incorrect, you have", y, "more guesses")
if word == "phone":
    print("It is a device used to call people")
    print("You have 3 guesses")
    for x in range(1, 4):
        guess = input("Guess the word: ")
        if guess == "phone":
            print("Correct")
            break
        else:
            y = 3 - int(x)
            print("Incorrect, you have", y, "more guesses")
if word == "bedroom":
    print("It is the room in which people sleep")
    print("You have 3 guesses")
    for x in range(1, 4):
        guess = input("Guess the word: ")
        if guess == "bedroom":
            print("Correct")
            break
        else:
            y = 3 - int(x)
            print("Incorrect, you have", y, "more guesses")
if word == "plate":
    print("It is a piece of kitchenware in which people put food")
    print("You have 3 guesses")
    for x in range(1, 4):
        guess = input("Guess the word: ")
        if guess == "plate":
            print("Correct")
            break
        else:
            y = 3 - int(x)
            print("Incorrect, you have", y, "more guesses")
if word == "jacket":
    print("It is a piece of clothing people put on when it is cold outside")
    print("You have 3 guesses")
    for x in range(1, 4):
        guess = input("Guess the word: ")
        if guess == "jacket":
            print("Correct")
            break
        else:
            y = 3 - int(x)
            print("Incorrect, you have", y, "more guesses")



