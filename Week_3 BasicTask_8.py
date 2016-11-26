"""
REMOVE_VOWELS(word <-- None, i <-- 0, vowels <-- ('a','e', 'i','o','u')  // (i) the index of the current letter
    if word [i].lowercase() in vowels                                    // Checks if the letter is a vowel and if t is it removes it
        remove w[i]
        i <-- i - 1
    if i = length[word] - 1
        return word
    REMOVE_VOWELS(word, i +1)

"""

def remove_vowels(word, i=0,vowels = ('a','e', 'i','o','u')):  # (i) the index of the current letter
    if word[i].lower() in vowels:                              # Checks if the letter is a vowel and if t is it removes it
        word = word.replace(word[i],"")
        i -= 1
    if i == len(word) -1:
        print (word)
        return
    remove_vowels(word,i+1)



remove_vowels("beautiful")
