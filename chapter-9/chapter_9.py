# Exercise 9-1
def long_words():
    fin = open("words.txt")
    for line in fin:
        if len(line) >= 20:
            print(line)

# long_words()

# Exercise 9-2
def has_no_e():
    fin = open("words.txt")
    for line in fin:
        for char in line:
            if char == "e":
                print(False)
        print(line + " " + "true!")

# has_no_e()

def print_words_with_no_e():
    fin = open("words.txt")
    word_counter = 0
    words_without_e = 0
    for line in fin:
        word_counter += 1
        for char in line:
            if char == "e":
                pass
        print(line)
        words_without_e += 1

    percentage_without_e = words_without_e/word_counter
    print(percentage_without_e, "%")

# print_words_with_no_e()

# Exercise 9-3
def avoids(word, str):
    letter_list = list(str)
    for letter in word:
        if letter in letter_list:
            print(False)
            return

    print(True)

# avoids("cat", "pickle")
# avoids("qwerty", "u")

def avoids_with_prompt():
    words = open("words.txt")
    words_list_length = 0
    for i, l in enumerate(words):
        words_list_length += 1

    letters = input("What letters shall we avoid?")
    letters_list = list(letters)

    for word in words:
        for letter in word:
            if letter in letters:
                words_list_length -= 1
            pass
    print("It finished.")
    print(words_list_length)

avoids_with_prompt()