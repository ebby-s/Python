import turtle

alkanes = ["methan","ethan","propan","butan","pentan","hexan","heptan","octan"]
alkenes = []
prefixes = ["fluoro","chloro","bromo","iodo","hydroxy"]
numprefixes = ["mono","di","tri","terta","penta","hexa","hepta","octa"]
suffixes = ["oic acid","enitrile","one","ol","al","cycloe"]
for i in alkanes:
    temp = i[0:-2]
    ene = temp + "en"
    pre = temp + "yl"
    alkenes.append(ene)
    prefixes.insert(0,pre)

def Type(char):
    try:
        temp = int(char)
        out = "int"
    except ValueError:
        out = "str"
    return out

def Find(phrase,array):
    out = []
    for i in array:
        if i in phrase:
            out.append(i)
    return out

def Remove(phrase,chars,num=False):
    out = ""
    for j in phrase:
        if j in chars:
            phrase = phrase.replace(j,'')
    if num:
        for i in phrase:
            if Type(i) == "int":
                phrase = phrase.replace(i,'')
    return phrase

def ReadInput(inword):
    pos = []
    groups = [Remove(inword,",- ",True)]
    for i in range(len(inword)):
        temp = Type(inword[i])
        if temp == "int":
            pos.append(inword[i])
        elif inword[i] in [" ",","]:
            line = Remove(inword[0:i],",- ",True)
            groups.insert(-1,line)
    for i in range(len(groups)-1,0,-1):
        groups[i] = groups[i][len(groups[i-1]):]
    return {"positions":pos,"groups":groups}

def GroupCount(info):
    positions = info["positions"]
    groups = info["groups"]
    med = []
    gcount = []
    for i in groups:
        scount = 0
        for j in numprefixes:
            if j in i:
                med.append(numprefixes.index(j)+1)
            else:
                scount += 1
        if scount == 8 and i != '':
            med.append(1)
    csum = 0
    for i in range(len(med)):
        if len(positions) < csum+med[i]:
            break
        else:
            csum += med[i]
            gcount.append(med[i])
    return gcount

def Compound(info):
    positions = info["positions"]
    groups = info["groups"]
    main = groups[-1]
    for i in range(len(alkanes)):
        if alkanes[i] in main:
            group = alkanes[i]
            gnum = i
        elif alkenes[i] in main:
            group = alkenes[i]
            gnum = 1
    main = main.replace(group,'')
    fgroup = suffixes[suffixes.index(main)]
    return {"text":[group,fgroup],"number":gnum}

def Draw(size,angle,num,draw=True):
    if draw:
        pen.pendown()
    for i in range(num):
        pen.forward(size)
        if i%2 == 0:
            pen.left(angle)
        else:
            pen.right(angle)
    pen.penup()



inword = "2,3-dibromo cyclopentane"

info = ReadInput(inword)
groupcount = GroupCount(info)
compound = Compound(info)
print(info,groupcount,compound)



pen = turtle.Turtle()
pen.penup()
pen.right(30)
Draw(50,60,compound["number"])
pen.left(60)
Draw(-50,-60,compound["number"],False)
pen.right(30)
