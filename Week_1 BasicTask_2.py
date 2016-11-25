number = int(input("Enter a number: "))

for i in range(number, 0, -1):             # Calculates the factorial number
    number = number * i

print ("The factoria number is : ", number)
number = list( map(int, str(number)))      # Makes a list of the digits in the number

count = len(number)
while True:                                # Counts the number of trailing 0s in the end of the factorial number
    if number[count - 1] == 0:             # Iterates over the digits in the factorial number starting from the end
        count -= 1
    else:
        print("The number of trailing 0s is the factorial number is : ", int(len(number)) - count)
        break




