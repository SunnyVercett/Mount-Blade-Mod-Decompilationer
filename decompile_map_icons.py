#! /usr/bin/env python
#coding=utf-8

# decompile map_icons.txt to module_map_icons.py 

from module_info import *
from decompiled_ID_sounds import *
from decompile_operations import *


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
#-------------------------- above this are constants -------------------------#
#-----------------------------------------------------------------------------#


def get_flag_code(line):
    icon_flag = int(line[1])
    if icon_flag==0:
        return '0'
    elif icon_flag==1:
        return 'mcn_no_shadow '
    else:
        return line[1]
    
    
def get_scale_code(line):
    icon_scale = float(line[3])
    if icon_scale==0.0:
        return '0.0'
    elif icon_scale==0.3:
        return 'banner_scale'
    elif icon_scale==0.15:
        return 'avatar_scale'
    else:
        return line[3]
    
    
def get_sound_code(line):   # needs update after decompiling sounds.txt
    icon_sound = int(line[4])
    if icon_sound==0:
        return '0'
    return sound_ids[icon_sound]


def decompile():
    ofile = open(export_dir+"map_icons.txt",'r')
    tfile = open(export_dir+"decompiled files/module_map_icons.py",'w')
    idfile = open(export_dir+"decompiled files/ID_map_icons.py",'w')
    
    tfile.write('''from header_map_icons import *
from module_constants import *
from header_operations import *
from header_triggers import *
from ID_sounds import *

####################################################################################################################
#  Each map icon record contains the following fields:
#  1) Map icon id: used for referencing map icons in other files.
#     The prefix icon_ is automatically added before each map icon id.
#  2) Map icon flags. See header_map icons.py for a list of available flags
#  3) Mesh name.
#  4) Scale. 
#  5) Sound.
#  6) Offset x position for the flag icon.
#  7) Offset y position for the flag icon.
#  8) Offset z position for the flag icon.
####################################################################################################################

banner_scale = 0.3
avatar_scale = 0.15

''')
    
    tfile.write("map_icons = [\n")
    
    isTrigLine = 0
    isEndLine = 0
    
    id = 0
    for line in ofile:
        if 'map_icons_file' in line:
            continue
        if ' ' not in line:    # skip the second line where there's only the count of map icons
            continue
        
        #if u'\u0061'<=line[0]<=u'\u007a':   # check if the first char of the line is a lowercase English char
        if not isTrigLine:
            line = line.split()
            
            flag_code = get_flag_code(line)   # line[1]
            scale_code = get_scale_code(line)   # line[3]
            sound_code = get_sound_code(line)   # line[4]
            
            tfile.write('''  ("%s",%s,"%s", %s, %s, %.2f,%.2f,%.2f, \n    [''' %(line[0],flag_code,line[2],scale_code,sound_code,float(line[5]),float(line[6]),float(line[7])))
            idfile.write("icon_%s = %d\n" %(line[0],id))
            id += 1
            
            isTrigLine = int(line[8])
            if isTrigLine==0:
                tfile.write("],\n")    # write an end to the triggers list
                tfile.write("  ),\n")   # end of this icon block
            continue    # prevent next scripts from parsing
        
        if isTrigLine:
            line = line.split()
            
            timer = float(line[0])
            if timer in trigger_timers:
                timer = trigger_timers[timer]
            else:
                timer = line[0]
            
            tfile.write("\n      (%s,\n%s,\n      )," %(timer,decompile_statement_block(' '.join(line[1:]))))
            
            isTrigLine -= 1
            if isTrigLine==0:
                tfile.write("\n    ],\n")
                tfile.write("  ),\n")   # end of this icon block
            continue    # prevent next scripts from parsing
            
    tfile.write("]\n")
    tfile.close()
    ofile.close()
    idfile.close()
    
    
if __name__=='__main__':
    print "Decompiling map icons ..."
    decompile()