#! /usr/bin/env python
#coding=utf-8

# decompile actions.txt to module_animations.py

from module_info import *


anim_flags_old = {
   'acf_synch_with_horse        ': 0x00000001,
   'acf_align_with_ground       ': 0x00000002,
   'acf_enforce_lowerbody       ': 0x00000100,
   'acf_enforce_rightside       ': 0x00000200,
   'acf_enforce_all             ': 0x00000400,
   'acf_parallels_for_look_slope': 0x00001000,
   'acf_lock_camera             ': 0x00002000,
   'acf_displace_position       ': 0x00004000,
   'acf_ignore_slope            ': 0x00008000,
   'acf_thrust                  ': 0x00010000,
   'acf_right_cut               ': 0x00020000,
   'acf_left_cut                ': 0x00040000,
   'acf_overswing               ': 0x00080000,
   'acf_rot_vertical_mask       ': 0x00300000,
   'acf_rot_vertical_bow        ': 0x00100000,
   'acf_rot_vertical_sword      ': 0x00200000,
   #'acf_anim_length_mask        ': 0xff000000,
}
anim_flags = {}
for k,v in anim_flags_old.iteritems():
    anim_flags[v] = k.replace(' ','')
    
    
anim_mflags_old = {
   'amf_priority_jump          ': 2,
   'amf_priority_ride          ': 2,
   'amf_priority_continue      ': 1,
   'amf_priority_attack        ': 10,
   'amf_priority_cancel        ': 12,
   'amf_priority_defend        ': 14,
   'amf_priority_defend_parry  ': 15,  # amf_priority_defend + 1
   'amf_priority_throw         ': 15,  # amf_priority_defend + 1
   'amf_priority_blocked       ': 15,  # amf_priority_defend_parry
   'amf_priority_parried       ': 15,  # amf_priority_defend_parry
   'amf_priority_kick          ': 33,
   'amf_priority_jump_end      ': 33,
   'amf_priority_reload        ': 60,
   'amf_priority_mount         ': 64,
   'amf_priority_equip         ': 70,
   'amf_priority_rear          ': 74,
   'amf_priority_striked       ': 80,
   'amf_priority_fall_from_horse': 81,
   'amf_priority_die           ': 95,
    #'amf_priority_mask                         ': 0x00000fff,
   'amf_rider_rot_bow                         ': 0x00001000,
   'amf_rider_rot_throw                       ': 0x00002000,
   'amf_rider_rot_crossbow                    ': 0x00003000,
   'amf_rider_rot_pistol                      ': 0x00004000,
   'amf_rider_rot_overswing                   ': 0x00005000,
   'amf_rider_rot_thrust                      ': 0x00006000,
   'amf_rider_rot_swing_right                 ': 0x00007000,
   'amf_rider_rot_swing_left                  ': 0x00008000,
   'amf_rider_rot_couched_lance               ': 0x00009000,
   'amf_rider_rot_shield                      ': 0x0000a000,
   'amf_rider_rot_defend                      ': 0x0000b000,
   'amf_start_instantly                       ': 0x00010000,
   'amf_use_cycle_period                      ': 0x00100000,
   'amf_use_weapon_speed                      ': 0x00200000,
   'amf_use_defend_speed                      ': 0x00400000,
   'amf_accurate_body                         ': 0x00800000,
   'amf_client_prediction                     ': 0x01000000,
   'amf_play                                  ': 0x02000000,
   'amf_keep	                              ': 0x04000000,
   'amf_restart                               ': 0x08000000, # restart animation even if it is the current animation
   'amf_hide_weapon                           ': 0x10000000,
   'amf_client_owner_prediction               ': 0x20000000,
   'amf_use_inertia                           ': 0x40000000,
   'amf_continue_to_next                      ': 0x80000000,
}
anim_mflags = {}
for k,v in anim_mflags_old.iteritems():
    anim_mflags[v] = k.replace(' ','')
    
    
