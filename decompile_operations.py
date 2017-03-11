#! /usr/bin/env python
#coding=utf-8

# decompile operations

from module_info import *
from header_operations import *

from decompiled_ID_global_variables import *
from decompiled_ID_quick_strings import *
from decompiled_ID_animations import *
from decompiled_ID_factions import *
from decompiled_ID_info_pages import *
from decompiled_ID_items import *
from decompiled_ID_map_icons import *
from decompiled_ID_menus import *
from decompiled_ID_meshes import *
from decompiled_ID_mission_templates import *
from decompiled_ID_music import *
from decompiled_ID_particle_systems import *
from decompiled_ID_parties import *
from decompiled_ID_party_templates import *
from decompiled_ID_postfx_params import *
from decompiled_ID_presentations import *
from decompiled_ID_quests import *
from decompiled_ID_scene_props import *
from decompiled_ID_scenes import *
from decompiled_ID_scripts import *
from decompiled_ID_skills import *
from decompiled_ID_sounds import *
from decompiled_ID_strings import *
from decompiled_ID_tableau_materials import *
from decompiled_ID_troops import *


operation_ids_old = {
    'neg                  ': 0x80000000,  # (neg|<operation_name>, ...),
    'this_or_next         ': 0x40000000,  # (this_or_next|<operation_name>, ...),
    'call_script                ':    1,  # (call_script, <script_id>, [<script_param>...]),
    'try_begin                  ':    4,  # (try_begin),
    'else_try                   ':    5,  # (else_try),
    'try_end                    ':    3,  # (try_end),
    'try_for_range              ':    6,  # (try_for_range, <destination>, <lower_bound>, <upper_bound>),
    'try_for_range_backwards    ':    7,  # (try_for_range_backwards, <destination>, <lower_bound>, <upper_bound>),
    'try_for_parties            ':   11,  # (try_for_parties, <destination>),
    'try_for_agents             ':   12,  # (try_for_agents, <destination>),
    'try_for_prop_instances     ':   16,  # (try_for_prop_instances, <destination>, [<scene_prop_id>]),
    'try_for_players            ':   17,  # (try_for_players, <destination>, [skip_server]),
    'gt                         ':   32,      # (gt, <value1>, <value2>),
    'ge                         ':   30,      # (ge, <value1>, <value2>),
    'eq                         ':   31,      # (eq, <value1>, <value2>),
    'is_between                 ':   33,      # (is_between, <value>, <lower_bound>, <upper_bound>),
    'assign                     ': 2133,    # (assign, <destination>, <value>),
    'store_add                  ': 2120,    # (store_add, <destination>, <value>, <value>),
    'store_sub                  ': 2121,    # (store_sub, <destination>, <value>, <value>),
    'store_mul                  ': 2122,    # (store_mul, <destination>, <value>, <value>),
    'store_div                  ': 2123,    # (store_div, <destination>, <value>, <value>),
    'store_mod                  ': 2119,    # (store_mod, <destination>, <value>, <value>),
    'val_add                    ': 2105,    # (val_add, <destination>, <value>),
    'val_sub                    ': 2106,    # (val_sub, <destination>, <value>),
    'val_mul                    ': 2107,    # (val_mul, <destination>, <value>),
    'val_div                    ': 2108,    # (val_div, <destination>, <value>),
    'val_mod                    ': 2109,    # (val_mod, <destination>, <value>),
    'val_min                    ': 2110,    # (val_min, <destination>, <value>),
    'val_max                    ': 2111,    # (val_max, <destination>, <value>),
    'val_clamp                  ': 2112,    # (val_clamp, <destination>, <lower_bound>, <upper_bound>),
    'val_abs                    ': 2113,    # (val_abs, <destination>),
    'store_or                   ': 2116,    # (store_or, <destination>, <value>, <value>),
    'store_and                  ': 2117,    # (store_and, <destination>, <value>, <value>),
    'val_or                     ': 2114,    # (val_or, <destination>, <value>),
    'val_and                    ': 2115,    # (val_and, <destination>, <value>),
    'val_lshift                 ': 2100,    # (val_lshift, <destination>, <value>),
    'val_rshift                 ': 2101,    # (val_rshift, <destination>, <value>),
    'store_sqrt                 ': 2125,    # (store_sqrt, <destination_fixed_point>, <value_fixed_point>),
    'store_pow                  ': 2126,    # (store_pow, <destination_fixed_point>, <value_fixed_point>, <power_fixed_point),
    'store_sin                  ': 2127,    # (store_sin, <destination_fixed_point>, <value_fixed_point>),
    'store_cos                  ': 2128,    # (store_cos, <destination_fixed_point>, <value_fixed_point>),
    'store_tan                  ': 2129,    # (store_tan, <destination_fixed_point>, <value_fixed_point>),
    'store_asin                 ': 2140,    # (store_asin, <destination_fixed_point>, <value_fixed_point>),
    'store_acos                 ': 2141,    # (store_acos, <destination_fixed_point>, <value_fixed_point>),
    'store_atan                 ': 2142,    # (store_atan, <destination_fixed_point>, <value_fixed_point>),
    'store_atan2                ': 2143,    # (store_atan2, <destination_fixed_point>, <y_fixed_point>, <x_fixed_point>),
    'store_random               ': 2135,    # (store_random, <destination>, <upper_range>),
    'store_random_in_range      ': 2136,    # (store_random_in_range, <destination>, <range_low>, <range_high>),
    'shuffle_range              ': 2134,    # (shuffle_range, <reg_no>, <reg_no>),
    'set_fixed_point_multiplier ': 2124,    # (set_fixed_point_multiplier, <value>),
    'convert_to_fixed_point     ': 2130,    # (convert_to_fixed_point, <destination_fixed_point>),
    'convert_from_fixed_point   ': 2131,    # (convert_from_fixed_point, <destination>),
    'store_script_param_1       ':   21,  # (store_script_param_1, <destination>),
    'store_script_param_2       ':   22,  # (store_script_param_2, <destination>),
    'store_script_param         ':   23,  # (store_script_param, <destination>, <script_param_index>),
    'set_result_string          ':   60,  # (set_result_string, <string>),
    'store_trigger_param_1      ': 2071,  # (store_trigger_param_1, <destination>),
    'store_trigger_param_2      ': 2072,  # (store_trigger_param_2, <destination>),
    'store_trigger_param_3      ': 2073,  # (store_trigger_param_3, <destination>),
    'store_trigger_param        ': 2070,  # (store_trigger_param, <destination>, <trigger_param_no>),
    'get_trigger_object_position':  702,  # (get_trigger_object_position, <position>),
    'set_trigger_result         ': 2075,  # (set_trigger_result, <value>),
    'key_is_down                ':   70,  # (key_is_down, <key_code>),
    'key_clicked                ':   71,  # (key_clicked, <key_code>),
    'game_key_is_down           ':   72,  # (game_key_is_down, <game_key_code>),
    'game_key_clicked           ':   73,  # (game_key_clicked, <game_key_code>),
    'omit_key_once              ':   77,  # (omit_key_once, <key_code>),
    'clear_omitted_keys         ':   78,  # (clear_omitted_keys),
    'mouse_get_position         ':   75,  # (mouse_get_position, <position>),
    'is_currently_night         ': 2273,  # (is_currently_night),
    'map_free                   ':   37,  # (map_free),
    'get_global_cloud_amount    ':   90,  # (get_global_cloud_amount, <destination>),
    'set_global_cloud_amount    ':   91,  # (set_global_cloud_amount, <value>),
    'get_global_haze_amount     ':   92,  # (get_global_haze_amount, <destination>),
    'set_global_haze_amount     ':   93,  # (set_global_haze_amount, <value>),
    'store_current_hours        ': 2270,  # (store_current_hours, <destination>),
    'store_time_of_day          ': 2271,  # (store_time_of_day, <destination>),
    'store_current_day          ': 2272,  # (store_current_day, <destination>),
    'rest_for_hours             ': 1030,  # (rest_for_hours, <rest_time_in_hours>, [time_speed_multiplier], [remain_attackable]),
    'rest_for_hours_interactive ': 1031,  # (rest_for_hours_interactive, <rest_time_in_hours>, [time_speed_multiplier], [remain_attackable]),
    'is_trial_version                     ':  250,  # (is_trial_version),
    'is_edit_mode_enabled                 ':  255,  # (is_edit_mode_enabled),
    'get_operation_set_version            ':   55,  # (get_operation_set_version, <destination>),
    'set_player_troop                     ':   47, # (set_player_troop, <troop_id>),
    'show_object_details_overlay          ':  960,  # (show_object_details_overlay, <value>),
    'auto_save                            ':  985,  # (auto_save),
    'options_get_damage_to_player         ':  260,  # (options_get_damage_to_player, <destination>),
    'options_set_damage_to_player         ':  261,  # (options_set_damage_to_player, <value>),
    'options_get_damage_to_friends        ':  262,  # (options_get_damage_to_friends, <destination>),
    'options_set_damage_to_friends        ':  263,  # (options_set_damage_to_friends, <value>),
    'options_get_combat_ai                ':  264,  # (options_get_combat_ai, <destination>),
    'options_set_combat_ai                ':  265,  # (options_set_combat_ai, <value>),
    'game_get_reduce_campaign_ai          ':  424,  # (game_get_reduce_campaign_ai, <destination>),
    'options_get_campaign_ai              ':  266,  # (options_get_campaign_ai, <destination>),
    'options_set_campaign_ai              ':  267,  # (options_set_campaign_ai, <value>),
    'options_get_combat_speed             ':  268,  # (options_get_combat_speed, <destination>),
    'options_set_combat_speed             ':  269,  # (options_set_combat_speed, <value>),
    'options_get_battle_size              ':  270,  # (options_get_battle_size, <destination>),
    'options_set_battle_size              ':  271,  # (options_set_battle_size, <value>),
    'get_average_game_difficulty          ':  990,  # (get_average_game_difficulty, <destination>),
    'get_achievement_stat                 ':  370,  # (get_achievement_stat, <destination>, <achievement_id>, <stat_index>),
    'set_achievement_stat                 ':  371,  # (set_achievement_stat, <achievement_id>, <stat_index>, <value>),
    'unlock_achievement                   ':  372,  # (unlock_achievement, <achievement_id>),
    'get_player_agent_kill_count          ': 1701,  # (get_player_agent_kill_count, <destination>, [get_wounded]),
    'get_player_agent_own_troop_kill_count': 1705,  # (get_player_agent_own_troop_kill_count, <destination>, [get_wounded]),
    'faction_set_slot               ':  502,  # (faction_set_slot, <faction_id>, <slot_no>, <value>),
    'faction_get_slot               ':  522,  # (faction_get_slot, <destination>, <faction_id>, <slot_no>),
    'faction_slot_eq                ':  542,  # (faction_slot_eq, <faction_id>, <slot_no>, <value>),
    'faction_slot_ge                ':  562,  # (faction_slot_ge, <faction_id>, <slot_no>, <value>),
    'set_relation                   ': 1270,  # (set_relation, <faction_id_1>, <faction_id_2>, <value>),
    'store_relation                 ': 2190,  # (store_relation, <destination>, <faction_id_1>, <faction_id_2>),
    'faction_set_name               ': 1275,  # (faction_set_name, <faction_id>, <string>),
    'faction_set_color              ': 1276,  # (faction_set_color, <faction_id>, <color_code>),
    'faction_get_color              ': 1277,  # (faction_get_color, <destination>, <faction_id>)
    'hero_can_join                        ':  101, # (hero_can_join, [party_id]),
    'hero_can_join_as_prisoner            ':  102, # (hero_can_join_as_prisoner, [party_id]),
    'party_can_join                       ':  103, # (party_can_join),
    'party_can_join_as_prisoner           ':  104, # (party_can_join_as_prisoner),
    'troops_can_join                      ':  105, # (troops_can_join, <value>),
    'troops_can_join_as_prisoner          ':  106, # (troops_can_join_as_prisoner, <value>),
    'party_can_join_party                 ':  107, # (party_can_join_party, <joiner_party_id>, <host_party_id>, [flip_prisoners]),
    'main_party_has_troop                 ':  110, # (main_party_has_troop, <troop_id>),
    'party_is_in_town                     ':  130, # (party_is_in_town, <party_id>, <town_party_id>),
    'party_is_in_any_town                 ':  131, # (party_is_in_any_town, <party_id>),
    'party_is_active                      ':  132, # (party_is_active, <party_id>),
    'party_template_set_slot              ':  504, # (party_template_set_slot, <party_template_id>, <slot_no>, <value>),
    'party_template_get_slot              ':  524, # (party_template_get_slot, <destination>, <party_template_id>, <slot_no>),
    'party_template_slot_eq               ':  544, # (party_template_slot_eq, <party_template_id>, <slot_no>, <value>),
    'party_template_slot_ge               ':  564, # (party_template_slot_ge, <party_template_id>, <slot_no>, <value>),
    'party_set_slot                       ':  501, # (party_set_slot, <party_id>, <slot_no>, <value>),
    'party_get_slot                       ':  521, # (party_get_slot, <destination>, <party_id>, <slot_no>),
    'party_slot_eq                        ':  541, # (party_slot_eq, <party_id>, <slot_no>, <value>),
    'party_slot_ge                        ':  561, # (party_slot_ge, <party_id>, <slot_no>, <value>),
    'set_party_creation_random_limits     ': 1080, # (set_party_creation_random_limits, <min_value>, <max_value>),
    'set_spawn_radius                     ': 1103, # (set_spawn_radius, <value>),
    'spawn_around_party                   ': 1100, # (spawn_around_party, <party_id>, <party_template_id>),
    'disable_party                        ': 1230, # (disable_party, <party_id>),
    'enable_party                         ': 1231, # (enable_party, <party_id>),
    'remove_party                         ': 1232, # (remove_party, <party_id>),
    'party_get_current_terrain            ': 1608, # (party_get_current_terrain, <destination>, <party_id>),
    'party_relocate_near_party            ': 1623, # (party_relocate_near_party, <relocated_party_id>, <target_party_id>, <spawn_radius>),
    'party_get_position                   ': 1625, # (party_get_position, <dest_position>, <party_id>),
    'party_set_position                   ': 1626, # (party_set_position, <party_id>, <position>),
    'set_camera_follow_party              ': 1021, # (set_camera_follow_party, <party_id>),
    'party_attach_to_party                ': 1660, # (party_attach_to_party, <party_id>, <party_id_to_attach_to>),
    'party_detach                         ': 1661, # (party_detach, <party_id>),
    'party_collect_attachments_to_party   ': 1662, # (party_collect_attachments_to_party, <source_party_id>, <collected_party_id>),
    'party_get_cur_town                   ': 1665, # (party_get_cur_town, <destination>, <party_id>),
    'party_get_attached_to                ': 1694, # (party_get_attached_to, <destination>, <party_id>),
    'party_get_num_attached_parties       ': 1695, # (party_get_num_attached_parties, <destination>, <party_id>),
    'party_get_attached_party_with_rank   ': 1696, # (party_get_attached_party_with_rank, <destination>, <party_id>, <attached_party_index>),
    'party_set_name                       ': 1669, # (party_set_name, <party_id>, <string>),
    'party_set_extra_text                 ': 1605, # (party_set_extra_text, <party_id>, <string>),
    'party_get_icon                       ': 1681, # (party_get_icon, <destination>, <party_id>),
    'party_set_icon                       ': 1676, # (party_set_icon, <party_id>, <map_icon_id>),
    'party_set_banner_icon                ': 1677, # (party_set_banner_icon, <party_id>, <map_icon_id>),
    'party_set_extra_icon                 ': 1682, # (party_set_extra_icon, <party_id>, <map_icon_id>, <vertical_offset_fixed_point>, <up_down_frequency_fixed_point>, <rotate_frequency_fixed_point>, <fade_in_out_frequency_fixed_point>),
    'party_add_particle_system            ': 1678, # (party_add_particle_system, <party_id>, <particle_system_id>),
    'party_clear_particle_systems         ': 1679, # (party_clear_particle_systems, <party_id>),
    'context_menu_add_item                ':  980, # (context_menu_add_item, <string_id>, <value>),
    'party_get_template_id                ': 1609, # (party_get_template_id, <destination>, <party_id>),
    'party_set_faction                    ': 1620, # (party_set_faction, <party_id>, <faction_id>),
    'store_faction_of_party               ': 2204, # (store_faction_of_party, <destination>, <party_id>),
    'store_random_party_in_range          ': 2254, # (store_random_party_in_range, <destination>, <lower_bound>, <upper_bound>),
    'store01_random_parties_in_range      ': 2255, # (store01_random_parties_in_range, <lower_bound>, <upper_bound>),
    'store_distance_to_party_from_party   ': 2281, # (store_distance_to_party_from_party, <destination>, <party_id>, <party_id>),
    'store_num_parties_of_template        ': 2310, # (store_num_parties_of_template, <destination>, <party_template_id>),
    'store_random_party_of_template       ': 2311, # (store_random_party_of_template, <destination>, <party_template_id>),
    'store_num_parties_created            ': 2300, # (store_num_parties_created, <destination>, <party_template_id>),
    'store_num_parties_destroyed          ': 2301, # (store_num_parties_destroyed, <destination>, <party_template_id>),
    'store_num_parties_destroyed_by_player': 2302, # (store_num_parties_destroyed_by_player, <destination>, <party_template_id>),
    'party_get_morale                     ': 1671, # (party_get_morale, <destination>, <party_id>),
    'party_set_morale                     ': 1672, # (party_set_morale, <party_id>, <value>),
    'party_join                           ': 1201, # (party_join),
    'party_join_as_prisoner               ': 1202, # (party_join_as_prisoner),
    'troop_join                           ': 1203, # (troop_join, <troop_id>),
    'troop_join_as_prisoner               ': 1204, # (troop_join_as_prisoner, <troop_id>),
    'add_companion_party                  ': 1233, # (add_companion_party, <troop_id_hero>),
    'party_add_members                    ': 1610, # (party_add_members, <party_id>, <troop_id>, <number>),
    'party_add_prisoners                  ': 1611, # (party_add_prisoners, <party_id>, <troop_id>, <number>),
    'party_add_leader                     ': 1612, # (party_add_leader, <party_id>, <troop_id>, [number]),
    'party_force_add_members              ': 1613, # (party_force_add_members, <party_id>, <troop_id>, <number>),
    'party_force_add_prisoners            ': 1614, # (party_force_add_prisoners, <party_id>, <troop_id>, <number>),
    'party_add_template                   ': 1675, # (party_add_template, <party_id>, <party_template_id>, [reverse_prisoner_status]),
    'distribute_party_among_party_group   ': 1698, # (distribute_party_among_party_group, <party_to_be_distributed>, <group_root_party>),
    'remove_member_from_party             ': 1210, # (remove_member_from_party, <troop_id>, [party_id]),
    'remove_regular_prisoners             ': 1211, # (remove_regular_prisoners, <party_id>),
    'remove_troops_from_companions        ': 1215, # (remove_troops_from_companions, <troop_id>, <value>),
    'remove_troops_from_prisoners         ': 1216, # (remove_troops_from_prisoners, <troop_id>, <value>),
    'party_remove_members                 ': 1615, # (party_remove_members, <party_id>, <troop_id>, <number>),
    'party_remove_prisoners               ': 1616, # (party_remove_members, <party_id>, <troop_id>, <number>),
    'party_clear                          ': 1617, # (party_clear, <party_id>),
    'add_gold_to_party                    ': 1070, # (add_gold_to_party, <value>, <party_id>),
    'party_get_num_companions             ': 1601, # (party_get_num_companions, <destination>, <party_id>),
    'party_get_num_prisoners              ': 1602, # (party_get_num_prisoners, <destination>, <party_id>),
    'party_count_members_of_type          ': 1630, # (party_count_members_of_type, <destination>, <party_id>, <troop_id>),
    'party_count_companions_of_type       ': 1631, # (party_count_companions_of_type, <destination>, <party_id>, <troop_id>),
    'party_count_prisoners_of_type        ': 1632, # (party_count_prisoners_of_type, <destination>, <party_id>, <troop_id>),
    'party_get_free_companions_capacity   ': 1633, # (party_get_free_companions_capacity, <destination>, <party_id>),
    'party_get_free_prisoners_capacity    ': 1634, # (party_get_free_prisoners_capacity, <destination>, <party_id>),
    'party_get_num_companion_stacks       ': 1650, # (party_get_num_companion_stacks, <destination>, <party_id>),
    'party_get_num_prisoner_stacks        ': 1651, # (party_get_num_prisoner_stacks, <destination>, <party_id>),
    'party_stack_get_troop_id             ': 1652, # (party_stack_get_troop_id, <destination>, <party_id>, <stack_no>),
    'party_stack_get_size                 ': 1653, # (party_stack_get_size, <destination>, <party_id>, <stack_no>),
    'party_stack_get_num_wounded          ': 1654, # (party_stack_get_num_wounded, <destination>, <party_id>, <stack_no>),
    'party_stack_get_troop_dna            ': 1655, # (party_stack_get_troop_dna, <destination>, <party_id>, <stack_no>),
    'party_prisoner_stack_get_troop_id    ': 1656, # (party_get_prisoner_stack_troop, <destination>, <party_id>, <stack_no>),
    'party_prisoner_stack_get_size        ': 1657, # (party_get_prisoner_stack_size, <destination>, <party_id>, <stack_no>),
    'party_prisoner_stack_get_troop_dna   ': 1658, # (party_prisoner_stack_get_troop_dna, <destination>, <party_id>, <stack_no>),
    'store_num_free_stacks                ': 2154, # (store_num_free_stacks, <destination>, <party_id>),
    'store_num_free_prisoner_stacks       ': 2155, # (store_num_free_prisoner_stacks, <destination>, <party_id>),
    'store_party_size                     ': 2156, # (store_party_size, <destination>,[party_id]),
    'store_party_size_wo_prisoners        ': 2157, # (store_party_size_wo_prisoners, <destination>, [party_id]),
    'store_troop_kind_count               ': 2158, # (store_troop_kind_count, <destination>, <troop_type_id>),
    'store_num_regular_prisoners          ': 2159, # (store_num_regular_prisoners, <destination>, <party_id>),
    'store_troop_count_companions         ': 2160, # (store_troop_count_companions, <destination>, <troop_id>, [party_id]),
    'store_troop_count_prisoners          ': 2161, # (store_troop_count_prisoners, <destination>, <troop_id>, [party_id]),
    'party_add_xp_to_stack                ': 1670, # (party_add_xp_to_stack, <party_id>, <stack_no>, <xp_amount>),
    'party_upgrade_with_xp                ': 1673, # (party_upgrade_with_xp, <party_id>, <xp_amount>, <upgrade_path>), #upgrade_path can be:
    'party_add_xp                         ': 1674, # (party_add_xp, <party_id>, <xp_amount>),
    'party_get_skill_level                ': 1685, # (party_get_skill_level, <destination>, <party_id>, <skill_no>),
    'heal_party                           ': 1225, # (heal_party, <party_id>),
    'party_wound_members                  ': 1618, # (party_wound_members, <party_id>, <troop_id>, <number>),
    'party_remove_members_wounded_first   ': 1619, # (party_remove_members_wounded_first, <party_id>, <troop_id>, <number>),
    'party_quick_attach_to_current_battle ': 1663, # (party_quick_attach_to_current_battle, <party_id>, <side>),
    'party_leave_cur_battle               ': 1666, # (party_leave_cur_battle, <party_id>),
    'party_set_next_battle_simulation_time': 1667, # (party_set_next_battle_simulation_time, <party_id>, <next_simulation_time_in_hours>),
    'party_get_battle_opponent            ': 1680, # (party_get_battle_opponent, <destination>, <party_id>)
    'inflict_casualties_to_party_group    ': 1697, # (inflict_casualties_to_party, <parent_party_id>, <damage_amount>, <party_id_to_add_causalties_to>), 
    'party_end_battle                     ':  108, # (party_end_battle, <party_no>),
    'party_set_marshall                   ': 1604, # (party_set_marshall, <party_id>, <value>),
    'party_set_flags                      ': 1603, # (party_set_flag, <party_id>, <flag>, <clear_or_set>),
    'party_set_aggressiveness             ': 1606, # (party_set_aggressiveness, <party_id>, <number>),
    'party_set_courage                    ': 1607, # (party_set_courage, <party_id>, <number>),
    'party_get_ai_initiative              ': 1638, # (party_get_ai_initiative, <destination>, <party_id>),
    'party_set_ai_initiative              ': 1639, # (party_set_ai_initiative, <party_id>, <value>),
    'party_set_ai_behavior                ': 1640, # (party_set_ai_behavior, <party_id>, <ai_bhvr>),
    'party_set_ai_object                  ': 1641, # (party_set_ai_object, <party_id>, <object_party_id>),
    'party_set_ai_target_position         ': 1642, # (party_set_ai_target_position, <party_id>, <position>),
    'party_set_ai_patrol_radius           ': 1643, # (party_set_ai_patrol_radius, <party_id>, <radius_in_km>),
    'party_ignore_player                  ': 1644, # (party_ignore_player, <party_id>, <duration_in_hours>),
    'party_set_bandit_attraction          ': 1645, # (party_set_bandit_attraction, <party_id>, <attaraction>),
    'party_get_helpfulness                ': 1646, # (party_get_helpfulness, <destination>, <party_id>),
    'party_set_helpfulness                ': 1647, # (party_set_helpfulness, <party_id>, <number>),
    'get_party_ai_behavior                ': 2290, # (get_party_ai_behavior, <destination>, <party_id>),
    'get_party_ai_object                  ': 2291, # (get_party_ai_object, <destination>, <party_id>),
    'party_get_ai_target_position         ': 2292, # (party_get_ai_target_position, <position>, <party_id>),
    'get_party_ai_current_behavior        ': 2293, # (get_party_ai_current_behavior, <destination>, <party_id>),
    'get_party_ai_current_object          ': 2294, # (get_party_ai_current_object, <destination>, <party_id>),
    'party_set_ignore_with_player_party   ': 1648, # (party_set_ignore_with_player_party, <party_id>, <value>),
    'party_get_ignore_with_player_party   ': 1649, # (party_get_ignore_with_player_party, <party_id>),
    'troop_has_item_equipped                 ':  151, # (troop_has_item_equipped, <troop_id>, <item_id>),
    'troop_is_mounted                        ':  152, # (troop_is_mounted, <troop_id>),
    'troop_is_guarantee_ranged               ':  153, # (troop_is_guarantee_ranged, <troop_id>),
    'troop_is_guarantee_horse                ':  154, # (troop_is_guarantee_horse, <troop_id>),
    'troop_is_hero                           ': 1507, # (troop_is_hero, <troop_id>),
    'troop_is_wounded                        ': 1508, # (troop_is_wounded, <troop_id>),
    'player_has_item                         ':  150, # (player_has_item, <item_id>),
    'troop_set_slot                          ':  500, # (troop_set_slot, <troop_id>, <slot_no>, <value>),
    'troop_get_slot                          ':  520, # (troop_get_slot, <destination>, <troop_id>, <slot_no>),
    'troop_slot_eq                           ':  540, # (troop_slot_eq, <troop_id>, <slot_no>, <value>),
    'troop_slot_ge                           ':  560, # (troop_slot_ge, <troop_id>, <slot_no>, <value>),
    'troop_set_type                          ': 1505, # (troop_set_type, <troop_id>, <gender>),
    'troop_get_type                          ': 1506, # (troop_get_type, <destination>, <troop_id>),
    'troop_set_class                         ': 1517, # (troop_set_class, <troop_id>, <value>),
    'troop_get_class                         ': 1516, # (troop_get_class, <destination>, <troop_id>),
    'class_set_name                          ': 1837, # (class_set_name, <sub_class>, <string_id>),
    'add_xp_to_troop                         ': 1062, # (add_xp_to_troop, <value>, [troop_id]),
    'add_xp_as_reward                        ': 1064, # (add_xp_as_reward, <value>),
    'troop_get_xp                            ': 1515, # (troop_get_xp, <destination>, <troop_id>),
    'store_attribute_level                   ': 2172, # (store_attribute_level, <destination>, <troop_id>, <attribute_id>),
    'troop_raise_attribute                   ': 1520, # (troop_raise_attribute, <troop_id>, <attribute_id>, <value>),
    'store_skill_level                       ': 2170, # (store_skill_level, <destination>, <skill_id>, [troop_id]),
    'troop_raise_skill                       ': 1521, # (troop_raise_skill, <troop_id>, <skill_id>, <value>),
    'store_proficiency_level                 ': 2176, # (store_proficiency_level, <destination>, <troop_id>, <attribute_id>),
    'troop_raise_proficiency                 ': 1522, # (troop_raise_proficiency, <troop_id>, <proficiency_no>, <value>),
    'troop_raise_proficiency_linear          ': 1523, # (troop_raise_proficiency, <troop_id>, <proficiency_no>, <value>),
    'troop_add_proficiency_points            ': 1525, # (troop_add_proficiency_points, <troop_id>, <value>),                    
    'store_troop_health                      ': 2175, # (store_troop_health, <destination>, <troop_id>, [absolute]), # set absolute to 1 to get actual health; otherwise this will return percentage health in range (0-100)
    'troop_set_health                        ': 1560, # (troop_set_health, <troop_id>, <relative health (0-100)>),
    'troop_get_upgrade_troop                 ': 1561, # (troop_get_upgrade_troop, <destination>, <troop_id>, <upgrade_path>),
    'store_character_level                   ': 2171, # (store_character_level, <destination>, [troop_id]),
    'get_level_boundary                      ':  991, # (get_level_boundary, <destination>, <level_no>),
    'add_gold_as_xp                          ': 1063, # (add_gold_as_xp, <value>, [troop_id]),, # Default troop is player
    'troop_set_auto_equip                    ': 1509, # (troop_set_auto_equip, <troop_id>, <value>),
    'troop_ensure_inventory_space            ': 1510, # (troop_ensure_inventory_space, <troop_id>, <value>),
    'troop_sort_inventory                    ': 1511, # (troop_sort_inventory, <troop_id>),
    'troop_add_item                          ': 1530, # (troop_add_item, <troop_id>, <item_id>, [modifier]),
    'troop_remove_item                       ': 1531, # (troop_remove_item, <troop_id>, <item_id>),
    'troop_clear_inventory                   ': 1532, # (troop_clear_inventory, <troop_id>),
    'troop_equip_items                       ': 1533, # (troop_equip_items, <troop_id>),
    'troop_inventory_slot_set_item_amount    ': 1534, # (troop_inventory_slot_set_item_amount, <troop_id>, <inventory_slot_no>, <value>),
    'troop_inventory_slot_get_item_amount    ': 1537, # (troop_inventory_slot_get_item_amount, <destination>, <troop_id>, <inventory_slot_no>),
    'troop_inventory_slot_get_item_max_amount': 1538, # (troop_inventory_slot_get_item_max_amount, <destination>, <troop_id>, <inventory_slot_no>),
    'troop_add_items                         ': 1535, # (troop_add_items, <troop_id>, <item_id>, <number>),
    'troop_remove_items                      ': 1536, # (troop_remove_items, <troop_id>, <item_id>, <number>),
    'troop_loot_troop                        ': 1539, # (troop_loot_troop, <target_troop>, <source_troop_id>, <probability>), 
    'troop_get_inventory_capacity            ': 1540, # (troop_get_inventory_capacity, <destination>, <troop_id>),
    'troop_get_inventory_slot                ': 1541, # (troop_get_inventory_slot, <destination>, <troop_id>, <inventory_slot_no>),
    'troop_get_inventory_slot_modifier       ': 1542, # (troop_get_inventory_slot_modifier, <destination>, <troop_id>, <inventory_slot_no>),
    'troop_set_inventory_slot                ': 1543, # (troop_set_inventory_slot, <troop_id>, <inventory_slot_no>, <item_id>),
    'troop_set_inventory_slot_modifier       ': 1544, # (troop_set_inventory_slot_modifier, <troop_id>, <inventory_slot_no>, <imod_value>),
    'store_item_kind_count                   ': 2165, # (store_item_kind_count, <destination>, <item_id>, [troop_id]),
    'store_free_inventory_capacity           ': 2167, # (store_free_inventory_capacity, <destination>, [troop_id]),
    'reset_price_rates                  ': 1170, # (reset_price_rates),
    'set_price_rate_for_item            ': 1171, # (set_price_rate_for_item, <item_id>, <value_percentage>),
    'set_price_rate_for_item_type       ': 1172, # (set_price_rate_for_item_type, <item_type_id>, <value_percentage>),
    'set_merchandise_modifier_quality   ': 1490, # (set_merchandise_modifier_quality, <value>),
    'set_merchandise_max_value          ': 1491, # (set_merchandise_max_value, <value>),
    'reset_item_probabilities           ': 1492, # (reset_item_probabilities, <value>),
    'set_item_probability_in_merchandise': 1493, # (set_item_probability_in_merchandise, <item_id>, <value>),
    'troop_add_merchandise              ': 1512, # (troop_add_merchandise, <troop_id>, <item_type_id>, <value>),
    'troop_add_merchandise_with_faction ': 1513, # (troop_add_merchandise_with_faction, <troop_id>, <faction_id>, <item_type_id>, <value>), #faction_id is given to check if troop is eligible to produce that item
    'troop_set_name                          ': 1501, # (troop_set_name, <troop_id>, <string_no>),
    'troop_set_plural_name                   ': 1502, # (troop_set_plural_name, <troop_id>, <string_no>),
    'troop_set_face_key_from_current_profile ': 1503, # (troop_set_face_key_from_current_profile, <troop_id>),
    'troop_add_gold                          ': 1528, # (troop_add_gold, <troop_id>, <value>),
    'troop_remove_gold                       ': 1529, # (troop_remove_gold, <troop_id>, <value>),
    'store_troop_gold                        ': 2149, # (store_troop_gold, <destination>, <troop_id>),
    'troop_set_faction                       ': 1550, # (troop_set_faction, <troop_id>, <faction_id>),
    'store_troop_faction                     ': 2173, # (store_troop_faction, <destination>, <troop_id>),
    'store_faction_of_troop                  ': 2173, # (store_troop_faction, <destination>, <troop_id>),
    'troop_set_age                           ': 1555, # (troop_set_age, <troop_id>, <age_slider_pos>),
    'store_troop_value                       ': 2231, # (store_troop_value, <destination>, <troop_id>),
    'str_store_player_face_keys              ': 2747, # (str_store_player_face_keys, <string_no>, <player_id>),
    'player_set_face_keys                    ': 2748, # (player_set_face_keys, <player_id>, <string_no>),
    'str_store_troop_face_keys               ': 2750, # (str_store_troop_face_keys, <string_no>, <troop_no>, [<alt>]),
    'troop_set_face_keys                     ': 2751, # (troop_set_face_keys, <troop_no>, <string_no>, [<alt>]),
    'face_keys_get_hair                      ': 2752, # (face_keys_get_hair, <destination>, <string_no>),
    'face_keys_set_hair                      ': 2753, # (face_keys_set_hair, <string_no>, <value>),
    'face_keys_get_beard                     ': 2754, # (face_keys_get_beard, <destination>, <string_no>),
    'face_keys_set_beard                     ': 2755, # (face_keys_set_beard, <string_no>, <value>),
    'face_keys_get_face_texture              ': 2756, # (face_keys_get_face_texture, <destination>, <string_no>),
    'face_keys_set_face_texture              ': 2757, # (face_keys_set_face_texture, <string_no>, <value>),
    'face_keys_get_hair_texture              ': 2758, # (face_keys_get_hair_texture, <destination>, <string_no>),
    'face_keys_set_hair_texture              ': 2759, # (face_keys_set_hair_texture, <string_no>, <value>),
    'face_keys_get_hair_color                ': 2760, # (face_keys_get_hair_color, <destination>, <string_no>),
    'face_keys_set_hair_color                ': 2761, # (face_keys_set_hair_color, <string_no>, <value>),
    'face_keys_get_age                       ': 2762, # (face_keys_get_age, <destination>, <string_no>),
    'face_keys_set_age                       ': 2763, # (face_keys_set_age, <string_no>, <value>),
    'face_keys_get_skin_color                ': 2764, # (face_keys_get_skin_color, <destination>, <string_no>),
    'face_keys_set_skin_color                ': 2765, # (face_keys_set_skin_color, <string_no>, <value>),
    'face_keys_get_morph_key                 ': 2766, # (face_keys_get_morph_key, <destination>, <string_no>, <key_no>),
    'face_keys_set_morph_key                 ': 2767, # (face_keys_set_morph_key, <string_no>, <key_no>, <value>),
    'check_quest_active           ':  200, # (check_quest_active, <quest_id>),
    'check_quest_finished         ':  201, # (check_quest_finished, <quest_id>),
    'check_quest_succeeded        ':  202, # (check_quest_succeeded, <quest_id>),
    'check_quest_failed           ':  203, # (check_quest_failed, <quest_id>),
    'check_quest_concluded        ':  204, # (check_quest_concluded, <quest_id>),
    'quest_set_slot               ':  506, # (quest_set_slot, <quest_id>, <slot_no>, <value>),
    'quest_get_slot               ':  526, # (quest_get_slot, <destination>, <quest_id>, <slot_no>),
    'quest_slot_eq                ':  546, # (quest_slot_eq, <quest_id>, <slot_no>, <value>),
    'quest_slot_ge                ':  566, # (quest_slot_ge, <quest_id>, <slot_no>, <value>),
    'start_quest                  ': 1280, # (start_quest, <quest_id>, <giver_troop_id>),
    'conclude_quest               ': 1286, # (conclude_quest, <quest_id>),
    'succeed_quest                ': 1282, # (succeed_quest, <quest_id>), #also concludes the quest
    'fail_quest                   ': 1283, # (fail_quest, <quest_id>), #also concludes the quest
    'complete_quest               ': 1281, # (complete_quest, <quest_id>),
    'cancel_quest                 ': 1284, # (cancel_quest, <quest_id>),
    'setup_quest_text             ': 1290, # (setup_quest_text, <quest_id>),
    'store_partner_quest          ': 2240, # (store_partner_quest, <destination>),
    'setup_quest_giver            ': 1291, # (setup_quest_giver, <quest_id>, <string_id>),
    'store_random_quest_in_range  ': 2250, # (store_random_quest_in_range, <destination>, <lower_bound>, <upper_bound>),
    'set_quest_progression        ': 1285, # (set_quest_progression, <quest_id>, <value>),
    'store_random_troop_to_raise  ': 2251, # (store_random_troop_to_raise, <destination>, <lower_bound>, <upper_bound>),
    'store_random_troop_to_capture': 2252, # (store_random_troop_to_capture, <destination>, <lower_bound>, <upper_bound>),
    'store_quest_number           ': 2261, # (store_quest_number, <destination>, <quest_id>),
    'store_quest_item             ': 2262, # (store_quest_item, <destination>, <item_id>),
    'store_quest_troop            ': 2263, # (store_quest_troop, <destination>, <troop_id>),
    'item_has_property                  ': 2723, # (item_has_property, <item_kind_no>, <property>),
    'item_has_capability                ': 2724, # (item_has_capability, <item_kind_no>, <capability>),
    'item_has_modifier                  ': 2725, # (item_has_modifier, <item_kind_no>, <item_modifier_no>),
    'item_has_faction                   ': 2726, # (item_has_faction, <item_kind_no>, <faction_no>),
    'item_set_slot                      ':  507, # (item_set_slot, <item_id>, <slot_no>, <value>),
    'item_get_slot                      ':  527, # (item_get_slot, <destination>, <item_id>, <slot_no>),
    'item_slot_eq                       ':  547, # (item_slot_eq, <item_id>, <slot_no>, <value>),
    'item_slot_ge                       ':  567, # (item_slot_ge, <item_id>, <slot_no>, <value>),
    'item_get_type                      ': 1570, # (item_get_type, <destination>, <item_id>),
    'store_item_value                   ': 2230, # (store_item_value, <destination>, <item_id>),
    'store_random_horse                 ': 2257, # (store_random_horse, <destination>),
    'store_random_equipment             ': 2258, # (store_random_equipment, <destination>),
    'store_random_armor                 ': 2259, # (store_random_armor, <destination>),
    'cur_item_add_mesh                  ': 1964, # (cur_item_add_mesh, <mesh_name_string>, [<lod_begin>], [<lod_end>]),
    'cur_item_set_material              ': 1978, # (cur_item_set_material, <string_no>, <sub_mesh_no>, [<lod_begin>], [<lod_end>]),
    'item_get_weight                    ': 2700, # (item_get_weight, <destination_fixed_point>, <item_kind_no>),
    'item_get_value                     ': 2701, # (item_get_value, <destination>, <item_kind_no>),
    'item_get_difficulty                ': 2702, # (item_get_difficulty, <destination>, <item_kind_no>),
    'item_get_head_armor                ': 2703, # (item_get_head_armor, <destination>, <item_kind_no>),
    'item_get_body_armor                ': 2704, # (item_get_body_armor, <destination>, <item_kind_no>),
    'item_get_leg_armor                 ': 2705, # (item_get_leg_armor, <destination>, <item_kind_no>),
    'item_get_hit_points                ': 2706, # (item_get_hit_points, <destination>, <item_kind_no>),
    'item_get_weapon_length             ': 2707, # (item_get_weapon_length, <destination>, <item_kind_no>),
    'item_get_speed_rating              ': 2708, # (item_get_speed_rating, <destination>, <item_kind_no>),
    'item_get_missile_speed             ': 2709, # (item_get_missile_speed, <destination>, <item_kind_no>),
    'item_get_max_ammo                  ': 2710, # (item_get_max_ammo, <destination>, <item_kind_no>),
    'item_get_accuracy                  ': 2711, # (item_get_accuracy, <destination>, <item_kind_no>),
    'item_get_shield_height             ': 2712, # (item_get_shield_height, <destination_fixed_point>, <item_kind_no>),
    'item_get_horse_scale               ': 2713, # (item_get_horse_scale, <destination_fixed_point>, <item_kind_no>),
    'item_get_horse_speed               ': 2714, # (item_get_horse_speed, <destination>, <item_kind_no>),
    'item_get_horse_maneuver            ': 2715, # (item_get_horse_maneuver, <destination>, <item_kind_no>),
    'item_get_food_quality              ': 2716, # (item_get_food_quality, <destination>, <item_kind_no>),
    'item_get_abundance                 ': 2717, # (item_get_abundance, <destination>, <item_kind_no>),
    'item_get_thrust_damage             ': 2718, # (item_get_thrust_damage, <destination>, <item_kind_no>),
    'item_get_thrust_damage_type        ': 2719, # (item_get_thrust_damage_type, <destination>, <item_kind_no>),
    'item_get_swing_damage              ': 2720, # (item_get_swing_damage, <destination>, <item_kind_no>),
    'item_get_swing_damage_type         ': 2721, # (item_get_swing_damage_type, <destination>, <item_kind_no>),
    'item_get_horse_charge_damage       ': 2722, # (item_get_horse_charge_damage, <destination>, <item_kind_no>),
    'play_sound_at_position             ':  599, # (play_sound_at_position, <sound_id>, <position>, [options]),
    'play_sound                         ':  600, # (play_sound, <sound_id>, [options]),
    'play_track                         ':  601, # (play_track, <track_id>, [options]),
    'play_cue_track                     ':  602, # (play_cue_track, <track_id>),
    'music_set_situation                ':  603, # (music_set_situation, <situation_type>),
    'music_set_culture                  ':  604, # (music_set_culture, <culture_type>),
    'stop_all_sounds                    ':  609, # (stop_all_sounds, [options]), 
    'store_last_sound_channel           ':  615, # (store_last_sound_channel, <destination>),
    'stop_sound_channel                 ':  616, # (stop_sound_channel, <sound_channel_no>),
    'init_position                              ':  701, # (init_position, <position>),
    'copy_position                              ':  700, # (copy_position, <position_target>, <position_source>),
    'position_copy_origin                       ':  719, # (position_copy_origin, <position_target>, <position_source>),
    'position_copy_rotation                     ':  718, # (position_copy_rotation, <position_target>, <position_source>),
    'position_transform_position_to_parent      ':  716, # (position_transform_position_to_parent, <position_dest>, <position_anchor>, <position_relative_to_anchor>),
    'position_transform_position_to_local       ':  717, # (position_transform_position_to_local, <position_dest>, <position_anchor>, <position_source>),
    'position_get_x                             ':  726, # (position_get_x, <destination_fixed_point>, <position>),
    'position_get_y                             ':  727, # (position_get_y, <destination_fixed_point>, <position>),
    'position_get_z                             ':  728, # (position_get_z, <destination_fixed_point>, <position>),
    'position_set_x                             ':  729, # (position_set_x, <position>, <value_fixed_point>),
    'position_set_y                             ':  730, # (position_set_y, <position>, <value_fixed_point>),
    'position_set_z                             ':  731, # (position_set_z, <position>, <value_fixed_point>),
    'position_move_x                            ':  720, # (position_move_x, <position>, <movement>, [value]),
    'position_move_y                            ':  721, # (position_move_y, <position>, <movement>,[value]),
    'position_move_z                            ':  722, # (position_move_z, <position>, <movement>,[value]),
    'position_set_z_to_ground_level             ':  791, # (position_set_z_to_ground_level, <position>),
    'position_get_distance_to_terrain           ':  792, # (position_get_distance_to_terrain, <destination>, <position>),
    'position_get_distance_to_ground_level      ':  793, # (position_get_distance_to_ground_level, <destination>, <position>),
    'position_get_rotation_around_x             ':  742, # (position_get_rotation_around_x, <destination>, <position>),
    'position_get_rotation_around_y             ':  743, # (position_get_rotation_around_y, <destination>, <position>),
    'position_get_rotation_around_z             ':  740, # (position_get_rotation_around_z, <destination>, <position>),
    'position_rotate_x                          ':  723, # (position_rotate_x, <position>, <angle>),
    'position_rotate_y                          ':  724, # (position_rotate_y, <position>, <angle>),
    'position_rotate_z                          ':  725, # (position_rotate_z, <position>, <angle>, [use_global_z_axis]),
    'position_rotate_x_floating                 ':  738, # (position_rotate_x_floating, <position>, <angle_fixed_point>),
    'position_rotate_y_floating                 ':  739, # (position_rotate_y_floating, <position>, <angle_fixed_point>),
    'position_rotate_z_floating                 ':  734, # (position_rotate_z_floating, <position_no>, <angle_fixed_point>),
    'position_get_scale_x                       ':  735, # (position_get_scale_x, <destination_fixed_point>, <position>),
    'position_get_scale_y                       ':  736, # (position_get_scale_y, <destination_fixed_point>, <position>),
    'position_get_scale_z                       ':  737, # (position_get_scale_z, <destination_fixed_point>, <position>),
    'position_set_scale_x                       ':  744, # (position_set_scale_x, <position>, <value_fixed_point>),
    'position_set_scale_y                       ':  745, # (position_set_scale_y, <position>, <value_fixed_point>),
    'position_set_scale_z                       ':  746, # (position_set_scale_z, <position>, <value_fixed_point>),
    'get_angle_between_positions                ':  705, # (get_angle_between_positions, <destination_fixed_point>, <position_no_1>, <position_no_2>),
    'position_has_line_of_sight_to_position     ':  707, # (position_has_line_of_sight_to_position, <position_no_1>, <position_no_2>),
    'get_distance_between_positions             ':  710, # (get_distance_between_positions, <destination>, <position_no_1>, <position_no_2>),
    'get_distance_between_positions_in_meters   ':  711, # (get_distance_between_positions_in_meters, <destination>, <position_no_1>, <position_no_2>),
    'get_sq_distance_between_positions          ':  712, # (get_sq_distance_between_positions, <destination>, <position_no_1>, <position_no_2>),
    'get_sq_distance_between_positions_in_meters':  713, # (get_sq_distance_between_positions_in_meters, <destination>, <position_no_1>, <position_no_2>),
    'position_is_behind_position                ':  714, # (position_is_behind_position, <position_base>, <position_to_check>),
    'get_sq_distance_between_position_heights   ':  715, # (get_sq_distance_between_position_heights, <destination>, <position_no_1>, <position_no_2>),
    'position_normalize_origin                  ':  741, # (position_normalize_origin, <destination_fixed_point>, <position>),
    'position_get_screen_projection             ':  750, # (position_get_screen_projection, <position_screen>, <position_world>),
    'map_get_random_position_around_position    ': 1627, # (map_get_random_position_around_position, <dest_position_no>, <source_position_no>, <radius>),
    'map_get_land_position_around_position      ': 1628, # (map_get_land_position_around_position, <dest_position_no>, <source_position_no>, <radius>),
    'map_get_water_position_around_position     ': 1629, # (map_get_water_position_around_position, <dest_position_no>, <source_position_no>, <radius>),
    'troop_set_note_available       ': 1095, # (troop_set_note_available, <troop_id>, <value>),
    'add_troop_note_tableau_mesh    ': 1108, # (add_troop_note_tableau_mesh, <troop_id>, <tableau_material_id>),
    'add_troop_note_from_dialog     ': 1114, # (add_troop_note_from_dialog, <troop_id>, <note_slot_no>, <expires_with_time>),
    'add_troop_note_from_sreg       ': 1117, # (add_troop_note_from_sreg, <troop_id>, <note_slot_no>, <string_id>, <expires_with_time>),
    'faction_set_note_available     ': 1096, # (faction_set_note_available, <faction_id>, <value>),, #1': available, 0': not available
    'add_faction_note_tableau_mesh  ': 1109, # (add_faction_note_tableau_mesh, <faction_id>, <tableau_material_id>),
    'add_faction_note_from_dialog   ': 1115, # (add_faction_note_from_dialog, <faction_id>, <note_slot_no>, <expires_with_time>),
    'add_faction_note_from_sreg     ': 1118, # (add_faction_note_from_sreg, <faction_id>, <note_slot_no>, <string_id>, <expires_with_time>),
    'party_set_note_available       ': 1097, # (party_set_note_available, <party_id>, <value>),, #1': available, 0': not available
    'add_party_note_tableau_mesh    ': 1110, # (add_party_note_tableau_mesh, <party_id>, <tableau_material_id>),
    'add_party_note_from_dialog     ': 1116, # (add_party_note_from_dialog, <party_id>, <note_slot_no>, <expires_with_time>),
    'add_party_note_from_sreg       ': 1119, # (add_party_note_from_sreg, <party_id>, <note_slot_no>, <string_id>, <expires_with_time>),
    'quest_set_note_available       ': 1098, # (quest_set_note_available, <quest_id>, <value>),, #1': available, 0': not available
    'add_quest_note_tableau_mesh    ': 1111, # (add_quest_note_tableau_mesh, <quest_id>, <tableau_material_id>),
    'add_quest_note_from_dialog     ': 1112, # (add_quest_note_from_dialog, <quest_id>, <note_slot_no>, <expires_with_time>),
    'add_quest_note_from_sreg       ': 1113, # (add_quest_note_from_sreg, <quest_id>, <note_slot_no>, <string_id>, <expires_with_time>),
    'add_info_page_note_tableau_mesh': 1090, # (add_info_page_note_tableau_mesh, <info_page_id>, <tableau_material_id>),
    'add_info_page_note_from_dialog ': 1091, # (add_info_page_note_from_dialog, <info_page_id>, <note_slot_no>, <expires_with_time>),
    'add_info_page_note_from_sreg   ': 1092, # (add_info_page_note_from_sreg, <info_page_id>, <note_slot_no>, <string_id>, <expires_with_time>),
    'cur_item_set_tableau_material                   ': 1981, # (cur_item_set_tableu_material, <tableau_material_id>, <instance_code>),
    'cur_scene_prop_set_tableau_material             ': 1982, # (cur_scene_prop_set_tableau_material, <tableau_material_id>, <instance_code>),
    'cur_map_icon_set_tableau_material               ': 1983, # (cur_map_icon_set_tableau_material, <tableau_material_id>, <instance_code>),
    'cur_agent_set_banner_tableau_material           ': 1986, # (cur_agent_set_banner_tableau_material, <tableau_material_id>)
    'cur_tableau_add_tableau_mesh                    ': 1980, # (cur_tableau_add_tableau_mesh, <tableau_material_id>, <value>, <position_register_no>),
    'cur_tableau_render_as_alpha_mask                ': 1984, # (cur_tableau_render_as_alpha_mask)
    'cur_tableau_set_background_color                ': 1985, # (cur_tableau_set_background_color, <value>),
    'cur_tableau_set_ambient_light                   ': 1987, # (cur_tableau_set_ambient_light, <red_fixed_point>, <green_fixed_point>, <blue_fixed_point>),
    'cur_tableau_set_camera_position                 ': 1988, # (cur_tableau_set_camera_position, <position>),
    'cur_tableau_set_camera_parameters               ': 1989, # (cur_tableau_set_camera_parameters, <is_perspective>, <camera_width_times_1000>, <camera_height_times_1000>, <camera_near_times_1000>, <camera_far_times_1000>),
    'cur_tableau_add_point_light                     ': 1990, # (cur_tableau_add_point_light, <position>, <red_fixed_point>, <green_fixed_point>, <blue_fixed_point>),
    'cur_tableau_add_sun_light                       ': 1991, # (cur_tableau_add_sun_light, <position>, <red_fixed_point>, <green_fixed_point>, <blue_fixed_point>),
    'cur_tableau_add_mesh                            ': 1992, # (cur_tableau_add_mesh, <mesh_id>, <position>, <value_fixed_point>, <value_fixed_point>),
    'cur_tableau_add_mesh_with_vertex_color          ': 1993, # (cur_tableau_add_mesh_with_vertex_color, <mesh_id>, <position>, <value_fixed_point>, <value_fixed_point>, <value>),
    'cur_tableau_add_mesh_with_scale_and_vertex_color': 2000, # (cur_tableau_add_mesh_with_scale_and_vertex_color, <mesh_id>, <position>, <scale_position>, <value_fixed_point>, <value>),
    'cur_tableau_add_map_icon                        ': 1994, # (cur_tableau_add_map_icon, <map_icon_id>, <position>, <value_fixed_point>),
    'cur_tableau_add_troop                           ': 1995, # (cur_tableau_add_troop, <troop_id>, <position>, <animation_id>, <instance_no>),
    'cur_tableau_add_horse                           ': 1996, # (cur_tableau_add_horse, <item_id>, <position>, <animation_id>),
    'cur_tableau_set_override_flags                  ': 1997, # (cur_tableau_set_override_flags, <value>),
    'cur_tableau_clear_override_items                ': 1998, # (cur_tableau_clear_override_items),
    'cur_tableau_add_override_item                   ': 1999, # (cur_tableau_add_override_item, <item_kind_id>),
    'str_is_empty                   ': 2318, # (str_is_empty, <string_register>),
    'str_clear                      ': 2319, # (str_clear, <string_register>)
    'str_store_string               ': 2320, # (str_store_string, <string_register>, <string_id>),
    'str_store_string_reg           ': 2321, # (str_store_string, <string_register>, <string_no>),
    'str_store_troop_name           ': 2322, # (str_store_troop_name, <string_register>, <troop_id>),
    'str_store_troop_name_plural    ': 2323, # (str_store_troop_name_plural, <string_register>, <troop_id>),
    'str_store_troop_name_by_count  ': 2324, # (str_store_troop_name_by_count, <string_register>, <troop_id>, <number>),
    'str_store_item_name            ': 2325, # (str_store_item_name, <string_register>, <item_id>),
    'str_store_item_name_plural     ': 2326, # (str_store_item_name_plural, <string_register>, <item_id>),
    'str_store_item_name_by_count   ': 2327, # (str_store_item_name_by_count, <string_register>, <item_id>),
    'str_store_party_name           ': 2330, # (str_store_party_name, <string_register>, <party_id>),
    'str_store_agent_name           ': 2332, # (str_store_agent_name, <string_register>, <agent_id>),
    'str_store_faction_name         ': 2335, # (str_store_faction_name, <string_register>, <faction_id>),
    'str_store_quest_name           ': 2336, # (str_store_quest_name, <string_register>, <quest_id>),
    'str_store_info_page_name       ': 2337, # (str_store_info_page_name, <string_register>, <info_page_id>),
    'str_store_date                 ': 2340, # (str_store_date, <string_register>, <number_of_hours_to_add_to_the_current_date>),
    'str_store_troop_name_link      ': 2341, # (str_store_troop_name_link, <string_register>, <troop_id>),
    'str_store_party_name_link      ': 2342, # (str_store_party_name_link, <string_register>, <party_id>),
    'str_store_faction_name_link    ': 2343, # (str_store_faction_name_link, <string_register>, <faction_id>),
    'str_store_quest_name_link      ': 2344, # (str_store_quest_name_link, <string_register>, <quest_id>),
    'str_store_info_page_name_link  ': 2345, # (str_store_info_page_name_link, <string_register>, <info_page_id>),
    'str_store_class_name           ': 2346, # (str_store_class_name, <stribg_register>, <class_id>)
    'game_key_get_mapped_key_name   ':   65, # (game_key_get_mapped_key_name, <string_register>, <game_key>),
    'str_store_player_username      ': 2350, # (str_store_player_username, <string_register>, <player_id>),
    'str_store_server_password      ': 2351, # (str_store_server_password, <string_register>),
    'str_store_server_name          ': 2352, # (str_store_server_name, <string_register>),
    'str_store_welcome_message      ': 2353, # (str_store_welcome_message, <string_register>),
    'str_encode_url                 ': 2355, # (str_encode_url, <string_register>),
    'display_debug_message              ': 1104, # (display_debug_message, <string_id>, [hex_colour_code]),
    'display_log_message                ': 1105, # (display_log_message, <string_id>, [hex_colour_code]),
    'display_message                    ': 1106, # (display_message, <string_id>,[hex_colour_code]),
    'set_show_messages                  ': 1107, # (set_show_messages, <value>),
    'tutorial_box                       ': 1120, # (tutorial_box, <string_id>, <string_id>),
    'dialog_box                         ': 1120, # (dialog_box, <text_string_id>, [title_string_id]),
    'question_box                       ': 1121, # (question_box, <string_id>, [<yes_string_id>], [<no_string_id>]),
    'tutorial_message                   ': 1122, # (tutorial_message, <string_id>, [color], [auto_close_time]),
    'tutorial_message_set_position      ': 1123, # (tutorial_message_set_position, <position_x>, <position_y>), 
    'tutorial_message_set_size          ': 1124, # (tutorial_message_set_size, <size_x>, <size_y>), 
    'tutorial_message_set_center_justify': 1125, # (tutorial_message_set_center_justify, <val>),
    'tutorial_message_set_background    ': 1126, # (tutorial_message_set_background, <value>),
    'entering_town                        ':   36, # (entering_town, <town_id>),
    'encountered_party_is_attacker        ':   39, # (encountered_party_is_attacker),
    'conversation_screen_is_active        ':   42, # (conversation_screen_active),
    'in_meta_mission                      ':   44, # (in_meta_mission),
    'change_screen_return                 ': 2040, # (change_screen_return),
    'change_screen_loot                   ': 2041, # (change_screen_loot, <troop_id>),
    'change_screen_trade                  ': 2042, # (change_screen_trade, [troop_id]),
    'change_screen_exchange_members       ': 2043, # (change_screen_exchange_members, [exchange_leader], [party_id]),
    'change_screen_trade_prisoners        ': 2044, # (change_screen_trade_prisoners),
    'change_screen_buy_mercenaries        ': 2045, # (change_screen_buy_mercenaries),
    'change_screen_view_character         ': 2046, # (change_screen_view_character),
    'change_screen_training               ': 2047, # (change_screen_training),
    'change_screen_mission                ': 2048, # (change_screen_mission),
    'change_screen_map_conversation       ': 2049, # (change_screen_map_conversation, <troop_id>),
    'change_screen_exchange_with_party    ': 2050, # (change_screen_exchange_with_party, <party_id>),
    'change_screen_equip_other            ': 2051, # (change_screen_equip_other, [troop_id]),
    'change_screen_map                    ': 2052, # (change_screen_map),
    'change_screen_notes                  ': 2053, # (change_screen_notes, <note_type>, <object_id>),
    'change_screen_quit                   ': 2055, # (change_screen_quit),
    'change_screen_give_members           ': 2056, # (change_screen_give_members, [party_id]),
    'change_screen_controls               ': 2057, # (change_screen_controls),
    'change_screen_options                ': 2058, # (change_screen_options),
    'set_mercenary_source_party           ': 1320, # (set_mercenary_source_party, <party_id>),
    'start_map_conversation               ': 1025, # (start_map_conversation, <troop_id>, [troop_dna]),
    'set_background_mesh                  ': 2031, # (set_background_mesh, <mesh_id>),
    'set_game_menu_tableau_mesh           ': 2032, # (set_game_menu_tableau_mesh, <tableau_material_id>, <value>, <position_register_no>),
    'jump_to_menu                         ': 2060, # (jump_to_menu, <menu_id>),
    'disable_menu_option                  ': 2061, # (disable_menu_option),
    'set_party_battle_mode                ': 1020, # (set_party_battle_mode),
    'finish_party_battle_mode             ': 1019, # (finish_party_battle_mode),
    'start_encounter                      ': 1300, # (start_encounter, <party_id>),
    'leave_encounter                      ': 1301, # (leave_encounter),
    'encounter_attack                     ': 1302, # (encounter_attack),
    'select_enemy                         ': 1303, # (select_enemy, <value>),
    'set_passage_menu                     ': 1304, # (set_passage_menu, <value>),
    'start_mission_conversation           ': 1920, # (start_mission_conversation, <troop_id>),
    'set_conversation_speaker_troop       ': 2197, # (set_conversation_speaker_troop, <troop_id>),
    'set_conversation_speaker_agent       ': 2198, # (set_conversation_speaker_agent, <agent_id>),
    'store_conversation_agent             ': 2199, # (store_conversation_agent, <destination>),
    'store_conversation_troop             ': 2200, # (store_conversation_troop, <destination>),
    'store_partner_faction                ': 2201, # (store_partner_faction, <destination>),
    'store_encountered_party              ': 2202, # (store_encountered_party, <destination>),
    'store_encountered_party2             ': 2203, # (store_encountered_party2, <destination>),
    'set_encountered_party                ': 2205, # (set_encountered_party, <party_no>),
    'end_current_battle                   ': 1307, # (end_current_battle),
    'store_repeat_object                  ':   50, # (store_repeat_object, <destination>),
    'talk_info_show                       ': 2020, # (talk_info_show, <hide_or_show>),
    'talk_info_set_relation_bar           ': 2021, # (talk_info_set_relation_bar, <value>),
    'talk_info_set_line                   ': 2022, # (talk_info_set_line, <line_no>, <string_no>)
    'all_enemies_defeated                        ': 1003, # (all_enemies_defeated, [team_id]),
    'race_completed_by_player                    ': 1004, # (race_completed_by_player),
    'num_active_teams_le                         ': 1005, # (num_active_teams_le, <value>),
    'main_hero_fallen                            ': 1006, # (main_hero_fallen),
    'scene_allows_mounted_units                  ': 1834, # (scene_allows_mounted_units),
    'is_zoom_disabled                            ': 2222, # (is_zoom_disabled),
    'scene_set_slot                              ':  503, # (scene_set_slot, <scene_id>, <slot_no>, <value>),
    'scene_get_slot                              ':  523, # (scene_get_slot, <destination>, <scene_id>, <slot_no>),
    'scene_slot_eq                               ':  543, # (scene_slot_eq, <scene_id>, <slot_no>, <value>),
    'scene_slot_ge                               ':  563, # (scene_slot_ge, <scene_id>, <slot_no>, <value>),
    'add_troop_to_site                           ': 1250, # (add_troop_to_site, <troop_id>, <scene_id>, <entry_no>),
    'remove_troop_from_site                      ': 1251, # (remove_troop_from_site, <troop_id>, <scene_id>),
    'modify_visitors_at_site                     ': 1261, # (modify_visitors_at_site, <scene_id>),
    'reset_visitors                              ': 1262, # (reset_visitors),
    'set_visitor                                 ': 1263, # (set_visitor, <entry_no>, <troop_id>, [<dna>]),
    'set_visitors                                ': 1264, # (set_visitors, <entry_no>, <troop_id>, <number_of_troops>),
    'add_visitors_to_current_scene               ': 1265, # (add_visitors_to_current_scene, <entry_no>, <troop_id>, <number_of_troops>, <team_no>, <group_no>),
    'mission_tpl_entry_set_override_flags        ': 1940, # (mission_entry_set_override_flags, <mission_template_id>, <entry_no>, <value>),
    'mission_tpl_entry_clear_override_items      ': 1941, # (mission_entry_clear_override_items, <mission_template_id>, <entry_no>),
    'mission_tpl_entry_add_override_item         ': 1942, # (mission_entry_add_override_item, <mission_template_id>, <entry_no>, <item_kind_id>),
    'set_mission_result                          ': 1906, # (set_mission_result, <value>),
    'finish_mission                              ': 1907, # (finish_mission, <delay_in_seconds>),
    'set_jump_mission                            ': 1911, # (set_jump_mission, <mission_template_id>),
    'jump_to_scene                               ': 1910, # (jump_to_scene, <scene_id>, [entry_no]),
    'set_jump_entry                              ': 1912, # (set_jump_entry, <entry_no>),
    'store_current_scene                         ': 2211, # (store_current_scene, <destination>),
    'close_order_menu                            ': 1789, # (close_order_menu),
    'entry_point_get_position                    ': 1780, # (entry_point_get_position, <position>, <entry_no>),
    'entry_point_set_position                    ': 1781, # (entry_point_set_position, <entry_no>, <position>),
    'entry_point_is_auto_generated               ': 1782, # (entry_point_is_auto_generated, <entry_no>),
    'scene_set_day_time                          ': 1266, # (scene_set_day_time, <value>),
    'set_rain                                    ': 1797, # (set_rain, <rain-type>, <strength>),
    'set_fog_distance                            ': 1798, # (set_fog_distance, <distance_in_meters>, [fog_color]),
    'set_skybox                                  ': 2389, # (set_skybox, <non_hdr_skybox_index>, <hdr_skybox_index>),
    'set_startup_sun_light                       ': 2390, # (set_startup_sun_light, <r>, <g>, <b>),
    'set_startup_ambient_light                   ': 2391, # (set_startup_ambient_light, <r>, <g>, <b>),
    'set_startup_ground_ambient_light            ': 2392, # (set_startup_ground_ambient_light, <r>, <g>, <b>),
    'get_startup_sun_light                       ': 2394, # (get_startup_sun_light, <position_no>),
    'get_startup_ambient_light                   ': 2395, # (get_startup_ambient_light, <position_no>),
    'get_startup_ground_ambient_light            ': 2396, # (get_startup_ground_ambient_light, <position_no>),
    'get_battle_advantage                        ': 1690, # (get_battle_advantage, <destination>),
    'set_battle_advantage                        ': 1691, # (set_battle_advantage, <value>),
    'get_scene_boundaries                        ': 1799, # (get_scene_boundaries, <position_min>, <position_max>),
    'mission_enable_talk                         ': 1935, # (mission_enable_talk),
    'mission_disable_talk                        ': 1936, # (mission_disable_talk),
    'mission_get_time_speed                      ': 2002, # (mission_get_time_speed, <destination_fixed_point>),
    'mission_set_time_speed                      ': 2003, # (mission_set_time_speed, <value_fixed_point>),
    'mission_time_speed_move_to_value            ': 2004, # (mission_speed_move_to_value, <value_fixed_point>, <duration-in-1/1000-seconds>),
    'mission_set_duel_mode                       ': 2006, # (mission_set_duel_mode, <value>),
    'store_zoom_amount                           ': 2220, # (store_zoom_amount, <destination_fixed_point>),
    'set_zoom_amount                             ': 2221, # (set_zoom_amount, <value_fixed_point>),
    'reset_mission_timer_a                       ': 2375, # (reset_mission_timer_a),
    'reset_mission_timer_b                       ': 2376, # (reset_mission_timer_b),
    'reset_mission_timer_c                       ': 2377, # (reset_mission_timer_c),
    'store_mission_timer_a                       ': 2370, # (store_mission_timer_a, <destination>),
    'store_mission_timer_b                       ': 2371, # (store_mission_timer_b, <destination>),
    'store_mission_timer_c                       ': 2372, # (store_mission_timer_c, <destination>),
    'store_mission_timer_a_msec                  ': 2365, # (store_mission_timer_a_msec, <destination>),
    'store_mission_timer_b_msec                  ': 2366, # (store_mission_timer_b_msec, <destination>),
    'store_mission_timer_c_msec                  ': 2367, # (store_mission_timer_c_msec, <destination>),
    'mission_cam_set_mode                        ': 2001, # (mission_cam_set_mode, <mission_cam_mode>, <duration-in-1/1000-seconds>, <value>),
    'mission_cam_set_screen_color                ': 2008, # (mission_cam_set_screen_color, <value>),
    'mission_cam_animate_to_screen_color         ': 2009, #(mission_cam_animate_to_screen_color, <value>, <duration-in-1/1000-seconds>),
    'mission_cam_get_position                    ': 2010, # (mission_cam_get_position, <position_register_no>)
    'mission_cam_set_position                    ': 2011, # (mission_cam_set_position, <position_register_no>)
    'mission_cam_animate_to_position             ': 2012, # (mission_cam_animate_to_position, <position_register_no>, <duration-in-1/1000-seconds>, <value>)
    'mission_cam_get_aperture                    ': 2013, # (mission_cam_get_aperture, <destination>)
    'mission_cam_set_aperture                    ': 2014, # (mission_cam_set_aperture, <value>)
    'mission_cam_animate_to_aperture             ': 2015, # (mission_cam_animate_to_aperture, <value>, <duration-in-1/1000-seconds>, <value>)
    'mission_cam_animate_to_position_and_aperture': 2016, # (mission_cam_animate_to_position_and_aperture, <position_register_no>, <value>, <duration-in-1/1000-seconds>, <value>)
    'mission_cam_set_target_agent                ': 2017, # (mission_cam_set_target_agent, <agent_id>, <value>)
    'mission_cam_clear_target_agent              ': 2018, # (mission_cam_clear_target_agent)
    'mission_cam_set_animation                   ': 2019, # (mission_cam_set_animation, <anim_id>),
    'mouse_get_world_projection                  ':  751, # (mouse_get_world_projection, <position_no_1>, <position_no_2>),
    'cast_ray                                    ': 1900, # (cast_ray, <destination>, <hit_position_register>, <ray_position_register>, [<ray_length_fixed_point>]),
    'set_postfx                                  ': 2386, # (set_postfx, ???)
    'set_river_shader_to_mud                     ': 2387, # (set_river_shader_to_mud, ???)
    'rebuild_shadow_map                          ': 2393, # (rebuild_shadow_map),
    'set_shader_param_int                        ': 2400, # (set_shader_param_int, <parameter_name>, <value>), #Sets the int shader parameter <parameter_name> to <value>
    'set_shader_param_float                      ': 2401, # (set_shader_param_float, <parameter_name>, <value_fixed_point>),
    'set_shader_param_float4                     ': 2402, # (set_shader_param_float4, <parameter_name>, <valuex>, <valuey>, <valuez>, <valuew>),
    'set_shader_param_float4x4                   ': 2403, # (set_shader_param_float4x4, <parameter_name>, [0][0], [0][1], [0][2], [1][0], [1][1], [1][2], [2][0], [2][1], [2][2], [3][0], [3][1], [3][2]),
    'prop_instance_is_valid                     ': 1838, # (prop_instance_is_valid, <scene_prop_instance_id>),
    'prop_instance_is_animating                 ': 1862, # (prop_instance_is_animating, <destination>, <scene_prop_id>),
    'prop_instance_intersects_with_prop_instance': 1880, # (prop_instance_intersects_with_prop_instance, <checked_scene_prop_id>, <scene_prop_id>),
    'scene_prop_has_agent_on_it                 ': 1801, # (scene_prop_has_agent_on_it, <scene_prop_instance_id>, <agent_id>)
    'scene_prop_set_slot                        ':  510, # (scene_prop_set_slot, <scene_prop_instance_id>, <slot_no>, <value>),
    'scene_prop_get_slot                        ':  530, # (scene_prop_get_slot, <destination>, <scene_prop_instance_id>, <slot_no>),
    'scene_prop_slot_eq                         ':  550, # (scene_prop_slot_eq, <scene_prop_instance_id>, <slot_no>, <value>),
    'scene_prop_slot_ge                         ':  570, # (scene_prop_slot_ge, <scene_prop_instance_id>, <slot_no>, <value>),
    'prop_instance_get_scene_prop_kind          ': 1853, # (prop_instance_get_scene_prop_type, <destination>, <scene_prop_id>)
    'scene_prop_get_num_instances               ': 1810, # (scene_prop_get_num_instances, <destination>, <scene_prop_id>),
    'scene_prop_get_instance                    ': 1811, # (scene_prop_get_instance, <destination>, <scene_prop_id>, <instance_no>),
    'scene_prop_enable_after_time               ': 1800, # (scene_prop_enable_after_time, <scene_prop_id>, <time_period>),
    'set_spawn_position                         ': 1970, # (set_spawn_position, <position>),
    'spawn_scene_prop                           ': 1974, # (spawn_scene_prop, <scene_prop_id>),
    'prop_instance_get_variation_id             ': 1840, # (prop_instance_get_variation_id, <destination>, <scene_prop_id>),
    'prop_instance_get_variation_id_2           ': 1841, # (prop_instance_get_variation_id_2, <destination>, <scene_prop_id>),
    'replace_prop_instance                      ': 1889, # (replace_prop_instance, <scene_prop_id>, <new_scene_prop_id>),
    'replace_scene_props                        ': 1890, # (replace_scene_props, <old_scene_prop_id>, <new_scene_prop_id>),
    'scene_prop_fade_out                        ': 1822, # (scene_prop_fade_out, <scene_prop_id>, <fade_out_time>)
    'scene_prop_fade_in                         ': 1823, # (scene_prop_fade_in, <scene_prop_id>, <fade_in_time>)
    'prop_instance_set_material                 ': 2617, # (prop_instance_set_material, <prop_instance_no>, <sub_mesh_no>, <string_register>),
    'scene_prop_get_visibility                  ': 1812, # (scene_prop_get_visibility, <destination>, <scene_prop_id>),
    'scene_prop_set_visibility                  ': 1813, # (scene_prop_set_visibility, <scene_prop_id>, <value>),
    'scene_prop_get_hit_points                  ': 1815, # (scene_prop_get_hit_points, <destination>, <scene_prop_id>),
    'scene_prop_get_max_hit_points              ': 1816, # (scene_prop_get_max_hit_points, <destination>, <scene_prop_id>),
    'scene_prop_set_hit_points                  ': 1814, # (scene_prop_set_hit_points, <scene_prop_id>, <value>),
    'scene_prop_set_cur_hit_points              ': 1820, # (scene_prop_set_cur_hit_points, <scene_prop_id>, <value>),
    'prop_instance_receive_damage               ': 1877, # (prop_instance_receive_damage, <scene_prop_id>, <agent_id>, <damage_value>),
    'prop_instance_refill_hit_points            ': 1870, # (prop_instance_refill_hit_points, <scene_prop_id>), 
    'scene_prop_get_team                        ': 1817, # (scene_prop_get_team, <value>, <scene_prop_id>),
    'scene_prop_set_team                        ': 1818, # (scene_prop_set_team, <scene_prop_id>, <value>),
    'scene_prop_set_prune_time                  ': 1819, # (scene_prop_set_prune_time, <scene_prop_id>, <value>),
    'prop_instance_get_position                 ': 1850, # (prop_instance_get_position, <position>, <scene_prop_id>),
    'prop_instance_get_starting_position        ': 1851, # (prop_instance_get_starting_position, <position>, <scene_prop_id>),
    'prop_instance_set_position                 ': 1855, # (prop_instance_set_position, <scene_prop_id>, <position>, [dont_send_to_clients]),
    'prop_instance_animate_to_position          ': 1860, # (prop_instance_animate_to_position, <scene_prop_id>, position, <duration-in-1/100-seconds>),
    'prop_instance_get_animation_target_position': 1863, # (prop_instance_get_animation_target_position, <pos>, <scene_prop_id>)
    'prop_instance_stop_animating               ': 1861, # (prop_instance_stop_animating, <scene_prop_id>),
    'prop_instance_get_scale                    ': 1852, # (prop_instance_get_scale, <position>, <scene_prop_id>),
    'prop_instance_set_scale                    ': 1854, # (prop_instance_set_scale, <scene_prop_id>, <value_x_fixed_point>, <value_y_fixed_point>, <value_z_fixed_point>),
    'prop_instance_enable_physics               ': 1864, # (prop_instance_enable_physics, <scene_prop_id>, <value>),
    'prop_instance_initialize_rotation_angles   ': 1866, # (prop_instance_initialize_rotation_angles, <scene_prop_id>),
    'prop_instance_rotate_to_position           ': 1865, # (prop_instance_rotate_to_position, <scene_prop_id>, <position>, <duration-in-1/100-seconds>, <total_rotate_angle_fixed_point>),
    'prop_instance_clear_attached_missiles      ': 1885, # (prop_instance_clear_attached_missiles, <scene_prop_id>),
    'prop_instance_dynamics_set_properties      ': 1871, # (prop_instance_dynamics_set_properties, <scene_prop_id>, <position>),
    'prop_instance_dynamics_set_velocity        ': 1872, # (prop_instance_dynamics_set_velocity, <scene_prop_id>, <position>),
    'prop_instance_dynamics_set_omega           ': 1873, # (prop_instance_dynamics_set_omega, <scene_prop_id>, <position>),
    'prop_instance_dynamics_apply_impulse       ': 1874, # (prop_instance_dynamics_apply_impulse, <scene_prop_id>, <position>),
    'prop_instance_deform_to_time               ': 2610, # (prop_instance_deform_to_time, <prop_instance_no>, <value>),
    'prop_instance_deform_in_range              ': 2611, # (prop_instance_deform_in_range, <prop_instance_no>, <start_frame>, <end_frame>, <duration-in-1/1000-seconds>),
    'prop_instance_deform_in_cycle_loop         ': 2612, # (prop_instance_deform_in_cycle_loop, <prop_instance_no>, <start_frame>, <end_frame>, <duration-in-1/1000-seconds>),
    'prop_instance_get_current_deform_progress  ': 2615, # (prop_instance_get_current_deform_progress, <destination>, <prop_instance_no>),
    'prop_instance_get_current_deform_frame     ': 2616, # (prop_instance_get_current_deform_frame, <destination>, <prop_instance_no>),
    'prop_instance_play_sound                   ': 1881, # (prop_instance_play_sound, <scene_prop_id>, <sound_id>, [flags]),
    'prop_instance_stop_sound                   ': 1882, # (prop_instance_stop_sound, <scene_prop_id>),
    'scene_item_get_num_instances               ': 1830, # (scene_item_get_num_instances, <destination>, <item_id>),
    'scene_item_get_instance                    ': 1831, # (scene_item_get_instance, <destination>, <item_id>, <instance_no>),
    'scene_spawned_item_get_num_instances       ': 1832, # (scene_spawned_item_get_num_instances, <destination>, <item_id>),
    'scene_spawned_item_get_instance            ': 1833, # (scene_spawned_item_get_instance, <destination>, <item_id>, <instance_no>),
    'replace_scene_items_with_scene_props       ': 1891, # (replace_scene_items_with_scene_props, <old_item_id>, <new_scene_prop_id>),
    'set_spawn_position                         ': 1970, # (set_spawn_position, <position>), ## DUPLICATE ENTRY
    'spawn_item                                 ': 1971, # (spawn_item, <item_kind_id>, <item_modifier>, [seconds_before_pruning]),
    'spawn_item_without_refill                  ': 1976, # (spawn_item_without_refill, <item_kind_id>, <item_modifier>, [seconds_before_pruning]),
    'set_current_color                          ': 1950, # (set_current_color, <red_value>, <green_value>, <blue_value>),
    'set_position_delta                         ': 1955, # (set_position_delta, <value>, <value>, <value>),
    'add_point_light                            ': 1960, # (add_point_light, [flicker_magnitude], [flicker_interval]),
    'add_point_light_to_entity                  ': 1961, # (add_point_light_to_entity, [flicker_magnitude], [flicker_interval]),
    'particle_system_add_new                    ': 1965, # (particle_system_add_new, <par_sys_id>,[position]),
    'particle_system_emit                       ': 1968, # (particle_system_emit, <par_sys_id>, <value_num_particles>, <value_period>),
    'particle_system_burst                      ': 1969, # (particle_system_burst, <par_sys_id>, <position>, [percentage_burst_strength]),
    'particle_system_burst_no_sync              ': 1975, # (particle_system_burst_without_sync,<par_sys_id>,<position_no>,[percentage_burst_strength]),
    'prop_instance_add_particle_system          ': 1886, # (prop_instance_add_particle_system, <scene_prop_id>, <par_sys_id>, <position_no>),
    'prop_instance_stop_all_particle_systems    ': 1887, # (prop_instance_stop_all_particle_systems, <scene_prop_id>),
    'agent_is_in_special_mode                ': 1693, # (agent_is_in_special_mode, <agent_id>),
    'agent_is_routed                         ': 1699, # (agent_is_routed, <agent_id>),
    'agent_is_alive                          ': 1702, # (agent_is_alive, <agent_id>),
    'agent_is_wounded                        ': 1703, # (agent_is_wounded, <agent_id>),
    'agent_is_human                          ': 1704, # (agent_is_human, <agent_id>),
    'agent_is_ally                           ': 1706, # (agent_is_ally, <agent_id>),
    'agent_is_non_player                     ': 1707, # (agent_is_non_player, <agent_id>),
    'agent_is_defender                       ': 1708, # (agent_is_defender, <agent_id>),
    'agent_is_active                         ': 1712, # (agent_is_active, <agent_id>),
    'agent_has_item_equipped                 ': 1729, # (agent_has_item_equipped, <agent_id>, <item_id>),
    'agent_is_in_parried_animation           ': 1769, # (agent_is_in_parried_animation, <agent_id>),
    'agent_is_alarmed                        ': 1806, # (agent_is_alarmed, <agent_id>),
    'class_is_listening_order                ': 1775, # (class_is_listening_order, <team_no>, <sub_class>),
    'teams_are_enemies                       ': 1788, # (teams_are_enemies, <team_no>, <team_no_2>), 
    'agent_is_in_line_of_sight               ': 1826, # (agent_is_in_line_of_sight, <agent_id>, <position_no>),
    'team_set_slot                           ':  509, # (team_set_slot, <team_id>, <slot_no>, <value>),
    'team_get_slot                           ':  529, # (team_get_slot, <destination>, <player_id>, <slot_no>),
    'team_slot_eq                            ':  549, # (team_slot_eq, <team_id>, <slot_no>, <value>),
    'team_slot_ge                            ':  569, # (team_slot_ge, <team_id>, <slot_no>, <value>),
    'agent_set_slot                          ':  505, # (agent_set_slot, <agent_id>, <slot_no>, <value>),
    'agent_get_slot                          ':  525, # (agent_get_slot, <destination>, <agent_id>, <slot_no>),
    'agent_slot_eq                           ':  545, # (agent_slot_eq, <agent_id>, <slot_no>, <value>),
    'agent_slot_ge                           ':  565, # (agent_slot_ge, <agent_id>, <slot_no>, <value>),
    'add_reinforcements_to_entry             ': 1930, # (add_reinforcements_to_entry, <mission_template_entry_no>, <wave_size>),
    'set_spawn_position                      ': 1970, # (set_spawn_position, <position>), ## DUPLICATE ENTRY
    'spawn_agent                             ': 1972, # (spawn_agent, <troop_id>),
    'spawn_horse                             ': 1973, # (spawn_horse, <item_kind_id>, <item_modifier>),
    'remove_agent                            ': 1755, # (remove_agent, <agent_id>),
    'agent_fade_out                          ': 1749, # (agent_fade_out, <agent_id>),
    'agent_play_sound                        ': 1750, # (agent_play_sound, <agent_id>, <sound_id>),
    'agent_stop_sound                        ': 1808, # (agent_stop_sound, <agent_id>),
    'agent_set_visibility                    ': 2096, # (agent_set_visibility, <agent_id>, <value>),
    'get_player_agent_no                     ': 1700, # (get_player_agent_no, <destination>),
    'agent_get_kill_count                    ': 1723, # (agent_get_kill_count, <destination>, <agent_id>, [get_wounded]),
    'agent_get_position                      ': 1710, # (agent_get_position, <position>, <agent_id>),
    'agent_set_position                      ': 1711, # (agent_set_position, <agent_id>, <position>),
    'agent_get_horse                         ': 1714, # (agent_get_horse, <destination>, <agent_id>),
    'agent_get_rider                         ': 1715, # (agent_get_rider, <destination>, <horse_agent_id>),
    'agent_get_party_id                      ': 1716, # (agent_get_party_id, <destination>, <agent_id>),
    'agent_get_entry_no                      ': 1717, # (agent_get_entry_no, <destination>, <agent_id>),
    'agent_get_troop_id                      ': 1718, # (agent_get_troop_id, <destination>, <agent_id>),
    'agent_get_item_id                       ': 1719, # (agent_get_item_id, <destination>, <horse_agent_id>),
    'store_agent_hit_points                  ': 1720, # (store_agent_hit_points, <destination>, <agent_id>, [absolute]),
    'agent_set_hit_points                    ': 1721, # (agent_set_hit_points, <agent_id>, <value>,[absolute]),
    'agent_set_max_hit_points                ': 2090, # (agent_set_max_hit_points, <agent_id>, <value>, [absolute]),
    'agent_deliver_damage_to_agent           ': 1722, # (agent_deliver_damage_to_agent, <agent_id_deliverer>, <agent_id>, [damage_amount], [weapon_item_id]),
    'agent_deliver_damage_to_agent_advanced  ': 1827, # (agent_deliver_damage_to_agent_advanced, <destination>, <attacker_agent_id>, <agent_id>, <value>, [weapon_item_id]),
    'add_missile                             ': 1829, # (add_missile, <agent_id>, <starting_position>, <starting_speed_fixed_point>, <weapon_item_id>, <weapon_item_modifier>, <missile_item_id>, <missile_item_modifier>),
    'agent_get_speed                         ': 1689, # (agent_get_speed, <position>, <agent_id>),
    'agent_set_no_death_knock_down_only      ': 1733, # (agent_set_no_death_knock_down_only, <agent_id>, <value>),
    'agent_set_horse_speed_factor            ': 1734, # (agent_set_horse_speed_factor, <agent_id>, <speed_multiplier-in-1/100>),
    'agent_set_speed_limit                   ': 1736, # (agent_set_speed_limit, <agent_id>, <speed_limit(kilometers/hour)>),
    'agent_set_damage_modifier               ': 2091, # (agent_set_damage_modifier, <agent_id>, <value>),
    'agent_set_accuracy_modifier             ': 2092, # (agent_set_accuracy_modifier, <agent_id>, <value>),
    'agent_set_speed_modifier                ': 2093, # (agent_set_speed_modifier, <agent_id>, <value>),
    'agent_set_reload_speed_modifier         ': 2094, # (agent_set_reload_speed_modifier, <agent_id>, <value>),
    'agent_set_use_speed_modifier            ': 2095, # (agent_set_use_speed_modifier, <agent_id>, <value>),
    'agent_set_ranged_damage_modifier        ': 2099, # (agent_set_ranged_damage_modifier, <agent_id>, <value>),
    'agent_get_time_elapsed_since_removed    ': 1760, # (agent_get_time_elapsed_since_removed, <destination>, <agent_id>),
    'agent_refill_wielded_shield_hit_points  ': 1692, # (agent_refill_wielded_shield_hit_points, <agent_id>),
    'agent_set_invulnerable_shield           ': 1725, # (agent_set_invulnerable_shield, <agent_id>, <value>),
    'agent_get_wielded_item                  ': 1726, # (agent_get_wielded_item, <destination>, <agent_id>, <hand_no>),
    'agent_get_ammo                          ': 1727, # (agent_get_ammo, <destination>, <agent_id>, <value>),
    'agent_get_item_cur_ammo                 ': 1977, # (agent_get_item_cur_ammo, <destination>, <agent_id>, <slot_no>),
    'agent_refill_ammo                       ': 1728, # (agent_refill_ammo, <agent_id>),
    'agent_set_wielded_item                  ': 1747, # (agent_set_wielded_item, <agent_id>, <item_id>),
    'agent_equip_item                        ': 1779, # (agent_equip_item, <agent_id>, <item_id>, [weapon_slot_no]),
    'agent_unequip_item                      ': 1774, # (agent_unequip_item, <agent_id>, <item_id>, [weapon_slot_no]),
    'agent_set_ammo                          ': 1776, # (agent_set_ammo, <agent_id>, <item_id>, <value>),
    'agent_get_item_slot                     ': 1804, # (agent_get_item_slot, <destination>, <agent_id>, <value>),
    'agent_get_ammo_for_slot                 ': 1825, # (agent_get_ammo_for_slot, <destination>, <agent_id>, <slot_no>),
    'agent_set_no_dynamics                   ': 1762, # (agent_set_no_dynamics, <agent_id>, <value>),
    'agent_get_animation                     ': 1768, # (agent_get_animation, <destination>, <agent_id>, <body_part),
    'agent_set_animation                     ': 1740, # (agent_set_animation, <agent_id>, <anim_id>, [channel_no]),
    'agent_set_stand_animation               ': 1741, # (agent_set_stand_action, <agent_id>, <anim_id>),
    'agent_set_walk_forward_animation        ': 1742, # (agent_set_walk_forward_action, <agent_id>, <anim_id>),
    'agent_set_animation_progress            ': 1743, # (agent_set_animation_progress, <agent_id>, <value_fixed_point>),
    'agent_ai_set_can_crouch                 ': 2083, # (agent_ai_set_can_crouch, <agent_id>, <value>),
    'agent_get_crouch_mode                   ': 2097, # (agent_ai_get_crouch_mode, <destination>, <agent_id>),
    'agent_set_crouch_mode                   ': 2098, # (agent_ai_set_crouch_mode, <agent_id>, <value>),
    'agent_get_attached_scene_prop           ': 1756, # (agent_get_attached_scene_prop, <destination>, <agent_id>)
    'agent_set_attached_scene_prop           ': 1757, # (agent_set_attached_scene_prop, <agent_id>, <scene_prop_id>)
    'agent_set_attached_scene_prop_x         ': 1758, # (agent_set_attached_scene_prop_x, <agent_id>, <value>)
    'agent_set_attached_scene_prop_y         ': 1809, # (agent_set_attached_scene_prop_y, <agent_id>, <value>)
    'agent_set_attached_scene_prop_z         ': 1759, # (agent_set_attached_scene_prop_z, <agent_id>, <value>)
    'agent_get_bone_position                 ': 2076, # (agent_get_bone_position, <position_no>, <agent_no>, <bone_no>, [<local_or_global>]),
    'agent_ai_set_interact_with_player       ': 2077, # (agent_ai_set_interact_with_player, <agent_no>, <value>),
    'agent_set_is_alarmed                    ': 1807, # (agent_set_is_alarmed, <agent_id>, <value>),
    'agent_clear_relations_with_agents       ': 1802, # (agent_clear_relations_with_agents, <agent_id>),
    'agent_add_relation_with_agent           ': 1803, # (agent_add_relation_with_agent, <agent_id>, <agent_id>, <value>),
    'agent_get_number_of_enemies_following   ': 1761, # (agent_get_number_of_enemies_following, <destination>, <agent_id>),
    'agent_ai_get_num_cached_enemies         ': 2670, # (agent_ai_get_num_cached_enemies, <destination>, <agent_no>),
    'agent_ai_get_cached_enemy               ': 2671, # (agent_ai_get_cached_enemy, <destination>, <agent_no>, <cache_index>),
    'agent_get_attack_action                 ': 1763, # (agent_get_attack_action, <destination>, <agent_id>),
    'agent_get_defend_action                 ': 1764, # (agent_get_defend_action, <destination>, <agent_id>),
    'agent_get_action_dir                    ': 1767, # (agent_get_action_dir, <destination>, <agent_id>),
    'agent_set_attack_action                 ': 1745, # (agent_set_attack_action, <agent_id>, <direction_value>, <action_value>),
    'agent_set_defend_action                 ': 1746, # (agent_set_defend_action, <agent_id>, <value>, <duration-in-1/1000-seconds>),
    'agent_set_scripted_destination          ': 1730, # (agent_set_scripted_destination, <agent_id>, <position>, [auto_set_z_to_ground_level], [no_rethink]),
    'agent_set_scripted_destination_no_attack': 1748, # (agent_set_scripted_destination_no_attack, <agent_id>, <position>, <auto_set_z_to_ground_level>),
    'agent_get_scripted_destination          ': 1731, # (agent_get_scripted_destination, <position>, <agent_id>),
    'agent_force_rethink                     ': 1732, # (agent_force_rethink, <agent_id>),
    'agent_clear_scripted_mode               ': 1735, # (agent_clear_scripted_mode, <agent_id>),
    'agent_ai_set_always_attack_in_melee     ': 1737, # (agent_ai_set_always_attack_in_melee, <agent_id>, <value>),
    'agent_get_simple_behavior               ': 1738, # (agent_get_simple_behavior, <destination>, <agent_id>),
    'agent_ai_get_behavior_target            ': 2082, # (agent_ai_get_behavior_target, <destination>, <agent_id>),
    'agent_get_combat_state                  ': 1739, # (agent_get_combat_state, <destination>, <agent_id>),
    'agent_ai_get_move_target                ': 2081, # (agent_ai_get_move_target, <destination>, <agent_id>),
    'agent_get_look_position                 ': 1709, # (agent_get_look_position, <position>, <agent_id>),
    'agent_set_look_target_position          ': 1744, # (agent_set_look_target_position, <agent_id>, <position>),
    'agent_ai_get_look_target                ': 2080, # (agent_ai_get_look_target, <destination>, <agent_id>),
    'agent_set_look_target_agent             ': 1713, # (agent_set_look_target_agent, <watcher_agent_id>, <observed_agent_id>),
    'agent_start_running_away                ': 1751, # (agent_start_running_away, <agent_id>, [<position_no>]),
    'agent_stop_running_away                 ': 1752, # (agent_stop_run_away, <agent_id>),
    'agent_ai_set_aggressiveness             ': 1753, # (agent_ai_set_aggressiveness, <agent_id>, <value>),
    'agent_set_kick_allowed                  ': 1754, # (agent_set_kick_allowed, <agent_id>, <value>),
    'set_cheer_at_no_enemy                   ': 2379, # (set_cheer_at_no_enemy, <value>),
    'agent_add_offer_with_timeout            ': 1777, # (agent_add_offer_with_timeout, <agent_id>, <offerer_agent_id>, <duration-in-1/1000-seconds>),
    'agent_check_offer_from_agent            ': 1778, # (agent_check_offer_from_agent, <agent_id>, <offerer_agent_id>), #second agent_id is offerer
    'agent_get_group                         ': 1765, # (agent_get_group, <destination>, <agent_id>),
    'agent_set_group                         ': 1766, # (agent_set_group, <agent_id>, <player_leader_id>),
    'agent_get_team                          ': 1770, # (agent_get_team, <destination>, <agent_id>),
    'agent_set_team                          ': 1771, # (agent_set_team, <agent_id>, <value>),
    'agent_get_class                         ': 1772, # (agent_get_class , <destination>, <agent_id>),
    'agent_get_division                      ': 1773, # (agent_get_division , <destination>, <agent_id>),
    'agent_set_division                      ': 1783, # (agent_set_division, <agent_id>, <value>),
    'team_get_hold_fire_order                ': 1784, # (team_get_hold_fire_order, <destination>, <team_no>, <division>),
    'team_get_movement_order                 ': 1785, # (team_get_movement_order, <destination>, <team_no>, <division>),
    'team_get_riding_order                   ': 1786, # (team_get_riding_order, <destination>, <team_no>, <division>),
    'team_get_weapon_usage_order             ': 1787, # (team_get_weapon_usage_order, <destination>, <team_no>, <division>),
    'team_give_order                         ': 1790, # (team_give_order, <team_no>, <division>, <order_id>),
    'team_set_order_position                 ': 1791, # (team_set_order_position, <team_no>, <division>, <position>),
    'team_get_leader                         ': 1792, # (team_get_leader, <destination>, <team_no>),
    'team_set_leader                         ': 1793, # (team_set_leader, <team_no>, <new_leader_agent_id>),
    'team_get_order_position                 ': 1794, # (team_get_order_position, <position>, <team_no>, <division>),
    'team_set_order_listener                 ': 1795, # (team_set_order_listener, <team_no>, <division>, [add_to_listeners]),
    'team_set_relation                       ': 1796, # (team_set_relation, <team_no>, <team_no_2>, <value>),
    'store_remaining_team_no                 ': 2360, # (store_remaining_team_no, <destination>),
    'team_get_gap_distance                   ': 1828, # (team_get_gap_distance, <destination>, <team_no>, <sub_class>),
    'store_enemy_count                       ': 2380, # (store_enemy_count, <destination>),
    'store_friend_count                      ': 2381, # (store_friend_count, <destination>),
    'store_ally_count                        ': 2382, # (store_ally_count, <destination>),
    'store_defender_count                    ': 2383, # (store_defender_count, <destination>),
    'store_attacker_count                    ': 2384, # (store_attacker_count, <destination>),
    'store_normalized_team_count             ': 2385, # (store_normalized_team_count, <destination>, <team_no>),
    'is_presentation_active                           ':  903, # (is_presentation_active, <presentation_id),
    'start_presentation                               ':  900, # (start_presentation, <presentation_id>),
    'start_background_presentation                    ':  901, # (start_background_presentation, <presentation_id>),
    'presentation_set_duration                        ':  902, # (presentation_set_duration, <duration-in-1/100-seconds>),
    'create_text_overlay                              ':  910, # (create_text_overlay, <destination>, <string_id>),
    'create_mesh_overlay                              ':  911, # (create_mesh_overlay, <destination>, <mesh_id>),
    'create_mesh_overlay_with_item_id                 ':  944, # (create_mesh_overlay_with_item_id, <destination>, <item_id>),
    'create_mesh_overlay_with_tableau_material        ':  939, # (create_mesh_overlay_with_tableau_material, <destination>, <mesh_id>, <tableau_material_id>, <value>),
    'create_button_overlay                            ':  912, # (create_button_overlay, <destination>, <string_id>),
    'create_game_button_overlay                       ':  940, # (create_game_button_overlay, <destination>, <string_id>),
    'create_in_game_button_overlay                    ':  941, # (create_in_game_button_overlay, <destination>, <string_id>),
    'create_image_button_overlay                      ':  913, # (create_image_button_overlay, <destination>, <mesh_id>, <mesh_id>),
    'create_image_button_overlay_with_tableau_material':  938, # (create_image_button_overlay_with_tableau_material, <destination>, <mesh_id>, <tableau_material_id>, <value>),
    'create_slider_overlay                            ':  914, # (create_slider_overlay, <destination>, <min_value>, <max_value>),
    'create_progress_overlay                          ':  915, # (create_progress_overlay, <destination>, <min_value>, <max_value>),
    'create_number_box_overlay                        ':  942, # (create_number_box_overlay, <destination>, <min_value>, <max_value>),
    'create_text_box_overlay                          ':  917, # (create_text_box_overlay, <destination>),
    'create_simple_text_box_overlay                   ':  919, # (create_simple_text_box_overlay, <destination>),
    'create_check_box_overlay                         ':  918, # (create_check_box_overlay, <destination>, <checkbox_off_mesh>, <checkbox_on_mesh>),
    'create_listbox_overlay                           ':  943, # (create_list_box_overlay, <destination>, <string>, <value>),
    'create_combo_label_overlay                       ':  948, # (create_combo_label_overlay, <destination>),
    'create_combo_button_overlay                      ':  916, # (create_combo_button_overlay, <destination>),
    'overlay_add_item                                 ':  931, # (overlay_add_item, <overlay_id>, <string_id>),
    'set_container_overlay                            ':  945, # (set_container_overlay, <overlay_id>),
    'overlay_set_container_overlay                    ':  951, # (overlay_set_container_overlay, <overlay_id>, <container_overlay_id>),
    'overlay_get_position                             ':  946, # (overlay_get_position, <position>, <overlay_id>)
    'overlay_set_val                                  ':  927, # (overlay_set_val, <overlay_id>, <value>),
    'overlay_set_text                                 ':  920, # (overlay_set_text, <overlay_id>, <string_id>),
    'overlay_set_boundaries                           ':  928, # (overlay_set_boundaries, <overlay_id>, <min_value>, <max_value>),
    'overlay_set_position                             ':  926, # (overlay_set_position, <overlay_id>, <position>),
    'overlay_set_size                                 ':  925, # (overlay_set_size, <overlay_id>, <position>),
    'overlay_set_area_size                            ':  929, # (overlay_set_area_size, <overlay_id>, <position>),
    'overlay_set_additional_render_height             ':  952, # (overlay_set_additional_render_height, <overlay_id>, <height_adder>),
    'overlay_animate_to_position                      ':  937, # (overlay_animate_to_position, <overlay_id>, <duration-in-1/1000-seconds>, <position>),
    'overlay_animate_to_size                          ':  936, # (overlay_animate_to_size, <overlay_id>, <duration-in-1/1000-seconds>, <position>),
    'overlay_set_mesh_rotation                        ':  930, # (overlay_set_mesh_rotation, <overlay_id>, <position>),
    'overlay_set_material                             ':  956, # (overlay_set_material, <overlay_id>, <string_no>),
    'overlay_set_color                                ':  921, # (overlay_set_color, <overlay_id>, <color>),
    'overlay_set_alpha                                ':  922, # (overlay_set_alpha, <overlay_id>, <alpha>),
    'overlay_set_hilight_color                        ':  923, # (overlay_set_hilight_color, <overlay_id>, <color>),
    'overlay_set_hilight_alpha                        ':  924, # (overlay_set_hilight_alpha, <overlay_id>, <alpha>),
    'overlay_animate_to_color                         ':  932, # (overlay_animate_to_color, <overlay_id>, <duration-in-1/1000-seconds>, <color>)
    'overlay_animate_to_alpha                         ':  933, # (overlay_animate_to_alpha, <overlay_id>, <duration-in-1/1000-seconds>, <color>),
    'overlay_animate_to_highlight_color               ':  934, # (overlay_animate_to_highlight_color, <overlay_id>, <duration-in-1/1000-seconds>, <color>),
    'overlay_animate_to_highlight_alpha               ':  935, # (overlay_animate_to_highlight_alpha, <overlay_id>, <duration-in-1/1000-seconds>, <color>),
    'overlay_set_display                              ':  947, # (overlay_set_display, <overlay_id>, <value>),
    'overlay_obtain_focus                             ':  949, # (overlay_obtain_focus, <overlay_id>),
    'overlay_set_tooltip                              ':  950, # (overlay_set_tooltip, <overlay_id>, <string_id>),
    'show_item_details                                ':  970, # (show_item_details, <item_id>, <position>, <price_multiplier_percentile>),
    'show_item_details_with_modifier                  ':  972, # (show_item_details_with_modifier, <item_id>, <item_modifier>, <position>, <price_multiplier_percentile>),
    'close_item_details                               ':  971, # (close_item_details)
    'show_troop_details                               ': 2388, # (show_troop_details, <troop_id>, <position>, <troop_price>)
    'player_is_active                            ':  401, # (player_is_active, <player_id>),
    'multiplayer_is_server                       ':  417, # (multiplayer_is_server),
    'multiplayer_is_dedicated_server             ':  418, # (multiplayer_is_dedicated_server),
    'game_in_multiplayer_mode                    ':  419, # (game_in_multiplayer_mode),
    'player_is_admin                             ':  430, # (player_is_admin, <player_id>),
    'player_is_busy_with_menus                   ':  438, # (player_is_busy_with_menus, <player_id>),
    'player_item_slot_is_picked_up               ':  461, # (player_item_slot_is_picked_up, <player_id>, <item_slot_no>),
    'player_set_slot                             ':  508, # (player_set_slot, <player_id>, <slot_no>, <value>),
    'player_get_slot                             ':  528, # (player_get_slot, <destination>, <player_id>, <slot_no>),
    'player_slot_eq                              ':  548, # (player_slot_eq, <player_id>, <slot_no>, <value>),
    'player_slot_ge                              ':  568, # (player_slot_ge, <player_id>, <slot_no>, <value>),
    'send_message_to_url                         ':  380, # (send_message_to_url, <string_id>, <encode_url>),
    'multiplayer_send_message_to_server          ':  388, # (multiplayer_send_message_to_server, <message_type>),
    'multiplayer_send_int_to_server              ':  389, # (multiplayer_send_int_to_server, <message_type>, <value>),
    'multiplayer_send_2_int_to_server            ':  390, # (multiplayer_send_2_int_to_server, <message_type>, <value>, <value>),
    'multiplayer_send_3_int_to_server            ':  391, # (multiplayer_send_3_int_to_server, <message_type>, <value>, <value>, <value>),
    'multiplayer_send_4_int_to_server            ':  392, # (multiplayer_send_4_int_to_server, <message_type>, <value>, <value>, <value>, <value>),
    'multiplayer_send_string_to_server           ':  393, # (multiplayer_send_string_to_server, <message_type>, <string_id>),
    'multiplayer_send_message_to_player          ':  394, # (multiplayer_send_message_to_player, <player_id>, <message_type>),
    'multiplayer_send_int_to_player              ':  395, # (multiplayer_send_int_to_player, <player_id>, <message_type>, <value>),
    'multiplayer_send_2_int_to_player            ':  396, # (multiplayer_send_2_int_to_player, <player_id>, <message_type>, <value>, <value>),
    'multiplayer_send_3_int_to_player            ':  397, # (multiplayer_send_3_int_to_player, <player_id>, <message_type>, <value>, <value>, <value>),
    'multiplayer_send_4_int_to_player            ':  398, # (multiplayer_send_4_int_to_player, <player_id>, <message_type>, <value>, <value>, <value>, <value>),
    'multiplayer_send_string_to_player           ':  399, # (multiplayer_send_string_to_player, <player_id>, <message_type>, <string_id>),
    'get_max_players                             ':  400, # (get_max_players, <destination>),
    'player_get_team_no                          ':  402, # (player_get_team_no, <destination>, <player_id>),
    'player_set_team_no                          ':  403, # (player_get_team_no, <player_id>, <team_id>),
    'player_get_troop_id                         ':  404, # (player_get_troop_id, <destination>, <player_id>),
    'player_set_troop_id                         ':  405, # (player_get_troop_id, <player_id>, <troop_id>),
    'player_get_agent_id                         ':  406, # (player_get_agent_id, <destination>, <player_id>),
    'agent_get_player_id                         ': 1724, # (agent_get_player_id, <destination>, <agent_id>),
    'player_get_gold                             ':  407, # (player_get_gold, <destination>, <player_id>),
    'player_set_gold                             ':  408, # (player_set_gold, <player_id>, <value>, <max_value>),
    'player_spawn_new_agent                      ':  409, # (player_spawn_new_agent, <player_id>, <entry_point>),
    'player_add_spawn_item                       ':  410, # (player_add_spawn_item, <player_id>, <item_slot_no>, <item_id>),
    'multiplayer_get_my_team                     ':  411, # (multiplayer_get_my_team, <destination>),
    'multiplayer_get_my_troop                    ':  412, # (multiplayer_get_my_troop, <destination>),
    'multiplayer_set_my_troop                    ':  413, # (multiplayer_get_my_troop, <destination>),
    'multiplayer_get_my_gold                     ':  414, # (multiplayer_get_my_gold, <destination>),
    'multiplayer_get_my_player                   ':  415, # (multiplayer_get_my_player, <destination>),
    'multiplayer_make_everyone_enemy             ':  420, # (multiplayer_make_everyone_enemy),
    'player_control_agent                        ':  421, # (player_control_agent, <player_id>, <agent_id>),
    'player_get_item_id                          ':  422, # (player_get_item_id, <destination>, <player_id>, <item_slot_no>),
    'player_get_banner_id                        ':  423, # (player_get_banner_id, <destination>, <player_id>),
    'player_set_is_admin                         ':  429, # (player_set_is_admin, <player_id>, <value>),
    'player_get_score                            ':  431, # (player_get_score, <destination>, <player_id>),
    'player_set_score                            ':  432, # (player_set_score, <player_id>, <value>),
    'player_get_kill_count                       ':  433, # (player_get_kill_count, <destination>, <player_id>),
    'player_set_kill_count                       ':  434, # (player_set_kill_count, <player_id>, <value>),
    'player_get_death_count                      ':  435, # (player_get_death_count, <destination>, <player_id>),
    'player_set_death_count                      ':  436, # (player_set_death_count, <player_id>, <value>),
    'player_get_ping                             ':  437, # (player_get_ping, <destination>, <player_id>),
    'player_get_is_muted                         ':  439, # (player_get_is_muted, <destination>, <player_id>),
    'player_set_is_muted                         ':  440, # (player_set_is_muted, <player_id>, <value>, [mute_for_everyone]), #mute_for_everyone optional parameter should be set to 1 if player is muted for everyone (this works only on server).
    'player_get_unique_id                        ':  441, # (player_get_unique_id, <destination>, <player_id>), #can only bew used on server side
    'player_get_gender                           ':  442, # (player_get_gender, <destination>, <player_id>),
    'player_save_picked_up_items_for_next_spawn  ':  459, # (player_save_picked_up_items_for_next_spawn, <player_id>),
    'player_get_value_of_original_items          ':  460, # (player_get_value_of_original_items, <player_id>),
    'profile_get_banner_id                       ':  350, # (profile_get_banner_id, <destination>),
    'profile_set_banner_id                       ':  351, # (profile_set_banner_id, <value>),
    'team_get_bot_kill_count                     ':  450, # (team_get_bot_kill_count, <destination>, <team_id>),
    'team_set_bot_kill_count                     ':  451, # (team_get_bot_kill_count, <destination>, <team_id>),
    'team_get_bot_death_count                    ':  452, # (team_get_bot_death_count, <destination>, <team_id>),
    'team_set_bot_death_count                    ':  453, # (team_get_bot_death_count, <destination>, <team_id>),
    'team_get_kill_count                         ':  454, # (team_get_kill_count, <destination>, <team_id>),
    'team_get_score                              ':  455, # (team_get_score, <destination>, <team_id>),
    'team_set_score                              ':  456, # (team_set_score, <team_id>, <value>),
    'team_set_faction                            ':  457, # (team_set_faction, <team_id>, <faction_id>),
    'team_get_faction                            ':  458, # (team_get_faction, <destination>, <team_id>),
    'multiplayer_clear_scene                     ':  416, # (multiplayer_clear_scene),
    'multiplayer_find_spawn_point                ':  425, # (multiplayer_find_spawn_point, <destination>, <team_no>, <examine_all_spawn_points>, <is_horseman>), 
    'set_spawn_effector_scene_prop_kind          ':  426, # (set_spawn_effector_scene_prop_kind, <team_no>, <scene_prop_kind_no>),
    'set_spawn_effector_scene_prop_id            ':  427, # (set_spawn_effector_scene_prop_id, <team_no>, <scene_prop_id>),
    'start_multiplayer_mission                   ':  470, # (start_multiplayer_mission, <mission_template_id>, <scene_id>, <started_manually>),
    'kick_player                                 ':  465, # (kick_player, <player_id>),
    'ban_player                                  ':  466, # (ban_player, <player_id>, <value>, <player_id>),
    'save_ban_info_of_player                     ':  467, # (save_ban_info_of_player, <player_id>),
    'ban_player_using_saved_ban_info             ':  468, # (ban_player_using_saved_ban_info),
    'server_add_message_to_log                   ':  473, # (server_add_message_to_log, <string_id>),
    'server_get_renaming_server_allowed          ':  475, # (server_get_renaming_server_allowed, <destination>),
    'server_get_changing_game_type_allowed       ':  476, # (server_get_changing_game_type_allowed, <destination>),
    'server_get_combat_speed                     ':  478, # (server_get_combat_speed, <destination>),
    'server_set_combat_speed                     ':  479, # (server_set_combat_speed, <value>),
    'server_get_friendly_fire                    ':  480, # (server_get_friendly_fire, <destination>),
    'server_set_friendly_fire                    ':  481, # (server_set_friendly_fire, <value>),
    'server_get_control_block_dir                ':  482, # (server_get_control_block_dir, <destination>),
    'server_set_control_block_dir                ':  483, # (server_set_control_block_dir, <value>),
    'server_set_password                         ':  484, # (server_set_password, <string_id>),
    'server_get_add_to_game_servers_list         ':  485, # (server_get_add_to_game_servers_list, <destination>),
    'server_set_add_to_game_servers_list         ':  486, # (server_set_add_to_game_servers_list, <value>),
    'server_get_ghost_mode                       ':  487, # (server_get_ghost_mode, <destination>),
    'server_set_ghost_mode                       ':  488, # (server_set_ghost_mode, <value>),
    'server_set_name                             ':  489, # (server_set_name, <string_id>),
    'server_get_max_num_players                  ':  490, # (server_get_max_num_players, <destination>),
    'server_set_max_num_players                  ':  491, # (server_set_max_num_players, <value>),
    'server_set_welcome_message                  ':  492, # (server_set_welcome_message, <string_id>),
    'server_get_melee_friendly_fire              ':  493, # (server_get_melee_friendly_fire, <destination>),
    'server_set_melee_friendly_fire              ':  494, # (server_set_melee_friendly_fire, <value>),
    'server_get_friendly_fire_damage_self_ratio  ':  495, # (server_get_friendly_fire_damage_self_ratio, <destination>),
    'server_set_friendly_fire_damage_self_ratio  ':  496, # (server_set_friendly_fire_damage_self_ratio, <value>),
    'server_get_friendly_fire_damage_friend_ratio':  497, # (server_get_friendly_fire_damage_friend_ratio, <destination>),
    'server_set_friendly_fire_damage_friend_ratio':  498, # (server_set_friendly_fire_damage_friend_ratio, <value>),
    'server_get_anti_cheat                       ':  499, # (server_get_anti_cheat, <destination>),
    'server_set_anti_cheat                       ':  477, # (server_set_anti_cheat, <value>),
    'set_tooltip_text                            ': 1130,  #  (set_tooltip_text, <string_id>),
    'ai_mesh_face_group_show_hide                ': 1805,  #  (ai_mesh_face_group_show_hide, <group_no>, <value>), # 1 for enable, 0 for disable
    'auto_set_meta_mission_at_end_commited       ': 1305,  # (auto_set_meta_mission_at_end_commited), Not documented. Not used in Native. Was (simulate_battle, <value>) before.    
}
operation_ids = {}
for k,v in operation_ids_old.iteritems():
    operation_ids[v] = k.replace(' ','')

    
