#! /usr/bin/env python
#coding=utf-8

# decompile factions.txt to module_factions.py

from module_info import *


ff_always_hide_label = 0x00000001

fac_flags_old = {
   'ff_always_hide_label': 0x00000001,
   'ff_max_rating_bits': 8,
   'ff_max_rating_mask': 0x0000ff00,
}
fac_flags = {}
for k,v in fac_flags_old.iteritems():
    fac_flags[v] = k.replace(' ','')


#-----------------------------------------------------------------------------#
#------------------------- above this are constants --------------------------#
#-----------------------------------------------------------------------------#


def get_flag_code(line):
    flag_code = ''''''
    fac_flag = int(line[2])
    if fac_flag==0:
        return '0'
    
    if ff_always_hide_label&fac_flag==ff_always_hide_label:
        flag_code += "|%s" %'ff_always_hide_label'
        fac_flag -= ff_always_hide_label
    if fac_flag==0:
        return flag_code.replace('|','',1)
    
    max_player_flag = 100-(fac_flag >> 8)
    flag_code += "|max_player_rating(%d)" %max_player_flag
    
    return flag_code.replace('|','',1)


def decompile():
    ofile = open(export_dir+"factions.txt",'r')
    idfile = open(export_dir+"decompiled files/ID_factions.py",'w')

    id = 0
    fac_ids = {}
    for line in ofile:
        if 'fac_' in line:
            line = line.split()
            if line[0]=='0':
                line = line[1:]
            
            fac_name = line[0]
            fac_ids[id] = fac_name[4:]
            idfile.write("%s = %d\n" %(fac_name,id))
            id += 1
        
    idfile.close()
    ofile.close()
    
    ofile = open(export_dir+"factions.txt",'r')
    tfile = open(export_dir+"decompiled files/module_factions.py",'w')
    tfile.write('''from header_factions import *

####################################################################################################################
#  Each faction record contains the following fields:
#  1) Faction id: used for referencing factions in other files.
#     The prefix fac_ is automatically added before each faction id.
#  2) Faction name.
#  3) Faction flags. See header_factions.py for a list of available flags
#  4) Faction coherence. Relation between members of this faction.
#  5) Relations. This is a list of relation records.
#     Each relation record is a tuple that contains the following fields:
#    5.1) Faction. Which other faction this relation is referring to
#    5.2) Value: Relation value between the two factions.
#         Values range between -1 and 1.
#  6) Ranks
#  7) Faction color (default is gray)
####################################################################################################################

default_kingdom_relations = [("outlaws",-0.05),("peasant_rebels", -0.1),("deserters", -0.05),("mountain_bandits", -0.02),("forest_bandits", -0.02)]

''')

    tfile.write("factions = [\n")
    
    isRelationLine = 0
    id = 0
    for line in ofile:
        if 'fac_' in line:
            line = line.split()
            if line[0]=='0':
                line = line[1:]
            
            fac_name = line[0][4:]
            flag_code = get_flag_code(line)   # line[2]
            color_code = hex(int(line[3])).replace('L','')
            
            tfile.write('''  ("%s", "%s", %s,''' %(fac_name,line[1].replace('_',' '),flag_code))
            isRelationLine = 1
            continue
        
        if isRelationLine:
            line = line.split()
            relations = [float(line[i]) for i in xrange(len(line))]
            tfile.write(" %5.2f, [" %relations[id])
            for i in xrange(len(relations)):
                if relations[i] and fac_name!=fac_ids[i]:
                    tfile.write('''("%s", %5.2f),''' %(fac_ids[i],relations[i]))
            tfile.write("], [], %s),\n" %color_code)
            
            isRelationLine = 0
            id += 1
            
    tfile.write("]\n")
    tfile.close()
    
    
if __name__=='__main__':
    print "Decompiling factions ..."
    decompile()