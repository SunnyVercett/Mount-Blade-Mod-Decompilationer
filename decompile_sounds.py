#! /usr/bin/env python
#coding=utf-8

# decompile sounds.txt to module_sounds.py

from module_info import *
from header_sounds import *

sound_flags_old = {
   'sf_2d       ': 0x00000001,
   'sf_looping  ': 0x00000002,
   'sf_start_at_random_pos': 0x00000004,
   'sf_stream_from_hd     ': 0x00000008,
   'sf_always_send_via_network': 0x00100000,

   'sf_priority_15   ': 0x000000f0,
   'sf_priority_14   ': 0x000000e0,
   'sf_priority_13   ': 0x000000d0,
   'sf_priority_12   ': 0x000000c0,
   'sf_priority_11   ': 0x000000b0,
   'sf_priority_10   ': 0x000000a0,
   'sf_priority_9    ': 0x00000090,
   'sf_priority_8    ': 0x00000080,
   'sf_priority_7    ': 0x00000070,
   'sf_priority_6    ': 0x00000060,
   'sf_priority_5    ': 0x00000050,
   'sf_priority_4    ': 0x00000040,
   'sf_priority_3    ': 0x00000030,
   'sf_priority_2    ': 0x00000020,
   'sf_priority_1    ': 0x00000010,

   'sf_vol_15        ': 0x00000f00,
   'sf_vol_14        ': 0x00000e00,
   'sf_vol_13        ': 0x00000d00,
   'sf_vol_12        ': 0x00000c00,
   'sf_vol_11        ': 0x00000b00,
   'sf_vol_10        ': 0x00000a00,
   'sf_vol_9         ': 0x00000900,
   'sf_vol_8         ': 0x00000800,
   'sf_vol_7         ': 0x00000700,
   'sf_vol_6         ': 0x00000600,
   'sf_vol_5         ': 0x00000500,
   'sf_vol_4         ': 0x00000400,
   'sf_vol_3         ': 0x00000300,
   'sf_vol_2         ': 0x00000200,
   'sf_vol_1         ': 0x00000100,
}
sound_flags = {}
for k,v in sound_flags_old.iteritems():
    sound_flags[v] = k.replace(' ','')
    
    
#-----------------------------------------------------------------------------#
#-------------------------- above this are constants -------------------------#
#-----------------------------------------------------------------------------#


def get_flag_code(line):
    flag_code = ''''''
    sound_flag = int(line[1])
    if sound_flag==0:
        return '0'
    
    sound_flag_keys = sound_flags.keys()
    sound_flag_keys.sort()
    sound_flag_keys.reverse()
    for each_flag in sound_flag_keys:
        if sound_flag&each_flag==each_flag:
            flag_code += "|%s" %sound_flags[each_flag]
            sound_flag -= each_flag
        if sound_flag==0:
            return flag_code.replace('|','',1)
    else:
        return line[1]


def decompile():
    ofile = open(export_dir+"sounds.txt",'r')
    tfile = open(export_dir+"decompiled files/module_sounds.py",'w')
    idfile = open(export_dir+"decompiled files/ID_sounds.py",'w')
      
    tfile.write('''from header_sounds import * \n\n''')
    
    tfile.write("sounds = [\n")
    
    sound_file_id = 0
    sound_file_ids = {}
    id = 0
    for line in ofile:
        if line[0]==' ':
            line = line.split()
            sound_file_ids[sound_file_id] = line[0]
            sound_file_id += 1
        
        # by the time the first snd_ line is reached, all sound files should have already been included in to sound_file_ids
        
        if 'snd_' in line:
            line = line.split()
            
            flag_code = get_flag_code(line)   # line[1]
            
            tfile.write('''  ("%s", %s, [''' %(line[0][4:],flag_code))
            idfile.write("%s = %d\n" %(line[0],id))
            id += 1
            
            sound_file_number = int(line[2])
            for i in xrange(sound_file_number):
                tfile.write('''"%s",''' %sound_file_ids[int(line[3+2*i])])
            tfile.write("]),\n")
            
    tfile.write("]\n")
    ofile.close()
    tfile.close()
    idfile.close()
    
    
if __name__=='__main__':
    print "Decompiling sounds ..."
    decompile()