tag_ids_old = {
    'tag_register       ':  1,
    '$                  ':  2,  # tag_variable
    'str_               ':  3,  # tag_string
    'itm_               ':  4,  # tag_item
    'trp_               ':  5,  # tag_troop
    'fac_               ':  6,  # tag_faction
    'qst_               ':  7,  # tag_quest
    'pt_                ':  8,  # tag_party_tpl
    'p_                 ':  9,  # tag_party
    'scn_               ': 10,  # tag_scene
    'mt_                ': 11,  # tag_mission_tpl
    'mnu_               ': 12,  # tag_menu
    'script_            ': 13,  # tag_script
    'psys_              ': 14,  # tag_particle_sys
    'spr_               ': 15,  # tag_scene_prop
    'snd_               ': 16,  # tag_sound
    ':                  ': 17,  # tag_local_variable
    'icon_              ': 18,  # tag_map_icon
    'skl_               ': 19,  # tag_skill
    'mesh_              ': 20,  # tag_mesh
    'prsnt_             ': 21,  # tag_presentation
    '@                  ': 22,  # tag_quick_string
    'track_  	        ': 23,  # tag_track
    'tableau_           ': 24,  # tag_tableau
    'anim_              ': 25,  # tag_animation
}
tag_ids = {}
for k,v in tag_ids_old.iteritems():
    tag_ids[v] = k.replace(' ','')
    
    
