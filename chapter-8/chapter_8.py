# Exercise 8-1
def letters_backward(str):
    index = len(str)
    for i in range(1, (index + 1)):
        print(str[-i])

letters_backward("dog")
letters_backward("platypus")