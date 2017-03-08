import string

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

# avoids_with_prompt()

# Exercise 9-4
def uses_only(word, letters):
    letters_list = list(set(letters))
    for char in word:
        if char in letters_list:
            pass
        else:
            print(False)
            return
    print(True)

# uses_only("embers", "abc")
# uses_only("embers", "embers")

# Exercise 9-5
def uses_all(word, letters):
    letters_list = list(set(letters))
    for letter in letters_list:
        if letter in word:
            pass
        else:
            print(False)
            return
    print(True)

# uses_all("embers", "emb")
# uses_all("embers", "pdq")

# Exercise 9-6
def is_abecedarian(word):
    alphabet_list = list(string.ascii_lowercase)
    index_last = 0
    index_this = 0
    for letter in word:
        index_last = index_this
        index_this = alphabet_list.index(letter)
        if index_this < index_last:
            print(False)
            return
        else:
            pass
    print(True)

is_abecedarian("abecedarian")
is_abecedarian("abcdefgzzz")
