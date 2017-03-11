#! /usr/bin/env python
#coding=utf-8

# Try to de-compile item_kinds1.txt file of mount&blade to module_items.py. 
# This process will not generate a full-functional module_items.py file,
# because triggers will be kept in its compiled txt form, and thus cannot be edited.

# If more than one itp_* statements share the same value, they will always come together in the outcoming module_items.py file,
# so don't be confused if you see something like itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield in one item.
# But don't worry, the value of itp_covers_legs|itp_doesnt_cover_hair|itp_can_penetrate_shield is identical to the value of any single one of them.


from module_info import *
from header_items import *
from decompiled_ID_factions import *
from decompile_operations import *


item_meshes_old = {
'ixmesh_inventory':       0x1000000000000000,
'ixmesh_flying_ammo':     0x2000000000000000,
'ixmesh_carry':           0x3000000000000000,
}
item_meshes = {}
for k,v in item_meshes_old.iteritems():
    item_meshes[v] = k.replace(' ','')
    
    
item_types_old = {
   'itp_type_horse          ': 0x0000000000000001,
   'itp_type_one_handed_wpn ': 0x0000000000000002,
   'itp_type_two_handed_wpn ': 0x0000000000000003,
   'itp_type_polearm        ': 0x0000000000000004,
   'itp_type_arrows         ': 0x0000000000000005,
   'itp_type_bolts          ': 0x0000000000000006,
   'itp_type_shield         ': 0x0000000000000007,
   'itp_type_bow            ': 0x0000000000000008,
   'itp_type_crossbow       ': 0x0000000000000009,
   'itp_type_thrown         ': 0x000000000000000a,
   'itp_type_goods          ': 0x000000000000000b,
   'itp_type_head_armor     ': 0x000000000000000c,
   'itp_type_body_armor     ': 0x000000000000000d,
   'itp_type_foot_armor     ': 0x000000000000000e,
   'itp_type_hand_armor     ': 0x000000000000000f,
   'itp_type_pistol         ': 0x0000000000000010,
   'itp_type_musket         ': 0x0000000000000011,
   'itp_type_bullets        ': 0x0000000000000012,
   'itp_type_animal         ': 0x0000000000000013,
   'itp_type_book           ': 0x0000000000000014,
}
item_types = {}
for k,v in item_types_old.iteritems():
    item_types[v] = k.replace(' ','')
    
    
