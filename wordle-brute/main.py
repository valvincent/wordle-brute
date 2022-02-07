# WELCOME! Please read the readme.md file first
# WELCOME! Please read the readme.md file first
# WELCOME! Please read the readme.md file first
# Follow me on Twitter @heyValVincent


from list import wordlist as wordle_list
import os

keep_running = True
while keep_running:
    initial_remaining_words = []
    secondary_remaining_words = []
    final_list = []

    print(
        "Welcome to Wordle Brute: A program that narrows down possible words for Wordle using elimination."
    )
    print(
        "You will be asked to enter the BLACK/GREY letters first, followed by YELLOW, then GREEN."
    )
    print("A list will be generated with possible words.")
    print(
        "Simply run the program again when you have more black, yellow, and green letters to get a shorter list."
    )

    print(
        "\n\nEnter the letters we know are NOT in the word (aka BLACK/GREY letters)."
    )
    print("Enter in any order without any separators then press enter.")
    black = input("If there are none, leave blank and press enter.\n").lower()
    b_list = list(black)
    b_list = list(dict.fromkeys(b_list))

    print("\n\nEnter the KNOWN letters (aka YELLOW letters).")
    print("Enter in any order without any separators then press enter.")
    yellow = input("If there are none, leave blank and press enter.\n").lower()
    y_list = list(yellow)
    y_list = list(dict.fromkeys(y_list))

    print(
        "\n\nEnter the CORRECT letters (aka GREEN letters) in order, using * for the letters in another color."
    )
    green = input("If there are none, input ***** and press enter.\n").lower()
    g_list = list(green)

    for item in wordle_list:
        broken_word = list(item)
        similar = False
        for x in broken_word:
            for y in b_list:
                if x == y:
                    similar = True
        if not similar:
            initial_remaining_words.append(item)

    for item in initial_remaining_words:
        broken_word = list(item)
        y_match_count = 0
        for x in range(0, len(y_list)):
            if y_list[x] in broken_word:
                y_match_count += 1
        if y_match_count == len(y_list):
            secondary_remaining_words.append(item)

    for item in secondary_remaining_words:
        broken_word = list(item)
        g_match_count = 0
        for x in range(0, 5):
            if g_list[x] == "*":
                continue
            if g_list[x] == broken_word[x]:
                g_match_count += 1
        if g_match_count == 5 - g_list.count("*"):
            final_list.append(item)

    final_list = list(dict.fromkeys(final_list))
    final_list.sort()



    print(f"\n\nPOSSIBLE WORDS:\n")
    for item in final_list:
        print(item.upper())

    if len(final_list) == 1:
        print(
            f"\nWe're left with only {final_list[0].upper()} as the remaining word."
        )
    elif len(final_list) == 0:
        print(
            f"\nLooks like there's no such word that matches the criteria. "
            f"Please review the letters you entered and try again."
        )
    else:
        print(
            f"\nWe've narrowed it down to {len(final_list)} words. See the list above, good luck!"
        )

    run_again = input(f"\nRun the program again? 'Y' or 'N'.\n").lower()
    if run_again == "y":
        os.system('clear')
        keep_running = True
    else:
        keep_running = False
