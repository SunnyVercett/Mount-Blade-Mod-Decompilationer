#! /usr/bin/env python
#coding=utf-8

# decompile scene_props.txt to module_scene_props.py

from module_info import *
from decompile_operations import *


spro_flags_old = {
   'sokf_type_container       ': 0x0000000000000005,
   'sokf_type_ai_limiter      ': 0x0000000000000008,
   'sokf_type_barrier         ': 0x0000000000000009,
   'sokf_type_barrier_leave   ': 0x000000000000000a,
   'sokf_type_ladder          ': 0x000000000000000b,
   'sokf_type_barrier3d       ': 0x000000000000000c,
   'sokf_type_player_limiter  ': 0x000000000000000d,
   'sokf_type_mask            ': 0x00000000000000FF,
   'sokf_add_fire             ': 0x0000000000000100,
   'sokf_add_smoke            ': 0x0000000000000200,
   'sokf_add_light            ': 0x0000000000000400,
   'sokf_show_hit_point_bar   ': 0x0000000000000800,
   'sokf_place_at_origin      ': 0x0000000000001000,
   'sokf_dynamic              ': 0x0000000000002000,
   'sokf_invisible            ': 0x0000000000004000,
   'sokf_destructible         ': 0x0000000000008000,
   'sokf_moveable             ': 0x0000000000010000,
   'sokf_face_player          ': 0x0000000000020000,
   'sokf_dynamic_physics      ': 0x0000000000040000,
   'sokf_missiles_not_attached': 0x0000000000080000, #works only for dynamic mission objects
   'sokf_enforce_shadows      ': 0x0000000000100000,
   'sokf_dont_move_agent_over ': 0x0000000000200000,
   'sokf_handle_as_flora      ': 0x0000000001000000,
   'sokf_static_movement      ': 0x0000000002000000,
}
spro_flags = {}
for k,v in spro_flags_old.iteritems():
    spro_flags[v] = k.replace(' ','')
    
    
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
#--------------------------- above this are constants ------------------------#
#-----------------------------------------------------------------------------#


def get_flag_code(line):
    flag_code = ''''''
    spro_flag = int(line[1])
    if spro_flag==0:
        return '0'
    
    spro_flag_keys = spro_flags.keys()
    spro_flag_keys.sort()
    spro_flag_keys.reverse()
    for each_flag in spro_flag_keys:
        if spro_flag&each_flag==each_flag:
            flag_code += "|%s" %spro_flags[each_flag]
            spro_flag -= each_flag
        if spro_flag==0:
            return flag_code.replace('|','',1)
    else:
        return line[1]