key_ids_old = {
    'key_1': 0x02,
    'key_2': 0x03,
    'key_3': 0x04,
    'key_4': 0x05,
    'key_5': 0x06,
    'key_6': 0x07,
    'key_7': 0x08,
    'key_8': 0x09,
    'key_9': 0x0a,
    'key_0': 0x0b,
    'key_a': 0x1e,
    'key_b': 0x30,
    'key_c': 0x2e,
    'key_d': 0x20,
    'key_e': 0x12,
    'key_f': 0x21,
    'key_g': 0x22,
    'key_h': 0x23,
    'key_i': 0x17,
    'key_j': 0x24,
    'key_k': 0x25,
    'key_l': 0x26,
    'key_m': 0x32,
    'key_n': 0x31,
    'key_o': 0x18,
    'key_p': 0x19,
    'key_q': 0x10,
    'key_r': 0x13,
    'key_s': 0x1f,
    'key_t': 0x14,
    'key_u': 0x16,
    'key_v': 0x2f,
    'key_w': 0x11,
    'key_x': 0x2d,
    'key_y': 0x15,
    'key_z': 0x2c,
    'key_numpad_0': 0x52,
    'key_numpad_1': 0x4f,
    'key_numpad_2': 0x50,
    'key_numpad_3': 0x51,
    'key_numpad_4': 0x4b,
    'key_numpad_5': 0x4c,
    'key_numpad_6': 0x4d,
    'key_numpad_7': 0x47,
    'key_numpad_8': 0x48,
    'key_numpad_9': 0x49,
    'key_num_lock       ': 0x45,
    'key_numpad_slash   ': 0xb5,
    'key_numpad_multiply': 0x37,
    'key_numpad_minus   ': 0x4a,
    'key_numpad_plus    ': 0x4e,
    'key_numpad_enter   ': 0x9c,
    'key_numpad_period  ': 0x53,
    'key_insert   ': 0xd2,
    'key_delete   ': 0xd3,
    'key_home     ': 0xc7,
    'key_end      ': 0xcf,
    'key_page_up  ': 0xc9,
    'key_page_down': 0xd1,
    'key_up     ': 0xc8,
    'key_down   ': 0xd0,
    'key_left   ': 0xcb,
    'key_right  ': 0xcd,
    'key_f1 ': 0x3b,
    'key_f2 ': 0x3c,
    'key_f3 ': 0x3d,
    'key_f4 ': 0x3e,
    'key_f5 ': 0x3f,
    'key_f6 ': 0x40,
    'key_f7 ': 0x41,
    'key_f8 ': 0x42,
    'key_f9 ': 0x43,
    'key_f10': 0x44,
    'key_f11': 0x57,
    'key_f12': 0x58,
    'key_space        ': 0x39,
    'key_escape       ': 0x01,
    'key_enter        ': 0x1c,
    'key_tab          ': 0x0f,
    'key_back_space   ': 0x0e,
    'key_open_braces  ': 0x1a,
    'key_close_braces ': 0x1b,
    'key_comma        ': 0x33,
    'key_period       ': 0x34,
    'key_slash        ': 0x35,
    'key_back_slash   ': 0x2b,
    'key_equals       ': 0x0d,
    'key_minus        ': 0x0c,
    'key_semicolon    ': 0x27,
    'key_apostrophe   ': 0x28,
    'key_tilde        ': 0x29,
    'key_caps_lock    ': 0x3a,
    'key_left_shift    ': 0x2a,
    'key_right_shift   ': 0x36,
    'key_left_control  ': 0x1d,
    'key_right_control ': 0x9d,
    'key_left_alt      ': 0x38,
    'key_right_alt     ': 0xb8,
    'key_left_mouse_button  ': 0xe0,
    'key_right_mouse_button ': 0xe1,
    'key_middle_mouse_button': 0xe2,
    'key_mouse_button_4     ': 0xe3,
    'key_mouse_button_5     ': 0xe4,
    'key_mouse_button_6     ': 0xe5,
    'key_mouse_button_7     ': 0xe6,
    'key_mouse_button_8     ': 0xe7,
    'key_mouse_scroll_up    ': 0xee,
    'key_mouse_scroll_down  ': 0xef,
    'key_xbox_a             ': 0xf0,
    'key_xbox_b             ': 0xf1,
    'key_xbox_x             ': 0xf2,
    'key_xbox_y             ': 0xf3,
    'key_xbox_dpad_up       ': 0xf4,
    'key_xbox_dpad_down     ': 0xf5,
    'key_xbox_dpad_right    ': 0xf6,
    'key_xbox_dpad_left     ': 0xf7,
    'key_xbox_start         ': 0xf8,
    'key_xbox_back          ': 0xf9,
    'key_xbox_rbumper       ': 0xfa,
    'key_xbox_lbumper       ': 0xfb,
    'key_xbox_ltrigger      ': 0xfc,
    'key_xbox_rtrigger      ': 0xfd,
    'key_xbox_rstick        ': 0xfe,
    'key_xbox_lstick        ': 0xff,
}
key_ids = {}
for k,v in key_ids_old.iteritems():
    key_ids[v] = k.replace(' ','')
    
    
