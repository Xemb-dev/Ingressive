# Check if two words are anagrams 
# Example:g
#print(find_anagram("hello", "check")) --> False
#print(find_anagram("below", "elbow"))  --> True


def find_anagram(word, anagram):
    """"
    Determines if a code is an anagram or not
    
    Argument: takes in two parameters of type string
    
    returns: a boolean value to signify if both arguments are Anagrams or not
    """
    # [assignment] Add your code here
    if len(word) == len(anagram):
        word=list(word)
        anagram= list(anagram)
        for i in word:
            if word.count(i) != anagram.count(i):
                return False
            print(i)
        return True
    else:
        return False
                