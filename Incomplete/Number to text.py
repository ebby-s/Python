digit1 = ["","one","two","three","four","five","six","seven","eight","nine"]
digit2 = ["","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
other = ["","thousand","million","billion","trillion","quadrillion","quintillion","sextillion","septillion","octillion","nonillion","decillion","undecillion","duodecillion","tredecillion","quattuordecillion","quindecillion","sexdecillion","septendecillion","octodecillion","novemdecillion","vigintillion","centillion"]
teens = ["","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
text = ""

number = int(input("Enter number: "))

def Num2Text(num):
    out = ""
    if len(num) == 3:
        out += digit1[int(num[0])] + " hundred "
    if len(num) >= 2 and num[-2] == "1":
        out += teens[int(num[-1])] + " "
    elif len(num) >= 2 and num[-2] != "0":
        print(int(num[-2])-1)
        out += digit2[int(num[-2])-1] + " "
    if len(num) >= 1 and num[-2] != "1":
        out += digit1[int(num[-1])] + " "
    return out

cycles = round(len(str(number))/3+0.49)

for i in range(cycles,0,-1):
    cnumber = str(number%1000**i-number%1000**(i-1))
    cnumber = cnumber[:3]
    text += Num2Text(cnumber) + other[i-1]  + " "
    
print(text)
