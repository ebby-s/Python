Alphabet = [" ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
loop = True

def Encrypt(shift,phrase,alphabet = Alphabet):
    output = ""
    for i in range(len(phrase)):
        if phrase[i] in alphabet:
            char = (alphabet.index(phrase[i]) + shift) % 27
            output += Alphabet[char]
    return output

def Crack(phrase,alphabet = Alphabet):
    outputs = []
    for k in range (1,27):
        output = str(27 - k) + "-"
        for i in range(len(phrase)):
            if phrase[i] in alphabet:
                char = (alphabet.index(phrase[i]) + k) % 27
                output += Alphabet[char]
        outputs.append(output)
    return outputs

while loop == True:
    choice = int(input("_____________________________\n Menu: \n 1. Encrypt \n 2. Decrypt \n 3. Crack \n 4. Exit \n  :"))
    if choice == 1:
        shift = int(input("Places to shift message by: "))
        phrase = str(input("Enter message to be coded: "))
        print(Encrypt(shift,phrase))
    elif choice == 2:
        shift = int(input("Places message was shifted by: "))
        phrase = str(input("Enter message to be decoded: "))
        print(Encrypt(-shift,phrase))
    elif choice == 3:
        phrase = str(input("Enter message to be cracked: "))
        print(Crack(phrase))
    elif choice == 4:
        exit()
