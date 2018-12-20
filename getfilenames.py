import os
seenblocks=[]
seenruns=[]
def getatts():
    path="/home/anusha/Documents/hobby_projs/kartheekproj/blocks/"
    blocks=os.listdir(path)
    blocks.sort()
    for block in blocks:
        if block not in seenblocks:
            seenblocks+=[block]
            innerpath=path+block+'/'
            runs=os.listdir(innerpath)
            runs.sort()
        for run in runs:
            if run not in seenruns:
                seenruns+=[run]
                innerp=innerpath+run+'/'
                reps=os.listdir(innerp)
                reps.sort()
            for rep in reps:
                print(innerp+rep)
                os.system('wc -l '+innerp+rep+'>>statusfile')
    f=open('statusfile','r')
    con=f.readlines()
    for i in range(len(con)):
        line=con[i]
        line=line.split()
        p=line[1].split('/')
        con[i]=p[-3]+" "+p[-2]+" "+p[-1]+" "+line[0]
    con="\n".join(con)
    f=open('statusfile','w')
    f.write (con)
    print con
    f.close()
    seenruns.sort()
    print seenblocks,seenruns