game_key_ids_old = {
    'gk_move_forward': 0,
    'gk_move_backward': 1,
    'gk_move_left': 2,
    'gk_move_right': 3,
    'gk_action': 4,
    'gk_jump': 5,
    'gk_attack': 6,
    'gk_defend': 7,
    'gk_kick': 8,
    'gk_toggle_weapon_mode': 9,
    'gk_equip_weapon_1': 10,
    'gk_equip_weapon_2': 11,
    'gk_equip_weapon_3': 12,
    'gk_equip_weapon_4': 13,
    'gk_equip_primary_weapon': 14,
    'gk_equip_secondary_weapon': 15,
    'gk_drop_weapon': 16,
    'gk_sheath_weapon': 17,
    'gk_leave': 18,
    'gk_zoom': 19,
    'gk_view_char': 20,
    'gk_cam_toggle': 21,
    'gk_view_orders': 22,
    'gk_order_1': 23,
    'gk_order_2': 24,
    'gk_order_3': 25,
    'gk_order_4': 26,
    'gk_order_5': 27,
    'gk_order_6': 28,
    'gk_everyone_hear': 29,
    'gk_infantry_hear': 30,
    'gk_archers_hear': 31,
    'gk_cavalry_hear': 32,
    'gk_group3_hear': 33,
    'gk_group4_hear': 34,
    'gk_group5_hear': 35,
    'gk_group6_hear': 36,
    'gk_group7_hear': 37,
    'gk_group8_hear': 38,
    'gk_reverse_order_group': 39,
    'gk_everyone_around_hear': 40,
    'gk_mp_message_all': 41,
    'gk_mp_message_team': 42,
    'gk_character_window': 43,
    'gk_inventory_window': 44,
    'gk_party_window': 45,
    'gk_quests_window': 46,
    'gk_game_log_window': 47,
    'gk_quick_save': 48,
    'gk_crouch': 49,
    'gk_order_7': 50,
    'gk_order_8': 51,
}
game_key_ids = {}
for k,v in game_key_ids_old.iteritems():
    game_key_ids[v] = k.replace(' ','')
    

