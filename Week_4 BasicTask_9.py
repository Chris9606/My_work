"""
BINARY_SEARCH_RANGE(alist, range_f, range_l)      // Searches for a value within a specific interval (range_f = range from -/- range_l = range last
    count <-- 0
    lst <-- alist.copy()                          // Makes a copy of the list as it gets altered
    lst.add(None)
    first <-- 0
    last <-- len(lst) - 1
    fount <-- TRUE

    while first <= last and fount != TRUE
        midpoint <-- (first + last) //2               // Gets the middle of the list
        if last[midpoint] in range_f to (range_l+1)   // If the middle is in the range return True
            found <-- TRUE
        else:
            if lst[midpoint] < range_f                // Depending on the middle point ( smaller or larger than the range) splits the list in two
                first <-- midpoint
            else
                last <-- midpoint

        count <-- count + 1
        if count > length[alist] / 2
            return found
            
            
The Big (O) notation is : -----log(n)-------
"""

def binarySearch_range(alist, range_f, range_l):              # Searches for a value within a specific interval (range_f = range from -/- range_l = range last
    count = 0
    lst = alist.copy()                                        # Makes a copy of the list as it gets altered
    lst.append(None)
    first = 0
    last = len(lst)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last) //2                    # Gets the middle of the list
        if lst[midpoint] in range(range_f, (range_l+1)): # If the middle is in the range return True
            found = True
        else:
            if lst[midpoint] < range_f:                  # Depending on the middle point ( smaller or larger than the range) splits the list in two
                first = midpoint
            else:
                last = midpoint
        count = count +1
        if count > (len(alist)/ 2):
            break


    return found
#      0 1 2 3 4  5  6  7  8  9  10
lstt = [1,3,4,9,14,18,27,35,62,75,81]
print (lstt)
range_f =int(input("Range from : "))
range_l = int(input("Range to : "))
print (binarySearch_range(lstt,range_f,range_l))
