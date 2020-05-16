# Faulty calculator
operator = input("Enter operator:")
val1 = int(input("Enter first operand = "))
val2 = int(input("Enter second operand = "))

if operator == "+":
    if val1 == 56 and val2 == 9:
        print("77")
    else:
        print("Sum is:",val1 + val2)
if operator == "-":
    print("Substract is:",val1-val2)
if operator == "*":
    if val1 == 45 and val2 == 3:
        print("555")
    else:
        print("Multiply is :",val1*val2)
if operator == "/":
    if val1 ==56 and val2 == 6:
        print("4")
    else:
        print("Divide is:",float(val1/val2))

# Faulty calculator try again version!

while True:
    operator = input("Enter operator:")
    val1 = int(input("Enter first operand = "))
    val2 = int(input("Enter second operand = "))

    if operator == "+" and val1 == 56 and val2 == 9:
        print("Ans:77")
        inp = input("press y for continue\n and press n for quit!")
        if inp == "y":
            continue
        else:
            break
    elif operator == "+":
        print("Ans: " , val1 + val2)
        inp = input("press y for continue\n and press n for quit!")
        if inp == "y":
            continue
        else:
            break
    elif operator == "-":
        print("Ans: " , val1 - val2)
        inp = input("press y for continue\n and press n for quit!")
        if inp == "y":
            continue
        else:
            break
    elif operator == "*" and val1 == 45 and val2 == 3:
        print("Ans: 555")
        inp = input("press y for continue\n and press n for quit!")
        if inp == "y":
            continue
        else:
            break
    elif operator == "*":
        print("Ans: " , val1 * val2)
        inp = input("press y for continue\n and press n for quit!")
        if inp == "y":
            continue
        else:
            break
    elif operator == "/" and val1 == 56 and val2 == 6:
        print("4")
        inp = input("press y for continue\n and press n for quit!")
        if inp == "y":
            continue
        else:
            break
    elif operator == "/":
        print("Ans: " , val1 / val2)
        inp = input("press y for continue\n and press n for quit!")
        if inp == "y":
            continue
        else:
            break
    else:
        break








