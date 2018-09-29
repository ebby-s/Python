digit1 = ["","one","two","three","four","five","six","seven","eight","nine"]
digit2 = ["","","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
teens = ["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]

number = str(int(input("Enter number: ")))

def Num2Text(number,alphabet):
    return alphabet[int(number)]

if len(number) == 1:
    text = Num2Text(number,digit1)
elif len(number) == 2:
    text = Num2Text(number[0],digit2)
    text += " " + Num2Text(number[1],digit1)
else:
    print("Only 2 digit numbers")

if int(number[0]) == 1:
    text = Num2Text(number[1],teens)
    
print(text)
