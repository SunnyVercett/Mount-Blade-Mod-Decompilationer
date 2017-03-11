#! /usr/bin/env python
#coding=utf-8

# decompile quests.txt to module_quests.py

from module_info import *


quest_flags_old = {
   'qf_show_progression     ': 0x00000001,
   'qf_random_quest         ': 0x00000002,
}
quest_flags = {}
for k,v in quest_flags_old.iteritems():
    quest_flags[v] = k.replace(' ','')
    

#-----------------------------------------------------------------------------#


def get_flag_code(line):
    flag_code = ''''''
    quest_flag = int(line[2])
    if quest_flag==0:
        return '0'
    
    quest_flag_keys = quest_flags.keys()
    quest_flag_keys.sort()
    quest_flag_keys.reverse()
    for each_flag in quest_flag_keys:
        if quest_flag&each_flag==each_flag:
            flag_code += "|%s" %quest_flags[each_flag]
            quest_flag -= each_flag
        if quest_flag==0:
            return flag_code.replace('|','',1)
    else:
        return line[2]


def decompile():
    ofile = open(export_dir+"quests.txt",'r')
    tfile = open(export_dir+"decompiled files/module_quests.py",'w')
    idfile = open(export_dir+"decompiled files/ID_quests.py",'w')

    tfile.write('''from header_quests import *

####################################################################################################################
#  Each quest record contains the following fields:
#  1) Quest id: used for referencing quests in other files. The prefix qst_ is automatically added before each quest-id.
#  2) Quest Name: Name displayed in the quest screen.
#  3) Quest flags. See header_quests.py for a list of available flags
#  4) Quest Description: Description displayed in the quest screen.
#
# Note that you may call the opcode setup_quest_text for setting up the name and description
####################################################################################################################

''')
    
    tfile.write("quests = [\n")
    
    id = 0
    for line in ofile:
        if 'qst_' in line:
            line = line.split()
            
            flag_code = get_flag_code(line)   # line[2]
            
            tfile.write('''  ("%s","%s",%s,\n    "%s"\n  ),\n''' %(line[0][4:],line[1].replace('_',' '),flag_code,line[3].replace('_',' ')))
            idfile.write("%s = %d\n" %(line[0],id))
            id += 1
            
    tfile.write("]\n")
    tfile.close()
    idfile.close()
    ofile.close()
    
    
if __name__=='__main__':
    print "Decompiling quests ..."
    decompile()