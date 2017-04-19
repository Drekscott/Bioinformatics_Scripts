#! /usr/bin/python

"""
Author: Dreyton Scott

Problem: Finding a pattern and counting the occurence of pattern

Usage: Given a text file and pattern this program searches for pattern and keeps track of its occurence.
Returns number of times the pattern exists.
"""
import sys
import os
import time

class FindPatternLocation:

    def __init__(self, pattern, file):
        self.oricpattern = pattern
        self.filetoread = file
        self.find_nucleotide_pattern_occurence()

    def find_nucleotide_pattern_occurence(self):
        count = 0
        string_count = 0
        self.filetoread = open(self.filetoread,"r")
        for line in self.filetoread:
            for word in line:
                string_count +=1
            for i in range(string_count):
                pattern_to_check = line[i:i+len(self.oricpattern)]
                if pattern_to_check == self.oricpattern:
                    count += 1
        print ("Nucleotide Count: %d") % count

if (len(sys.argv) != 3):
    print "Usage: %s <pattern> <file>" % sys.argv[0]
else:
    start_time = time.time()
    FindPatternLocation(sys.argv[1],sys.argv[2])
    print "Search time: %f" % float(time.time() - start_time)
