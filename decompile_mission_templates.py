#! /usr/bin/env python
#coding=utf-8

# decompile mission_templates.txt to module_mission_templates.py

from module_info import *
#from header_mission_templates import *
from decompiled_ID_items import *
from decompile_operations import *

# these are the flags defined in header_mission_templates.py
# instead of importing that module, define these values here at the beginning
# could prevent errors
mtef_enemy_party        = 0x00000001
mtef_ally_party         = 0x00000002
mtef_scene_source       = 0x00000004
mtef_conversation_source= 0x00000008
mtef_visitor_source     = 0x00000010
mtef_defenders          = 0x00000040
mtef_attackers          = 0x00000080
mtef_no_leader          = 0x00000100
mtef_no_companions      = 0x00000200
mtef_no_regulars        = 0x00000400
mtef_team_0             = 0x00001000
mtef_team_1             = 0x00002000
mtef_team_2             = 0x00003000
mtef_team_3             = 0x00004000
mtef_team_4             = 0x00005000
mtef_team_5             = 0x00006000
mtef_team_member_2      = 0x00008000
mtef_infantry_first     = 0x00010000
mtef_archers_first      = 0x00020000
mtef_cavalry_first      = 0x00040000
mtef_no_auto_reset      = 0x00080000
mtef_reverse_order      = 0x01000000
mtef_use_exact_number   = 0x02000000
mtef_leader_only        = mtef_no_companions | mtef_no_regulars
mtef_regulars_only      = mtef_no_companions | mtef_no_leader

af_override_weapons        = 0x0000000f
af_override_weapon_0       = 0x00000001
af_override_weapon_1       = 0x00000002
af_override_weapon_2       = 0x00000004
af_override_weapon_3       = 0x00000008
af_override_head           = 0x00000010
af_override_body           = 0x00000020
af_override_foot           = 0x00000040
af_override_gloves         = 0x00000080
af_override_horse          = 0x00000100
af_override_fullhelm       = 0x00000200
af_require_civilian        = 0x10000000
af_override_all_but_horse  = af_override_weapons | af_override_head | af_override_body |af_override_gloves
af_override_all            = af_override_horse | af_override_all_but_horse
af_override_everything     = af_override_all | af_override_foot
af_castle_lord             = af_override_horse | af_override_weapons| af_require_civilian


mtmp_flags_old = {
   'mtf_arena_fight        ': 0x00000001, #identify enemies through team_no
   'mtf_team_fight         ': 0x00000001, #identify enemies through team_no
   'mtf_battle_mode        ': 0x00000002, #No inventory access
   'mtf_commit_casualties  ': 0x00000010,
   'mtf_no_blood           ': 0x00000100,
   'mtf_synch_inventory    ': 0x00010000, #Make a backup of player inventory and restore it at mission end.
}
mtmp_flags = {}
for k,v in mtmp_flags_old.iteritems():
    mtmp_flags[v] = k.replace(' ','')
    
    
mtmp_types_old = {
    'leave_wo_battle': 0,
    'leave_during_battle': 1,
    'cancel_attack': 2,
    'speak': 3,
    'intend_battle': 4,
    'cancel_reinforce': 5,
    'surrender': 6,
    'stay_back': 7,
    'charge': 8,
    'stay_back_with_ally': 9,
    'charge_with_ally': 10,
}
mtmp_types = {}
for k,v in mtmp_types_old.iteritems():
    mtmp_types[v] = k.replace(' ','')
    
    
mtefs_old = {
   'mtef_enemy_party        ': 0x00000001,
   'mtef_ally_party         ': 0x00000002,
   'mtef_scene_source       ': 0x00000004,
   'mtef_conversation_source': 0x00000008,
   'mtef_visitor_source     ': 0x00000010,
   'mtef_defenders          ': 0x00000040,
   'mtef_attackers          ': 0x00000080,
   'mtef_no_leader          ': 0x00000100,
   'mtef_no_companions      ': 0x00000200,
   'mtef_no_regulars        ': 0x00000400,
   #'mtef_team_0             ': 0x00001000,
   'mtef_team_0             ': 0x00001000,
   'mtef_team_1             ': 0x00002000,
   'mtef_team_2             ': 0x00003000,
   'mtef_team_3             ': 0x00004000,
   'mtef_team_4             ': 0x00005000,
   'mtef_team_5             ': 0x00006000,
   'mtef_team_member_2      ': 0x00008000,
   'mtef_infantry_first     ': 0x00010000,
   'mtef_archers_first      ': 0x00020000,
   'mtef_cavalry_first      ': 0x00040000,
   'mtef_no_auto_reset      ': 0x00080000,
   'mtef_reverse_order      ': 0x01000000,
   'mtef_use_exact_number   ': 0x02000000,
   'mtef_leader_only        ': mtef_no_companions | mtef_no_regulars,
   'mtef_regulars_only      ': mtef_no_companions | mtef_no_leader,
}
mtefs = {}
for k,v in mtefs_old.iteritems():
    mtefs[v] = k.replace(' ','')
    
    
