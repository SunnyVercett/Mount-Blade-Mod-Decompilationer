#! /usr/bin/env python
#coding=utf-8

# decompile scripts.txt to module_scripts.py

from module_info import *
from decompile_operations import *


#-----------------------------------------------------------------------------#


def decompile():
    ofile = open(export_dir+"scripts.txt",'r')
    tfile = open(export_dir+"decompiled files/module_scripts.py",'w')
    idfile = open(export_dir+"decompiled files/ID_scripts.py",'w')

    tfile.write('''
from header_common import *
from header_operations import *
from module_constants import *
from module_constants import *
from header_parties import *
from header_skills import *
from header_mission_templates import *
from header_items import *
from header_triggers import *
from header_terrain_types import *
from header_music import *
from header_map_icons import *
from ID_animations import *


####################################################################################################################
# scripts is a list of script records.
# Each script record contns the following two fields:
# 1) Script id: The prefix "script_" will be inserted when referencing scripts.
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference.
####################################################################################################################

''')

    tfile.write("scripts = [\n")
    
    isOpLine = 0
    
    id = 0
    scriptName = 'void'
    for line in ofile:
        if '_' in line:
            line = line.split()
            
            tfile.write('''    ("%s",''' %line[0])
            idfile.write("%s = %d\n" %('script_%s' %line[0], id))
            id += 1
            scriptName = line[0]
            
            isOpLine = 1
            continue    # next line
        
        if isOpLine:
            tfile.write('''\n%s,\n    ),\n\n''' %decompile_statement_block(line.replace('\n','')))
            
            isOpLine = 0
            continue
        
    tfile.write("]\n")
    tfile.close()
    idfile.close()
    ofile.close()
    
    
if __name__=='__main__':
    print "Decompiling scripts ..."
    decompile()