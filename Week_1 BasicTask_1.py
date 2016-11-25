from random import randint

list_1 = [5,3,8,6,1,9,2,7]                   # The list that has to be randomized
list_2 = [i for i in range(len(list_1))]     # Creates a second list with the same size
count=0
filled_index=[]                              # Stores the indexes already taken in the second list

while count!=len(list_1):                    # Stops when all of the elements of the first list have been added to the second
    el = randint(0,(len(list_1) - 1))        # Generates a random index from the second list
    if el not in filled_index:               # Checks if that index has already been taken in order to insert
        filled_index.append(el)              # Updates the taken indexes
        list_2[el] = list_1[count]           # Inserts from the first list into the free index  of the second list
        count = count + 1

print ("Original list : ",list_1)
print ("Shuffled list : ",list_2)