afs_old = {
   'af_override_weapons        ': 0x0000000f,
   'af_override_weapon_0       ': 0x00000001,
   'af_override_weapon_1       ': 0x00000002,
   'af_override_weapon_2       ': 0x00000004,
   'af_override_weapon_3       ': 0x00000008,
   'af_override_head           ': 0x00000010,
   'af_override_body           ': 0x00000020,
    #'af_override_leg            ': 0x00000040,
   'af_override_foot           ': 0x00000040,
   'af_override_gloves         ': 0x00000080,
   'af_override_horse          ': 0x00000100,
   'af_override_fullhelm       ': 0x00000200,

    #'af_override_hands          ': 0x00000100,
   'af_require_civilian        ': 0x10000000,

    #'af_override_all_but_horse  ': 0x000000ff,
   'af_override_all_but_horse  ': af_override_weapons | af_override_head | af_override_body |af_override_gloves,
   'af_override_all            ': af_override_horse | af_override_all_but_horse,
   'af_override_everything     ': af_override_all | af_override_foot,
   'af_castle_lord             ': af_override_horse | af_override_weapons| af_require_civilian,
}
afs = {}
for k,v in afs_old.iteritems():
    afs[v] = k.replace(' ','')
    
    
trigger_timers_old = {
   'ti_simulate_battle           ': -5.0,
   'ti_on_party_encounter        ': -6.0,
   'ti_question_answered         ': -8.0,
   'ti_on_switch_to_map          ': -75.0,
   'ti_on_init_item              ': -50.0,
   'ti_on_weapon_attack          ': -51.0,
   'ti_on_missile_hit            ': -52.0,
   'ti_on_shield_hit             ': -80.0,
   'ti_on_init_map_icon          ': -70.0,
   'ti_server_player_joined      ': -15.0,
   'ti_on_player_exit            ': -29.0,
   'ti_on_multiplayer_mission_end': -16.0,
   'ti_battle_window_opened      ': -24.0,
   'ti_before_mission_start      ': -19.0,
   'ti_after_mission_start       ': -20.0,
   'ti_tab_pressed               ': -21.0,
   'ti_inventory_key_pressed     ': -22.0,
   'ti_escape_pressed            ': -23.0,
   'ti_on_agent_spawn            ': -25.0,
   'ti_on_agent_killed_or_wounded': -26.0,
   'ti_on_agent_knocked_down     ': -27.0,
   'ti_on_agent_hit              ': -28.0,
   'ti_on_leave_area             ': -30.0,
   'ti_on_item_picked_up         ': -53.0,
   'ti_on_item_dropped           ': -54.0,
   'ti_on_agent_mount            ': -55.0,
   'ti_on_agent_dismount         ': -56.0,
   'ti_on_item_wielded           ': -57.0,
   'ti_on_item_unwielded         ': -58.0,
   'ti_on_order_issued           ': -71.0,
   'ti_on_presentation_load              ': -60.0,
   'ti_on_presentation_run               ': -61.0,
   'ti_on_presentation_event_state_change': -62.0,
   'ti_on_presentation_mouse_enter_leave ': -63.0,
   'ti_on_presentation_mouse_press       ': -64.0,
   'ti_on_scene_prop_init              ': -40.0,
   'ti_on_scene_prop_hit               ': -42.0,
   'ti_on_scene_prop_destroy           ': -43.0,
   'ti_on_scene_prop_start_use         ': -47.0,
   'ti_on_scene_prop_cancel_use        ': -48.0,
   'ti_on_scene_prop_use               ': -44.0,
   'ti_on_scene_prop_is_animating      ': -45.0,
   'ti_on_scene_prop_animation_finished': -46.0,
   'ti_scene_prop_deformation_finished ': -76.0,
   'ti_once       ': 100000000.0
}
trigger_timers = {}
for k,v in trigger_timers_old.iteritems():
    trigger_timers[v] = k.replace(' ','')

    

