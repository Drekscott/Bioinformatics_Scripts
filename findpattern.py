#! /usr/bin/python

"""
Author: Dreyton Scott

Problem: Finding a pattern and counting the occurence of pattern

Usage: Given a text file and pattern this program searches for pattern and keeps track of its occurence.
Returns number of times the pattern exists.
"""
import sys
import os
import Tkinter as Tk
import Tkinter
from tkFileDialog import askopenfilename
import time

def main():
    App()


class App(object):

    def __init__(self):
        self.root = Tk.Tk()
        self.root.wm_title("Genome Search")
        self.root.geometry("900x900")
        self.root["bg"] = "#00aced"
        self.label = Tk.Label(self.root, text="Please chose a file and a pattern.",font="bold",bd=3,bg="#00aced")
        self.label.pack()
        self.exitbutton = Tk.StringVar()
        self.exitbutton.set("Exit")
        Tk.Button(self.root,
            textvariable=self.exitbutton,
            command=self.exit,bd=3).pack()
        self.ui = Tk.StringVar()
        self.label = Tk.Label(self.root, text="Please chose a pattern.",font="bold",bd=3,bg="#00aced")
        self.label.pack()
        y = Tk.Entry(self.root, textvariable=self.ui,bd=5)
        y.pack()
        pattern = self.ui.get()
        self.buttontext = Tk.StringVar()
        self.buttontext.set("Click to chose a file.")
        Tk.Button(self.root,
            textvariable=self.buttontext,
            command=self.clicked1,bd=3).pack()
        self.root.mainloop()

    def exit(self):
        sys.exit()

    def clicked1(self):
        root = Tkinter.Tk()
        root.withdraw()
        filename = askopenfilename()
        pattern = self.ui.get()
        start_time = time.time()
        o = FindPatternLocation(pattern,filename)
        f = open(time.strftime("%c")+".txt","w")
        f.write("Searched for: %s\n" % pattern)
        f.write("Results: %s" % str(o))
        f.close()
        self.label = Tk.Label(self.root, text=o,font="bold",bd=3,bg="#00aced")
        self.label.pack()
        self.label = Tk.Label(self.root, text="Search Time %f" % float(time.time()-start_time),font="bold",bd=3,bg="#00aced")
        self.label.pack()


class FindPatternLocation:

    def __init__(self, pattern, file):
        self.oricpattern = pattern
        self.filetoread = file
        self.o = ""
        self.find_nucleotide_pattern_occurence()


    def find_nucleotide_pattern_occurence(self):
        self.filetoread = open(self.filetoread,"r")
        data_file = self.filetoread.read()
        self.filetoread.close()
        self.o = "Nucleotide Count: %d" % data_file.count(self.oricpattern)

    def __str__(self):
        return self.o
main()
