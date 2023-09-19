print("\nWelcome to Taeyeon quiz!\n")

playing = input("Do you want to play? (yes/quit) ")

if playing.lower() != "yes":
    quit()

print("Sure! Let's play\n")
score = 0

while True:
    answer = input("What is the real name of Taeyeon 태연?\n")
    if answer.upper() == "KIM TAEYEON":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    answer = input("\nWhen is the birthday of Taeyeon 태연?\n")
    if answer.upper() == "MARCH 9 1989" or "9 MARCH 1989":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    answer = input("\nShe is part of what group/subunit?\n")
    if answer.upper() == "SNSD" or "GIRLS GENERATION" or "GOT" or "TAETISEO" \
            or "OH!GG":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    answer = input("\nWhere she was born?\n")
    if answer.upper() == "JEONJU":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    answer = input("\nWhat is the latest album of Taeyeon?\n")
    if answer.upper() == "INVU":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    answer = input("\nWhat is the most awarded song of Taeyeon song?\n")
    if answer.upper() == "INVU":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    answer = input("\nWhat is the song that telling to love yourself/myself?\n")
    if answer.upper() == "DEAR ME":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    answer = input("\nWhat is the second full album of her?\n")
    if answer.upper() == "PURPOSE":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    answer = input("\nWhat is the nickname everyone giving by fans that already know or should know?\n")
    if answer.upper() == "KING OST":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    answer = input("\nWhat is the first solo album of Taeyeon?\n")
    if answer.upper() == "I":
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    break

print("\nYou got " + str(score) + " questions out of 10 correct!")
print("That's equivalent to " + str((score / 10) * 100) + "%")
