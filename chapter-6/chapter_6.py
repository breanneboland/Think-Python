# Exercise 6-5
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

word1 = "hi"
word2 = "how"
word3 = "i"
word4 = ""

# last(word4)
# middle(word1)
# first(word4)

# Exercise 6-6
def is_palindrome(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

# print(is_palindrome("allen"))
# print(is_palindrome("bob"))
# print(is_palindrome("a man a plan a canal panama"))
# print(is_palindrome("p"))

# Exercise 6-7
def is_power(a, b):
    if type(a) != int and type(b) != int:
        print("Not ints, can't play.")
    elif a % b == 0 and (a/b) % b == 0:
        print(True)
    else:
        print(False)

is_power(4, 2)
is_power(16, 4)
is_power(23, 5)
is_power("donut", 1.5)