item_flags_old = {
   'itp_type_horse          ': 0x0000000000000001,
   'itp_type_one_handed_wpn ': 0x0000000000000002,
   'itp_type_two_handed_wpn ': 0x0000000000000003,
   'itp_type_polearm        ': 0x0000000000000004,
   'itp_type_arrows         ': 0x0000000000000005,
   'itp_type_bolts          ': 0x0000000000000006,
   'itp_type_shield         ': 0x0000000000000007,
   'itp_type_bow            ': 0x0000000000000008,
   'itp_type_crossbow       ': 0x0000000000000009,
   'itp_type_thrown         ': 0x000000000000000a,
   'itp_type_goods          ': 0x000000000000000b,
   'itp_type_head_armor     ': 0x000000000000000c,
   'itp_type_body_armor     ': 0x000000000000000d,
   'itp_type_foot_armor     ': 0x000000000000000e,
   'itp_type_hand_armor     ': 0x000000000000000f,
   'itp_type_pistol         ': 0x0000000000000010,
   'itp_type_musket         ': 0x0000000000000011,
   'itp_type_bullets        ': 0x0000000000000012,
   'itp_type_animal         ': 0x0000000000000013,
   'itp_type_book           ': 0x0000000000000014,
    
   'itp_force_attach_left_hand     ': 0x0000000000000100,
   'itp_force_attach_right_hand    ': 0x0000000000000200,
   'itp_force_attach_left_forearm  ': 0x0000000000000300,
   'itp_attach_armature            ': 0x0000000000000f00,
   'itp_attachment_mask            ': 0x0000000000000f00,

   'itp_unique              ': 0x0000000000001000,
   'itp_always_loot         ': 0x0000000000002000,
   'itp_no_parry            ': 0x0000000000004000,
   'itp_default_ammo        ': 0x0000000000008000,
   'itp_merchandise         ': 0x0000000000010000,
   'itp_wooden_attack       ': 0x0000000000020000,
   'itp_wooden_parry        ': 0x0000000000040000,
   'itp_food                ': 0x0000000000080000,

   'itp_cant_reload_on_horseback': 0x0000000000100000,
   'itp_two_handed              ': 0x0000000000200000,
   'itp_primary                 ': 0x0000000000400000, # for weapons
   'itp_replaces_helm           ': 0x0000000000400000, # for armor, allows body armor items which include helmet
   'itp_secondary               ': 0x0000000000800000, # for weapons
   'itp_replaces_shoes          ': 0x0000000000800000, # for armor, allows body armor items which include boots
   'itp_covers_legs             ': 0x0000000001000000,
   'itp_doesnt_cover_hair       ': 0x0000000001000000,
   'itp_can_penetrate_shield    ': 0x0000000001000000,
   'itp_consumable              ': 0x0000000002000000,
   'itp_bonus_against_shield    ': 0x0000000004000000,
   'itp_penalty_with_shield     ': 0x0000000008000000,
   'itp_cant_use_on_horseback   ': 0x0000000010000000,
   'itp_civilian                ': 0x0000000020000000,
   'itp_next_item_as_melee      ': 0x0000000020000000,
   'itp_fit_to_head             ': 0x0000000040000000,
   'itp_offset_lance            ': 0x0000000040000000,
   'itp_covers_head             ': 0x0000000080000000,
   'itp_couchable               ': 0x0000000080000000,
   'itp_crush_through           ': 0x0000000100000000,
    #'itp_knock_back              ': 0x0000000200000000, being used?
   'itp_remove_item_on_use      ': 0x0000000400000000,
   'itp_unbalanced              ': 0x0000000800000000,

   'itp_covers_beard            ': 0x0000001000000000,    #remove beard mesh
   'itp_no_pick_up_from_ground  ': 0x0000002000000000,
   'itp_can_knock_down          ': 0x0000004000000000,
   'itp_covers_hair             ': 0x0000008000000000,    #remove hair mesh for armors only

   'itp_force_show_body         ': 0x0000010000000000, # forces showing body (works on body armor items)
   'itp_force_show_left_hand    ': 0x0000020000000000, # forces showing left hand (works on hand armor items)
   'itp_force_show_right_hand   ': 0x0000040000000000, # forces showing right hand (works on hand armor items)

   'itp_extra_penetration       ': 0x0000100000000000,
   'itp_has_bayonet             ': 0x0000200000000000,
   'itp_cant_reload_while_moving': 0x0000400000000000,
   'itp_ignore_gravity          ': 0x0000800000000000,
    
   'itp_ignore_friction         ': 0x0001000000000000,
   'itp_is_pike                 ': 0x0002000000000000,
   'itp_offset_musket           ': 0x0004000000000000,
   'itp_no_blur                 ': 0x0008000000000000,

   'itp_cant_reload_while_moving_mounted': 0x0010000000000000,
   'itp_has_upper_stab          ': 0x0020000000000000,
}
item_flags = {}
for k,v in item_flags_old.iteritems():
    item_flags[v] = k.replace(' ','')
    
    
