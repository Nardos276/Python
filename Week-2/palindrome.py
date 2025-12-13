x = int(input("Enter an integer: "))
if x < 0:
    print(False)
else:
    original = x
    reversed_num = 0
    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x = x // 10
    if original == reversed_num:
        print(True)
    else:
        print(False)
