# Astrologer's Stars program

# Ques. Input two values from the user, one for no. of rows of stars and
#       and second is boolean input(True or False) to determine the orientaion of the stars.

n = int(input("Enter num of rows: "))
orientation = int(input("Enter 0 for upper triangle\n Enter 1 for lower triangle"))
b = bool(orientation)
t = n

if b == True:
    while n > 0:
        print(n * "*")
        n = n - 1


elif b == False:
    while n > 0:
        a = (t + 1) - n
        print(a * "*")
        n = n - 1

# This is amit's code