item_capas_old = {
   'itcf_thrust_onehanded                               ': 0x0000000000000001,
   'itcf_overswing_onehanded                            ': 0x0000000000000002,
   'itcf_slashright_onehanded                           ': 0x0000000000000004,
   'itcf_slashleft_onehanded                            ': 0x0000000000000008,

   'itcf_thrust_twohanded                               ': 0x0000000000000010,
   'itcf_overswing_twohanded                            ': 0x0000000000000020,
   'itcf_slashright_twohanded                           ': 0x0000000000000040,
   'itcf_slashleft_twohanded                            ': 0x0000000000000080,

   'itcf_thrust_polearm                                 ': 0x0000000000000100,
   'itcf_overswing_polearm                              ': 0x0000000000000200,
   'itcf_slashright_polearm                             ': 0x0000000000000400,
   'itcf_slashleft_polearm                              ': 0x0000000000000800,

   'itcf_shoot_bow                                      ': 0x0000000000001000,
   'itcf_shoot_javelin                                  ': 0x0000000000002000,
   'itcf_shoot_crossbow                                 ': 0x0000000000004000,
   'itcf_throw_stone                                    ': 0x0000000000010000,
   'itcf_throw_knife                                    ': 0x0000000000020000,
   'itcf_throw_axe                                      ': 0x0000000000030000,
   'itcf_throw_javelin                                  ': 0x0000000000040000,
   'itcf_shoot_pistol                                   ': 0x0000000000070000,
   'itcf_shoot_musket                                   ': 0x0000000000080000,
   'itcf_shoot_mask                                     ': 0x00000000000ff000,

   'itcf_horseback_thrust_onehanded                     ': 0x0000000000100000,
   'itcf_horseback_overswing_right_onehanded            ': 0x0000000000200000,
   'itcf_horseback_overswing_left_onehanded             ': 0x0000000000400000,
   'itcf_horseback_slashright_onehanded                 ': 0x0000000000800000,
   'itcf_horseback_slashleft_onehanded                  ': 0x0000000001000000,
   'itcf_thrust_onehanded_lance                         ': 0x0000000004000000,
   'itcf_thrust_onehanded_lance_horseback               ': 0x0000000008000000,

   'itcf_carry_mask                                     ': 0x00000007f0000000,
   'itcf_carry_sword_left_hip                           ': 0x0000000010000000,
   'itcf_carry_axe_left_hip                             ': 0x0000000020000000,
   'itcf_carry_dagger_front_left                        ': 0x0000000030000000,
   'itcf_carry_dagger_front_right                       ': 0x0000000040000000,
   'itcf_carry_quiver_front_right                       ': 0x0000000050000000,
   'itcf_carry_quiver_back_right                        ': 0x0000000060000000,
   'itcf_carry_quiver_right_vertical                    ': 0x0000000070000000,
   'itcf_carry_quiver_back                              ': 0x0000000080000000,
   'itcf_carry_revolver_right                           ': 0x0000000090000000,
   'itcf_carry_pistol_front_left                        ': 0x00000000a0000000,
   'itcf_carry_bowcase_left                             ': 0x00000000b0000000,
   'itcf_carry_mace_left_hip                            ': 0x00000000c0000000,
   'itcf_carry_axe_back                                 ': 0x0000000100000000,
   'itcf_carry_sword_back                               ': 0x0000000110000000,
   'itcf_carry_kite_shield                              ': 0x0000000120000000,
   'itcf_carry_round_shield                             ': 0x0000000130000000,
   'itcf_carry_buckler_left                             ': 0x0000000140000000,
   'itcf_carry_crossbow_back                            ': 0x0000000150000000,
   'itcf_carry_bow_back                                 ': 0x0000000160000000,
   'itcf_carry_spear                                    ': 0x0000000170000000,
   'itcf_carry_board_shield                             ': 0x0000000180000000,
   'itcf_carry_katana                                   ': 0x0000000210000000,
   'itcf_carry_wakizashi                                ': 0x0000000220000000,

   'itcf_show_holster_when_drawn                        ': 0x0000000800000000,

   'itcf_reload_pistol                                  ': 0x0000007000000000,
   'itcf_reload_musket                                  ': 0x0000008000000000,
   'itcf_reload_mask                                    ': 0x000000f000000000,

   'itcf_parry_forward_onehanded                        ': 0x0000010000000000,
   'itcf_parry_up_onehanded                             ': 0x0000020000000000,
   'itcf_parry_right_onehanded                          ': 0x0000040000000000,
   'itcf_parry_left_onehanded                           ': 0x0000080000000000,

   'itcf_parry_forward_twohanded                        ': 0x0000100000000000,
   'itcf_parry_up_twohanded                             ': 0x0000200000000000,
   'itcf_parry_right_twohanded                          ': 0x0000400000000000,
   'itcf_parry_left_twohanded                           ': 0x0000800000000000,

   'itcf_parry_forward_polearm                          ': 0x0001000000000000,
   'itcf_parry_up_polearm                               ': 0x0002000000000000,
   'itcf_parry_right_polearm                            ': 0x0004000000000000,
   'itcf_parry_left_polearm                             ': 0x0008000000000000,

   'itcf_horseback_slash_polearm                        ': 0x0010000000000000,
   'itcf_overswing_spear                                ': 0x0020000000000000,
   'itcf_overswing_musket                               ': 0x0040000000000000,
   'itcf_thrust_musket                                  ': 0x0080000000000000,

   'itcf_force_64_bits                                  ': 0x8000000000000000,
}
item_capas = {}
for k,v in item_capas_old.iteritems():
    item_capas[v] = k.replace(' ','')
    
    
