Alphabet = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
Cipher = [0,4,13,20,23,19,9,12,18,21,25,17,14,11,6,5,10,3,1,26,2,16,7,24,15,8,22]

def NumberSequence(alphabet = Alphabet):
    sequence = []
    for i in range(len(alphabet)):
        for j in range(len(Alphabet)):
            if Alphabet[j] == alphabet[i]:
                sequence.append(j)
    return sequence

def AlphabetSequence(number = Cipher):
    sequence = []
    for i in range(len(number)):
        sequence.append(Alphabet[number[i]])
    return sequence

def CaesarCipherEncryptOld(shift,phrase,alphabet = Alphabet,decrypt = False):
    output = ""
    if decrypt == True:
        shift = -shift
    for i in range(len(phrase)):
        for j in range(27):
            if phrase[i] == Alphabet[j]:
                while j + shift > 26:
                    shift -= 27
                while j + shift < 0:
                    shift += 27
                output += Alphabet[j + shift]
    return output

def CaesarCipherCrackOld(phrase,alphabet = Alphabet):
    outputs = []
    for k in range (1,27):
        output = ""
        for i in range(len(phrase)):
            for j in range(27):
                if phrase[i] == Alphabet[j]:
                    if j + k > 26:
                        k -= 27
                    output += Alphabet[j + k]
        outputs.append(output)
    return outputs

def CaesarCipherEncrypt(shift,phrase,alphabet = Alphabet,decrypt = False):
    output = ""
    if decrypt == True:
        shift = -shift
    for i in range(len(phrase)):
        if phrase[i] in alphabet:
            char = (alphabet.index(phrase[i]) + shift) % 27
            output += Alphabet[char]
    return output

def CaesarCipherCrack(phrase,alphabet = Alphabet):
    outputs = []
    for k in range (1,27):
        output = str(27 - k) + "-"
        for i in range(len(phrase)):
            if phrase[i] in alphabet:
                char = (alphabet.index(phrase[i]) + k) % 27
                output += Alphabet[char]
        outputs.append(output)
    return outputs

def EnigmaRotor(phrase,alphabet = Alphabet,cipher = Cipher,rate = 1,decrypt=False):
    global output
    output = ""
    tempword = []
    if decrypt == True:
        rotation = 27
    else:
        rotation = -1 
    for i in range(len(phrase)):
        for j in range(len(alphabet)):
            if alphabet[j] == phrase[i]:
                tempword.append(j)
            else:
                "Do nothing"
    if decrypt == True:
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

def EnigmaPlugboard(ori_phrase,encrypt_phrase,ori_char = ["E","T","A"],code_char = ["W","R","M"]):
    output = []
    for i in range(len(encrypt_phrase)):
        output.append(encrypt_phrase[i])
    for i in range(len(ori_phrase)):
        for j in range(len(ori_char)):
            if ori_phrase[i] == ori_char[j]:
                output[i] = code_char[j]
    output = ''.join(output)
    return output
