from Tkinter import *
import Tkinter
import tkFileDialog
import os

rd={}
h={}



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
    f.close()
    seenruns.sort()
    return seenblocks,seenruns




def opf(k):
    os.system('xdg-open '+h[k])





def creategui(seenblocks,seenruns):
    root=Tk()
    d=800
    ci=-1
    cj=1
    root.geometry('{}x{}'.format(d,d))
    rows=len(seenruns)
    cols=len(seenblocks)
    flag=0
    frame1=Frame(root, width=d/cols, height=d/rows)
    frame1.grid(row=0, column=0,padx=3,pady=3)
    b = Label(frame1, bg="pink",text = "block/run")
    b.grid(row=0, column=0)
    for coln in range(len(seenruns)):
        frame1=Frame(root, highlightbackground="red", highlightcolor="red", highlightthickness=1, width=d/cols, height=d/rows)
        frame1.grid(row=0, column=coln+1)
        b = Label(frame1,text = seenruns[coln])
        b.grid(row=0, column=coln+1)
    for rown in range(len(seenblocks)):
        frame1=Frame(root, highlightbackground="red", highlightcolor="red", highlightthickness=1, width=d/cols, height=d/rows)
        frame1.grid(row=rown+1, column=0)
        b = Label(frame1, text = seenblocks[rown])
        b.grid(row=rown+1, column=0)
    f1=open("statusfile","r")
    frame1=Frame(root, highlightbackground="green", highlightcolor="green", highlightthickness=1, width=d/cols, height=d/rows)
    frame1.grid(row=1, column=1,padx=5,pady=5)
    for line in f1:
        tmp=line.split()
        block_name=tmp[0]
        run_name=tmp[1]
        report=tmp[2]
        stat=tmp[3]
        rownum=seenblocks.index(block_name)+1
        colnum=seenruns.index(run_name)+1
        if(flag==0):
            prev_b=rownum
            prev_r=colnum
            flag=1
        pres_b=rownum
        pres_r=colnum
        if(prev_b==pres_b and prev_r==pres_r):
            ci+=1
        else:
            ci=0
            frame1=Frame(root, highlightbackground="green", highlightcolor="green", highlightthickness=1, width=d/cols, height=d/rows)
            frame1.grid(row=pres_b, column=pres_r,padx=5,pady=5)
        b1l = Label(frame1, text =report+":")
        b1=Label(frame1,text=stat)
        b1l.grid(row=ci, column=0)
        b1.grid(row=ci,column=1)
        prev_b=pres_b
        prev_r=pres_r
    frame1=Frame(root, width=d/cols, height=d/rows)
    frame1.grid(row=0, column=len(seenruns)+1,padx=3,pady=3)
    b = Label(frame1, bg="pink",text = "run directories")
    b.grid(row=0, column=0)
    f1=open('origpaths','r')
    for p in f1:
        for k in range(len(seenblocks)):
            if seenblocks[k] in p:
                frame1=Frame(root, width=d/cols, height=d/rows)
                frame1.grid(row=k+1, column=len(seenruns)+1,padx=3,pady=3)
                rd[k]=Button(frame1,text=seenblocks[k])#,command=lambda: opf(self))
                h[rd[k]]=p
                rd[k].configure(command=lambda button=rd[k]: opf(button))
                rd[k].grid(row=0,column=0)
                break

    root.mainloop()





if __name__=="__main__":
    f=open("statusfile","w").close()
    seenblocks=[]
    seenruns=[]
    seenblocks,seenruns=getatts(seenblocks,seenruns)
    creategui(seenblocks,seenruns)