item_capa_combinations_old = {
   'itc_cleaver':itcf_force_64_bits | (itcf_overswing_onehanded|itcf_slashright_onehanded|itcf_slashleft_onehanded |itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded),
   'itc_dagger ':itc_cleaver | itcf_thrust_onehanded,
   'itc_parry_onehanded':itcf_force_64_bits | itcf_parry_forward_onehanded| itcf_parry_up_onehanded | itcf_parry_right_onehanded |itcf_parry_left_onehanded,
   'itc_longsword':itc_dagger | itc_parry_onehanded,
   'itc_scimitar ':itc_cleaver | itc_parry_onehanded,
   'itc_parry_two_handed':itcf_force_64_bits | itcf_parry_forward_twohanded | itcf_parry_up_twohanded | itcf_parry_right_twohanded | itcf_parry_left_twohanded,
   'itc_cut_two_handed':itcf_force_64_bits | (itcf_slashright_twohanded | itcf_slashleft_twohanded | itcf_overswing_twohanded |itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded),
   'itc_greatsword':itc_cut_two_handed |  itcf_thrust_twohanded | itc_parry_two_handed |itcf_thrust_onehanded_lance,
   'itc_nodachi   ':itc_cut_two_handed | itc_parry_two_handed,
   'itc_bastardsword':itc_cut_two_handed |  itcf_thrust_twohanded | itc_parry_two_handed |itc_dagger,
   'itc_morningstar':itc_cut_two_handed |  itc_parry_two_handed |itc_cleaver,
   'itc_parry_polearm':itcf_parry_forward_polearm | itcf_parry_up_polearm | itcf_parry_right_polearm | itcf_parry_left_polearm,
   'itc_poleaxe   ':itc_parry_polearm| itcf_overswing_polearm |itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm,
   'itc_staff     ':itc_parry_polearm| itcf_thrust_onehanded_lance |itcf_thrust_onehanded_lance_horseback| itcf_overswing_polearm |itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm,
   'itc_spear     ':itc_parry_polearm| itcf_thrust_onehanded_lance |itcf_thrust_onehanded_lance_horseback | itcf_thrust_polearm,
   'itc_cutting_spear':itc_spear|itcf_overswing_polearm,
   'itc_pike      ':itcf_thrust_onehanded_lance |itcf_thrust_onehanded_lance_horseback | itcf_thrust_polearm,
   'itc_guandao   ':itc_parry_polearm|itcf_overswing_polearm|itcf_thrust_polearm|itcf_slashright_polearm|itcf_slashleft_polearm|itcf_horseback_slashright_onehanded|itcf_horseback_slashleft_onehanded|itcf_horseback_slash_polearm,
   'itc_greatlance':itcf_thrust_onehanded_lance |itcf_thrust_onehanded_lance_horseback| itcf_thrust_polearm,
   'itc_musket_melee':itc_parry_polearm|itcf_overswing_musket|itcf_thrust_musket|itcf_slashright_twohanded|itcf_slashleft_twohanded,
}
item_capa_combinations = {}
for k,v in item_capa_combinations_old.iteritems():
    item_capa_combinations[v] = k.replace(' ','')


