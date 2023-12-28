j1 = open("j1.txt", "r").read().splitlines()
res = 0
for elem in j1:
    c1 = 0
    c1t = False
    cf = 0
    cft = False
    for c in elem:
        if c.isdigit() :
            if (not c1t) :
                c1 = int(c)
                c1t = True
            else:
                cf = int(c)
                cft = True
    if cft == False:
        cf = c1
    res += c1*10+cf
print(res)    