#-----------------------------------------------------------------------------#


def get_flag_code(line):
    flag_code = ''''''
    mtmp_flag = int(line[2])
    if mtmp_flag==0:
        return '0'
    
    mtmp_flag_keys = mtmp_flags.keys()
    mtmp_flag_keys.sort()
    mtmp_flag_keys.reverse()
    for each_flag in mtmp_flag_keys:
        if mtmp_flag&each_flag==each_flag:
            flag_code += "|%s" %mtmp_flags[each_flag]
            mtmp_flag -= each_flag
        if mtmp_flag==0:
            return flag_code.replace('|','',1)
    else:
        return line[2]
    
    
def get_type_code(line):
    type = int(line[3])
    if type in mtmp_types:
        return mtmp_types[type]
    else:
        return line[3]
    
    
def get_mtef_code(line):
    mtef_code = ''''''
    mtef = int(line[1])
    if mtef==0:
        return '0'
    
    mtef_keys = mtefs.keys()
    mtef_keys.sort()
    mtef_keys.reverse()
    for each_mtef in mtef_keys:
        if mtef&each_mtef==each_mtef:
            mtef_code += "|%s" %mtefs[each_mtef]
            mtef -= each_mtef
        if mtef==0:
            return mtef_code.replace('|','',1)
    else:
        return line[1]
    
    
def get_af_code(line):
    af_code = ''''''
    af = int(line[2])
    if af==0:
        return '0'
    
    af_keys = afs.keys()
    af_keys.sort()
    af_keys.reverse()
    for each_af in af_keys:
        if af&each_af==each_af:
            af_code += "|%s" %afs[each_af]
            af -= each_af
        if af==0:
            return af_code.replace('|','',1)
    else:
        return line[2]
    
    
def get_aif_code(line):
    aif = int(line[3])
    if aif==0:
        return '0'
    elif aif==16:
        return 'aif_start_alarmed'
    else:
        return line[3]
    
    
def get_timer_code(line):
    timer = float(line[0])
    if timer in trigger_timers:
        return trigger_timers[timer]
    else:
        return line[0]


def get_repeat_code(line):
    repeat = float(line[2])
    if repeat==100000000.0:
        return 'ti_once'
    else:
        return line[2]


def get_cdtn_csqs_code(line):
    pos = 3
    begin_pos = pos
    num_ops = int(line[pos])
    
    while num_ops:
        pos += 2
        params = int(line[pos])
        pos += params
        num_ops -= 1
        
    end_pos = pos+1
    cdtn_code = decompile_statement_block(' '.join(line[begin_pos:end_pos]))
    csqs_code = decompile_statement_block(' '.join(line[end_pos:]))
    return cdtn_code,csqs_code


