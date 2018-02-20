vals = []
lvl1st = False
lvl2nd = False
lvlval = 0
def lvl(val,lvlval):
    lvl1st = []
    for i in range(lenval-lvlval):
        temp = val[i+1] - val[i]
        lvl1st.append(temp)
    return lvl1st


lenval = int(input("How many values? :"))
for i in range(lenval):
    temp = int(input("Enter value:"))
    vals.append(temp)
if vals[0] - vals[lenval-1] == 0:
    print("nothing here")
else:
    lvlval = 1
    lvl1st = lvl(vals,lvlval)
    print(lvl1st)


if lvl1st != False:
    if lvl1st[0] - lvl1st[lenval-2] == 0:
        print("Level 1 Sequence")
    else:
        lvl2nd = lvl(lvl1st,2)
        print(lvl2nd)
if lvl2nd != False:
    if lvl2nd[0] - lvl2nd[lenval-3] == 0:
        print("Level 2 sequence")
    else:
        lvl3rd = lvl(lvl2nd,3)
        print(lvl3rd)
