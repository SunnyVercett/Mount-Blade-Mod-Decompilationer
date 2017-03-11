#! /usr/bin/env python
#coding=utf-8

# decompile scenes.txt to module_scenes.py

from module_info import *
from decompiled_ID_troops import *


scene_flags_old = {
   'sf_indoors          ': 0x00000001,   #The scene shouldn't have a skybox and lighting by sun.
   'sf_force_skybox     ': 0x00000002,   #Force adding a skybox even if indoors flag is set.
   'sf_generate         ': 0x00000100,   #Generate terrain by terran-generator
   'sf_randomize        ': 0x00000200,   #Randomize terrain generator key
   'sf_auto_entry_points': 0x00000400,   #Automatically create entry points
   'sf_no_horses        ': 0x00000800,   #Horses are not avaible
   'sf_muddy_water      ': 0x00001000,   #Changes the shader of the river mesh
}
scene_flags = {}
for k,v in scene_flags_old.iteritems():
    scene_flags[v] = k.replace(' ','')


#-----------------------------------------------------------------------------#
#--------------------------- above this are constants-------------------------#
#-----------------------------------------------------------------------------#


#def find_troop(troop_id):   # int
#    troop_file = open(export_dir+"troops.txt",'r')
#    id = 0
#    for line in troop_file:
#        if 'trp_' in line:
#            troop_name = line.split()[0][4:]
#            if id==troop_id:
#                return troop_name
#            else:
#                id +=1


def get_flag_code(line):
    flag_code = ''''''
    scene_flag = int(line[2])
    if scene_flag==0:
        return '0'
    
    for each_flag in scene_flags:
        if scene_flag&each_flag==each_flag:
            flag_code += "|%s" %scene_flags[each_flag]
            scene_flag -= each_flag
        if scene_flag==0:
            return flag_code.replace('|','',1)
    else:
        return line[2]



def decompile():
    ofile = open(export_dir+"scenes.txt",'r')
    idfile = open(export_dir+"/decompiled files/ID_scenes.py",'w')

    scene_ids = {}
    id = 0
    for line in ofile:
        if 'scn_' in line:
            line = line.split()
            scene_ids[id] = line[0][4:]
            idfile.write("%s = %d\n" %(line[0],id))
            
            id += 1
            
    idfile.close()
    ofile.close()
    
    ofile = open(export_dir+"scenes.txt",'r')
    tfile = open(export_dir+"/decompiled files/module_scenes.py",'w')
    tfile.write('''from header_common import *
from header_operations import *
from header_triggers import *
from header_scenes import *
from module_constants import *

####################################################################################################################
#  Each scene record contains the following fields:
#  1) Scene id {string}: used for referencing scenes in other files. The prefix scn_ is automatically added before each scene-id.
#  2) Scene flags {int}. See header_scenes.py for a list of available flags
#  3) Mesh name {string}: This is used for indoor scenes only. Use the keyword "none" for outdoor scenes.
#  4) Body name {string}: This is used for indoor scenes only. Use the keyword "none" for outdoor scenes.
#  5) Min-pos {(float,float)}: minimum (x,y) coordinate. Player can't move beyond this limit.
#  6) Max-pos {(float,float)}: maximum (x,y) coordinate. Player can't move beyond this limit.
#  7) Water-level {float}. 
#  8) Terrain code {string}: You can obtain the terrain code by copying it from the terrain generator screen
#  9) List of other scenes accessible from this scene {list of strings}.
#     (deprecated. This will probably be removed in future versions of the module system)
#     (In the new system passages are used to travel between scenes and
#     the passage's variation-no is used to select the game menu item that the passage leads to.)
# 10) List of chest-troops used in this scene {list of strings}. You can access chests by placing them in edit mode.
#     The chest's variation-no is used with this list for selecting which troop's inventory it will access.
#  town_1   Sargoth     #plain
#  town_2   Tihr        #steppe
#  town_3   Veluca      #steppe
#  town_4   Suno        #plain
#  town_5   Jelkala     #plain
#  town_6   Praven      #plain
#  town_7   Uxkhal      #plain
#  town_8   Reyvadin    #plain
#  town_9   Khudan      #snow
#  town_10  Tulga       #steppe
#  town_11  Curaw       #snow
#  town_12  Wercheg     #plain
#  town_13  Rivacheg    #plain
#  town_14  Halmar      #steppe
#  town_15  Yalen
#  town_16  Dhirim
#  town_17  Ichamur
#  town_18  Narra
#  town_19  Shariz
#  town_20  Durquba
#  town_21  Ahmerrad
#  town_22  Bariyye
####################################################################################################################

''')
    
    tfile.write("scenes = [\n")
    
    isPassLine = 0
    isChestLine = 0
    isOuterLine = 0
    for line in ofile:
        if 'scn_' in line:
            line = line.split()
            
            flag_code = get_flag_code(line)   # line[2]
            
            tfile.write('''("%s",%s,"%s","%s", %s, %s, %f,"%s",\n''' %(line[1],flag_code,line[3],line[4],str((int(float(line[5])),int(float(line[6])))),str((int(float(line[7])),int(float(line[8])))),float(line[9]),line[10]))
            
            isPassLine = 1
            continue
        
        if isPassLine:
            tfile.write("  [")
            line = line.split()
            for i in xrange(int(line[0])):
                if line[i+1]=='0':
                    tfile.write('''"",''')
                elif line[i+1]=='100000':
                    tfile.write('''"exit",''')
                else:
                    tfile.write('''"%s",''' %scene_ids[int(line[i+1])])
            tfile.write("], ")
            
            isPassLine = 0
            isChestLine = 1
            continue
        
        if isChestLine:
            tfile.write("[")
            line = line.split()
            for i in xrange(int(line[0])):
                tfile.write('''"%s",''' %troop_ids[int(line[i+1])][4:])
            tfile.write("], ")
            
            isChestLine = 0
            isOuterLine = 1
            continue
        
        if isOuterLine:
            line = line.split()
            if line[0]=='0':
                tfile.write("),\n")
            else:
                tfile.write('''"%s"),\n''' %line[0])
                
            isOuterLine = 0
            continue
    
    tfile.write("]\n")
    tfile.close()
    ofile.close()

    
    
if __name__=='__main__':
    print "Decompiling scenes ..."
    decompile()