def decompile():
    ofile = open(export_dir+"mission_templates.txt",'r')
    tfile = open(export_dir+"decompiled files/module_mission_templates.py",'w')
    idfile = open(export_dir+"decompiled files/ID_mission_templates.py",'w')

    tfile.write('''from header_common import *
from header_operations import *
from header_mission_templates import *
from header_animations import *
from header_sounds import *
from header_music import *
from header_items import *
from module_constants import *

####################################################################################################################
#   Each mission-template is a tuple that contains the following fields:
#  1) Mission-template id (string): used for referencing mission-templates in other files.
#     The prefix mt_ is automatically added before each mission-template id
#
#  2) Mission-template flags (int): See header_mission-templates.py for a list of available flags
#  3) Mission-type(int): Which mission types this mission template matches.
#     For mission-types to be used with the default party-meeting system,
#     this should be 'charge' or 'charge_with_ally' otherwise must be -1.
#     
#  4) Mission description text (string).
#  5) List of spawn records (list): Each spawn record is a tuple that contains the following fields:
#    5.1) entry-no: Troops spawned from this spawn record will use this entry
#    5.2) spawn flags.
#    5.3) alter flags. which equipment will be overriden
#    5.4) ai flags.
#    5.5) Number of troops to spawn.
#    5.6) list of equipment to add to troops spawned from here (maximum 8).
#  6) List of triggers (list).
#     See module_triggers.py for infomation about triggers.
#
#  Please note that mission templates is work in progress and can be changed in the future versions.
# 
####################################################################################################################

pilgrim_disguise = [itm_pilgrim_hood,itm_pilgrim_disguise,itm_practice_staff, itm_throwing_daggers]
af_castle_lord = af_override_horse | af_override_weapons| af_require_civilian

''')

    tfile.write("mission_templates = [\n")
    
    isDescLine = 0
    isGroupStartLine = 0
    isGroupLine = 0
    isTrigCntLine = 0
    isTrigLine = 0
    
    id = 0
    for line in ofile:
        if len(line)<2:
            continue
        
        if 'mst_' in line:
            #print line
            line = line.split()
            
            flag_code = get_flag_code(line)   # line[2]
            type_code = get_type_code(line)   # line[3]
            
            tfile.write('''  ("%s", %s, %s,''' %(line[1],flag_code,type_code))
            idfile.write("%s = %d\n" %(line[0],id))
            id += 1
            
            isDescLine = 1
            continue
        
        if isDescLine:
            line = line.split()
            
            tfile.write('''\n    "%s",''' %line[0].replace('_',' '))
            
            isDescLine = 0
            isGroupStartLine = 1
            continue
        
        if isGroupStartLine:
            isGroupStartLine = 0
            line = line.split()
            isGroupLine = int(line[0])-1
            
            if isGroupLine==-1:
                tfile.write('''\n    [],''')   # write an empty group
                isTrigLine = int(line[1])
                if isTrigLine==0:
                    tfile.write('''\n    [],\n  ),\n''')   # write an tmpty trigger
                else:
                    tfile.write('''\n    [''')                
                continue
            elif isGroupLine==0:
                isTrigCntLine = 1
                
            line = line[1:]
            
            tfile.write('''\n    [''')
            
            mtef_code = get_mtef_code(line)   # line[1]
            af_code = get_af_code(line)   # line[2]
            aif_code = get_aif_code(line)   # line[3]
            
            tfile.write('''\n        (%s,%s,%s,%s,%s,[''' %(line[0],mtef_code,af_code,aif_code,line[4]))
            
            for i in xrange(int(line[5])):
                tfile.write("%s," %item_ids[int(line[6+i])])
                
            tfile.write("]),")
            
            if isGroupLine==0:
                tfile.write('''\n    ],''')            
            
            continue
            
        if isGroupLine>0:   # isGroupLine = -1 also needs to be excluded
            line = line.split()
            
            mtef_code = get_mtef_code(line)   # line[1]
            af_code = get_af_code(line)   # line[2]
            aif_code = get_aif_code(line)   # line[3]
            
            tfile.write('''\n        (%s,%s,%s,%s,%s,[''' %(line[0],mtef_code,af_code,aif_code,line[4]))
            
            for i in xrange(int(line[5])):
                tfile.write("%s," %item_ids[int(line[6+i])])
                
            tfile.write("]),")
            
            isGroupLine -= 1
            if isGroupLine==0:
                tfile.write('''\n    ],''')
                isTrigCntLine = 1
            continue
            
        if isTrigCntLine:
            line = line.split()
            isTrigLine = int(line[0])
            
            if isTrigLine==0:
                tfile.write('''\n    [],\n  ),\n''')
            else:
                tfile.write('''\n    [''')
            
            isTrigCntLine = 0
            continue
        
        if isTrigLine:
            line = line.split()
            
            timer = get_timer_code(line)   # line[0]
            repeat = get_repeat_code(line)   # line[2]
            
            tfile.write('''\n      (%s, %.1f, %s,''' %(timer,float(line[1]),repeat))
            
            cdtn_code,csqs_code = get_cdtn_csqs_code(line)
            
            tfile.write("\n%s,\n%s,\n      )," %(cdtn_code,csqs_code))
            
            isTrigLine -= 1
            if isTrigLine==0:
                tfile.write("\n    ],\n  ),\n\n")
            continue
        
    tfile.write("]\n")
    tfile.close()
    idfile.close()
    ofile.close()
    
    
if __name__=='__main__':
    print "Decompiling mission templates ..."
    decompile()