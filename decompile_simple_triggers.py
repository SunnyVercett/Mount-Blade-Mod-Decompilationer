#! /usr/bin/env python
#coding=utf-8

# decompile simple_triggers.txt to module_simple_triggers.py

from module_info import *
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


def get_timer_code(line):
    timer = float(line[0])
    if timer in trigger_timers:
        return trigger_timers[timer]
    else:
        return line[0]


def decompile():
    ofile = open(export_dir+"simple_triggers.txt",'r')
    tfile = open(export_dir+"decompiled files/module_simple_triggers.py",'w')
    
    tfile.write('''from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *
from header_music import *

from module_constants import *

####################################################################################################################
# Simple triggers are the alternative to old style triggers. They do not preserve state, and thus simpler to maintain.
#
#  Each simple trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked
# 2) Operation block: This must be a valid operation block. See header_operations.py for reference. 
####################################################################################################################

''')

    tfile.write("simple_triggers = [\n")
    
    for line in ofile:
        if '.' in line:
            line = line.split()
            
            timer = get_timer_code(line)   # line[0]
            ops_code = decompile_statement_block(' '.join(line[1:]))   # line[1:]
            
            tfile.write("    (%s,\n%s,\n    ),\n" %(timer,ops_code))
            
    tfile.write("]\n")
    ofile.close()
    tfile.close()
    
    
if __name__=='__main__':
    print "Decompiling simple triggers ..."
    decompile()