item_modbs_old = {
   'imodbit_plain      ': 0x000000000001,
   'imodbit_cracked    ': 0x000000000002,
   'imodbit_rusty      ': 0x000000000004,
   'imodbit_bent       ': 0x000000000008,
   'imodbit_chipped    ': 0x000000000010,
   'imodbit_battered   ': 0x000000000020,
   'imodbit_poor       ': 0x000000000040,
   'imodbit_crude      ': 0x000000000080,
   'imodbit_old        ': 0x000000000100,
   'imodbit_cheap      ': 0x000000000200,
   'imodbit_fine       ': 0x000000000400,
   'imodbit_well_made  ': 0x000000000800,
   'imodbit_sharp      ': 0x000000001000,
   'imodbit_balanced   ': 0x000000002000,
   'imodbit_tempered   ': 0x000000004000,
   'imodbit_deadly     ': 0x000000008000,
   'imodbit_exquisite  ': 0x000000010000,
   'imodbit_masterwork ': 0x000000020000,
   'imodbit_heavy      ': 0x000000040000,
   'imodbit_strong     ': 0x000000080000,
   'imodbit_powerful   ': 0x000000100000,
   'imodbit_tattered   ': 0x000000200000,
   'imodbit_ragged     ': 0x000000400000,
   'imodbit_rough      ': 0x000000800000,
   'imodbit_sturdy     ': 0x000001000000,
   'imodbit_thick      ': 0x000002000000,
   'imodbit_hardened   ': 0x000004000000,
   'imodbit_reinforced ': 0x000008000000,
   'imodbit_superb     ': 0x000010000000,
   'imodbit_lordly     ': 0x000020000000,
   'imodbit_lame       ': 0x000040000000,
   'imodbit_swaybacked ': 0x000080000000,
   'imodbit_stubborn   ': 0x000100000000,
   'imodbit_timid      ': 0x000200000000,
   'imodbit_meek       ': 0x000400000000,
   'imodbit_spirited   ': 0x000800000000,
   'imodbit_champion   ': 0x001000000000,
   'imodbit_fresh      ': 0x002000000000,
   'imodbit_day_old    ': 0x004000000000,
   'imodbit_two_day_old': 0x008000000000,
   'imodbit_smelling   ': 0x010000000000,
   'imodbit_rotten     ': 0x020000000000,
   'imodbit_large_bag  ': 0x040000000000,
}
item_modbs = {}
for k,v in item_modbs_old.iteritems():
    item_modbs[v] = k.replace(' ','')


item_modb_combinations_old = {
    'imodbits_none ': 0,
    'imodbits_horse_basic ': imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn,
    'imodbits_cloth  ': imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened,
    'imodbits_armor  ': imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly,
    'imodbits_plate  ': imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly,
    'imodbits_polearm ': imodbit_cracked | imodbit_bent | imodbit_balanced,
    'imodbits_shield  ': imodbit_cracked | imodbit_battered |imodbit_thick | imodbit_reinforced,
    'imodbits_sword   ': imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered,
    'imodbits_sword_high   ': imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork,
    'imodbits_axe   ': imodbit_rusty | imodbit_chipped | imodbit_heavy,
    'imodbits_mace   ': imodbit_rusty | imodbit_chipped | imodbit_heavy,
    'imodbits_pick   ': imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy,
    'imodbits_bow ': imodbit_cracked | imodbit_bent | imodbit_strong |imodbit_masterwork,
    'imodbits_crossbow ': imodbit_cracked | imodbit_bent | imodbit_masterwork,
    'imodbits_missile   ': imodbit_bent | imodbit_large_bag,
    'imodbits_thrown   ': imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag,
    'imodbits_thrown_minus_heavy ': imodbit_bent | imodbit_balanced| imodbit_large_bag,
    'imodbits_horse_basic|imodbit_champion': 110595670016,
}
item_modb_combinations = {}
for k,v in item_modb_combinations_old.iteritems():
    item_modb_combinations[v] = k.replace(' ','')
    

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


#----------------------------------------------------------------------------#
#------------------- Codes above this point are hardwired -------------------#
#----------------------------------------------------------------------------#


def distill(integer):
    result = []
    binInt = bin(integer)[2:]
    for d in xrange(len(binInt)):
        if binInt[d]=='1':
            zeros = '0'*(len(binInt)-d-1)
            result.append(int("0b1%s" %zeros,2))
            
    return result


