from Tkinter import *
import os


def getatts(seenblocks,seenruns):
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
    return seenblocks,seenruns

def creategui(seenblocks,seenruns):
    root=Tk()
    d=800
    root.geometry('{}x{}'.format(d,d))
    rows=len(seenruns)
    cols=len(seenblocks)
    k=0

    for i in range(rows):
        for j in range(cols):
            if(i==0 and j==0):
                frame1=Frame(root, width=d/cols, height=d/rows, background="Blue")
                frame1.grid(row=i, column=j)
                b = Label(frame1, bg="pink",text = "block/run")
                b.grid(row=0, column=0)
            elif(j==0):
                frame1=Frame(root, width=d/cols, height=d/rows, background="Blue")
                frame1.grid(row=i, column=j)
                b = Label(frame1, text = "block"+str(i))
                b.grid(row=i, column=j)
            elif(i==0):
                frame1=Frame(root, width=d/cols, height=d/rows, background="Blue")
                frame1.grid(row=i, column=j)
                b = Label(frame1, text = "run"+str(j))
                b.grid(row=i, column=j)
            else:
                frame1=Frame(root, width=d/cols, height=d/rows, background="Blue")
                frame1.grid(row=i, column=j)
                k=0
                for k in range(3):
                    b1l = Label(frame1, text = "run"+str(i)+str(j))
                    b1=Label(frame1,text="1")
                    b1l.grid(row=k, column=0)
                    b1.grid(row=k,column=1)



    root.mainloop()
if __name__=="__main__":
    f=open("statusfile","w").close()
    seenblocks=[]
    seenruns=[]
    seenblocks,seenruns=getatts(seenblocks,seenruns)
    creategui(seenblocks,seenruns)
