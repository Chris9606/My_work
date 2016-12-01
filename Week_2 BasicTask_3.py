"""
PERFECT_SQUARE(number)
digit <-- 0
perfect_square <-- none

while TRUE                      // Incrementing a digit starting from 1 until it's perfect square
    digit <-- digit + digit      // is more than the given number and prints the previous perfect square
    if digit**2 <-- number
        perfect_square <-- digit**2
    else
        return perfect_square

"""

def perfect_square(number):
    digit = 0
    perfect_square = None

    while True:                                           # Incrementing a digit starting from 1 until it's perfect square
        digit += 1                                        # is more than the given number and prints the previous perfect square
        if digit**2 < number:
            perfect_square = digit**2
        else:
            print ("The closest perfect square is : ", perfect_square)
            break

number = int(input("Enter a number to find the closest perfect square which is less or equal to it : "))
perfect_square(number)


