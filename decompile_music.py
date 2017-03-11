#! /usr/bin/env python
#coding=utf-8

# decompile music.txt to module_music.py
# The id slot of each track is not presented in music.txt, so some of the ids in ID_music.py is invalid.
# As a result, the decompiled module_music.py file cannot be fully used in module editing.
# Always use the original txt string in other decompiling process related to music.
# So this file is nearly useless. Too bad I wrote this after finished coding this file.


from module_info import *
from header_music import *


track_flags_old = {
   'mtf_culture_1                         ': 0x00000001,
   'mtf_culture_2                         ': 0x00000002,
   'mtf_culture_3                         ': 0x00000004,
   'mtf_culture_4                         ': 0x00000008,
   'mtf_culture_5                         ': 0x00000010,
   'mtf_culture_6                         ': 0x00000020,
   'mtf_culture_all                       ': 0x0000003F,
   'mtf_looping                           ': 0x00000040,
   'mtf_start_immediately                 ': 0x00000080,
   'mtf_persist_until_finished            ': 0x00000100,
   'mtf_sit_tavern                        ': 0x00000200,
   'mtf_sit_fight                         ': 0x00000400,
   'mtf_sit_multiplayer_fight             ': 0x00000800,
   'mtf_sit_ambushed                      ': 0x00001000,
   'mtf_sit_town                          ': 0x00002000,
   'mtf_sit_town_infiltrate               ': 0x00004000,
   'mtf_sit_killed                        ': 0x00008000,
   'mtf_sit_travel                        ': 0x00010000,
   'mtf_sit_arena                         ': 0x00020000,
   'mtf_sit_siege                         ': 0x00040000,
   'mtf_sit_night                         ': 0x00080000,
   'mtf_sit_day                           ': 0x00100000,
   'mtf_sit_encounter_hostile             ': 0x00200000,
   'mtf_sit_main_title                    ': 0x00400000,
   'mtf_sit_victorious                    ': 0x00800000,
   'mtf_sit_feast                         ': 0x01000000,
   'mtf_module_track                      ': 0x10000000, ##set this flag for tracks placed under module folder
}
track_flags = {}
for k,v in track_flags_old.iteritems():
    track_flags[v] = k.replace(' ','')
    

#-----------------------------------------------------------------------------#
#--------------------------- above this are constants ------------------------#
#-----------------------------------------------------------------------------#


def get_flag_code(line):
    flag_code = ''''''
    track_flag = int(line[1])
    if track_flag==0:
        return '0'
    
    track_flag_keys = track_flags.keys()
    track_flag_keys.sort()
    track_flag_keys.reverse()
    for each_flag in track_flag_keys:
        if track_flag&each_flag==each_flag:
            flag_code += "|%s" %track_flags[each_flag]
            track_flag -= each_flag
        if track_flag==0:
            return flag_code.replace('|','',1)
    else:
        return line[1]
    
    
def get_cflag_code(line):
    flag_code = ''''''
    track_flag = int(line[2])
    if track_flag==0:
        return '0'
    
    track_flag_keys = track_flags.keys()
    track_flag_keys.sort()
    track_flag_keys.reverse()
    for each_flag in track_flag_keys:
        if track_flag&each_flag==each_flag:
            flag_code += "|%s" %track_flags[each_flag]
            track_flag -= each_flag
        if track_flag==0:
            return flag_code.replace('|','',1)
    else:
        return line[2]    


def decompile():
    ofile = open(export_dir+"music.txt",'r')
    tfile = open(export_dir+"decompiled files/module_music.py",'w')
    idfile = open(export_dir+"decompiled files/ID_music.py",'w')
    
    tfile.write('''from header_music import *
    
####################################################################################################################
#  Each track record contains the following fields:
#  1) Track id: used for referencing tracks.
#  2) Track file: filename of the track
#  3) Track flags. See header_music.py for a list of available flags
#  4) Continue Track flags: Shows in which situations or cultures the track can continue playing. See header_music.py for a list of available flags
####################################################################################################################

# WARNING: You MUST add mtf_module_track flag to the flags of the tracks located under module directory

''')

    tfile.write("tracks = [\n")
    
    id = 0
    for line in ofile:
        if 0<len(line)<5:
            continue
        
        line = line.split()
        
        track_name = line[0]
        flag_code = get_flag_code(line)   # line[1]
        continuous_flag_code = get_cflag_code(line)   # line[2]
        
        tfile.write('''  ("%s","%s", %s, %s),\n''' %(track_name.split('.')[0],track_name,flag_code,continuous_flag_code))
        idfile.write("%s = %d\n" %(track_name.split('.')[0],id))
        id += 1
        
    tfile.write("]\n")
    idfile.close()
    tfile.close()
    ofile.close()
    
    
if __name__=='__main__':
    print "Decompiling music ..."
    decompile()