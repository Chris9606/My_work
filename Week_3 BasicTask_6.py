"""
REVERSE_SENTENCE(sentence)
    sentence <-- sentence + " "                     O(1)
    container <-- ()                                 -
    start <-- 0                                      -
    end <-- 0                                        -
    rev_sent <-- ''                                 O(1)

    while end < length[sentence]                      O(n)
        if sentence[end] <-- " "                      O(n?)
            container.add(sentence[start:end + 1])      -
            end <-- end + 1                             -
            start <-- end                             O(n?)
        end <-- end + 1                               O(n)

    for i <-- len(container)-1 to -1 by -1            O(n)
        rev_sent <-- rev_sent + container[i]          O(n)
    return rev_sent                                   O(1)

    Big (O) Notation : O(n)


"""


def reverse_sentace(sentence):
    sentence = sentence + " "  #adds a white space in the end of the sentance
    container = []
    start = 0
    end = 0
    rev_sent = ""
    while end < len(sentence):   # Makes the string input a list of strings
        if sentence[end] == " ":
            container.append(sentence[start:end + 1])
            end += 1
            start = end
        end += 1

    for i in range((len(container)-1),-1, -1):    # Turns the list of words around
        rev_sent = rev_sent + container[i]
    print (rev_sent)

reverse_sentace("This is awesome")

