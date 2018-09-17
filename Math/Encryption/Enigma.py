Alphabet = ["0","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
Cipher = [0,4,13,20,23,19,9,12,18,21,25,17,14,11,6,5,10,3,1,26,2,16,7,24,15,8,22]
Cipher2 = [0,8,17,26,7,16,10,20,13,15,2,12,14,3,9,6,4,25,1,23,22,5,21,19,18,11,24]
RefCipher = [0,17,25,8,15,7,14,5,3,22,16,21,26,20,6,4,10,1,24,23,13,11,9,19,18,2,12]
inword = "ATLKUCYLSGJITASGQAGJ"

def NumberSequence(alphabet):
    sequence = []
    for i in range(len(alphabet)):
        for j in range(len(Alphabet)):
            if Alphabet[j] == alphabet[i]:
                sequence.append(j)
    return sequence

def AlphabetSequence(number):
    sequence = []
    for i in range(len(number)):
        sequence.append(Alphabet[number[i]])
    return sequence

Numbers = NumberSequence(Alphabet)
CipherAlphabet = AlphabetSequence(Cipher)
Cipher2Alphabet = AlphabetSequence(Cipher2)
RefCipherAlphabet = AlphabetSequence(RefCipher)

def code(original,alphabet,cipher,rate,reverse=False):
    global output
    output = ""
    tempword = []
    if reverse == True:
        rotation = 27
    else:
        rotation = -1 
    for i in range(len(original)):
        for j in range(len(alphabet)):
            if alphabet[j] == original[i]:
                tempword.append(j)
            else:
                "Do nothing"
    if reverse == True:
        for i in range(len(tempword)):
            if i%rate == 0:
                rotation -= 1
            temp = tempword[i]+rotation
            if temp > 26:
                temp -= 26
            output += str(cipher[temp])
        return output
    for i in range(len(tempword)):
        if i%rate == 0:
            rotation += 1
        if rotation > 26:
            rotation = 0
        temp = tempword[i]+rotation
        if temp > 26:
            temp -= 26
        output += str(alphabet[cipher[temp]])
    return output

def plugboard(phrase,coded,original,changed):
    sep = ''
    output = []
    for i in range(len(coded)):
        output.append(coded[i])
    for i in range(len(phrase)):
        for j in range(len(original)):
            if phrase[i] == original[j]:
                output[i] = changed[j]
    output = sep.join(output)
    return output


r1word = code(inword,Alphabet,Cipher,1)
r2word = code(r1word,Alphabet,Cipher,3)
refword = code(r2word,Alphabet,RefCipher,1000)
rev2word = code(refword,CipherAlphabet,Alphabet,3,True)
rev1word = code(rev2word,CipherAlphabet,Alphabet,1,True)
finalword = plugboard(inword,rev1word,["E","T","A"],["W","R","M"])

print(inword)
print(r1word)
print(r2word)
print(refword)
print(rev2word)
print(rev1word)
print(finalword)

