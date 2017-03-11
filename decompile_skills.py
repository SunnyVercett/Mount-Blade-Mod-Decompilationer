#! /usr/bin/env python
#coding=utf-8

# decompile skills.txt to module_skills.py

from module_info import *

skill_flags_old = {
   #'sf_base_att_str ': 0x000,
   'sf_base_att_agi ': 0x001,
   'sf_base_att_int ': 0x002,
   'sf_base_att_cha ': 0x003,
   'sf_effects_party': 0x010,
   'sf_inactive     ': 0x100,
}
skill_flags = {}
for k,v in skill_flags_old.iteritems():
    skill_flags[v] = k.replace(' ','')


#-----------------------------------------------------------------------------#
#-------------------------- above this are constants -------------------------#
#-----------------------------------------------------------------------------#


def get_flag_code(line):
    flag_code = ''''''
    skill_flag = int(line[2])
    
    if skill_flag==0:
        return "sf_base_att_str"
    if skill_flag==0x100:
        return "sf_base_att_str|sf_inactive"
    
    skill_flag_keys = skill_flags.keys()
    skill_flag_keys.sort()
    skill_flag_keys.reverse()
    for each_flag in skill_flag_keys:
        if skill_flag&each_flag==each_flag:
            flag_code += "|%s" %skill_flags[each_flag]
            skill_flag -= each_flag
        if skill_flag==0:
            return flag_code.replace('|','',1)
    else:
        return line[2]
    

def decompile():
    ofile = open(export_dir+"skills.txt",'r')
    tfile = open(export_dir+"decompiled files/module_skills.py",'w')
    idfile = open(export_dir+"decompiled files/ID_skills.py",'w')

    tfile.write('''from header_common import *
from header_skills import *

####################################################################################################################
#  Each skill contains the following fields:
#  1) Skill id (string): used for referencing skills in other files. The prefix skl_ is automatically added before each skill-id .
#  2) Skill name (string).
#  3) Skill flags (int). See header_skills.py for a list of available flags
#  4) Maximum level of the skill (int).
#  5) Skill description (string): used in character window for explaining the skills.
# 
####################################################################################################################

#Hardcoded skills are {names (indexes, beginning with 0)}:
# Trade (1)
# Leadership (2)
# Prisoner Management (3)
# First Aid (9)
# Surgery (10)
# Wound Treatment (11)
# Inventory Management (12)
# Spotting (13)
# Pathfinding (14)
# Tactics (15)
# Tracking (16)
# Trainer (17)
# Engineer (18)
# Horse Archery (24)
# Riding (25)
# Athletics (26)
# Shield (27)
# Weapon Master (28)
# Power Draw (34)
# Power Throw (35)
# Power Strike (36)
# Ironflesh (37)
#
# The effects of these skills can only be removed if the skill is disabled with sf_inactive flag.
# If you want to add a new skill, use the reserved skills or use non-hardcoded skills.
''')

    tfile.write("skills = [\n")
    
    id = 0
    for line in ofile:
        if 'skl_' in line:
            line = line.split()
            flag_code = get_flag_code(line)
            
            tfile.write('''  ("%s","%s", %s, %d, "%s"),\n''' %(line[0][4:],line[1].replace('_',' '),flag_code,int(line[3]),line[4].replace('_',' ')))
            
            idfile.write("%s = %d\n" %(line[0],id))
            
            id += 1
    
    tfile.write("]\n")
    tfile.close()
    ofile.close()
    idfile.close()
    
    
if __name__=='__main__':
    print "Decompiling skills ..."
    decompile()