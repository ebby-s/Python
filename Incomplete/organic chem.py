alkanes = ["0","methan","ethan","propan","butan","pentan","hexan","heptan","octan"]
alkenes = ["0",'methen','ethen','propen','buten','penten','hexen','hepten','octen']
prefixes = ['methyl','ethyl','propyl','fluoro','chloro','bromo','iodo','hydroxy']
numprefixes = ["0","mono","di","tri","tetra"]
suffixes = ["oic acid","enitrile","one","ol","al","cyclo",]
lists = [alkanes,alkenes,prefixes,numprefixes,suffixes]

def Check(inword,lists):
    found = []
    for i in lists:
        for j in i:
            if j in inword:
                found.append(j)
                inword = inword.replace(j,"")
    return(found)



print(Check("2-bromo,3-chloro pentane",lists))



def Remove(phrase,chars):
    out = ""
    for j in phrase:
        if j in chars:
            phrase = phrase.replace(j,'')
    return phrase

def ReadInput(inword):
    pos = []
    groups = []
    for i,j in enumerate(inword):
        try:
            posint = int(j)
            inword = Remove(inword,j)
            pos.append(posint)
        except ValueError:
            "do nothing"
        if j in [" ",","]:
            line = Remove(inword[0:i-1],",- ")
            groups.insert(-1,line)
    
    main = Remove(inword,",- ")
    for i in groups:
        main = main.replace(i,"")
    return {"positions":pos,"groups":groups,"main":main}

def GroupCount(info):
    positions = info["positions"]
    groups = info["groups"]
    med = []
    gcount = []
    for i in groups:
        scount = 0
        for j in numprefixes:
            if j in i:
                med.append(numprefixes.index(j))
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