def get_mesh_code(line):
    mesh_code = "["
    for i_mesh in xrange(int(line[3])):
        mesh_name = line[4+2*i_mesh]
        mesh_type = int(line[5+2*i_mesh])
        
        if mesh_type==0:
            mesh_type_code = "0"
            mesh_code = mesh_code + '''("%s", %s),''' %(mesh_name,mesh_type_code)
            
        else:
            mesh_type_code = ""
            
            item_mesh_keys = item_meshes.keys()
            item_mesh_keys.sort()
            item_mesh_keys.reverse()
            for each_mesh_type in item_mesh_keys:
                if mesh_type&each_mesh_type==each_mesh_type:
                    mesh_type_code += "|%s" %item_meshes[each_mesh_type]
                    mesh_type -= each_mesh_type
            
            if mesh_type==0:
                mesh_type_code = mesh_type_code.replace('|','',1)
            else:
                item_modb_keys = item_modbs.keys()
                item_modb_keys.sort()
                item_modb_keys.reverse()
                for each_modb in item_modb_keys:
                    if mesh_type&each_modb==each_modb:
                        mesh_type_code += "|%s" %item_modbs[each_modb]
                        mesh_type -= each_modb
                    if mesh_type==0:
                        mesh_type_code = mesh_type_code.replace('|','',1)
                        break
            
            mesh_code = mesh_code + '''("%s", %s),''' %(mesh_name,mesh_type_code)
    mesh_code = mesh_code + "]"
    return mesh_code


def get_flag_code(line):
    flag_code = ''''''
    mesh_count = int(line[3])
    item_flag = int(line[4+2*mesh_count])
    
    if item_flag==0:
        return '0'
    
    item_flag_keys = item_flags.keys()
    item_flag_keys.sort()
    item_flag_keys.reverse()
    for each_flag in item_flag_keys:
        if item_flag&each_flag==each_flag:
            flag_code += "|%s" %item_flags[each_flag]
            item_flag -= each_flag
        if item_flag==0:
            return flag_code.replace('|','',1)
    else:
        return line[4+2*mesh_count]
    
    
def get_capa_code(line):
    capa_code = ''''''
    mesh_count = int(line[3])
    item_capa = int(line[5+2*mesh_count])
    
    if item_capa==0:
        return '0'
    
    item_capa_combination_keys = item_capa_combinations.keys()
    item_capa_combination_keys.sort()
    item_capa_combination_keys.reverse()   # capability coombinations with greater value have higher priority
    for each_capa_combination in item_capa_combination_keys:
        if item_capa&each_capa_combination==each_capa_combination:
            capa_code += "|%s" %item_capa_combinations[each_capa_combination]
            item_capa -= each_capa_combination
        if item_capa==0:
            return capa_code.replace('|','',1)    
    
    item_capa_keys = item_capas.keys()
    item_capa_keys.sort()
    item_capa_keys.reverse()
    for each_capa in item_capa_keys:
        if item_capa&each_capa==each_capa:
            capa_code += "|%s" %item_capas[each_capa]
            item_capa -= each_capa
        if item_capa==0:
            return capa_code.replace('|','',1)
    else:
        return line[5+2*mesh_count]
    

def get_modb_code(line):
    modb_code = ''''''
    mesh_count = int(line[3])
    item_modb = int(line[7+2*mesh_count])
    
    item_modb_combination_keys = item_modb_combinations.keys()
    item_modb_combination_keys.sort()
    item_modb_combination_keys.reverse()
    for each_modb_combination in item_modb_combination_keys:
        if item_modb&each_modb_combination==each_modb_combination:
            modb_code += "|%s" %item_modb_combinations[each_modb_combination]
            item_modb -= each_modb_combination
    if item_modb==0:
        return modb_code.replace('|','',1)
    
    item_modb_keys = item_modbs.keys()
    item_modb_keys.sort()
    item_modb_keys.reverse()
    for each_modb in item_modb_keys:
        if item_modb&each_modb==each_modb:
            modb_code += "|%s" %item_modbs[each_modb]
            item_modb -= each_modb
    if item_modb==0:
        return modb_code.replace('|','',1)
    else:
        return line[7+2*mesh_count]


