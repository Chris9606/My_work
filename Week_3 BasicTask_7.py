"""
PRIME_NUMBER_CHECK(number, count <-- 2)
    check <-- number % count
    if check = 0 and number != count or number = 1
        OUTPUT "It is not a prime number!"
        return
    elseif number = check
        OUTPUT "It is a prime number!"
        return

    count <-- count + 1
    PRIME_NUMBER_CHECK(number, count)
"""
def prime_number_check(number,count = 2):
    check = number % count
    if check == 0 and  number != count or number == 1:
        print ( "It's not a prime number")
        return
    elif number == check:
        print ("It is a prime number")
        return
    print (count)
    count+=1
    prime_number_check(number,count)

prime_number_check(199)