item_slot_ops = {
    'item_set_slot': (1,),
    'item_get_slot': (2,),
    'item_slot_eq': (1,),
    'item_slot_ge': (1,),
}


item_slot_ids_old = {
    'slot_item_is_checked              ': 0,
    'slot_item_food_bonus              ': 1,
    'slot_item_book_reading_progress   ': 2,
    'slot_item_book_read               ': 3,
    'slot_item_intelligence_requirement': 4,
    'slot_item_amount_available        ': 7,
    'slot_item_urban_demand            ': 11,  #consumer demand for a good in town, measured in abstract units. The more essential the item (ie, like grain) the higher the price
    'slot_item_rural_demand            ': 12,  #consumer demand in villages, measured in abstract units
    'slot_item_desert_demand           ': 13,  #consumer demand in villages, measured in abstract units
    'slot_item_production_slot         ': 14, 
    'slot_item_production_string       ': 15,
    'slot_item_tied_to_good_price      ': 20,  #ie, weapons and metal armor to tools, padded to cloth, leather to leatherwork, etc
    'slot_item_num_positions           ': 22,
    'slot_item_positions_begin         ': 23,  #reserve around 5 slots after this
    'slot_item_multiplayer_faction_price_multipliers_begin': 30,  #reserve around 10 slots after this
    'slot_item_primary_raw_material    		': 50,
    'slot_item_is_raw_material_only_for     ': 51,
    'slot_item_input_number                 ': 52,  #ie, how many items of inputs consumed per run
    'slot_item_base_price                   ': 53,  #taken from module_items
    'slot_item_output_per_run               ': 55,  #number of items produced per run
    'slot_item_overhead_per_run             ': 56,  #labor and overhead per run
    'slot_item_secondary_raw_material       ': 57,  #in this case, the amount used is only one
    'slot_item_enterprise_building_cost     ': 58,  #enterprise building cost
    'slot_item_multiplayer_item_class  ': 60,  #temporary, can be moved to higher values
    'slot_item_multiplayer_availability_linked_list_begin': 61,  #temporary, can be moved to higher values
}
item_slot_ids = {}
for k,v  in item_slot_ids_old.iteritems():
    item_slot_ids[v] = k.replace(' ','')
    

