# Exercise 7-1
def print_n(s, n):
    if n <= 0:
        return
    while n > 0:
        print(s)
        n = n -1

print_n("hello kittens", 5)