def get_stat_code(line):
    stat_code = ''''''
    mesh_count = int(line[3])
    item_stat = line[8+2*mesh_count:]
    
    thrust_damage = int(item_stat[11])
    thrust_damage_hex = hex(thrust_damage)
    thrust_damage_type = thrust_damage_hex[-3]
    if thrust_damage_type=='x' or thrust_damage_type=='0':
        thrust_damage_type = 'cut'
    elif thrust_damage_type=='1':
        thrust_damage -= 256
        thrust_damage_type = 'pierce'
    elif thrust_damage_type=='2':
        thrust_damage -= 511
        thrust_damage_type = 'blunt'
        
    swing_damage = int(item_stat[12])
    swing_damage_hex = hex(swing_damage)
    swing_damage_type = swing_damage_hex[-3]
    if swing_damage_type=='x' or swing_damage_type=='0':
        swing_damage_type = 'cut'
    elif swing_damage_type=='1':
        swing_damage -= 256
        swing_damage_type = 'pierce'
    elif swing_damage_type=='2':
        swing_damage -= 511
        swing_damage_type = 'blunt'
    
    stat_code = '''weight(%s)|abundance(%s)|head_armor(%s)|body_armor(%s)|leg_armor(%s)|difficulty(%s)|hit_points(%s)|spd_rtng(%s)|shoot_speed(%s)|weapon_length(%s)|max_ammo(%s)|thrust_damage(%d,%s)|swing_damage(%d,%s)\
''' %(str(float(item_stat[0])),item_stat[1],item_stat[2],item_stat[3],item_stat[4],item_stat[5],item_stat[6],item_stat[7],item_stat[8],item_stat[9],item_stat[10],thrust_damage,thrust_damage_type,swing_damage,swing_damage_type)
    
    return stat_code


def get_fac_code(line):
    fac_code = "\n    ["
    for this_fac in line:
        this_fac = int(this_fac)
        fac_code += "%s," %faction_ids[this_fac]
    return fac_code+"]"


