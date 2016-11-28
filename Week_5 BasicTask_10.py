
def biggest_sequence (lst,count=0,output=[], A=0):

    if A >= (len(lst) - 1):
        print(max(output,key=len))  # max applies the key function to each element of your list and picks the one where the key function returned the biggest
        return

    output.append([])

    while True:
        i = lst[A]
        if i != lst[len(lst)-1] and  i < lst[lst.index(i)+1]:
            output[count].append(i)
            A +=1
        else:
            output[count].append(i)
            A +=1
            count += 1
            biggest_sequence(lst,count,output,A)
            return



sequence = [3,4,6,12,1,7,3,25,28,29,50,30]
biggest_sequence(sequence)

