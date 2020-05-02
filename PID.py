import string
import re

from collections import Counter
import collections
import sys 

def first():
    infile = open("PID count check.txt", "r+")
    outfile = open('output.txt', "w+")
    for line in infile:
        words = line.split()
        x = words[1]
        print(x)
        outfile.write(x)
        outfile.write("\n")
    print ("\n","*********End of PID List***************")    
    outfile.close()

def second():
    lines_seen = set()  # holds lines already seen
    outfile = open('output.txt', "r+").readlines()
    ffile = open('result.txt', "w+")

    for line in outfile:
        #print (line)
        if line not in lines_seen:  # not a duplicate
            ffile.write(line)
            lines_seen.add(line)
    ffile.close()
    for line in open('result.txt', "r"):
        #print (line)
        print("\n", line)
    print ("\n","********End of Unique Count***************")
def third():
    import collections
    outfile = open ("output.txt", "r").readlines()
    ffile = open('result.txt', "w+")
    with open('output.txt') as infile:
        counts = collections.Counter(l.strip() for l in infile)
        for line, count in counts.most_common():
            print ("\n", line, " - ", count,"times appeared")
        print ("\n", "*****End status for Counts of Unique Value********")    
    ffile.close()
stdoutOrigin=sys.stdout 
sys.stdout = open("log.txt", "w")
first()
second()
third()
    
