#! /usr/bin/env python
#coding=utf-8

# decompile tableau_materials.txt to module_tableau_materials.py

from module_info import *
from decompile_operations import *


#-----------------------------------------------------------------------------#
#-------------------------- above this are constants -------------------------#
#-----------------------------------------------------------------------------#


def get_flag_code(line):
    tabl_flag = int(line[1])
    if tabl_flag==0:
        return '0'
    else:
        return line[1]


def decompile():
    ofile = open(export_dir+"tableau_materials.txt",'r')
    tfile = open(export_dir+"decompiled files/module_tableau_materials.py",'w')
    idfile = open(export_dir+"decompiled files/ID_tableau_materials.py",'w')
    
    tfile.write('''from header_common import *
from ID_animations import *
from header_mission_templates import *
from header_tableau_materials import *
from header_items import *
from module_constants import *

####################################################################################################################
#  Each tableau material contains the following fields:
#  1) Tableau id (string): used for referencing tableaux in other files. The prefix tab_ is automatically added before each tableau-id.
#  2) Tableau flags (int). See header_tableau_materials.py for a list of available flags
#  3) Tableau sample material name (string).
#  4) Tableau width (int).
#  5) Tableau height (int).
#  6) Tableau mesh min x (int): divided by 1000 and used when a mesh is auto-generated using the tableau material
#  7) Tableau mesh min y (int): divided by 1000 and used when a mesh is auto-generated using the tableau material
#  8) Tableau mesh max x (int): divided by 1000 and used when a mesh is auto-generated using the tableau material
#  9) Tableau mesh max y (int): divided by 1000 and used when a mesh is auto-generated using the tableau material
#  10) Operations block (list): A list of operations. See header_operations.py for reference.
#     The operations block is executed when the tableau is activated.
# 
####################################################################################################################

#banner height = 200, width = 85 with wood, 75 without wood

''')

    tfile.write("tableaus = [\n")
    
    id = 0
    for line in ofile:
        if 'tab_' in line:
            line = line.split()
            
            flag_code = get_flag_code(line)   # line[1]
            
            tfile.write('''    ("%s",%s,"%s",%s,%s,%s,%s,%s,%s,''' %(line[0][4:],flag_code,line[2],line[3],line[4],line[5],line[6],line[7],line[8]))
            idfile.write("%s = %d\n" %(line[0],id))
            id += 1
            
            op_code = decompile_statement_block(' '.join(line[9:]))
            tfile.write("\n%s,\n    ),\n" %op_code)
            
    tfile.write("]\n")
    tfile.close()
    idfile.close()
    ofile.close()
    
    
if __name__=='__main__':
    print "Decompiling tableau materials ..."
    decompile()