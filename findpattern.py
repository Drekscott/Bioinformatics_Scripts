#! /usr/bin/python

"""
Author: Dreyton Scott

Problem: Finding a pattern and counting the occurence of pattern

Usage: Given a text file and pattern this program searches for pattern and keeps track of its occurence.
Returns number of times the pattern exists.
"""
import sys
import os

class FindPatternLocation:

    def __init__(self, pattern, file):
        self.oricpattern = pattern
        self.filetoread = file
        self.find_nucleotide_pattern_occurence()

    def find_nucleotide_pattern_occurence(self):
        self.filetoread = open(self.filetoread,"r")
        data_file = self.filetoread.read()
        self.filetoread.close()
        print ("Nucleotide Count: %d") % data_file.count(self.oricpattern)

if (len(sys.argv) != 3):
    print "Usage: %s <pattern> <file>" % sys.argv[0]
else:
    FindPatternLocation(sys.argv[1],sys.argv[2])
