try:
    a = int(input("Give me a number, please "))
    b = int(input("Give me another number, please "))
except ValueError:
    print("one of the numbers was invalid")
else:
    if a > b:
        print(a, ">", b)
    elif a < b:
        print(a, "<", b)
    else:
        print(a, "=", b)