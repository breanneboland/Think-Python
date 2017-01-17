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

def is_palindrome(word):
    if len(word) <= 1:
        return True
    if first(word) != last(word):
        return False
    return is_palindrome(middle(word))

print(is_palindrome("allen"))
print(is_palindrome("bob"))
print(is_palindrome("a man a plan a canal panama"))
print(is_palindrome("p"))