def decompile():
    ofile = open(export_dir+"scene_props.txt",'r')
    tfile = open(export_dir+"decompiled files/module_scene_props.py",'w')
    idfile = open(export_dir+"decompiled files/ID_scene_props.py",'w')
    
    tfile.write('''# -*- coding: cp1252 -*-
from header_common import *
from header_scene_props import *
from header_operations import *
from header_triggers import *
from header_sounds import *
from module_constants import *
import string

####################################################################################################################
#  Each scene prop record contains the following fields:
#  1) Scene prop id: used for referencing scene props in other files. The prefix spr_ is automatically added before each scene prop id.
#  2) Scene prop flags. See header_scene_props.py for a list of available flags
#  3) Mesh name: Name of the mesh.
#  4) Physics object name:
#  5) Triggers: Simple triggers that are associated with the scene prop
####################################################################################################################

check_item_use_trigger = (ti_on_scene_prop_use,
    [
      (store_trigger_param_1, ":agent_id"),
      (store_trigger_param_2, ":instance_id"),
      
      #for only server itself-----------------------------------------------------------------------------------------------
      (call_script, "script_use_item", ":instance_id", ":agent_id"),
      #for only server itself-----------------------------------------------------------------------------------------------
      (get_max_players, ":num_players"),                               
      (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
        (player_is_active, ":player_no"),
        (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_use_item, ":instance_id", ":agent_id"),
      (try_end),
    ])

check_sally_door_use_trigger_double = (ti_on_scene_prop_use,
    [
      (store_trigger_param_1, ":agent_id"),
      (store_trigger_param_2, ":instance_id"),

      (agent_get_position, pos1, ":agent_id"),
      (prop_instance_get_starting_position, pos2, ":instance_id"),
      
      (scene_prop_get_slot, ":opened_or_closed", ":instance_id", scene_prop_open_or_close_slot),

      (try_begin),
        #out doors like castle sally door can be opened only from inside, if door coordinate is behind your coordinate. Also it can be closed from both sides.
        
        (prop_instance_get_scene_prop_kind, ":scene_prop_id", ":instance_id"),
        
        (assign, ":can_open_door", 0),
        (try_begin),
          (neg|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_right"),
          (neg|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_left"),
          (neg|eq, ":scene_prop_id", "spr_earth_sally_gate_right"),
          (neg|eq, ":scene_prop_id", "spr_earth_sally_gate_left"),
          
          (position_is_behind_position, pos1, pos2),
          (assign, ":can_open_door", 1),
        (else_try),  
          (this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_right"),
          (this_or_next|eq, ":scene_prop_id", "spr_viking_keep_destroy_sally_door_left"),
          (this_or_next|eq, ":scene_prop_id", "spr_earth_sally_gate_right"),
          (eq, ":scene_prop_id", "spr_earth_sally_gate_left"),

          (neg|position_is_behind_position, pos1, pos2),
          (assign, ":can_open_door", 1),
        (try_end),
        
        (this_or_next|eq, ":can_open_door", 1),
        (eq, ":opened_or_closed", 1),
      
        (try_begin),
          #for only server itself-----------------------------------------------------------------------------------------------
          (call_script, "script_use_item", ":instance_id", ":agent_id"),
          #for only server itself-----------------------------------------------------------------------------------------------
          (get_max_players, ":num_players"),                               
          (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
            (player_is_active, ":player_no"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_use_item, ":instance_id", ":agent_id"),
          (try_end),
        (try_end),
      (try_end),
    ])

check_sally_door_use_trigger = (ti_on_scene_prop_use,
    [
      (store_trigger_param_1, ":agent_id"),
      (store_trigger_param_2, ":instance_id"),

      (agent_get_position, pos1, ":agent_id"),
      (prop_instance_get_starting_position, pos2, ":instance_id"),
      
      (scene_prop_get_slot, ":opened_or_closed", ":instance_id", scene_prop_open_or_close_slot),

      (try_begin),
        #out doors like castle sally door can be opened only from inside, if door coordinate is behind your coordinate. Also it can be closed from both sides.
        (this_or_next|position_is_behind_position, pos1, pos2),
        (eq, ":opened_or_closed", 1),
      
        (try_begin),
          #for only server itself-----------------------------------------------------------------------------------------------
          (call_script, "script_use_item", ":instance_id", ":agent_id"),
          #for only server itself-----------------------------------------------------------------------------------------------
          (get_max_players, ":num_players"),                               
          (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
            (player_is_active, ":player_no"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_use_item, ":instance_id", ":agent_id"),
          (try_end),
        (try_end),
      (try_end),
    ])

check_castle_door_use_trigger = (ti_on_scene_prop_use,
    [
      (store_trigger_param_1, ":agent_id"),
      (store_trigger_param_2, ":instance_id"),

      (agent_get_position, pos1, ":agent_id"),
      (prop_instance_get_starting_position, pos2, ":instance_id"),
      
      (scene_prop_get_slot, ":opened_or_closed", ":instance_id", scene_prop_open_or_close_slot),

      (try_begin),
        (ge, ":agent_id", 0),
        (agent_get_team, ":agent_team", ":agent_id"),

        #in doors like castle room doors can be opened from both sides, but only defenders can open these doors. Also it can be closed from both sides.
        (this_or_next|eq, ":agent_team", 0),
        (eq, ":opened_or_closed", 1),
      
        (try_begin),
          #for only server itself-----------------------------------------------------------------------------------------------
          (call_script, "script_use_item", ":instance_id", ":agent_id"),
          #for only server itself-----------------------------------------------------------------------------------------------
          (get_max_players, ":num_players"),                               
          (try_for_range, ":player_no", 1, ":num_players"), #0 is server so starting from 1
            (player_is_active, ":player_no"),
            (multiplayer_send_2_int_to_player, ":player_no", multiplayer_event_use_item, ":instance_id", ":agent_id"),
          (try_end),
        (try_end),
      (try_end),
    ])

check_ladder_animate_trigger = (ti_on_scene_prop_is_animating,
    [      
      (store_trigger_param_1, ":instance_id"),
      (store_trigger_param_2, ":remaining_time"),

      (call_script, "script_check_creating_ladder_dust_effect", ":instance_id", ":remaining_time"),
      ])

check_ladder_animation_finish_trigger = (ti_on_scene_prop_animation_finished,
    [
      (store_trigger_param_1, ":instance_id"),

      (prop_instance_enable_physics, ":instance_id", 1),
      ])

''')
    
    tfile.write("scene_props = [\n")

    isTrigLine = 0
    id = 0
    for line in ofile:
        if 'spr_' in line:
            line = line.split()
            
            flag_code = get_flag_code(line)   # line[1]
            
            tfile.write('''  ("%s",%s,"%s","%s",\n    [''' %(line[0][4:],flag_code,line[3],line[4]))
            idfile.write("%s = %d\n" %(line[0],id))
            id += 1
            
            isTrigLine = int(line[5])
            if not isTrigLine:
                tfile.write('''\n    ]\n  ),\n''')
            continue
        
        if isTrigLine:
            line = line.split()
            
            timer = float(line[0])
            if timer in trigger_timers:
                timer = trigger_timers[timer]
            else:
                timer = line[0]
            tfile.write('''\n      (%s,\n%s,\n      ),''' %(timer,decompile_statement_block(' '.join(line[1:]))))
            
            isTrigLine -= 1
            if not isTrigLine:
                tfile.write('''\n    ]\n  ),\n''')
            continue
        
    tfile.write("]\n")
    tfile.close()
    idfile.close()
    ofile.close()
    
    
if __name__=='__main__':
    print "Decompiling scene props ..."
    decompile()