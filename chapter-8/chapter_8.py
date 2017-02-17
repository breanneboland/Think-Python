# Exercise 8-1
def letters_backward(str):
    index = len(str)
    for i in range(1, (index + 1)):
        print(str[-i])

# letters_backward("dog")
# letters_backward("platypus")

# Exercise 8-2
def ack_maker():
    prefixes = "JKLMNOPQ"
    suffix = "ack"
    for letter in prefixes:
        if letter == "O" or letter == "Q":
            print(letter + "u" + suffix)
        else:
            print(letter + suffix)

# ack_maker()

# Exercise 8-4
def find(word, letter, index=0):
    while index < len(word):
        if word[index] == letter:
            print(index)
        index = index + 1
    return -1

# find("pragmatism", "i")
# find("banana", "a", 5)
# find("hyperdrive", "q")

# Exercise 8-5
def count(string, letter):
    count = 0
    for char in string:
        if char == letter:
            count += 1
    print(count)

# count("banana", "a")
# count("chicken", "e")
# count("sad panda", "q")

# Exercise 8-7
sample_string = "banana"
# print(sample_string.count("a"))

# Exercise 8-8
string_again = "121212hi121212"
string_again_again = "     hello     "
print(string_again.strip("12"))
print(string_again_again.strip(" "))

string1 = "this is a sample string I will replace things in"
print(string1.replace("is", "declares"))
print(string1.replace("i", "super pickles"))