anim_rflags_old = {
   'arf_blend_in_0              ': 0x00000001,
   'arf_blend_in_1              ': 0x00000002,
   'arf_blend_in_2              ': 0x00000003,
   'arf_blend_in_3              ': 0x00000004,
   'arf_blend_in_4              ': 0x00000005,
   'arf_blend_in_5              ': 0x00000006,
   'arf_blend_in_6              ': 0x00000007,
   'arf_blend_in_7              ': 0x00000008,
   'arf_blend_in_8              ': 0x00000009,
   'arf_blend_in_9              ': 0x0000000a,
   'arf_blend_in_10             ': 0x0000000b,
   'arf_blend_in_11             ': 0x0000000c,
   'arf_blend_in_12             ': 0x0000000d,
   'arf_blend_in_13             ': 0x0000000e,
   'arf_blend_in_14             ': 0x0000000f,
   'arf_blend_in_15             ': 0x00000010,
   'arf_blend_in_16             ': 0x00000011,
   'arf_blend_in_17             ': 0x00000012,
   'arf_blend_in_18             ': 0x00000013,
   'arf_blend_in_19             ': 0x00000014,
   'arf_blend_in_20             ': 0x00000015,
   'arf_blend_in_21             ': 0x00000016,
   'arf_blend_in_22             ': 0x00000017,
   'arf_blend_in_23             ': 0x00000018,
   'arf_blend_in_24             ': 0x00000019,
   'arf_blend_in_25             ': 0x0000001a,
   'arf_blend_in_26             ': 0x0000001b,
   'arf_blend_in_27             ': 0x0000001c,
   'arf_blend_in_28             ': 0x0000001d,
   'arf_blend_in_29             ': 0x0000001e,
   'arf_blend_in_30             ': 0x0000001f,
   'arf_blend_in_31             ': 0x00000020,
   'arf_blend_in_32             ': 0x00000021,
   'arf_blend_in_48             ': 0x00000031,
   'arf_blend_in_64             ': 0x00000041,
   'arf_blend_in_128            ': 0x00000081,
   'arf_blend_in_254            ': 0x000000ff,
   'arf_make_walk_sound         ': 0x00000100,
   'arf_make_custom_sound       ': 0x00000200,
   'arf_two_handed_blade        ': 0x01000000,
   'arf_lancer                  ': 0x02000000,
   'arf_stick_item_to_left_hand ': 0x04000000,
   'arf_cyclic                  ': 0x10000000,
   'arf_use_walk_progress       ': 0x20000000,
   'arf_use_stand_progress      ': 0x40000000,
   'arf_use_inv_walk_progress   ': 0x80000000,
}
anim_rflags = {}
for k,v in anim_rflags_old.iteritems():
    anim_rflags[v] = k.replace(' ','')
    

#-----------------------------------------------------------------------------#
#------------------------- above this are constants --------------------------#
#-----------------------------------------------------------------------------#


def get_flag_code(line):
    flag_code = ''''''
    anim_flag = int(line[1])
    if anim_flag==0:
        return '0'
    
    anim_length = (anim_flag&0xff000000) >> 24
    if anim_length!=0:
        flag_code += "|acf_anim_length(%d)" %anim_length
        anim_flag -= (anim_flag&0xff000000)
    if anim_flag==0:
        return flag_code.replace('|','',1)
    
    anim_flag_keys = anim_flags.keys()
    anim_flag_keys.sort()
    anim_flag_keys.reverse()
    for each_flag in anim_flag_keys:
        if anim_flag&each_flag==each_flag:
            flag_code += "|%s" %anim_flags[each_flag]
            anim_flag -= each_flag
        if anim_flag==0:
            return flag_code.replace('|','',1)
    else:
        return line[1]
    
    
def get_mflag_code(line):
    mflag_code = ''''''
    anim_mflag = int(line[2])
    if anim_mflag==0:
        return '0'
    
    anim_mflag_keys = anim_mflags.keys()
    anim_mflag_keys.sort()
    anim_mflag_keys.reverse()
    for each_mflag in anim_mflag_keys:
        if anim_mflag&each_mflag==each_mflag:
            mflag_code += "|%s" %anim_mflags[each_mflag]
            anim_mflag -= each_mflag
        if anim_mflag==0:
            return mflag_code.replace('|','',1)
    else:
        return line[2]


def get_rflag_code(line):
    rflag_code = ''''''
    anim_rflag = int(line[4])
    if anim_rflag==0:
        return '0'
    
    anim_rflag_keys = anim_rflags.keys()
    anim_rflag_keys.sort()
    anim_rflag_keys.reverse()
    for each_rflag in anim_rflag_keys:
        if anim_rflag&each_rflag==each_rflag:
            rflag_code += "|%s" %anim_rflags[each_rflag]
            anim_rflag -= each_rflag
        if anim_rflag==0:
            return rflag_code.replace('|','',1)
    else:
        return line[4]
    
    
def get_pack_code(line):
    anim_pack = int(line[5])
    
    ai = (anim_pack&0xff)
    bi = (anim_pack&0xff00) >> 8
    ci = (anim_pack&0xff0000) >> 16
    di = (anim_pack&0xff000000) >> 24
    
    a = float(ai)/255.
    b = float(bi)/255.
    c = float(ci)/255.
    d = float(di)/255.
    
    if c or d:
        return  "pack4f(%.2f,%.2f,%.2f,%.2f)" %(a,b,c,d)
    elif a or b:
        return  "pack2f(%.2f,%.2f)" %(a,b)
    else:
        return '0'


