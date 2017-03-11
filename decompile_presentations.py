#! /usr/bin/env python
#coding=utf-8

# decompile presentations.txt to module_presentations.py

from module_info import *
from decompiled_ID_meshes import *
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


def get_flag_code(line):
    prst_flag = int(line[1])
    if prst_flag==0:
        return '0'
    elif prst_flag==1:
        return 'prsntf_read_only'
    elif prst_flag==2:
        return 'prsntf_manual_end_only'
    elif prst_flag==3:
        return 'prsntf_manual_end_only|prsntf_read_only'
    else:
        return line[1]
    
    
def get_mesh_code(line):
    prst_mesh = int(line[2])
    if prst_mesh in mesh_ids:
        return mesh_ids[prst_mesh]
    else:
        return line[2]


def decompile():
    ofile = open(export_dir+"presentations.txt",'r')
    tfile = open(export_dir+"decompiled files/module_presentations.py",'w')
    idfile = open(export_dir+"decompiled files/ID_presentations.py",'w')

    tfile.write('''from header_common import *
from header_presentations import *
from header_mission_templates import *
from ID_meshes import *
from header_operations import *
from header_triggers import *
from module_constants import *
import string

####################################################################################################################
#  Each presentation record contains the following fields:
#  1) Presentation id: used for referencing presentations in other files. The prefix prsnt_ is automatically added before each presentation id.
#  2) Presentation flags. See header_presentations.py for a list of available flags
#  3) Presentation background mesh: See module_meshes.py for a list of available background meshes
#  4) Triggers: Simple triggers that are associated with the presentation
####################################################################################################################

''')
    
    tfile.write("presentations = [\n")
    
    isTrigLine = 0
    id = 0
    for line in ofile:
        if 'prsnt_' in line:
            line = line.split()
            
            flag_code = get_flag_code(line)   # line[1]
            mesh_code = get_mesh_code(line)   # line[2]
            
            tfile.write('''  ("%s",%s,%s,\n    [''' %(line[0][6:],flag_code,mesh_code))
            idfile.write("%s = %d\n" %(line[0],id))
            id += 1
            
            isTrigLine = int(line[-1])
            if not isTrigLine:
                tfile.write(''']\n  ),\n''')
            continue
        
        if isTrigLine:
            line = line.split()
            
            timer = float(line[0])
            if timer in trigger_timers:
                timer = trigger_timers[timer]
            else:
                timer = line[0]
            tfile.write("\n      (%s,\n%s,\n      )," %(timer,decompile_statement_block(' '.join(line[1:]))))
            
            isTrigLine -= 1
            if not isTrigLine:
                tfile.write('''\n    ]\n  ),\n''')
            continue
        
    tfile.write("]\n")
    tfile.close()
    idfile.close()
    ofile.close()
    
    
if __name__=='__main__':
    print "Decompiling presentations ..."
    decompile()