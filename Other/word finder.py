dictionary = open("WordList.txt").readlines()
words = []
matches = []
letters = list("zcabheinpavz")      # control letters here

for line in dictionary:
    line = line[:-1]
    if len(line) == 5:       # control size here
        words.append(line)

# different ways to search
def exact_search(words,letters):    # searches only with letters
    matches = []
    for word in words:
        try:
            cletters = list(letters)
            for letter in list(word):
                cletters.remove(letter)
            matches.append(word)
        except:
            "do nothing"
    return matches

def contains(array,term):         # does array contain smaller array in order
    for i in range(len(array)):
        if len(term) > len(array): return False
        if len(term) == len(array): return array == term

        cont = True
        for j in range(len(term)):
            if array[j] != term[j]: cont = False
        if cont: return True

        array = array[1:]
    return False

def wide_search(words,letters):   # search allows suffixes and prefixes
    matches = []
    for word in words:
        try:
            cletters = list(letters)+list("ingedry")
            for letter in list(word):
                cletters.remove(letter)
            matches.append(word)
        except:
            "do nothing"
    return matches

print(len(words))      # number of words of same length

matches = exact_search(words,letters)
print(len(matches))
print(matches)

matches = wide_search(words,letters)
print(len(matches))
print(matches)