agent_slot_ops = {
    'agent_set_slot': (1,),
    'agent_get_slot': (2,),
    'agent_slot_eq': (1,),
    'agent_slot_ge': (1,),
}


agent_slot_ids_old = {
    'slot_agent_target_entry_point    ': 0,
    'slot_agent_target_x_pos          ': 1,
    'slot_agent_target_y_pos          ': 2,
    'slot_agent_is_alive_before_retreat': 3,
    'slot_agent_is_in_scripted_mode   ': 4,
    'slot_agent_is_not_reinforcement  ': 5,
    'slot_agent_tournament_point      ': 6,
    'slot_agent_arena_team_set        ': 7,
    'slot_agent_spawn_entry_point     ': 8,
    'slot_agent_target_prop_instance  ': 9,
    'slot_agent_map_overlay_id        ': 10,
    'slot_agent_target_entry_point    ': 11,
    'slot_agent_initial_ally_power    ': 12,
    'slot_agent_initial_enemy_power   ': 13,
    'slot_agent_enemy_threat          ': 14,
    'slot_agent_is_running_away       ': 15,
    'slot_agent_courage_score         ': 16,
    'slot_agent_is_respawn_as_bot     ': 17,
    'slot_agent_cur_animation         ': 18,
    'slot_agent_next_action_time      ': 19,
    'slot_agent_state                 ': 20,
    'slot_agent_in_duel_with          ': 21,
    'slot_agent_duel_start_time       ': 22,
    'slot_agent_walker_occupation     ': 25,
    'slot_agent_bought_horse          ': 26,
}
agent_slot_ids = {}
for k,v in agent_slot_ids_old.iteritems():
    agent_slot_ids[v] = k.replace(' ','')
    

faction_slot_ops = {
    'faction_set_slot': (1,),
    'faction_get_slot': (2,),
    'faction_slot_eq': (1,),
    'faction_slot_ge': (1,),   
}


faction_slot_ids_old = {
    'slot_faction_ai_state                  ': 4,
    'slot_faction_ai_object                 ': 5,
    'slot_faction_ai_rationale              ': 6,  #Currently unused, can be linked to strings generated from decision checklists
    'slot_faction_marshall                  ': 8,
    'slot_faction_ai_offensive_max_followers': 9,
    'slot_faction_culture                   ': 10,
    'slot_faction_leader                    ': 11,
    'slot_faction_temp_slot                 ': 12,
    'slot_faction_banner                    ': 15,
    'slot_faction_number_of_parties   ': 20,
    'slot_faction_state               ': 21,
    'slot_faction_adjective           ': 22,
    'slot_faction_player_alarm         		': 30,
    'slot_faction_last_mercenary_offer_time 	': 31,
    'slot_faction_recognized_player    		': 32,
    'slot_faction_quick_battle_tier_1_infantry     ': 41,
    'slot_faction_quick_battle_tier_2_infantry     ': 42,
    'slot_faction_quick_battle_tier_1_archer       ': 43,
    'slot_faction_quick_battle_tier_2_archer       ': 44,
    'slot_faction_quick_battle_tier_1_cavalry      ': 45,
    'slot_faction_quick_battle_tier_2_cavalry      ': 46,
    'slot_faction_tier_1_troop        ': 41,
    'slot_faction_tier_2_troop        ': 42,
    'slot_faction_tier_3_troop        ': 43,
    'slot_faction_tier_4_troop        ': 44,
    'slot_faction_tier_5_troop        ': 45,
    'slot_faction_deserter_troop      ': 48,
    'slot_faction_guard_troop         ': 49,
    'slot_faction_messenger_troop     ': 50,
    'slot_faction_prison_guard_troop  ': 51,
    'slot_faction_castle_guard_troop  ': 52,
    'slot_faction_town_walker_male_troop     ': 53,
    'slot_faction_town_walker_female_troop   ': 54,
    'slot_faction_village_walker_male_troop  ': 55,
    'slot_faction_village_walker_female_troop': 56,
    'slot_faction_town_spy_male_troop        ': 57,
    'slot_faction_town_spy_female_troop      ': 58,
    'slot_faction_has_rebellion_chance': 60,
    'slot_faction_instability         ': 61,  #last time measured
    'slot_faction_war_damage_inflicted_when_marshal_appointed': 62,  #Probably deprecate
    'slot_faction_war_damage_suffered_when_marshal_appointed ': 63,  #Probably deprecate
    'slot_faction_political_issue 							': 64,  #Center or marshal appointment
    'slot_faction_political_issue_time 						': 65,  #Now is used
    'slot_faction_reinforcements_a       ': 77,
    'slot_faction_reinforcements_b       ': 78,
    'slot_faction_reinforcements_c       ': 79,
    'slot_faction_num_armies             ': 80,
    'slot_faction_num_castles            ': 81,
    'slot_faction_num_towns              ': 82,
    'slot_faction_last_attacked_center   ': 85,
    'slot_faction_last_attacked_hours    ': 86,
    'slot_faction_last_safe_hours        ': 87,
    'slot_faction_num_routed_agents      ': 90,
    'slot_faction_biggest_feast_score     ': 91,
    'slot_faction_biggest_feast_time      ': 92,
    'slot_faction_biggest_feast_host      ': 93,
    'slot_faction_last_feast_concluded      ': 94,  #Set when a feast starts -- this needs to be deprecated
    'slot_faction_last_feast_start_time     ': 94,  #this is a bit confusing
    'slot_faction_ai_last_offensive_time 	': 95,  #Set when an offensive concludes
    'slot_faction_last_offensive_concluded 	': 95,  #Set when an offensive concludes
    'slot_faction_ai_last_rest_time      	': 96,  #the last time that the faction has had default or feast AI -- this determines lords' dissatisfaction with the campaign. Set during faction_ai script
    'slot_faction_ai_current_state_started  ': 97,  #
    'slot_faction_ai_last_decisive_event    ': 98,  #capture a fortress or declaration of war
    'slot_faction_morale_of_player_troops   ': 99,
    'slot_faction_truce_days_with_factions_begin 			': 120,
    'slot_faction_provocation_days_with_factions_begin 		': 130,
    'slot_faction_war_damage_inflicted_on_factions_begin 	': 140,
    'slot_faction_sum_advice_about_factions_begin 			': 150,
}
faction_slot_ids = {}
for k,v in faction_slot_ids_old.iteritems():
    faction_slot_ids[v] = k.replace(' ','')
    

party_slot_ops = {
    'party_set_slot': (1,),
    'party_get_slot': (2,),
    'party_slot_eq': (1,),
    'party_slot_ge': (1,),
}