def decompile():
    ofile = open(export_dir+"actions.txt",'r')
    tfile = open(export_dir+"decompiled files/module_animations.py",'w')
    idfile = open(export_dir+"decompiled files/ID_animations.py",'w')
    
    tfile.write('''from header_common import *
from header_animations import *

####################################################################################################################
#  There are two animation arrays (one for human and one for horse). Each animation in these arrays contains the following fields:
#  1) Animation id (string): used for referencing animations in other files. The prefix anim_ is automatically added before each animation-id .
#  2) Animation flags: could be anything beginning with acf_ defined in header_animations.py
#  3) Animation master flags: could be anything beginning with amf_ defined in header_animations.py
#  4) Animation sequences (list).
#  4.1) Duration of the sequence.
#  4.2) Name of the animation resource.
#  4.3) Beginning frame of the sequence within the animation resource.
#  4.4) Ending frame of the sequence within the animation resource.
#  4.5) Sequence flags: could be anything beginning with arf_ defined in header_animations.py
# 
####################################################################################################################

#plan : 
# basic movement : walk ride etc. 0 -20000
#  on_foot  : 0     - 10000
#  horse    : 10000 - 20000
# combat         :                20000 - 40000
# fall           :                4000 - 70000
# act            : misc.          70000 - ...

amf_priority_jump           = 2
amf_priority_ride           = 2
amf_priority_continue       = 1
amf_priority_attack         = 10
amf_priority_cancel         = 12
amf_priority_defend         = 14
amf_priority_defend_parry   = amf_priority_defend + 1
amf_priority_throw          = amf_priority_defend + 1
amf_priority_blocked        = amf_priority_defend_parry
amf_priority_parried        = amf_priority_defend_parry
amf_priority_kick           = 33
amf_priority_jump_end       = 33
amf_priority_reload         = 60
amf_priority_mount          = 64
amf_priority_equip          = 70
amf_priority_rear           = 74
amf_priority_striked        = 80
amf_priority_fall_from_horse= 81
amf_priority_die            = 95



horse_move = 10000
combat     = 20000
defend     = 35000
blow       = 40000

attack_parried_duration = 0.6
attack_blocked_duration = 0.3
attack_blocked_duration_thrust = attack_blocked_duration + 0.3
attack_parried_duration_thrust = attack_parried_duration + 0.1
defend_parry_duration_1 = 0.6
defend_parry_duration_2 = 0.6
defend_parry_duration_3 = 0.8
ready_durn     = 0.35
defend_duration = 0.75
defend_keep_duration = 2.0
cancel_duration = 0.25

blend_in_defense = arf_blend_in_3
blend_in_ready = arf_blend_in_6
blend_in_release = arf_blend_in_5
blend_in_parry = arf_blend_in_5
blend_in_parried = arf_blend_in_3


blend_in_walk = arf_blend_in_3
blend_in_continue = arf_blend_in_1

#### Animations begin here

# All of the animations are hardcoded. You can edit the individual sequences, resources or times. But each
# animation must stay at the same position, otherwise the game won't run properly. If you want to add a new animation,
# you can change both the ids and values of the animations which are named as unused_human_anim_???
# and unused_horse_anim_??? (??? = any number). You must not change used animations' ids.

''')
    
    tfile.write("animations = [\n")
        
    id = 0
    isSeqsLine = 0
    for line in ofile:
        c = 0
        spaces = 0
        while line[c]==' ':
            spaces += 1
            c += 1
            
        if c==1:
            line = line.split()
            
            flag_code = get_flag_code(line)   # line[1]
            mflag_code = get_mflag_code(line)   # line[2]
            
            tfile.write('''  ["%s", %s, %s,\n''' %(line[0],flag_code,mflag_code))
            idfile.write("%s = %d\n" %(line[0],id))
            
            id += 1
            
            isSeqsLine = int(line[3])
            continue
        
        if isSeqsLine:
            line = line.split()
            
            rflag_code = get_rflag_code(line)   # line[4]
            pack_code = get_pack_code(line)    # line[5]
            
            tfile.write('''    [%.2f, "%s", %s,%s, %s, %s, (%.1f,%.1f,%.1f), %.2f],\n''' %(float(line[0]),line[1],line[2],line[3],rflag_code,pack_code,float(line[6]),float(line[7]),float(line[8]),float(line[9])))
            
            isSeqsLine -= 1
            if isSeqsLine==0:
                tfile.write("  ],\n")
            continue
        
    tfile.write("]\n")
    tfile.close()
    idfile.close()
    ofile.close()
    
    
if __name__=='__main__':
    print "Decompiling animations ..."
    decompile()