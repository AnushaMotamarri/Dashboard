from tkinter import *
from tkinter import filedialog
import tkFileDialog as filedialog
from tkFileDialog import askopenfilename
import os
import Tkinter
import tkFileDialog
import os

root = Tkinter.Tk()
root.withdraw() #use to hide tkinter window

currdir = os.getcwd()
pa='/home/anusha/Documents/hobby_projs/kartheekproj/blocks/blockD/scan'
tempdir = tkFileDialog.askdirectory(parent=root, initialdir=pa, title='Please select a directory')
if len(tempdir) > 0:
    print "You chose %s" % tempdir
    os.system('xdg-open '+tempdir)
