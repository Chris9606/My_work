"""
PRIME_NUMBER_CHECK(number, count <-- 2)
    check <-- number % count
    if check = 0 and number != count or number = 1
        OUTPUT "It is not a prime number!"
        return
    elseif number = count
        OUTPUT "It is a prime number!"
        return

    count <-- count + 1
    PRIME_NUMBER_CHECK(number, count)
"""
def prime_number_check(number,count = 2):            # Devides the number by 2 up to the value of the number.
    check = number % count
    if check == 0 and  number != count or number == 1:   # If The number devides by anything which is not itself or if the number is 1
        print ( "It's not a prime number")               # It is NOT  a prime number
        return
    elif number == count:                            # Otherwise, it is.
        print ("It is a prime number")
        return
    count+=1
    prime_number_check(number,count)

prime_number_check(199)