party_slot_ids_old = {
    'slot_party_type                ': 0,  #spt_caravan, spt_town, spt_castle
    'slot_party_retreat_flag        ': 2,
    'slot_party_ignore_player_until ': 3,
    'slot_party_ai_state            ': 4,
    'slot_party_ai_object           ': 5,
    'slot_party_ai_rationale        ': 6,  #Currently unused, but can be used to save a string explaining the lord's thinking
    'slot_town_lord                 ': 7,
    'slot_party_ai_substate         ': 8,
    'slot_town_claimed_by_player    ': 9,
    'slot_town_center        ': 10,
    'slot_town_castle        ': 11,
    'slot_town_prison        ': 12,
    'slot_town_tavern        ': 13,
    'slot_town_store         ': 14,
    'slot_town_arena         ': 16,
    'slot_town_alley         ': 17,
    'slot_town_walls         ': 18,
    'slot_center_culture     ': 19,
    'slot_town_tavernkeeper  ': 20,
    'slot_town_weaponsmith   ': 21,
    'slot_town_armorer       ': 22,
    'slot_town_merchant      ': 23,
    'slot_town_horse_merchant': 24,
    'slot_town_elder         ': 25,
    'slot_center_player_relation ': 26,
    'slot_center_siege_with_belfry ': 27,
    'slot_center_last_taken_by_troop ': 28,
    'slot_party_commander_party ': 30,  #default -1  ,  #Deprecate
    'slot_party_following_player    ': 31,
    'slot_party_follow_player_until_time ': 32,
    'slot_party_dont_follow_player_until_time ': 33,
    'slot_village_raided_by        ': 34,
    'slot_village_state            ': 35,  #svs_normal, svs_being_raided, svs_looted, svs_recovering, svs_deserted
    'slot_village_raid_progress    ': 36,
    'slot_village_recover_progress ': 37,
    'slot_village_smoke_added      ': 38,
    'slot_village_infested_by_bandits   ': 39,
    'slot_center_last_visited_by_lord   ': 41,
    'slot_center_last_player_alarm_hour ': 42,
    'slot_village_player_can_not_steal_cattle ': 46,
    'slot_center_accumulated_rents      ': 47,  #collected automatically by NPC lords
    'slot_center_accumulated_tariffs    ': 48,  #collected automatically by NPC lords
    'slot_town_wealth        ': 49,  #total amount of accumulated wealth in the center, pays for the garrison
    'slot_town_prosperity    ': 50,  #affects the amount of wealth generated
    'slot_town_player_odds   ': 51,
    'slot_party_last_toll_paid_hours ': 52,
    'slot_party_food_store           ': 53,  #used for sieges
    'slot_center_is_besieged_by      ': 54,  #used for sieges
    'slot_center_last_spotted_enemy  ': 55,
    'slot_party_cached_strength        ': 56,
    'slot_party_nearby_friend_strength ': 57,
    'slot_party_nearby_enemy_strength  ': 58,
    'slot_party_follower_strength      ': 59,
    'slot_town_reinforcement_party_template ': 60,
    'slot_center_original_faction           ': 61,
    'slot_center_ex_faction                 ': 62,
    'slot_party_follow_me                   ': 63,
    'slot_center_siege_begin_hours          ': 64,  #used for sieges
    'slot_center_siege_hardness             ': 65,
    'slot_center_sortie_strength            ': 66,
    'slot_center_sortie_enemy_strength      ': 67,
    'slot_party_last_in_combat              ': 68,  #used for AI
    'slot_party_last_in_home_center         ': 69,  #used for AI
    'slot_party_leader_last_courted         ': 70,  #used for AI
    'slot_party_last_in_any_center          ': 71,  #used for AI
    'slot_town_village_product ': 76,
    'slot_town_rebellion_readiness ': 77,
    'slot_town_arena_melee_mission_tpl ': 78,
    'slot_town_arena_torny_mission_tpl ': 79,
    'slot_town_arena_melee_1_num_teams ': 80,
    'slot_town_arena_melee_1_team_size ': 81,
    'slot_town_arena_melee_2_num_teams ': 82,
    'slot_town_arena_melee_2_team_size ': 83,
    'slot_town_arena_melee_3_num_teams ': 84,
    'slot_town_arena_melee_3_team_size ': 85,
    'slot_town_arena_melee_cur_tier    ': 86,
    'slot_center_npc_volunteer_troop_type   ': 90,
    'slot_center_npc_volunteer_troop_amount ': 91,
    'slot_center_mercenary_troop_type  ': 90,
    'slot_center_mercenary_troop_amount': 91,
    'slot_center_volunteer_troop_type  ': 92,
    'slot_center_volunteer_troop_amount': 93,
    'slot_center_ransom_broker         ': 95,
    'slot_center_tavern_traveler       ': 96,
    'slot_center_traveler_info_faction ': 97,
    'slot_center_tavern_bookseller     ': 98,
    'slot_center_tavern_minstrel       ': 99,
    'slot_party_next_looted_item_slot  ': 109,
    'slot_party_looted_item_1          ': 110,
    'slot_party_looted_item_2          ': 111,
    'slot_party_looted_item_3          ': 112,
    'slot_party_looted_item_4          ': 113,
    'slot_party_looted_item_5          ': 114,
    'slot_party_looted_item_1_modifier ': 115,
    'slot_party_looted_item_2_modifier ': 116,
    'slot_party_looted_item_3_modifier ': 117,
    'slot_party_looted_item_4_modifier ': 118,
    'slot_party_looted_item_5_modifier ': 119,
    'slot_village_bound_center         ': 120,
    'slot_village_market_town          ': 121,
    'slot_village_farmer_party         ': 122,
    'slot_party_home_center            ': 123,  #Only use with caravans and villagers
    'slot_center_current_improvement   ': 124,
    'slot_center_improvement_end_hour  ': 125,
    'slot_party_last_traded_center     ': 126, 
    'slot_center_has_manor            ': 130,  #village
    'slot_center_has_fish_pond        ': 131,  #village
    'slot_center_has_watch_tower      ': 132,  #village
    'slot_center_has_school           ': 133,  #village
    'slot_center_has_messenger_post   ': 134,  #town, castle, village
    'slot_center_has_prisoner_tower   ': 135,  #town, castle
    'slot_center_player_enterprise     				  ': 137,  #noted with the item produced
    'slot_center_player_enterprise_production_order    ': 138,
    'slot_center_player_enterprise_consumption_order   ': 139,  #not used
    'slot_center_player_enterprise_days_until_complete ': 139,  #Used instead
    'slot_center_player_enterprise_balance             ': 140,  #not used
    'slot_center_player_enterprise_input_price         ': 141,  #not used
    'slot_center_player_enterprise_output_price        ': 142,  #not used
    'slot_center_has_bandits                        ': 155,
    'slot_town_has_tournament                       ': 156,
    'slot_town_tournament_max_teams                 ': 157,
    'slot_town_tournament_max_team_size             ': 158,
    'slot_center_faction_when_oath_renounced        ': 159,
    'slot_center_walker_0_troop                   ': 160,
    'slot_center_walker_1_troop                   ': 161,
    'slot_center_walker_2_troop                   ': 162,
    'slot_center_walker_3_troop                   ': 163,
    'slot_center_walker_4_troop                   ': 164,
    'slot_center_walker_5_troop                   ': 165,
    'slot_center_walker_6_troop                   ': 166,
    'slot_center_walker_7_troop                   ': 167,
    'slot_center_walker_8_troop                   ': 168,
    'slot_center_walker_9_troop                   ': 169,
    'slot_center_walker_0_dna                     ': 170,
    'slot_center_walker_1_dna                     ': 171,
    'slot_center_walker_2_dna                     ': 172,
    'slot_center_walker_3_dna                     ': 173,
    'slot_center_walker_4_dna                     ': 174,
    'slot_center_walker_5_dna                     ': 175,
    'slot_center_walker_6_dna                     ': 176,
    'slot_center_walker_7_dna                     ': 177,
    'slot_center_walker_8_dna                     ': 178,
    'slot_center_walker_9_dna                     ': 179,
    'slot_center_walker_0_type                    ': 180,
    'slot_center_walker_1_type                    ': 181,
    'slot_center_walker_2_type                    ': 182,
    'slot_center_walker_3_type                    ': 183,
    'slot_center_walker_4_type                    ': 184,
    'slot_center_walker_5_type                    ': 185,
    'slot_center_walker_6_type                    ': 186,
    'slot_center_walker_7_type                    ': 187,
    'slot_center_walker_8_type                    ': 188,
    'slot_center_walker_9_type                    ': 189,
    'slot_town_trade_route_1           ': 190,
    'slot_town_trade_route_2           ': 191,
    'slot_town_trade_route_3           ': 192,
    'slot_town_trade_route_4           ': 193,
    'slot_town_trade_route_5           ': 194,
    'slot_town_trade_route_6           ': 195,
    'slot_town_trade_route_7           ': 196,
    'slot_town_trade_route_8           ': 197,
    'slot_town_trade_route_9           ': 198,
    'slot_town_trade_route_10          ': 199,
    'slot_town_trade_route_11          ': 200,
    'slot_town_trade_route_12          ': 201,
    'slot_town_trade_route_13          ': 202,
    'slot_town_trade_route_14          ': 203,
    'slot_town_trade_route_15          ': 204,
    'slot_village_number_of_cattle   ': 205,
    'slot_center_head_cattle         ': 205,  #dried meat, cheese, hides, butter
    'slot_center_head_sheep			': 206,  #sausages, wool
    'slot_center_head_horses		 	': 207,  #horses can be a trade item used in tracking but which are never offered for sale
    'slot_center_acres_pasture       ': 208,  #pasture area for grazing of cattles and sheeps, if this value is high then number of cattles and sheeps increase faster
    'slot_production_sources_begin   ': 209,
    'slot_center_acres_grain			': 209,  #grain
    'slot_center_acres_olives        ': 210,  #olives
    'slot_center_acres_vineyard		': 211,  #fruit
    'slot_center_acres_flax          ': 212,  #flax
    'slot_center_acres_dates			': 213,  #dates
    'slot_center_fishing_fleet		': 214,  #smoked fish
    'slot_center_salt_pans		    ': 215,  #salt
    'slot_center_apiaries       		': 216,  #honey
    'slot_center_silk_farms			': 217,  #silk
    'slot_center_kirmiz_farms		': 218,  #dyes
    'slot_center_iron_deposits       ': 219,  #iron
    'slot_center_fur_traps			': 220,  #furs
    'slot_center_mills				': 221,  #bread
    'slot_center_breweries			': 222,  #ale
    'slot_center_wine_presses		': 223,  #wine
    'slot_center_olive_presses		': 224,  #oil
    'slot_center_linen_looms			': 225,  #linen
    'slot_center_silk_looms          ': 226,  #velvet
    'slot_center_wool_looms          ': 227,  #wool cloth
    'slot_center_pottery_kilns		': 228,  #pottery
    'slot_center_smithies			': 229,  #tools
    'slot_center_tanneries			': 230,  #leatherwork
    'slot_center_shipyards			': 231,  #naval stores - uses timber, pitch, and linen
    'slot_center_household_gardens   ': 232,  #cabbages
    'slot_production_sources_end ': 233,
    'slot_town_last_nearby_fire_time                         ': 240,
    'slot_party_following_orders_of_troop        ': 244,
    'slot_party_orders_type				        ': 245,
    'slot_party_orders_object				    ': 246,
    'slot_party_orders_time				    	': 247,
    'slot_party_temp_slot_1			            ': 248,  #right now used only within a single script, merchant_road_info_to_s42, to denote closed roads. Now also used in comparative scripts
    'slot_party_under_player_suggestion			': 249,  #move this up a bit
    'slot_town_trade_good_prices_begin 			': 250,
    'slot_center_last_reconnoitered_by_faction_time 				': 350,
}
party_slot_ids = {}
for k,v in party_slot_ids_old.iteritems():
    party_slot_ids[v] = k.replace(' ','')
    

scene_slot_ops = {
    'scene_set_slot': (1,),
    'scene_get_slot': (2,),
    'scene_slot_eq': (1,),
    'scene_slot_ge': (1,),
}


scene_slot_ids_old = {
    'slot_scene_visited              ': 0,
    'slot_scene_belfry_props_begin   ': 10,
}
scene_slot_ids = {}
for k,v in scene_slot_ids_old.iteritems():
    scene_slot_ids[v] = k.replace(' ','')
    

troop_slot_ops = {
    'troop_set_slot': (1,),
    'troop_get_slot': (2,),
    'troop_slot_eq': (1,),
    'troop_slot_ge': (1,),
}


troop_slot_ids_old = {
    'slot_troop_occupation          ': 2,  # 0 ': free, 1 ': merchant
    'slot_troop_state               ': 3, 
    'slot_troop_last_talk_time      ': 4,
    'slot_troop_met                 ': 5, #i also use this for the courtship state -- may become cumbersome
    'slot_troop_courtship_state     ': 5, #2 professed admiration, 3 agreed to seek a marriage, 4 ended relationship
    'slot_troop_party_template      ': 6,
    'slot_troop_renown              ': 7,
    'slot_troop_prisoner_of_party   ': 8,  # important for heroes only
    'slot_troop_present_at_event    ': 9,
    'slot_troop_leaded_party         ': 10, # important for kingdom heroes only
    'slot_troop_wealth               ': 11, # important for kingdom heroes only
    'slot_troop_cur_center           ': 12, # important for royal family members only (non-kingdom heroes)
    'slot_troop_banner_scene_prop    ': 13, # important for kingdom heroes and player only
    'slot_troop_original_faction     ': 14, # for pretenders
    'slot_troop_player_order_state   ': 16, #Deprecated
    'slot_troop_player_order_object  ': 17, #Deprecated
    'slot_troop_age                 ':  18,
    'slot_troop_age_appearance      ':  19,
    'slot_troop_does_not_give_quest ': 20,
    'slot_troop_player_debt         ': 21,
    'slot_troop_player_relation     ': 22,
    'slot_troop_last_quest          ': 24,
    'slot_troop_last_quest_betrayed ': 25,
    'slot_troop_last_persuasion_time': 26,
    'slot_troop_last_comment_time   ': 27,
    'slot_troop_spawned_before      ': 28,
    'slot_troop_last_comment_slot   ': 29,
    'slot_troop_spouse              ': 30,
    'slot_troop_father              ': 31,
    'slot_troop_mother              ': 32,
    'slot_troop_guardian            ': 33, #Usually siblings are identified by a common parent.This is used for brothers if the father is not an active npc. At some point we might introduce geneologies
    'slot_troop_betrothed           ': 34, #Obviously superseded once slot_troop_spouse is filled
    'slot_troop_love_interest_1     ': 35, #each unmarried lord has three love interests
    'slot_troop_love_interest_2     ': 36,
    'slot_troop_love_interest_3     ': 37,
    'slot_troop_love_interests_end  ': 38,
    'slot_lady_no_messages          				': 37,
    'slot_lady_last_suitor          				': 38,
    'slot_lord_granted_courtship_permission      ': 38,
    'slot_troop_betrothal_time                   ': 39, #used in scheduling the wedding
    'slot_troop_trainer_met                       ': 30,
    'slot_troop_trainer_waiting_for_result        ': 31,
    'slot_troop_trainer_training_fight_won        ': 32,
    'slot_troop_trainer_num_opponents_to_beat     ': 33,
    'slot_troop_trainer_training_system_explained ': 34,
    'slot_troop_trainer_opponent_troop            ': 35,
    'slot_troop_trainer_training_difficulty       ': 36,
    'slot_troop_trainer_training_fight_won        ': 37,
    'slot_lady_used_tournament					': 40,
    'slot_troop_current_rumor                ': 45,
    'slot_troop_temp_slot                    ': 46,
    'slot_troop_promised_fief                ': 47,
    'slot_troop_set_decision_seed                ': 48, #Does not change
    'slot_troop_temp_decision_seed               ': 49, #Resets at recalculate_ai
    'slot_troop_recruitment_random               ': 50, #used in a number of different places in the intrigue procedures to overcome intermediate hurdles, although not for the final calculation, might be replaced at some point by the global decision seed
    'slot_troop_intrigue_impatience          ': 51,
    'slot_lord_reputation_type     		  ': 52,
    'slot_lord_recruitment_argument        ': 53, #the last argument proposed by the player to the lord
    'slot_lord_recruitment_candidate       ': 54, #the last candidate proposed by the player to the lord
    'slot_troop_change_to_faction          ': 55,
    'slot_troop_first_encountered          ': 59,
    'slot_troop_home                       ': 60,
    'slot_troop_morality_state             ': 61,
    'slot_troop_morality_type              ': 62,
    'slot_troop_morality_value             ': 63,
    'slot_troop_2ary_morality_type            ': 64,
    'slot_troop_2ary_morality_state           ': 65,
    'slot_troop_2ary_morality_value           ': 66,
    'slot_troop_town_with_contacts            ': 67,
    'slot_troop_town_contact_type             ': 68, #1 are nobles, 2 are commons
    'slot_troop_morality_penalties            ': 69, ### accumulated grievances from morality conflicts
    'slot_troop_personalityclash_object       ': 71,
    'slot_troop_personalityclash_state        ': 72, #1 ': pclash_penalty_to_self, 2 ': pclash_penalty_to_other, 3 ': pclash_penalty_to_other,
    'slot_troop_personalityclash2_object      ': 73,
    'slot_troop_personalityclash2_state       ': 74,
    'slot_troop_personalitymatch_object       ': 75,
    'slot_troop_personalitymatch_state        ': 76,
    'slot_troop_personalityclash_penalties    ': 77, ### accumulated grievances from personality clash
    'slot_troop_personalityclash_penalties    ': 77, ### accumulated grievances from personality clash
    'slot_troop_home_speech_delivered         ': 78, #only for companions
    'slot_troop_discussed_rebellion           ': 78, #only for pretenders
    'slot_lady_courtship_heroic_recited       ': 74,
    'slot_lady_courtship_allegoric_recited    ': 75,
    'slot_lady_courtship_comic_recited        ': 76,
    'slot_lady_courtship_mystic_recited       ': 77,
    'slot_lady_courtship_tragic_recited 	     ': 78,
    'slot_troop_met_previously                ': 80,
    'slot_troop_turned_down_twice             ': 81,
    'slot_troop_playerparty_history           ': 82,
    'slot_troop_playerparty_history_string    ': 83,
    'slot_troop_return_renown                 ': 84,
    'slot_troop_custom_banner_bg_color_1      ': 85,
    'slot_troop_custom_banner_bg_color_2      ': 86,
    'slot_troop_custom_banner_charge_color_1  ': 87,
    'slot_troop_custom_banner_charge_color_2  ': 88,
    'slot_troop_custom_banner_charge_color_3  ': 89,
    'slot_troop_custom_banner_charge_color_4  ': 90,
    'slot_troop_custom_banner_bg_type         ': 91,
    'slot_troop_custom_banner_charge_type_1   ': 92,
    'slot_troop_custom_banner_charge_type_2   ': 93,
    'slot_troop_custom_banner_charge_type_3   ': 94,
    'slot_troop_custom_banner_charge_type_4   ': 95,
    'slot_troop_custom_banner_flag_type       ': 96,
    'slot_troop_custom_banner_num_charges     ': 97,
    'slot_troop_custom_banner_positioning     ': 98,
    'slot_troop_custom_banner_map_flag_type   ': 99,
    'slot_troop_intro 						': 101,
    'slot_troop_intro_response_1 			': 102,
    'slot_troop_intro_response_2 			': 103,
    'slot_troop_backstory_a 					': 104,
    'slot_troop_backstory_b 					': 105,
    'slot_troop_backstory_c 					': 106,
    'slot_troop_backstory_delayed 			': 107,
    'slot_troop_backstory_response_1 		': 108,
    'slot_troop_backstory_response_2 		': 109,
    'slot_troop_signup   					': 110,
    'slot_troop_signup_2 					': 111,
    'slot_troop_signup_response_1 			': 112,
    'slot_troop_signup_response_2 			': 113,
    'slot_troop_mentions_payment 			': 114, #Not actually used
    'slot_troop_payment_response 			': 115, #Not actually used
    'slot_troop_morality_speech   			': 116,
    'slot_troop_2ary_morality_speech 		': 117,
    'slot_troop_personalityclash_speech 		': 118,
    'slot_troop_personalityclash_speech_b 	': 119,
    'slot_troop_personalityclash2_speech 	': 120,
    'slot_troop_personalityclash2_speech_b 	': 121,
    'slot_troop_personalitymatch_speech 		': 122,
    'slot_troop_personalitymatch_speech_b 	': 123,
    'slot_troop_retirement_speech 			': 124,
    'slot_troop_rehire_speech 				': 125,
    'slot_troop_home_intro           		': 126,
    'slot_troop_home_description    			': 127,
    'slot_troop_home_description_2 			': 128,
    'slot_troop_home_recap         			': 129,
    'slot_troop_honorific   					': 130,
    'slot_troop_kingsupport_string_1			': 131,
    'slot_troop_kingsupport_string_2			': 132,
    'slot_troop_kingsupport_string_2a		': 133,
    'slot_troop_kingsupport_string_2b		': 134,
    'slot_troop_kingsupport_string_3			': 135,
    'slot_troop_kingsupport_objection_string	': 136,
    'slot_troop_intel_gathering_string	    ': 137,
    'slot_troop_fief_acceptance_string	    ': 138,
    'slot_troop_woman_to_woman_string	    ': 139,
    'slot_troop_turn_against_string	        ': 140,
    'slot_troop_strings_end 					': 141,
    'slot_troop_payment_request 				': 141,
    'slot_troop_kingsupport_state			': 142,
    'slot_troop_kingsupport_argument			': 143,
    'slot_troop_kingsupport_opponent			': 144,
    'slot_troop_kingsupport_objection_state  ': 145, #0, default, 1, needs to voice, 2, has voiced
    'slot_troop_days_on_mission		        ': 150,
    'slot_troop_current_mission			    ': 151,
    'slot_troop_mission_object               ': 152,
    'slot_troop_player_routed_agents         ': 146,
    'slot_troop_ally_routed_agents           ': 147,
    'slot_troop_enemy_routed_agents          ': 148,
    'slot_troop_mission_participation        ': 149,
    'slot_troop_controversy                  ': 150, #Determines whether or not a troop is likely to receive fief or marshalship
    'slot_troop_recent_offense_type 	        ': 151, #failure to join army, failure to support colleague
    'slot_troop_recent_offense_object        ': 152, #to whom it happened
    'slot_troop_recent_offense_time          ': 153,
    'slot_troop_stance_on_faction_issue      ': 154, #when it happened
    'slot_troop_will_join_prison_break       ': 161,
}
troop_slot_ids = {}
for k,v in troop_slot_ids_old.iteritems():
    troop_slot_ids[v] = k.replace(' ','')


