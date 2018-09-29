import turtle
import drawing_module

scale = [43.3,25]
wn = turtle.Screen()
pen = turtle.Turtle()
pen.penup()
pen.ht()
pen.speed(100)

chains = ["0","meth","eth","prop","but","pent","hex","hept","oct"]
suffixes = ["oic acid","enitrile","one","ol","al","cyclo","ene"]
prefixes = ['methyl','ethyl','propyl','fluoro','chloro','bromo','iodo','hydroxy']
numprefixes = ["0","mono","di","tri","tetra"]
lists = [chains,suffixes,prefixes,numprefixes]

def Type(inword):
    try:
        pos = int(inword)
        return True
    except ValueError:
        return False

def Groups(inword,lists):
    found = []
    outword = inword
    for i in lists:
        for j in i:
            if j in inword:
                found.append(j)
                outword = outword.replace(j,str(found.index(j)))
                inword = inword.replace(j,"")
    return {"groups":found,"pos":outword}

def GroupPos(inword,info):
    groups = info["groups"]
    pos = info["pos"]
    endpos = pos
    grouppositions = []
    for i,j in enumerate(pos):
        if j == "-" and Type(pos[i-1]) and pos[i-1] != "0":
            grouppos = [pos[i-1],groups[int(pos[i+1])]]
            grouppositions.append(grouppos)
            endpos = endpos.replace(pos[i-1:i+2],"")
    for i in endpos:
        if Type(i):
            main = groups[int(i)]
    return {"groups":grouppositions,"main":main}

def Draw(startpos,angle,length):
    pen.setpos(startpos)
    pen.seth(angle)
    pen.pendown()
    pen.left(30)
    for i in range(length-1):
        pen.forward(50)
        if i%2 == 0:
            pen.right(120)
        pen.left(60)
    pen.penup()

while True:
    inword = input("Enter name: ")
    info = Groups(inword,lists)
    if "-" not in inword:
        final = {"groups":[['1',info["groups"][1]]],"main":info["groups"][0]}
    else:
        final = GroupPos(inword,info)
    print(final)

Draw([0,0],0,chains.index(final["main"]))
for i in final["groups"]:
    if final["groups"].index(i)%2 == 0:
        direct = 60
        side = 25
    else:
        direct = 240
        side = 0
    Draw([(int(i[0])-1)*43.3,side],direct,2)
    if i[1] == "chloro":
        drawing_module.c(20,[(int(i[0])-1)*43.3,side+60],"black",1)
        drawing_module.l(20,[(int(i[0])-1)*43.3+10,side+60],"black",1)