def decompile_items():
    ofile = open(export_dir+"item_kinds1.txt", 'r')
    tfile = open(export_dir+"decompiled files/module_items.py", 'w')
    idfile = open(export_dir+"decompiled files/ID_items.py", 'w')
    
    tfile.write('''
from module_constants import *
from ID_factions import *
from header_items import  *
from header_operations import *
from header_triggers import *

####################################################################################################################
#  Each item record contains the following fields:
#  1) Item id: used for referencing items in other files.
#     The prefix itm_ is automatically added before each item id.
#  2) Item name. Name of item as it'll appear in inventory window
#  3) List of meshes.  Each mesh record is a tuple containing the following fields:
#    3.1) Mesh name.
#    3.2) Modifier bits that this mesh matches.
#     Note that the first mesh record is the default.
#  4) Item flags. See header_items.py for a list of available flags.
#  5) Item capabilities. Used for which animations this item is used with. See header_items.py for a list of available flags.
#  6) Item value.
#  7) Item stats: Bitwise-or of various stats about the item such as:
#      weight, abundance, difficulty, head_armor, body_armor,leg_armor, etc...
#  8) Modifier bits: Modifiers that can be applied to this item.
#  9) [Optional] Triggers: List of simple triggers to be associated with the item.
#  10) [Optional] Factions: List of factions that item can be found as merchandise.
####################################################################################################################

# Some constants for ease of use.
imodbits_none = 0
imodbits_horse_basic = imodbit_swaybacked|imodbit_lame|imodbit_spirited|imodbit_heavy|imodbit_stubborn
imodbits_cloth  = imodbit_tattered | imodbit_ragged | imodbit_sturdy | imodbit_thick | imodbit_hardened
imodbits_armor  = imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_plate  = imodbit_cracked | imodbit_rusty | imodbit_battered | imodbit_crude | imodbit_thick | imodbit_reinforced |imodbit_lordly
imodbits_polearm = imodbit_cracked | imodbit_bent | imodbit_balanced
imodbits_shield  = imodbit_cracked | imodbit_battered |imodbit_thick | imodbit_reinforced
imodbits_sword   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered
imodbits_sword_high   = imodbit_rusty | imodbit_chipped | imodbit_balanced |imodbit_tempered|imodbit_masterwork
imodbits_axe   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_mace   = imodbit_rusty | imodbit_chipped | imodbit_heavy
imodbits_pick   = imodbit_rusty | imodbit_chipped | imodbit_balanced | imodbit_heavy
imodbits_bow = imodbit_cracked | imodbit_bent | imodbit_strong |imodbit_masterwork
imodbits_crossbow = imodbit_cracked | imodbit_bent | imodbit_masterwork
imodbits_missile   = imodbit_bent | imodbit_large_bag
imodbits_thrown   = imodbit_bent | imodbit_heavy| imodbit_balanced| imodbit_large_bag
imodbits_thrown_minus_heavy = imodbit_bent | imodbit_balanced| imodbit_large_bag

imodbits_horse_good = imodbit_spirited|imodbit_heavy
imodbits_good   = imodbit_sturdy | imodbit_thick | imodbit_hardened | imodbit_reinforced
imodbits_bad    = imodbit_rusty | imodbit_chipped | imodbit_tattered | imodbit_ragged | imodbit_cracked | imodbit_bent
''')
    
    tfile.write("items = [\n")
    #tfile.write('''["no_item","INVALID ITEM", [("invalid_item",0)], itp_type_one_handed_wpn|itp_primary|itp_secondary, itc_longsword, 3,weight(1.5)|spd_rtng(103)|weapon_length(90)|swing_damage(16,blunt)|thrust_damage(10,blunt),imodbits_none],\n''')
    
    isFacCntLine = 0   # for next line
    isFacLine = 0      # for next line
    isTrgCntLine = 0   # for next line
    isTrgLine = 0      # for next line
    isEndLine = 0      # for next line
    id = 0
    for line in ofile:
        if ' itm_' in line:
            line = line.split()
            mesh_count = int(line[3])
            mesh_code = get_mesh_code(line)
            flag_code = get_flag_code(line)
            capa_code = get_capa_code(line)
            modb_code = get_modb_code(line)
            stat_code = get_stat_code(line)
                
            tfile.write('''  ["%s","%s", %s, %s,%s,%s, %s,%s,''' %(line[0][4:],line[1].replace('_',' '),mesh_code,flag_code,capa_code,line[6+2*mesh_count],stat_code,modb_code))
            idfile.write("%s = %d\n" %(line[0],id))
            id += 1
            
            fac_code = 0
            trigger_code = 0
            
            isFacCntLine = 1
            continue    # next line
        
        if isFacCntLine:
            if int(line)==0:
                isTrgCntLine = 1
            else:
                isFacLine = 1
            isFacCntLine = 0
            continue    # next line
        
        if isTrgCntLine:
            if int(line)==0:
                isEndLine = 1
            else:
                isTrgLine = int(line)   # probably have more than one triggers
                trigger_code = '''\n    ['''
            isTrgCntLine = 0
            continue   # next line
        
        if isFacLine:
            line = line.split()
            fac_code = get_fac_code(line)   # "\n    [xxxx|xxxx]"
            isFacLine = 0
            isTrgCntLine = 1
            continue
        
        if isTrgLine:
            line = line.split()
            timer = float(line[0])
            
            if timer in trigger_timers:
                timer = trigger_timers[timer]
            else:
                timer = line[0]
                
            this_trigger_code = "\n      (%s,\n%s,\n      )," %(timer,decompile_statement_block(' '.join(line[1:])))
            trigger_code += this_trigger_code
            isTrgLine = isTrgLine-1
            if isTrgLine==0:
                trigger_code += "\n    ],"
                isEndLine = 1
            continue
        
        if isEndLine:
            if fac_code==0 and trigger_code==0:   # no faction code nor trigger code
                tfile.write("  ],\n")   # end this item block
            elif fac_code!=0 and trigger_code!=0:
                tfile.write(trigger_code)   # "\n    [\n        'xxxx',\n        'xxxx',\n    ]"
                tfile.write(fac_code)
                tfile.write("\n  ],\n")
            elif fac_code==0 and trigger_code!=0:
                tfile.write(trigger_code)
                tfile.write("\n  ],\n")
            else:
                tfile.write("\n    [],")
                tfile.write(fac_code)
                tfile.write("\n  ],\n")
            
            isFacCntLine = 0
            isFacLine = 0
            isTrgCntLine = 0
            isTrgLine = 0
            isEndLine = 0         
            continue
            
    tfile.write(''']\n''')
    tfile.close()
    ofile.close()
    idfile.close()

        
        
if __name__=='__main__':
    print "Decompiling items ..."
    decompile_items()