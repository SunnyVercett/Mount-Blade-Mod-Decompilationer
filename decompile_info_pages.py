#! /usr/bin/env python
#coding=utf-8

# decompile info_pages.txt to module_info_pages.py

from module_info import *

#-----------------------------------------------------------------------------#
#---------------------- above this are (no) constants -------------------------$
#-----------------------------------------------------------------------------#


def decompile():
    ofile = open(export_dir+"info_pages.txt",'r')
    tfile = open(export_dir+"decompiled files/module_info_pages.py",'w')
    idfile = open(export_dir+"decompiled files/ID_info_pages.py",'w')
    
    tfile.write('''####################################################################################################################
#  Each quest record contains the following fields:
#  1) Info page id: used for referencing info pages in other files. The prefix ip_ is automatically added before each info page id.
#  2) Info page name: Name displayed in the info page screen.
#
####################################################################################################################

''')

    tfile.write("info_pages = [\n")
    
    id = 0
    for line in ofile:
        if 'ip_' in line:
            line = line.split()
            
            tfile.write('''  ("%s","%s",\n    "%s"),\n''' %(line[0][3:],line[1].replace('_',' '),line[2].replace('_',' ')))
            idfile.write("%s = %d\n" %(line[0],id))
            id += 1
            
    tfile.write("]\n")
    tfile.close()
    idfile.close()
    ofile.close()

    
    
if __name__=='__main__':
    print "Decompiling info pages ..."
    decompile()