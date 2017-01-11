# in-text exercises
def a_function():
    print("oh hi")

def do_n(obj, n):
    if n <= 0:
        return
    obj()
    print(n)
    do_n(obj, n-1)

# do_n(a_function, 4)

# Exercise 5-3
def check_fermat(a, b, c, n):
    if n > 2:
        if a ** n + b ** n == c ** n:
            print("Whoa, Fermat, dude")
        else:
            print("Yeah, that doesn't work. Checks out.")
    else:
        print("They're less than two. Doesn't count.")

# check_fermat(1, 2, 3, 2)

def fermat_input_check():
    a = int(input("Gimme one number.\n"))
    b = int(input("Gimme another number.\n"))
    c = int(input("Gimme one more number.\n"))
    n = int(input("Gimme one last number.\n"))

    check_fermat(a, b, c, n)

# fermat_input_check()

# Exercise 5-4
def is_triangle(a, b, c):
    nums = [a, b, c]
    nums.sort()
    print(nums)
    if nums[0] + nums[1] > nums[2]:
        print("Yes")
    else:
        print("No")

is_triangle(1, 1, 3)
is_triangle(10, 10, 10)
is_triangle(3, 2, 1)