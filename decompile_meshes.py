#! /usr/bin/env python
#coding=utf-8

# decompile meshes.txt to module_meshes.py

from module_info import *


#-----------------------------------------------------------------------------#
#-------------------------- above this are constants -------------------------#
#-----------------------------------------------------------------------------#


def get_flag_code(line):
    mesh_flag = int(line[1])
    if mesh_flag==1:
        return 'render_order_plus_1'
    elif mesh_flag==0:
        return '0'
    else:
        return line[1]


def decompile():
    ofile = open(export_dir+"meshes.txt",'r')
    tfile = open(export_dir+"decompiled files/module_meshes.py",'w')
    idfile = open(export_dir+"decompiled files/ID_meshes.py",'w')

    tfile.write('''from header_meshes import *

####################################################################################################################
#  Each mesh record contains the following fields:
#  1) Mesh id: used for referencing meshes in other files. The prefix mesh_ is automatically added before each mesh id.
#  2) Mesh flags. See header_meshes.py for a list of available flags
#  3) Mesh resource name: Resource name of the mesh
#  4) Mesh translation on x axis: Will be done automatically when the mesh is loaded
#  5) Mesh translation on y axis: Will be done automatically when the mesh is loaded
#  6) Mesh translation on z axis: Will be done automatically when the mesh is loaded
#  7) Mesh rotation angle over x axis: Will be done automatically when the mesh is loaded
#  8) Mesh rotation angle over y axis: Will be done automatically when the mesh is loaded
#  9) Mesh rotation angle over z axis: Will be done automatically when the mesh is loaded
#  10) Mesh x scale: Will be done automatically when the mesh is loaded
#  11) Mesh y scale: Will be done automatically when the mesh is loaded
#  12) Mesh z scale: Will be done automatically when the mesh is loaded
####################################################################################################################

''')
    
    tfile.write("meshes = [\n")

    id = 0
    for line in ofile:
        if 'mesh_' in line:
            line = line.split()
            
            flag_code = get_flag_code(line)   # line[1]
            
            tfile.write('''  ("%s", %s, "%s", %d, %d, %d, %d, %d, %d, %d, %d, %d),\n''' %(line[0][5:],flag_code,line[2],int(float(line[3])),int(float(line[4])),int(float(line[5])),int(float(line[6])),int(float(line[7])),int(float(line[8])),int(float(line[9])),int(float(line[10])),int(float(line[11]))))
            idfile.write("%s = %d\n" %(line[0],id))
            id += 1
            
    tfile.write("]\n")
    tfile.close()
    idfile.close()
    ofile.close()
    
    
if __name__=='__main__':
    print "Decompiling meshes ..."
    decompile()