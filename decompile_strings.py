#! /usr/bin/env python
#coding=utf-8

# decompile strings.txt to module_strings.py

from module_info import *


#-----------------------------------------------------------------------------#
#-------------------------- above this are constants -------------------------#
#-----------------------------------------------------------------------------#


def decompile():
    ofile = open(export_dir+"strings.txt",'r')
    tfile = open(export_dir+"decompiled files/module_strings.py",'w')
    idfile = open(export_dir+"decompiled files/ID_strings.py",'w')
    
    tfile.write("strings = [\n")
    
    id = 0
    for line in ofile:
        if 'str_' in line:
            line = line.split()
            
            str = line[1].replace('_',' ')
            str2 = ''
            for c in xrange(len(str)):    # parse the string character by character
                try:
                    character = str[c].decode('utf-8')    # firstly decode this character
                except UnicodeDecodeError:
                    character = str[c].decode('ISO-8859-1')
                try:
                    str2 += character.encode('ascii')    # secondly encode this character in ascii
                except UnicodeEncodeError:
                    continue    # pass this character    # if this character cannot be encoded with ascii then pass this character
            tfile.write('''  ("%s", "%s"),\n''' %(line[0][4:],str2))
            idfile.write("%s = %d\n" %(line[0],id))
            id += 1
            
    tfile.write("]\n")
    tfile.close()
    idfile.close()
    ofile.close()
    
    
if __name__=='__main__':
    print "Decompiling strings ..."
    decompile()