player_slot_ops = {
    'player_set_slot': (1,),
    'player_get_slot': (2,),
    'player_slot_eq': (1,),
    'player_slot_ge': (1,),
}

    
player_slot_ids_old = {
    'slot_player_spawned_this_round                ': 0,
    'slot_player_last_rounds_used_item_earnings    ': 1,
    'slot_player_selected_item_indices_begin       ': 2,
    'slot_player_selected_item_indices_end         ': 11,
    'slot_player_cur_selected_item_indices_end     ': 20,
    'slot_player_join_time                         ': 21,
    'slot_player_button_index                      ': 22, #used for presentations
    'slot_player_can_answer_poll                   ': 23,
    'slot_player_first_spawn                       ': 24,
    'slot_player_spawned_at_siege_round            ': 25,
    'slot_player_poll_disabled_until_time          ': 26,
    'slot_player_total_equipment_value             ': 27,
    'slot_player_last_team_select_time             ': 28,
    'slot_player_death_pos_x                       ': 29,
    'slot_player_death_pos_y                       ': 30,
    'slot_player_death_pos_z                       ': 31,
    'slot_player_damage_given_to_target_1          ': 32, #used only in destroy mod
    'slot_player_damage_given_to_target_2          ': 33, #used only in destroy mod
    'slot_player_last_bot_count                    ': 34,
    'slot_player_bot_type_1_wanted                 ': 35,
    'slot_player_bot_type_2_wanted                 ': 36,
    'slot_player_bot_type_3_wanted                 ': 37,
    'slot_player_bot_type_4_wanted                 ': 38,
    'slot_player_spawn_count                       ': 39,
}
player_slot_ids = {}
for k,v in player_slot_ids_old.iteritems():
    player_slot_ids[v] = k.replace(' ','')
    

quest_slot_ops = {
    'quest_set_slot': (1,),
    'quest_get_slot': (2,),
    'quest_slot_eq': (1,),
    'quest_slot_ge': (1,),
}


quest_slot_ids_old = {
    'slot_quest_target_center           ': 1,
    'slot_quest_target_troop            ': 2,
    'slot_quest_target_faction          ': 3,
    'slot_quest_object_troop            ': 4,
    'slot_quest_giver_troop             ': 6,
    'slot_quest_object_center           ': 7,
    'slot_quest_target_party            ': 8,
    'slot_quest_target_party_template   ': 9,
    'slot_quest_target_amount           ': 10,
    'slot_quest_current_state           ': 11,
    'slot_quest_giver_center            ': 12,
    'slot_quest_target_dna              ': 13,
    'slot_quest_target_item             ': 14,
    'slot_quest_object_faction          ': 15,
    'slot_quest_target_state            ': 16,
    'slot_quest_object_state            ': 17,
    'slot_quest_convince_value          ': 19,
    'slot_quest_importance              ': 20,
    'slot_quest_xp_reward               ': 21,
    'slot_quest_gold_reward             ': 22,
    'slot_quest_expiration_days         ': 23,
    'slot_quest_dont_give_again_period  ': 24,
    'slot_quest_dont_give_again_remaining_days': 25,
    'slot_quest_failure_consequence     ': 26,
    'slot_quest_temp_slot      		   ': 27,
}
quest_slot_ids = {}
for k,v in quest_slot_ids_old.iteritems():
    quest_slot_ids[v] = k.replace(' ','')

    
party_template_slot_ops = {
    'party_template_set_slot': (1,),
    'party_template_get_slot': (2,),
    'party_template_slot_eq': (1,),
    'party_template_slot_ge': (1,),
}

    
party_template_slot_ids_old = {
    'slot_party_template_num_killed   ': 1,
    'slot_party_template_lair_type    	 	': 3,
    'slot_party_template_lair_party    		': 4,
    'slot_party_template_lair_spawnpoint     ': 5,
}
party_template_slot_ids = {}
for k,v in party_template_slot_ids_old.iteritems():
    party_template_slot_ids[v] = k.replace(' ','')
    

scene_prop_slot_ops = {
    'scene_prop_set_slot': (1,),
    'scene_prop_get_slot': (2,),
    'scene_prop_slot_eq': (1,),
    'scene_prop_slot_ge': (1,),
}


scene_prop_slot_ids_old = {
    'scene_prop_open_or_close_slot       ': 1,
    'scene_prop_smoke_effect_done        ': 2,
    'scene_prop_number_of_agents_pushing ': 3, #for belfries only
    'scene_prop_next_entry_point_id      ': 4, #for belfries only
    'scene_prop_belfry_platform_moved    ': 5, #for belfries only
    'scene_prop_slots_end                ': 6,
}
scene_prop_slot_ids = {}
for k,v in scene_prop_slot_ids_old.iteritems():
    scene_prop_slot_ids[v] = k.replace(' ','')
    

team_slot_ops = {
    'team_set_slot': (1,),
    'team_get_slot': (2,),
    'team_slot_eq': (1,),
    'team_slot_ge': (1,),
}


team_slot_ids = {0:'slot_team_flag_situation'}


string_register_ops = {
    'prop_instance_set_material': (2,),
    'str_is_empty': (0,),
    'str_clear': (0,),
    'str_store_string': (0,),
    'str_store_string_reg': (0,1,),
    'str_store_troop_name': (0,),
    'str_store_troop_name_plural': (0,),
    'str_store_troop_name_by_count': (0,),
    'str_store_item_name': (0,),
    'str_store_item_name_plural': (0,),
    'str_store_item_name_by_count': (0,),
    'str_store_party_name': (0,),
    'str_store_agent_name': (0,),
    'str_store_faction_name': (0,),
    'str_store_quest_name': (0,),
    'str_store_info_page_name': (0,),
    'str_store_date': (0,),
    'str_store_troop_name_link': (0,),
    'str_store_party_name_link': (0,),
    'str_store_faction_name_link': (0,),
    'str_store_quest_name_link': (0,),
    'str_store_info_page_name_link': (0,),
    'str_store_class_name': (0,),
    'game_key_get_mapped_key_name': (0,),
    'str_store_player_username': (0,),
    'str_store_server_password': (0,),
    'str_store_server_name': (0,),
    'str_store_welcome_message': (0,),
    'str_encode_url': (0,),
}


pos_register_ops = {
    'prop_instance_get_position': (0,),
    'prop_instance_get_starting_position': (0,),
    'prop_instance_set_position': (1,),
    'prop_instance_animate_to_position': (1,),
    'prop_instance_get_animation_target_position': (0,),
    'prop_instance_get_scale': (0,),
    'prop_instance_rotate_to_position': (1,),
    'prop_instance_dynamics_set_properties': (1,),
    'prop_instance_dynamics_set_velocity': (1,),
    'prop_instance_dynamics_set_omega': (1,),
    'prop_instance_dynamics_apply_impulse': (1,),
    'set_spawn_position': (0,),
    'particle_system_burst': (1,),
    'agent_get_position': (0,),
    'agent_set_position': (1,),
    'agent_get_speed': (0,),
    'agent_set_scripted_destination': (1,),
    'agent_set_scripted_destination_no_attack': (1,),
    'agent_get_scripted_destination': (0,),
    'agent_get_look_position': (0,),
    'agent_set_look_target_position': (1,),
    'team_set_order_position': (2,),
    'team_get_order_position': (0,),
    'overlay_get_position': (0,),
    'overlay_set_position': (1,),
    'overlay_set_size': (1,),
    'overlay_set_area_size': (1,),
    'overlay_animate_to_position': (2,),
    'overlay_animate_to_size': (2,),
    'overlay_set_mesh_rotation': (1,),
    'show_item_details': (1,),
    'show_item_details_with_modifier': (2,),
    'show_troop_details': (1,),
    'get_trigger_object_position': (0,),
    'mouse_get_position': (0,),
    'party_set_position': (1,),
    'party_set_ai_target_position': (1,),
    'party_get_ai_target_position': (0,),
    'play_sound_at_position': (1,),
    'init_position': (0,),
    'position_get_x': (1,),
    'position_get_y': (1,),
    'position_get_z': (1,),
    'position_set_x': (0,),
    'position_set_y': (0,),
    'position_set_z': (0,),
    'position_move_x': (0,),
    'position_move_y': (0,),
    'position_move_z': (0,),
    'position_set_z_to_ground_level': (0,), 
    'position_get_distance_to_terrain': (1,),
    'position_get_distance_to_ground_level': (1,),
    'position_get_rotation_around_x': (1,),
    'position_get_rotation_around_y': (1,),
    'position_get_rotation_around_z': (1,),
    'position_rotate_x': (0,), 
    'position_rotate_y': (0,),
    'position_rotate_z': (0,),
    'position_rotate_x_floating': (0,),
    'position_rotate_x_floating': (0,),
    'position_rotate_x_floating': (0,),
    'position_get_scale_x': (1,),
    'position_get_scale_y': (1,),
    'position_get_scale_z': (1,),
    'position_set_scale_x': (0,),
    'position_set_scale_y': (0,),
    'position_set_scale_z': (0,),
    'get_angle_between_positions': (1,2,),
    'position_has_line_of_sight_to_position': (0,1,),
    'get_distance_between_positions': (1,2),
    'get_distance_between_positions_in_meters': (1,2),
    'get_sq_distance_between_positions': (1,2,),
    'get_sq_distance_between_positions_in_meters': (1,2,),
    'position_is_behind_position': (0,1,),
    'get_sq_distance_between_position_heights': (1,2),
    'position_normalize_origin': (1,),
    'position_get_screen_projection': (0,1,),
    'cur_tableau_add_tableau_mesh': (2,),
    'cur_tableau_set_camera_position': (0,),
    'cur_tableau_add_point_light': (0,),
    'cur_tableau_add_sun_light': (0,),
    'cur_tableau_add_mesh': (1,),
    'cur_tableau_add_mesh_with_vertex_color': (1,),
    'cur_tableau_add_mesh_with_scale_and_vertex_color': (1,2,),
    'cur_tableau_add_map_icon': (1,),
    'cur_tableau_add_troop': (1,),
    'cur_tableau_add_horse': (1,),
    'tutorial_message_set_position': (0,1,),
    'set_game_menu_tableau_mesh': (2,),
    'entry_point_get_position': (0,),
    'entry_point_set_position': (1,),
    'get_startup_sun_light': (0,),
    'get_startup_ambient_light': (0,),
    'get_startup_ground_ambient_light': (0,),
    'get_scene_boundaries': (0,1,),
    'mission_cam_get_position': (0,),
    'mission_cam_set_position': (0,),
    'mission_cam_animate_to_position': (0,),
    'mission_cam_animate_to_position_and_aperture': (0,),
    'mouse_get_world_projection': (0,1,),
    'set_spawn_position': (0,), 
}


slto_ids_old = {
    'slto_inactive          ': 0, #for companions at the beginning of the game
    'slto_kingdom_hero      ': 2,
    'slto_player_companion  ': 5, #This is specifically for companions in the employ of the player -- ie, in the party, or on a mission
    'slto_kingdom_lady      ': 6, #Usually inactive (Calradia is a traditional place). However, can be made potentially active if active_npcs are expanded to include ladies
    'slto_kingdom_seneschal ': 7,
    'slto_robber_knight     ': 8,
    'slto_inactive_pretender': 9,
    'slto_retirement        ': 11,
}
slto_ids = {}
for k,v in slto_ids_old.iteritems():
    slto_ids[v] = k.replace(' ','')
    

#-----------------------------------------------------------------------------#


def decompile_statement(statement,localVarList,localVarFirstAppearList,localVarLoopIndexList):
    statement_code = '''('''
    if len(statement)<2:
        print "Error. Too short statement."
    
    op = int(statement[0])
    op_code = ''''''
    operation_id_keys = operation_ids.keys()
    operation_id_keys.sort()
    operation_id_keys.reverse()
    for each_op in operation_id_keys:
        if op&each_op==each_op:
            op_code += "|%s" %operation_ids[each_op]
            op -= each_op
        if op==0:
            break
    op_code = op_code.replace('|','',1)
    statement_code += "%s" %op_code   # no comma, for something like (try_begin),
    
    num_params = int(statement[1])
    if num_params==0:
        statement_code += ")"
        return statement_code
    
    for p in xrange(num_params):
        this_param = int(statement[p+2])    # 1st position of this statement is the operation, 2nd position is the count of parameters
        
        tag_id = this_param >> 56
        param_id = this_param&0xffffffffffffff
        
        try:
            if tag_id==17:   # local variable
                param_code = '''":local_var_%d"''' %param_id   # cannot get the original name of an local variable, use this instead
                if param_code not in localVarList:    # first appearance
                    localVarList += [param_code]    # if this is the first time a parameter appears in a block, add it to local variables list
                    localVarFirstAppearList += [param_code]
                else:    # not the first appearance
                    paramIsLoopIndex = 0
                    if ('try_for_range' in op_code) and (p==0):
                        paramIsLoopIndex = 1
                    elif ('assign' in op_code) and (p==0):
                        paramIsLoopIndex = 1    # in face it's not a loop index but still it is not used in this block. i just dont wanna create a new variable, si use the pre-exsited one
                    if (param_code in localVarFirstAppearList) and (not paramIsLoopIndex):
                        localVarFirstAppearList.remove(param_code)    # if the parameter re-appears in a block, remove this parameter from the local variables list
            elif tag_id==2:   # global variable
                param_code = '''"""$%s"""''' %global_variable_ids[param_id]
            elif tag_id==22:   # quick string
                param_code = '''"""@%s"""''' %quick_string_ids[param_id]
            elif tag_id==3:
                param_code = '''"%s"''' %string_ids[param_id]
            elif tag_id==4:
                param_code = '''"%s"''' %item_ids[param_id]
            elif tag_id==5:
                param_code = '''"%s"''' %troop_ids[param_id]
            elif tag_id==6:
                param_code = '''"%s"''' %faction_ids[param_id]
            elif tag_id==7:
                param_code = '''"%s"''' %quest_ids[param_id]
            elif tag_id==8:
                param_code = '''"%s"''' %party_template_ids[param_id]
            elif tag_id==9:
                param_code = '''"%s"''' %party_ids[param_id]
            elif tag_id==10:
                param_code = '''"%s"''' %scene_ids[param_id]
            elif tag_id==11:
                param_code = '''"%s"''' %mission_template_ids[param_id]
            elif tag_id==12:
                param_code = '''"%s"''' %menu_ids[param_id]
            elif tag_id==13:
                param_code = '''"%s"''' %script_ids[param_id]
            elif tag_id==14:
                param_code = '''"%s"''' %particle_system_ids[param_id]
            elif tag_id==15:
                param_code = '''"%s"''' %scene_prop_ids[param_id]
            elif tag_id==16:
                param_code = '''"%s"''' %sound_ids[param_id]
            elif tag_id==18:
                param_code = '''"%s"''' %map_icon_ids[param_id]
            elif tag_id==19:
                param_code = '''"%s"''' %skill_ids[param_id]
            elif tag_id==20:
                param_code = '''"%s"''' %mesh_ids[param_id]
            elif tag_id==21:
                param_code = '''"%s"''' %presentation_ids[param_id]
            elif tag_id==23:
                param_code = '''"%s"''' %track_ids[param_id]
            elif tag_id==24:
                param_code = '''"%s"''' %tableau_material_ids[param_id]
            elif tag_id==25:
                param_code = '''"%s"''' %animation_ids[param_id]
            elif tag_id==1:
                param_code = "reg%d" %param_id
            elif tag_id==0:   # possible: string register, position register, slot, keys, constant, info_page variable
                if (op_code in pos_register_ops) and (p in pos_register_ops[op_code]):
                    param_code = "pos%d" %param_id
                elif (op_code in string_register_ops) and (p in string_register_ops[op_code]):
                    param_code = "s%d" %param_id
                elif (op_code in faction_slot_ops) and (p in faction_slot_ops[op_code]):
                    if param_id in faction_slot_ids:
                        param_code = faction_slot_ids[param_id]
                    else:
                        param_code = str(param_id)
                elif (op_code in item_slot_ops) and (p in item_slot_ops[op_code]):
                    if param_id in item_slot_ids:
                        param_code = item_slot_ids[param_id]
                    else:
                        param_code = str(param_id)
                elif (op_code in agent_slot_ops) and (p in agent_slot_ops[op_code]):
                    if param_id in agent_slot_ids:
                        param_code = agent_slot_ids[param_id]
                    else:
                        param_code = str(param_id)
                elif (op_code in player_slot_ops) and (p in player_slot_ops[op_code]):
                    param_code = player_slot_ids[param_id]
                elif (op_code in party_slot_ops) and (p in party_slot_ops[op_code]):
                    if param_id in party_slot_ids:
                        param_code = party_slot_ids[param_id]
                    elif param_id in quest_slot_ids:
                        param_code = quest_slot_ids[param_id]
                    else:
                        param_code = str(param_id)
                elif (op_code in party_template_slot_ops) and (p in party_template_slot_ops[op_code]):
                    if param_id in party_template_slot_ids:
                        param_code = party_template_slot_ids[param_id]
                    else:
                        param_code = str(param_id)
                elif (op_code in quest_slot_ops) and (p in quest_slot_ops[op_code]):
                    param_code = quest_slot_ids[param_id]
                elif (op_code in scene_slot_ops) and (p in scene_slot_ops[op_code]):
                    param_code = scene_slot_ids[param_id]
                elif (op_code in scene_prop_slot_ops) and (p in scene_prop_slot_ops[op_code]):
                    param_code = scene_prop_slot_ids[param_id]
                elif (op_code in team_slot_ops) and (p in team_slot_ops[op_code]):
                    param_code = team_slot_ids[param_id]
                elif (op_code in troop_slot_ops) and (p in troop_slot_ops[op_code]):
                    if param_id in troop_slot_ids:
                        param_code = troop_slot_ids[param_id]
                    elif param_id in slto_ids:
                        param_code = slto_ids[param_id]
                    else:
                        param_code = str(param_id)
                elif ('key_is_down' in op_code) or ('key_clicked' in op_code):
                    if param_id in key_ids:
                        param_code = key_ids[param_id]
                    else:
                        param_code = str(param_id).replace('L','')
                elif ('game_key_is_down' in op_code) or ('game_key_clicked' in op_code):
                    if param_id in game_key_ids:
                        param_code = game_key_ids[param_id]
                    else:
                        param_code = str(param_id).replace('L','')
                else:   # Others all treated as constants. Maybe will be fixed, in future.
                    param_code = str(param_id)
            elif this_param<0:   # negative value can only be constant
                param_code = str(this_param)
            else:
                print "Error. Invalid tag id: %d." %tag_id , statement
            
        except KeyError:
            param_code = str(param_id)
            
        statement_code += ", %s" %param_code
    
    statement_code += ")"
    return statement_code


def decompile_statement_block(block):   # block is a string filled with integers and spaces
    indent = 3
    
    block_code = '''        ['''
    block = block.split()
    pos = 0
    num_ops = int(block[pos])
    
    localVarList = []
    localVarFirstAppearList = []
    localVarLoopIndexList = []
    while num_ops:
        pos += 1
        this_op = block[pos]
        begin_pos = pos
        
        pos += 1
        num_params = int(block[pos])
        pos += num_params
        end_pos = pos
        
        this_statement = block[begin_pos:end_pos+1]
        this_statement_code = decompile_statement(this_statement,localVarList,localVarFirstAppearList,localVarLoopIndexList)
        if ('try_end' in this_statement_code) or ('end_try' in this_statement_code) or ('else_try' in this_statement_code):
            indent -= 1
        block_code += "\n%s%s," %('    '*indent,this_statement_code)
        if ('(try_begin)' in this_statement_code) or ('(try_for' in this_statement_code) or ('(else_try)' in this_statement_code):
            indent += 1
        num_ops -= 1
        
    if pos<len(block)-1:
        print "Something is wrong. Block is not fully used."
        
    block_code += '''\n        ]'''
    
    for eachLocalVar in localVarFirstAppearList:    # if there are still unused local var, that is only used as a loop index
        #print type(eachLocalVar),eachLocalVar,eachLocalVar=='''":local_var_29"'''
        block_code = block_code.replace(eachLocalVar,'''":unused"''')
    
    return block_code



if __name__=='__main__':
    print decompile_statement_block('52 21 1 1224979098644774912 22 1 1224979098644774913 2133 2 1224979098644774914 0 4 0 1073741855 2 1224979098644774912 360287970189639680 1073741855 2 1224979098644774912 360287970189640045 31 2 1224979098644774912 360287970189640044 5 0 33 3 1224979098644774912 360287970189640300 360287970189640305 5 0 2171 2 1224979098644774915 1224979098644774912 2133 2 1224979098644774914 1224979098644774915 2105 2 1224979098644774914 3 2107 2 1224979098644774914 1224979098644774914 2108 2 1224979098644774914 25 3 0 4 0 32 2 1224979098644774914 40 2147483681 3 1224979098644774912 360287970189640175 360287970189640195 520 3 1224979098644774916 1224979098644774912 172 31 2 1224979098644774916 2 2107 2 1224979098644774914 4 2108 2 1224979098644774914 3 3 0 4 0 152 1 1224979098644774912 2107 2 1224979098644774914 5 2108 2 1224979098644774914 3 3 0 4 0 33 3 1224979098644774912 360287970189639737 360287970189639764 2107 2 1224979098644774914 5 2108 2 1224979098644774914 3 3 0 4 0 33 3 1224979098644774912 360287970189640175 360287970189640195 2107 2 1224979098644774914 3 3 0 2170 3 1224979098644774917 1369094286720630785 360287970189639680 2122 3 1224979098644774918 5 1224979098644774917 2121 3 1224979098644774919 100 1224979098644774918 2107 2 1224979098644774914 1224979098644774919 2108 2 1224979098644774914 100 4 0 2147483679 2 1224979098644774912 360287970189639680 2147483679 2 1224979098644774912 360287970189640044 2147483679 2 1224979098644774912 360287970189640045 2147483681 3 1224979098644774912 360287970189640300 360287970189640305 2111 2 1224979098644774914 1 3 0 2133 2 72057594037927936 1224979098644774914 2075 1 72057594037927936 ')