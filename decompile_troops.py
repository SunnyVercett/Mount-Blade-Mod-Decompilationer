#! /usr/bin/env python
#coding=utf-8

# Decompiled face code could be a little different from original, donno why, donno how bad this is.


from module_info import *
from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from decompiled_ID_items import *
from decompiled_ID_scenes import *
from decompiled_ID_factions import *


troop_flags_old = {
   #'tf_male          ': 0x00000000,   # 0x00000000 means nothing
   'tf_female        ': 0x00000001,
   'tf_undead        ': 0x00000002,
   'tf_hero             ': 0x00000010,
   'tf_inactive         ': 0x00000020,
   'tf_unkillable       ': 0x00000040,
   'tf_allways_fall_dead': 0x00000080,
   'tf_no_capture_alive ': 0x00000100,
   'tf_mounted          ': 0x00000400, #Troop's movement speed on map is determined by riding skill.
   'tf_is_merchant      ': 0x00001000, #When set, troop does not equip stuff he owns
   'tf_randomize_face   ': 0x00008000, #randomize face at the beginning of the game.
   'tf_guarantee_boots           ': 0x00100000,
   'tf_guarantee_armor           ': 0x00200000,
   'tf_guarantee_helmet          ': 0x00400000,
   'tf_guarantee_gloves          ': 0x00800000,
   'tf_guarantee_horse           ': 0x01000000,
   'tf_guarantee_shield          ': 0x02000000,
   'tf_guarantee_ranged          ': 0x04000000,
   'tf_unmoveable_in_party_window': 0x10000000,
   'tf_guarantee_all             ': tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged,
   'tf_guarantee_all_wo_ranged   ': tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield,
}
troop_flags = {}
for k,v in troop_flags_old.iteritems():
    troop_flags[v] = k.replace(' ','')


troop_attrs_old = {
    'def_attrib' : str_7 | agi_5 | int_4 | cha_4,
    'def_attrib_multiplayer' : int_30 | cha_30,
    'lord_attrib' : str_20|agi_20|int_20|cha_20|level(38),
    'knight_attrib_1' : str_15|agi_14|int_8|cha_16|level(22),
    'knight_attrib_2' : str_16|agi_16|int_10|cha_18|level(26),
    'knight_attrib_3' : str_18|agi_17|int_12|cha_20|level(30),
    'knight_attrib_4' : str_19|agi_19|int_13|cha_22|level(35),
    'knight_attrib_5' : str_20|agi_20|int_15|cha_25|level(41),
}
troop_attrs = {}
for k,v in troop_attrs_old.iteritems():
    troop_attrs[v] = k.replace(' ','')
    

skl_trade                = 0
skl_leadership           = 1
skl_prisoner_management  = 2
skl_reserved_1           = 3
skl_reserved_2           = 4
skl_reserved_3           = 5
skl_reserved_4           = 6
skl_persuasion           = 7
skl_engineer             = 8
skl_first_aid            = 9
skl_surgery              = 10
skl_wound_treatment      = 11
skl_inventory_management = 12
skl_spotting             = 13
skl_pathfinding          = 14
skl_tactics              = 15
skl_tracking             = 16
skl_trainer              = 17
skl_reserved_5           = 18
skl_reserved_6           = 19
skl_reserved_7           = 20
skl_reserved_8           = 21
skl_looting              = 22
skl_horse_archery        = 23
skl_riding               = 24
skl_athletics            = 25
skl_shield               = 26
skl_weapon_master        = 27
skl_reserved_9           = 28
skl_reserved_10          = 29
skl_reserved_11          = 30
skl_reserved_12          = 31
skl_reserved_13          = 32
skl_power_draw           = 33
skl_power_throw          = 34
skl_power_strike         = 35
skl_ironflesh            = 36
skl_reserved_14          = 37
skl_reserved_15          = 38
skl_reserved_16          = 39
skl_reserved_17          = 40
skl_reserved_18          = 41
troop_skills_old = {
   'knows_trade_1                ':  0x01 << (skl_trade << 2),
   'knows_trade_2                ':  0x02 << (skl_trade << 2),
   'knows_trade_3                ':  0x03 << (skl_trade << 2),
   'knows_trade_4                ':  0x04 << (skl_trade << 2),
   'knows_trade_5                ':  0x05 << (skl_trade << 2),
   'knows_trade_6                ':  0x06 << (skl_trade << 2),
   'knows_trade_7                ':  0x07 << (skl_trade << 2),
   'knows_trade_8                ':  0x08 << (skl_trade << 2),
   'knows_trade_9                ':  0x09 << (skl_trade << 2),
   'knows_trade_10               ':  0x0A << (skl_trade << 2),
   'knows_trade_11               ':  0x0B << (skl_trade << 2),
   'knows_trade_12               ':  0x0C << (skl_trade << 2),
   'knows_trade_13               ':  0x0D << (skl_trade << 2),
   'knows_trade_14               ':  0x0E << (skl_trade << 2),
   'knows_trade_15               ':  0x0F << (skl_trade << 2),
   'knows_leadership_1           ':  0x01 << (skl_leadership << 2),
   'knows_leadership_2           ':  0x02 << (skl_leadership << 2),
   'knows_leadership_3           ':  0x03 << (skl_leadership << 2),
   'knows_leadership_4           ':  0x04 << (skl_leadership << 2),
   'knows_leadership_5           ':  0x05 << (skl_leadership << 2),
   'knows_leadership_6           ':  0x06 << (skl_leadership << 2),
   'knows_leadership_7           ':  0x07 << (skl_leadership << 2),
   'knows_leadership_8           ':  0x08 << (skl_leadership << 2),
   'knows_leadership_9           ':  0x09 << (skl_leadership << 2),
   'knows_leadership_10          ':  0x0A << (skl_leadership << 2),
   'knows_leadership_11          ':  0x0B << (skl_leadership << 2),
   'knows_leadership_12          ':  0x0C << (skl_leadership << 2),
   'knows_leadership_13          ':  0x0D << (skl_leadership << 2),
   'knows_leadership_14          ':  0x0E << (skl_leadership << 2),
   'knows_leadership_15          ':  0x0F << (skl_leadership << 2),
   'knows_prisoner_management_1  ':  0x01 << (skl_prisoner_management << 2),
   'knows_prisoner_management_2  ':  0x02 << (skl_prisoner_management << 2),
   'knows_prisoner_management_3  ':  0x03 << (skl_prisoner_management << 2),
   'knows_prisoner_management_4  ':  0x04 << (skl_prisoner_management << 2),
   'knows_prisoner_management_5  ':  0x05 << (skl_prisoner_management << 2),
   'knows_prisoner_management_6  ':  0x06 << (skl_prisoner_management << 2),
   'knows_prisoner_management_7  ':  0x07 << (skl_prisoner_management << 2),
   'knows_prisoner_management_8  ':  0x08 << (skl_prisoner_management << 2),
   'knows_prisoner_management_9  ':  0x09 << (skl_prisoner_management << 2),
   'knows_prisoner_management_10 ':  0x0A << (skl_prisoner_management << 2),
   'knows_prisoner_management_11 ':  0x0B << (skl_prisoner_management << 2),
   'knows_prisoner_management_12 ':  0x0C << (skl_prisoner_management << 2),
   'knows_prisoner_management_13 ':  0x0D << (skl_prisoner_management << 2),
   'knows_prisoner_management_14 ':  0x0E << (skl_prisoner_management << 2),
   'knows_prisoner_management_15 ':  0x0F << (skl_prisoner_management << 2),
   'knows_reserved_1_1           ':  0x01 << (skl_reserved_1 << 2),
   'knows_reserved_1_2           ':  0x02 << (skl_reserved_1 << 2),
   'knows_reserved_1_3           ':  0x03 << (skl_reserved_1 << 2),
   'knows_reserved_1_4           ':  0x04 << (skl_reserved_1 << 2),
   'knows_reserved_1_5           ':  0x05 << (skl_reserved_1 << 2),
   'knows_reserved_1_6           ':  0x06 << (skl_reserved_1 << 2),
   'knows_reserved_1_7           ':  0x07 << (skl_reserved_1 << 2),
   'knows_reserved_1_8           ':  0x08 << (skl_reserved_1 << 2),
   'knows_reserved_1_9           ':  0x09 << (skl_reserved_1 << 2),
   'knows_reserved_1_10          ':  0x0A << (skl_reserved_1 << 2),
   'knows_reserved_1_11          ':  0x0B << (skl_reserved_1 << 2),
   'knows_reserved_1_12          ':  0x0C << (skl_reserved_1 << 2),
   'knows_reserved_1_13          ':  0x0D << (skl_reserved_1 << 2),
   'knows_reserved_1_14          ':  0x0E << (skl_reserved_1 << 2),
   'knows_reserved_1_15          ':  0x0F << (skl_reserved_1 << 2),
   'knows_reserved_2_1           ':  0x01 << (skl_reserved_2 << 2),
   'knows_reserved_2_2           ':  0x02 << (skl_reserved_2 << 2),
   'knows_reserved_2_3           ':  0x03 << (skl_reserved_2 << 2),
   'knows_reserved_2_4           ':  0x04 << (skl_reserved_2 << 2),
   'knows_reserved_2_5           ':  0x05 << (skl_reserved_2 << 2),
   'knows_reserved_2_6           ':  0x06 << (skl_reserved_2 << 2),
   'knows_reserved_2_7           ':  0x07 << (skl_reserved_2 << 2),
   'knows_reserved_2_8           ':  0x08 << (skl_reserved_2 << 2),
   'knows_reserved_2_9           ':  0x09 << (skl_reserved_2 << 2),
   'knows_reserved_2_10          ':  0x0A << (skl_reserved_2 << 2),
   'knows_reserved_2_11          ':  0x0B << (skl_reserved_2 << 2),
   'knows_reserved_2_12          ':  0x0C << (skl_reserved_2 << 2),
   'knows_reserved_2_13          ':  0x0D << (skl_reserved_2 << 2),
   'knows_reserved_2_14          ':  0x0E << (skl_reserved_2 << 2),
   'knows_reserved_2_15          ':  0x0F << (skl_reserved_2 << 2),
   'knows_reserved_3_1           ':  0x01 << (skl_reserved_3 << 2),
   'knows_reserved_3_2           ':  0x02 << (skl_reserved_3 << 2),
   'knows_reserved_3_3           ':  0x03 << (skl_reserved_3 << 2),
   'knows_reserved_3_4           ':  0x04 << (skl_reserved_3 << 2),
   'knows_reserved_3_5           ':  0x05 << (skl_reserved_3 << 2),
   'knows_reserved_3_6           ':  0x06 << (skl_reserved_3 << 2),
   'knows_reserved_3_7           ':  0x07 << (skl_reserved_3 << 2),
   'knows_reserved_3_8           ':  0x08 << (skl_reserved_3 << 2),
   'knows_reserved_3_9           ':  0x09 << (skl_reserved_3 << 2),
   'knows_reserved_3_10          ':  0x0A << (skl_reserved_3 << 2),
   'knows_reserved_3_11          ':  0x0B << (skl_reserved_3 << 2),
   'knows_reserved_3_12          ':  0x0C << (skl_reserved_3 << 2),
   'knows_reserved_3_13          ':  0x0D << (skl_reserved_3 << 2),
   'knows_reserved_3_14          ':  0x0E << (skl_reserved_3 << 2),
   'knows_reserved_3_15          ':  0x0F << (skl_reserved_3 << 2),
   'knows_reserved_4_1           ':  0x01 << (skl_reserved_4 << 2),
   'knows_reserved_4_2           ':  0x02 << (skl_reserved_4 << 2),
   'knows_reserved_4_3           ':  0x03 << (skl_reserved_4 << 2),
   'knows_reserved_4_4           ':  0x04 << (skl_reserved_4 << 2),
   'knows_reserved_4_5           ':  0x05 << (skl_reserved_4 << 2),
   'knows_reserved_4_6           ':  0x06 << (skl_reserved_4 << 2),
   'knows_reserved_4_7           ':  0x07 << (skl_reserved_4 << 2),
   'knows_reserved_4_8           ':  0x08 << (skl_reserved_4 << 2),
   'knows_reserved_4_9           ':  0x09 << (skl_reserved_4 << 2),
   'knows_reserved_4_10          ':  0x0A << (skl_reserved_4 << 2),
   'knows_reserved_4_11          ':  0x0B << (skl_reserved_4 << 2),
   'knows_reserved_4_12          ':  0x0C << (skl_reserved_4 << 2),
   'knows_reserved_4_13          ':  0x0D << (skl_reserved_4 << 2),
   'knows_reserved_4_14          ':  0x0E << (skl_reserved_4 << 2),
   'knows_reserved_4_15          ':  0x0F << (skl_reserved_4 << 2),
   'knows_persuasion_1           ':  0x01 << (skl_persuasion << 2),
   'knows_persuasion_2           ':  0x02 << (skl_persuasion << 2),
   'knows_persuasion_3           ':  0x03 << (skl_persuasion << 2),
   'knows_persuasion_4           ':  0x04 << (skl_persuasion << 2),
   'knows_persuasion_5           ':  0x05 << (skl_persuasion << 2),
   'knows_persuasion_6           ':  0x06 << (skl_persuasion << 2),
   'knows_persuasion_7           ':  0x07 << (skl_persuasion << 2),
   'knows_persuasion_8           ':  0x08 << (skl_persuasion << 2),
   'knows_persuasion_9           ':  0x09 << (skl_persuasion << 2),
   'knows_persuasion_10          ':  0x0A << (skl_persuasion << 2),
   'knows_persuasion_11          ':  0x0B << (skl_persuasion << 2),
   'knows_persuasion_12          ':  0x0C << (skl_persuasion << 2),
   'knows_persuasion_13          ':  0x0D << (skl_persuasion << 2),
   'knows_persuasion_14          ':  0x0E << (skl_persuasion << 2),
   'knows_persuasion_15          ':  0x0F << (skl_persuasion << 2),
   'knows_engineer_1             ':  0x01 << (skl_engineer << 2),
   'knows_engineer_2             ':  0x02 << (skl_engineer << 2),
   'knows_engineer_3             ':  0x03 << (skl_engineer << 2),
   'knows_engineer_4             ':  0x04 << (skl_engineer << 2),
   'knows_engineer_5             ':  0x05 << (skl_engineer << 2),
   'knows_engineer_6             ':  0x06 << (skl_engineer << 2),
   'knows_engineer_7             ':  0x07 << (skl_engineer << 2),
   'knows_engineer_8             ':  0x08 << (skl_engineer << 2),
   'knows_engineer_9             ':  0x09 << (skl_engineer << 2),
   'knows_engineer_10            ':  0x0A << (skl_engineer << 2),
   'knows_engineer_11            ':  0x0B << (skl_engineer << 2),
   'knows_engineer_12            ':  0x0C << (skl_engineer << 2),
   'knows_engineer_13            ':  0x0D << (skl_engineer << 2),
   'knows_engineer_14            ':  0x0E << (skl_engineer << 2),
   'knows_engineer_15            ':  0x0F << (skl_engineer << 2),
   'knows_first_aid_1            ':  0x01 << (skl_first_aid << 2),
   'knows_first_aid_2            ':  0x02 << (skl_first_aid << 2),
   'knows_first_aid_3            ':  0x03 << (skl_first_aid << 2),
   'knows_first_aid_4            ':  0x04 << (skl_first_aid << 2),
   'knows_first_aid_5            ':  0x05 << (skl_first_aid << 2),
   'knows_first_aid_6            ':  0x06 << (skl_first_aid << 2),
   'knows_first_aid_7            ':  0x07 << (skl_first_aid << 2),
   'knows_first_aid_8            ':  0x08 << (skl_first_aid << 2),
   'knows_first_aid_9            ':  0x09 << (skl_first_aid << 2),
   'knows_first_aid_10           ':  0x0A << (skl_first_aid << 2),
   'knows_first_aid_11           ':  0x0B << (skl_first_aid << 2),
   'knows_first_aid_12           ':  0x0C << (skl_first_aid << 2),
   'knows_first_aid_13           ':  0x0D << (skl_first_aid << 2),
   'knows_first_aid_14           ':  0x0E << (skl_first_aid << 2),
   'knows_first_aid_15           ':  0x0F << (skl_first_aid << 2),
   'knows_surgery_1              ':  0x01 << (skl_surgery << 2),
   'knows_surgery_2              ':  0x02 << (skl_surgery << 2),
   'knows_surgery_3              ':  0x03 << (skl_surgery << 2),
   'knows_surgery_4              ':  0x04 << (skl_surgery << 2),
   'knows_surgery_5              ':  0x05 << (skl_surgery << 2),
   'knows_surgery_6              ':  0x06 << (skl_surgery << 2),
   'knows_surgery_7              ':  0x07 << (skl_surgery << 2),
   'knows_surgery_8              ':  0x08 << (skl_surgery << 2),
   'knows_surgery_9              ':  0x09 << (skl_surgery << 2),
   'knows_surgery_10             ':  0x0A << (skl_surgery << 2),
   'knows_surgery_11             ':  0x0B << (skl_surgery << 2),
   'knows_surgery_12             ':  0x0C << (skl_surgery << 2),
   'knows_surgery_13             ':  0x0D << (skl_surgery << 2),
   'knows_surgery_14             ':  0x0E << (skl_surgery << 2),
   'knows_surgery_15             ':  0x0F << (skl_surgery << 2),
   'knows_wound_treatment_1      ':  0x01 << (skl_wound_treatment << 2),
   'knows_wound_treatment_2      ':  0x02 << (skl_wound_treatment << 2),
   'knows_wound_treatment_3      ':  0x03 << (skl_wound_treatment << 2),
   'knows_wound_treatment_4      ':  0x04 << (skl_wound_treatment << 2),
   'knows_wound_treatment_5      ':  0x05 << (skl_wound_treatment << 2),
   'knows_wound_treatment_6      ':  0x06 << (skl_wound_treatment << 2),
   'knows_wound_treatment_7      ':  0x07 << (skl_wound_treatment << 2),
   'knows_wound_treatment_8      ':  0x08 << (skl_wound_treatment << 2),
   'knows_wound_treatment_9      ':  0x09 << (skl_wound_treatment << 2),
   'knows_wound_treatment_10     ':  0x0A << (skl_wound_treatment << 2),
   'knows_wound_treatment_11     ':  0x0B << (skl_wound_treatment << 2),
   'knows_wound_treatment_12     ':  0x0C << (skl_wound_treatment << 2),
   'knows_wound_treatment_13     ':  0x0D << (skl_wound_treatment << 2),
   'knows_wound_treatment_14     ':  0x0E << (skl_wound_treatment << 2),
   'knows_wound_treatment_15     ':  0x0F << (skl_wound_treatment << 2),
   'knows_inventory_management_1 ':  0x01 << (skl_inventory_management << 2),
   'knows_inventory_management_2 ':  0x02 << (skl_inventory_management << 2),
   'knows_inventory_management_3 ':  0x03 << (skl_inventory_management << 2),
   'knows_inventory_management_4 ':  0x04 << (skl_inventory_management << 2),
   'knows_inventory_management_5 ':  0x05 << (skl_inventory_management << 2),
   'knows_inventory_management_6 ':  0x06 << (skl_inventory_management << 2),
   'knows_inventory_management_7 ':  0x07 << (skl_inventory_management << 2),
   'knows_inventory_management_8 ':  0x08 << (skl_inventory_management << 2),
   'knows_inventory_management_9 ':  0x09 << (skl_inventory_management << 2),
   'knows_inventory_management_10':  0x0A << (skl_inventory_management << 2),
   'knows_inventory_management_11':  0x0B << (skl_inventory_management << 2),
   'knows_inventory_management_12':  0x0C << (skl_inventory_management << 2),
   'knows_inventory_management_13':  0x0D << (skl_inventory_management << 2),
   'knows_inventory_management_14':  0x0E << (skl_inventory_management << 2),
   'knows_inventory_management_15':  0x0F << (skl_inventory_management << 2),
   'knows_spotting_1             ':  0x01 << (skl_spotting << 2),
   'knows_spotting_2             ':  0x02 << (skl_spotting << 2),
   'knows_spotting_3             ':  0x03 << (skl_spotting << 2),
   'knows_spotting_4             ':  0x04 << (skl_spotting << 2),
   'knows_spotting_5             ':  0x05 << (skl_spotting << 2),
   'knows_spotting_6             ':  0x06 << (skl_spotting << 2),
   'knows_spotting_7             ':  0x07 << (skl_spotting << 2),
   'knows_spotting_8             ':  0x08 << (skl_spotting << 2),
   'knows_spotting_9             ':  0x09 << (skl_spotting << 2),
   'knows_spotting_10            ':  0x0A << (skl_spotting << 2),
   'knows_spotting_11            ':  0x0B << (skl_spotting << 2),
   'knows_spotting_12            ':  0x0C << (skl_spotting << 2),
   'knows_spotting_13            ':  0x0D << (skl_spotting << 2),
   'knows_spotting_14            ':  0x0E << (skl_spotting << 2),
   'knows_spotting_15            ':  0x0F << (skl_spotting << 2),
   'knows_pathfinding_1          ':  0x01 << (skl_pathfinding << 2),
   'knows_pathfinding_2          ':  0x02 << (skl_pathfinding << 2),
   'knows_pathfinding_3          ':  0x03 << (skl_pathfinding << 2),
   'knows_pathfinding_4          ':  0x04 << (skl_pathfinding << 2),
   'knows_pathfinding_5          ':  0x05 << (skl_pathfinding << 2),
   'knows_pathfinding_6          ':  0x06 << (skl_pathfinding << 2),
   'knows_pathfinding_7          ':  0x07 << (skl_pathfinding << 2),
   'knows_pathfinding_8          ':  0x08 << (skl_pathfinding << 2),
   'knows_pathfinding_9          ':  0x09 << (skl_pathfinding << 2),
   'knows_pathfinding_10         ':  0x0A << (skl_pathfinding << 2),
   'knows_pathfinding_11         ':  0x0B << (skl_pathfinding << 2),
   'knows_pathfinding_12         ':  0x0C << (skl_pathfinding << 2),
   'knows_pathfinding_13         ':  0x0D << (skl_pathfinding << 2),
   'knows_pathfinding_14         ':  0x0E << (skl_pathfinding << 2),
   'knows_pathfinding_15         ':  0x0F << (skl_pathfinding << 2),
   'knows_tactics_1              ':  0x01 << (skl_tactics << 2),
   'knows_tactics_2              ':  0x02 << (skl_tactics << 2),
   'knows_tactics_3              ':  0x03 << (skl_tactics << 2),
   'knows_tactics_4              ':  0x04 << (skl_tactics << 2),
   'knows_tactics_5              ':  0x05 << (skl_tactics << 2),
   'knows_tactics_6              ':  0x06 << (skl_tactics << 2),
   'knows_tactics_7              ':  0x07 << (skl_tactics << 2),
   'knows_tactics_8              ':  0x08 << (skl_tactics << 2),
   'knows_tactics_9              ':  0x09 << (skl_tactics << 2),
   'knows_tactics_10             ':  0x0A << (skl_tactics << 2),
   'knows_tactics_11             ':  0x0B << (skl_tactics << 2),
   'knows_tactics_12             ':  0x0C << (skl_tactics << 2),
   'knows_tactics_13             ':  0x0D << (skl_tactics << 2),
   'knows_tactics_14             ':  0x0E << (skl_tactics << 2),
   'knows_tactics_15             ':  0x0F << (skl_tactics << 2),
   'knows_tracking_1             ':  0x01 << (skl_tracking << 2),
   'knows_tracking_2             ':  0x02 << (skl_tracking << 2),
   'knows_tracking_3             ':  0x03 << (skl_tracking << 2),
   'knows_tracking_4             ':  0x04 << (skl_tracking << 2),
   'knows_tracking_5             ':  0x05 << (skl_tracking << 2),
   'knows_tracking_6             ':  0x06 << (skl_tracking << 2),
   'knows_tracking_7             ':  0x07 << (skl_tracking << 2),
   'knows_tracking_8             ':  0x08 << (skl_tracking << 2),
   'knows_tracking_9             ':  0x09 << (skl_tracking << 2),
   'knows_tracking_10            ':  0x0A << (skl_tracking << 2),
   'knows_tracking_11            ':  0x0B << (skl_tracking << 2),
   'knows_tracking_12            ':  0x0C << (skl_tracking << 2),
   'knows_tracking_13            ':  0x0D << (skl_tracking << 2),
   'knows_tracking_14            ':  0x0E << (skl_tracking << 2),
   'knows_tracking_15            ':  0x0F << (skl_tracking << 2),
   'knows_trainer_1              ':  0x01 << (skl_trainer << 2),
   'knows_trainer_2              ':  0x02 << (skl_trainer << 2),
   'knows_trainer_3              ':  0x03 << (skl_trainer << 2),
   'knows_trainer_4              ':  0x04 << (skl_trainer << 2),
   'knows_trainer_5              ':  0x05 << (skl_trainer << 2),
   'knows_trainer_6              ':  0x06 << (skl_trainer << 2),
   'knows_trainer_7              ':  0x07 << (skl_trainer << 2),
   'knows_trainer_8              ':  0x08 << (skl_trainer << 2),
   'knows_trainer_9              ':  0x09 << (skl_trainer << 2),
   'knows_trainer_10             ':  0x0A << (skl_trainer << 2),
   'knows_trainer_11             ':  0x0B << (skl_trainer << 2),
   'knows_trainer_12             ':  0x0C << (skl_trainer << 2),
   'knows_trainer_13             ':  0x0D << (skl_trainer << 2),
   'knows_trainer_14             ':  0x0E << (skl_trainer << 2),
   'knows_trainer_15             ':  0x0F << (skl_trainer << 2),
   'knows_reserved_5_1           ':  0x01 << (skl_reserved_5 << 2),
   'knows_reserved_5_2           ':  0x02 << (skl_reserved_5 << 2),
   'knows_reserved_5_3           ':  0x03 << (skl_reserved_5 << 2),
   'knows_reserved_5_4           ':  0x04 << (skl_reserved_5 << 2),
   'knows_reserved_5_5           ':  0x05 << (skl_reserved_5 << 2),
   'knows_reserved_5_6           ':  0x06 << (skl_reserved_5 << 2),
   'knows_reserved_5_7           ':  0x07 << (skl_reserved_5 << 2),
   'knows_reserved_5_8           ':  0x08 << (skl_reserved_5 << 2),
   'knows_reserved_5_9           ':  0x09 << (skl_reserved_5 << 2),
   'knows_reserved_5_10          ':  0x0A << (skl_reserved_5 << 2),
   'knows_reserved_5_11          ':  0x0B << (skl_reserved_5 << 2),
   'knows_reserved_5_12          ':  0x0C << (skl_reserved_5 << 2),
   'knows_reserved_5_13          ':  0x0D << (skl_reserved_5 << 2),
   'knows_reserved_5_14          ':  0x0E << (skl_reserved_5 << 2),
   'knows_reserved_5_15          ':  0x0F << (skl_reserved_5 << 2),
   'knows_reserved_6_1           ':  0x01 << (skl_reserved_6 << 2),
   'knows_reserved_6_2           ':  0x02 << (skl_reserved_6 << 2),
   'knows_reserved_6_3           ':  0x03 << (skl_reserved_6 << 2),
   'knows_reserved_6_4           ':  0x04 << (skl_reserved_6 << 2),
   'knows_reserved_6_5           ':  0x05 << (skl_reserved_6 << 2),
   'knows_reserved_6_6           ':  0x06 << (skl_reserved_6 << 2),
   'knows_reserved_6_7           ':  0x07 << (skl_reserved_6 << 2),
   'knows_reserved_6_8           ':  0x08 << (skl_reserved_6 << 2),
   'knows_reserved_6_9           ':  0x09 << (skl_reserved_6 << 2),
   'knows_reserved_6_10          ':  0x0A << (skl_reserved_6 << 2),
   'knows_reserved_6_11          ':  0x0B << (skl_reserved_6 << 2),
   'knows_reserved_6_12          ':  0x0C << (skl_reserved_6 << 2),
   'knows_reserved_6_13          ':  0x0D << (skl_reserved_6 << 2),
   'knows_reserved_6_14          ':  0x0E << (skl_reserved_6 << 2),
   'knows_reserved_6_15          ':  0x0F << (skl_reserved_6 << 2),
   'knows_reserved_7_1           ':  0x01 << (skl_reserved_7 << 2),
   'knows_reserved_7_2           ':  0x02 << (skl_reserved_7 << 2),
   'knows_reserved_7_3           ':  0x03 << (skl_reserved_7 << 2),
   'knows_reserved_7_4           ':  0x04 << (skl_reserved_7 << 2),
   'knows_reserved_7_5           ':  0x05 << (skl_reserved_7 << 2),
   'knows_reserved_7_6           ':  0x06 << (skl_reserved_7 << 2),
   'knows_reserved_7_7           ':  0x07 << (skl_reserved_7 << 2),
   'knows_reserved_7_8           ':  0x08 << (skl_reserved_7 << 2),
   'knows_reserved_7_9           ':  0x09 << (skl_reserved_7 << 2),
   'knows_reserved_7_10          ':  0x0A << (skl_reserved_7 << 2),
   'knows_reserved_7_11          ':  0x0B << (skl_reserved_7 << 2),
   'knows_reserved_7_12          ':  0x0C << (skl_reserved_7 << 2),
   'knows_reserved_7_13          ':  0x0D << (skl_reserved_7 << 2),
   'knows_reserved_7_14          ':  0x0E << (skl_reserved_7 << 2),
   'knows_reserved_7_15          ':  0x0F << (skl_reserved_7 << 2),
   'knows_reserved_8_1           ':  0x01 << (skl_reserved_8 << 2),
   'knows_reserved_8_2           ':  0x02 << (skl_reserved_8 << 2),
   'knows_reserved_8_3           ':  0x03 << (skl_reserved_8 << 2),
   'knows_reserved_8_4           ':  0x04 << (skl_reserved_8 << 2),
   'knows_reserved_8_5           ':  0x05 << (skl_reserved_8 << 2),
   'knows_reserved_8_6           ':  0x06 << (skl_reserved_8 << 2),
   'knows_reserved_8_7           ':  0x07 << (skl_reserved_8 << 2),
   'knows_reserved_8_8           ':  0x08 << (skl_reserved_8 << 2),
   'knows_reserved_8_9           ':  0x09 << (skl_reserved_8 << 2),
   'knows_reserved_8_10          ':  0x0A << (skl_reserved_8 << 2),
   'knows_reserved_8_11          ':  0x0B << (skl_reserved_8 << 2),
   'knows_reserved_8_12          ':  0x0C << (skl_reserved_8 << 2),
   'knows_reserved_8_13          ':  0x0D << (skl_reserved_8 << 2),
   'knows_reserved_8_14          ':  0x0E << (skl_reserved_8 << 2),
   'knows_reserved_8_15          ':  0x0F << (skl_reserved_8 << 2),
   'knows_looting_1              ':  0x01 << (skl_looting << 2),
   'knows_looting_2              ':  0x02 << (skl_looting << 2),
   'knows_looting_3              ':  0x03 << (skl_looting << 2),
   'knows_looting_4              ':  0x04 << (skl_looting << 2),
   'knows_looting_5              ':  0x05 << (skl_looting << 2),
   'knows_looting_6              ':  0x06 << (skl_looting << 2),
   'knows_looting_7              ':  0x07 << (skl_looting << 2),
   'knows_looting_8              ':  0x08 << (skl_looting << 2),
   'knows_looting_9              ':  0x09 << (skl_looting << 2),
   'knows_looting_10             ':  0x0A << (skl_looting << 2),
   'knows_looting_11             ':  0x0B << (skl_looting << 2),
   'knows_looting_12             ':  0x0C << (skl_looting << 2),
   'knows_looting_13             ':  0x0D << (skl_looting << 2),
   'knows_looting_14             ':  0x0E << (skl_looting << 2),
   'knows_looting_15             ':  0x0F << (skl_looting << 2),
   'knows_horse_archery_1        ':  0x01 << (skl_horse_archery << 2),
   'knows_horse_archery_2        ':  0x02 << (skl_horse_archery << 2),
   'knows_horse_archery_3        ':  0x03 << (skl_horse_archery << 2),
   'knows_horse_archery_4        ':  0x04 << (skl_horse_archery << 2),
   'knows_horse_archery_5        ':  0x05 << (skl_horse_archery << 2),
   'knows_horse_archery_6        ':  0x06 << (skl_horse_archery << 2),
   'knows_horse_archery_7        ':  0x07 << (skl_horse_archery << 2),
   'knows_horse_archery_8        ':  0x08 << (skl_horse_archery << 2),
   'knows_horse_archery_9        ':  0x09 << (skl_horse_archery << 2),
   'knows_horse_archery_10       ':  0x0A << (skl_horse_archery << 2),
   'knows_horse_archery_11       ':  0x0B << (skl_horse_archery << 2),
   'knows_horse_archery_12       ':  0x0C << (skl_horse_archery << 2),
   'knows_horse_archery_13       ':  0x0D << (skl_horse_archery << 2),
   'knows_horse_archery_14       ':  0x0E << (skl_horse_archery << 2),
   'knows_horse_archery_15       ':  0x0F << (skl_horse_archery << 2),
   'knows_riding_1               ':  0x01 << (skl_riding << 2),
   'knows_riding_2               ':  0x02 << (skl_riding << 2),
   'knows_riding_3               ':  0x03 << (skl_riding << 2),
   'knows_riding_4               ':  0x04 << (skl_riding << 2),
   'knows_riding_5               ':  0x05 << (skl_riding << 2),
   'knows_riding_6               ':  0x06 << (skl_riding << 2),
   'knows_riding_7               ':  0x07 << (skl_riding << 2),
   'knows_riding_8               ':  0x08 << (skl_riding << 2),
   'knows_riding_9               ':  0x09 << (skl_riding << 2),
   'knows_riding_10              ':  0x0A << (skl_riding << 2),
   'knows_riding_11              ':  0x0B << (skl_riding << 2),
   'knows_riding_12              ':  0x0C << (skl_riding << 2),
   'knows_riding_13              ':  0x0D << (skl_riding << 2),
   'knows_riding_14              ':  0x0E << (skl_riding << 2),
   'knows_riding_15              ':  0x0F << (skl_riding << 2),
   'knows_athletics_1            ':  0x01 << (skl_athletics << 2),
   'knows_athletics_2            ':  0x02 << (skl_athletics << 2),
   'knows_athletics_3            ':  0x03 << (skl_athletics << 2),
   'knows_athletics_4            ':  0x04 << (skl_athletics << 2),
   'knows_athletics_5            ':  0x05 << (skl_athletics << 2),
   'knows_athletics_6            ':  0x06 << (skl_athletics << 2),
   'knows_athletics_7            ':  0x07 << (skl_athletics << 2),
   'knows_athletics_8            ':  0x08 << (skl_athletics << 2),
   'knows_athletics_9            ':  0x09 << (skl_athletics << 2),
   'knows_athletics_10           ':  0x0A << (skl_athletics << 2),
   'knows_athletics_11           ':  0x0B << (skl_athletics << 2),
   'knows_athletics_12           ':  0x0C << (skl_athletics << 2),
   'knows_athletics_13           ':  0x0D << (skl_athletics << 2),
   'knows_athletics_14           ':  0x0E << (skl_athletics << 2),
   'knows_athletics_15           ':  0x0F << (skl_athletics << 2),
   'knows_shield_1               ':  0x01 << (skl_shield << 2),
   'knows_shield_2               ':  0x02 << (skl_shield << 2),
   'knows_shield_3               ':  0x03 << (skl_shield << 2),
   'knows_shield_4               ':  0x04 << (skl_shield << 2),
   'knows_shield_5               ':  0x05 << (skl_shield << 2),
   'knows_shield_6               ':  0x06 << (skl_shield << 2),
   'knows_shield_7               ':  0x07 << (skl_shield << 2),
   'knows_shield_8               ':  0x08 << (skl_shield << 2),
   'knows_shield_9               ':  0x09 << (skl_shield << 2),
   'knows_shield_10              ':  0x0A << (skl_shield << 2),
   'knows_shield_11              ':  0x0B << (skl_shield << 2),
   'knows_shield_12              ':  0x0C << (skl_shield << 2),
   'knows_shield_13              ':  0x0D << (skl_shield << 2),
   'knows_shield_14              ':  0x0E << (skl_shield << 2),
   'knows_shield_15              ':  0x0F << (skl_shield << 2),
   'knows_weapon_master_1        ':  0x01 << (skl_weapon_master << 2),
   'knows_weapon_master_2        ':  0x02 << (skl_weapon_master << 2),
   'knows_weapon_master_3        ':  0x03 << (skl_weapon_master << 2),
   'knows_weapon_master_4        ':  0x04 << (skl_weapon_master << 2),
   'knows_weapon_master_5        ':  0x05 << (skl_weapon_master << 2),
   'knows_weapon_master_6        ':  0x06 << (skl_weapon_master << 2),
   'knows_weapon_master_7        ':  0x07 << (skl_weapon_master << 2),
   'knows_weapon_master_8        ':  0x08 << (skl_weapon_master << 2),
   'knows_weapon_master_9        ':  0x09 << (skl_weapon_master << 2),
   'knows_weapon_master_10       ':  0x0A << (skl_weapon_master << 2),
   'knows_weapon_master_11       ':  0x0B << (skl_weapon_master << 2),
   'knows_weapon_master_12       ':  0x0C << (skl_weapon_master << 2),
   'knows_weapon_master_13       ':  0x0D << (skl_weapon_master << 2),
   'knows_weapon_master_14       ':  0x0E << (skl_weapon_master << 2),
   'knows_weapon_master_15       ':  0x0F << (skl_weapon_master << 2),
   'knows_reserved_9_1           ':  0x01 << (skl_reserved_9 << 2),
   'knows_reserved_9_2           ':  0x02 << (skl_reserved_9 << 2),
   'knows_reserved_9_3           ':  0x03 << (skl_reserved_9 << 2),
   'knows_reserved_9_4           ':  0x04 << (skl_reserved_9 << 2),
   'knows_reserved_9_5           ':  0x05 << (skl_reserved_9 << 2),
   'knows_reserved_9_6           ':  0x06 << (skl_reserved_9 << 2),
   'knows_reserved_9_7           ':  0x07 << (skl_reserved_9 << 2),
   'knows_reserved_9_8           ':  0x08 << (skl_reserved_9 << 2),
   'knows_reserved_9_9           ':  0x09 << (skl_reserved_9 << 2),
   'knows_reserved_9_10          ':  0x0A << (skl_reserved_9 << 2),
   'knows_reserved_9_11          ':  0x0B << (skl_reserved_9 << 2),
   'knows_reserved_9_12          ':  0x0C << (skl_reserved_9 << 2),
   'knows_reserved_9_13          ':  0x0D << (skl_reserved_9 << 2),
   'knows_reserved_9_14          ':  0x0E << (skl_reserved_9 << 2),
   'knows_reserved_9_15          ':  0x0F << (skl_reserved_9 << 2),
   'knows_reserved_10_1          ':  0x01 << (skl_reserved_10 << 2),
   'knows_reserved_10_2          ':  0x02 << (skl_reserved_10 << 2),
   'knows_reserved_10_3          ':  0x03 << (skl_reserved_10 << 2),
   'knows_reserved_10_4          ':  0x04 << (skl_reserved_10 << 2),
   'knows_reserved_10_5          ':  0x05 << (skl_reserved_10 << 2),
   'knows_reserved_10_6          ':  0x06 << (skl_reserved_10 << 2),
   'knows_reserved_10_7          ':  0x07 << (skl_reserved_10 << 2),
   'knows_reserved_10_8          ':  0x08 << (skl_reserved_10 << 2),
   'knows_reserved_10_9          ':  0x09 << (skl_reserved_10 << 2),
   'knows_reserved_10_10         ':  0x0A << (skl_reserved_10 << 2),
   'knows_reserved_10_11         ':  0x0B << (skl_reserved_10 << 2),
   'knows_reserved_10_12         ':  0x0C << (skl_reserved_10 << 2),
   'knows_reserved_10_13         ':  0x0D << (skl_reserved_10 << 2),
   'knows_reserved_10_14         ':  0x0E << (skl_reserved_10 << 2),
   'knows_reserved_10_15         ':  0x0F << (skl_reserved_10 << 2),
   'knows_reserved_11_1          ':  0x01 << (skl_reserved_11 << 2),
   'knows_reserved_11_2          ':  0x02 << (skl_reserved_11 << 2),
   'knows_reserved_11_3          ':  0x03 << (skl_reserved_11 << 2),
   'knows_reserved_11_4          ':  0x04 << (skl_reserved_11 << 2),
   'knows_reserved_11_5          ':  0x05 << (skl_reserved_11 << 2),
   'knows_reserved_11_6          ':  0x06 << (skl_reserved_11 << 2),
   'knows_reserved_11_7          ':  0x07 << (skl_reserved_11 << 2),
   'knows_reserved_11_8          ':  0x08 << (skl_reserved_11 << 2),
   'knows_reserved_11_9          ':  0x09 << (skl_reserved_11 << 2),
   'knows_reserved_11_10         ':  0x0A << (skl_reserved_11 << 2),
   'knows_reserved_11_11         ':  0x0B << (skl_reserved_11 << 2),
   'knows_reserved_11_12         ':  0x0C << (skl_reserved_11 << 2),
   'knows_reserved_11_13         ':  0x0D << (skl_reserved_11 << 2),
   'knows_reserved_11_14         ':  0x0E << (skl_reserved_11 << 2),
   'knows_reserved_11_15         ':  0x0F << (skl_reserved_11 << 2),
   'knows_reserved_12_1          ':  0x01 << (skl_reserved_12 << 2),
   'knows_reserved_12_2          ':  0x02 << (skl_reserved_12 << 2),
   'knows_reserved_12_3          ':  0x03 << (skl_reserved_12 << 2),
   'knows_reserved_12_4          ':  0x04 << (skl_reserved_12 << 2),
   'knows_reserved_12_5          ':  0x05 << (skl_reserved_12 << 2),
   'knows_reserved_12_6          ':  0x06 << (skl_reserved_12 << 2),
   'knows_reserved_12_7          ':  0x07 << (skl_reserved_12 << 2),
   'knows_reserved_12_8          ':  0x08 << (skl_reserved_12 << 2),
   'knows_reserved_12_9          ':  0x09 << (skl_reserved_12 << 2),
   'knows_reserved_12_10         ':  0x0A << (skl_reserved_12 << 2),
   'knows_reserved_12_11         ':  0x0B << (skl_reserved_12 << 2),
   'knows_reserved_12_12         ':  0x0C << (skl_reserved_12 << 2),
   'knows_reserved_12_13         ':  0x0D << (skl_reserved_12 << 2),
   'knows_reserved_12_14         ':  0x0E << (skl_reserved_12 << 2),
   'knows_reserved_12_15         ':  0x0F << (skl_reserved_12 << 2),
   'knows_reserved_13_1          ':  0x01 << (skl_reserved_13 << 2),
   'knows_reserved_13_2          ':  0x02 << (skl_reserved_13 << 2),
   'knows_reserved_13_3          ':  0x03 << (skl_reserved_13 << 2),
   'knows_reserved_13_4          ':  0x04 << (skl_reserved_13 << 2),
   'knows_reserved_13_5          ':  0x05 << (skl_reserved_13 << 2),
   'knows_reserved_13_6          ':  0x06 << (skl_reserved_13 << 2),
   'knows_reserved_13_7          ':  0x07 << (skl_reserved_13 << 2),
   'knows_reserved_13_8          ':  0x08 << (skl_reserved_13 << 2),
   'knows_reserved_13_9          ':  0x09 << (skl_reserved_13 << 2),
   'knows_reserved_13_10         ':  0x0A << (skl_reserved_13 << 2),
   'knows_reserved_13_11         ':  0x0B << (skl_reserved_13 << 2),
   'knows_reserved_13_12         ':  0x0C << (skl_reserved_13 << 2),
   'knows_reserved_13_13         ':  0x0D << (skl_reserved_13 << 2),
   'knows_reserved_13_14         ':  0x0E << (skl_reserved_13 << 2),
   'knows_reserved_13_15         ':  0x0F << (skl_reserved_13 << 2),
   'knows_power_draw_1           ':  0x01 << (skl_power_draw << 2),
   'knows_power_draw_2           ':  0x02 << (skl_power_draw << 2),
   'knows_power_draw_3           ':  0x03 << (skl_power_draw << 2),
   'knows_power_draw_4           ':  0x04 << (skl_power_draw << 2),
   'knows_power_draw_5           ':  0x05 << (skl_power_draw << 2),
   'knows_power_draw_6           ':  0x06 << (skl_power_draw << 2),
   'knows_power_draw_7           ':  0x07 << (skl_power_draw << 2),
   'knows_power_draw_8           ':  0x08 << (skl_power_draw << 2),
   'knows_power_draw_9           ':  0x09 << (skl_power_draw << 2),
   'knows_power_draw_10          ':  0x0A << (skl_power_draw << 2),
   'knows_power_draw_11          ':  0x0B << (skl_power_draw << 2),
   'knows_power_draw_12          ':  0x0C << (skl_power_draw << 2),
   'knows_power_draw_13          ':  0x0D << (skl_power_draw << 2),
   'knows_power_draw_14          ':  0x0E << (skl_power_draw << 2),
   'knows_power_draw_15          ':  0x0F << (skl_power_draw << 2),
   'knows_power_throw_1          ':  0x01 << (skl_power_throw << 2),
   'knows_power_throw_2          ':  0x02 << (skl_power_throw << 2),
   'knows_power_throw_3          ':  0x03 << (skl_power_throw << 2),
   'knows_power_throw_4          ':  0x04 << (skl_power_throw << 2),
   'knows_power_throw_5          ':  0x05 << (skl_power_throw << 2),
   'knows_power_throw_6          ':  0x06 << (skl_power_throw << 2),
   'knows_power_throw_7          ':  0x07 << (skl_power_throw << 2),
   'knows_power_throw_8          ':  0x08 << (skl_power_throw << 2),
   'knows_power_throw_9          ':  0x09 << (skl_power_throw << 2),
   'knows_power_throw_10         ':  0x0A << (skl_power_throw << 2),
   'knows_power_throw_11         ':  0x0B << (skl_power_throw << 2),
   'knows_power_throw_12         ':  0x0C << (skl_power_throw << 2),
   'knows_power_throw_13         ':  0x0D << (skl_power_throw << 2),
   'knows_power_throw_14         ':  0x0E << (skl_power_throw << 2),
   'knows_power_throw_15         ':  0x0F << (skl_power_throw << 2),
   'knows_power_strike_1         ':  0x01 << (skl_power_strike << 2),
   'knows_power_strike_2         ':  0x02 << (skl_power_strike << 2),
   'knows_power_strike_3         ':  0x03 << (skl_power_strike << 2),
   'knows_power_strike_4         ':  0x04 << (skl_power_strike << 2),
   'knows_power_strike_5         ':  0x05 << (skl_power_strike << 2),
   'knows_power_strike_6         ':  0x06 << (skl_power_strike << 2),
   'knows_power_strike_7         ':  0x07 << (skl_power_strike << 2),
   'knows_power_strike_8         ':  0x08 << (skl_power_strike << 2),
   'knows_power_strike_9         ':  0x09 << (skl_power_strike << 2),
   'knows_power_strike_10        ':  0x0A << (skl_power_strike << 2),
   'knows_power_strike_11        ':  0x0B << (skl_power_strike << 2),
   'knows_power_strike_12        ':  0x0C << (skl_power_strike << 2),
   'knows_power_strike_13        ':  0x0D << (skl_power_strike << 2),
   'knows_power_strike_14        ':  0x0E << (skl_power_strike << 2),
   'knows_power_strike_15        ':  0x0F << (skl_power_strike << 2),
   'knows_ironflesh_1            ':  0x01 << (skl_ironflesh << 2),
   'knows_ironflesh_2            ':  0x02 << (skl_ironflesh << 2),
   'knows_ironflesh_3            ':  0x03 << (skl_ironflesh << 2),
   'knows_ironflesh_4            ':  0x04 << (skl_ironflesh << 2),
   'knows_ironflesh_5            ':  0x05 << (skl_ironflesh << 2),
   'knows_ironflesh_6            ':  0x06 << (skl_ironflesh << 2),
   'knows_ironflesh_7            ':  0x07 << (skl_ironflesh << 2),
   'knows_ironflesh_8            ':  0x08 << (skl_ironflesh << 2),
   'knows_ironflesh_9            ':  0x09 << (skl_ironflesh << 2),
   'knows_ironflesh_10           ':  0x0A << (skl_ironflesh << 2),
   'knows_ironflesh_11           ':  0x0B << (skl_ironflesh << 2),
   'knows_ironflesh_12           ':  0x0C << (skl_ironflesh << 2),
   'knows_ironflesh_13           ':  0x0D << (skl_ironflesh << 2),
   'knows_ironflesh_14           ':  0x0E << (skl_ironflesh << 2),
   'knows_ironflesh_15           ':  0x0F << (skl_ironflesh << 2),
   'knows_reserved_14_1          ':  0x01 << (skl_reserved_14 << 2),
   'knows_reserved_14_2          ':  0x02 << (skl_reserved_14 << 2),
   'knows_reserved_14_3          ':  0x03 << (skl_reserved_14 << 2),
   'knows_reserved_14_4          ':  0x04 << (skl_reserved_14 << 2),
   'knows_reserved_14_5          ':  0x05 << (skl_reserved_14 << 2),
   'knows_reserved_14_6          ':  0x06 << (skl_reserved_14 << 2),
   'knows_reserved_14_7          ':  0x07 << (skl_reserved_14 << 2),
   'knows_reserved_14_8          ':  0x08 << (skl_reserved_14 << 2),
   'knows_reserved_14_9          ':  0x09 << (skl_reserved_14 << 2),
   'knows_reserved_14_10         ':  0x0A << (skl_reserved_14 << 2),
   'knows_reserved_14_11         ':  0x0B << (skl_reserved_14 << 2),
   'knows_reserved_14_12         ':  0x0C << (skl_reserved_14 << 2),
   'knows_reserved_14_13         ':  0x0D << (skl_reserved_14 << 2),
   'knows_reserved_14_14         ':  0x0E << (skl_reserved_14 << 2),
   'knows_reserved_14_15         ':  0x0F << (skl_reserved_14 << 2),
   'knows_reserved_15_1          ':  0x01 << (skl_reserved_15 << 2),
   'knows_reserved_15_2          ':  0x02 << (skl_reserved_15 << 2),
   'knows_reserved_15_3          ':  0x03 << (skl_reserved_15 << 2),
   'knows_reserved_15_4          ':  0x04 << (skl_reserved_15 << 2),
   'knows_reserved_15_5          ':  0x05 << (skl_reserved_15 << 2),
   'knows_reserved_15_6          ':  0x06 << (skl_reserved_15 << 2),
   'knows_reserved_15_7          ':  0x07 << (skl_reserved_15 << 2),
   'knows_reserved_15_8          ':  0x08 << (skl_reserved_15 << 2),
   'knows_reserved_15_9          ':  0x09 << (skl_reserved_15 << 2),
   'knows_reserved_15_10         ':  0x0A << (skl_reserved_15 << 2),
   'knows_reserved_15_11         ':  0x0B << (skl_reserved_15 << 2),
   'knows_reserved_15_12         ':  0x0C << (skl_reserved_15 << 2),
   'knows_reserved_15_13         ':  0x0D << (skl_reserved_15 << 2),
   'knows_reserved_15_14         ':  0x0E << (skl_reserved_15 << 2),
   'knows_reserved_15_15         ':  0x0F << (skl_reserved_15 << 2),
   'knows_reserved_16_1          ':  0x01 << (skl_reserved_16 << 2),
   'knows_reserved_16_2          ':  0x02 << (skl_reserved_16 << 2),
   'knows_reserved_16_3          ':  0x03 << (skl_reserved_16 << 2),
   'knows_reserved_16_4          ':  0x04 << (skl_reserved_16 << 2),
   'knows_reserved_16_5          ':  0x05 << (skl_reserved_16 << 2),
   'knows_reserved_16_6          ':  0x06 << (skl_reserved_16 << 2),
   'knows_reserved_16_7          ':  0x07 << (skl_reserved_16 << 2),
   'knows_reserved_16_8          ':  0x08 << (skl_reserved_16 << 2),
   'knows_reserved_16_9          ':  0x09 << (skl_reserved_16 << 2),
   'knows_reserved_16_10         ':  0x0A << (skl_reserved_16 << 2),
   'knows_reserved_16_11         ':  0x0B << (skl_reserved_16 << 2),
   'knows_reserved_16_12         ':  0x0C << (skl_reserved_16 << 2),
   'knows_reserved_16_13         ':  0x0D << (skl_reserved_16 << 2),
   'knows_reserved_16_14         ':  0x0E << (skl_reserved_16 << 2),
   'knows_reserved_16_15         ':  0x0F << (skl_reserved_16 << 2),
   'knows_reserved_17_1          ':  0x01 << (skl_reserved_17 << 2),
   'knows_reserved_17_2          ':  0x02 << (skl_reserved_17 << 2),
   'knows_reserved_17_3          ':  0x03 << (skl_reserved_17 << 2),
   'knows_reserved_17_4          ':  0x04 << (skl_reserved_17 << 2),
   'knows_reserved_17_5          ':  0x05 << (skl_reserved_17 << 2),
   'knows_reserved_17_6          ':  0x06 << (skl_reserved_17 << 2),
   'knows_reserved_17_7          ':  0x07 << (skl_reserved_17 << 2),
   'knows_reserved_17_8          ':  0x08 << (skl_reserved_17 << 2),
   'knows_reserved_17_9          ':  0x09 << (skl_reserved_17 << 2),
   'knows_reserved_17_10         ':  0x0A << (skl_reserved_17 << 2),
   'knows_reserved_17_11         ':  0x0B << (skl_reserved_17 << 2),
   'knows_reserved_17_12         ':  0x0C << (skl_reserved_17 << 2),
   'knows_reserved_17_13         ':  0x0D << (skl_reserved_17 << 2),
   'knows_reserved_17_14         ':  0x0E << (skl_reserved_17 << 2),
   'knows_reserved_17_15         ':  0x0F << (skl_reserved_17 << 2),
   'knows_reserved_18_1          ':  0x01 << (skl_reserved_18 << 2),
   'knows_reserved_18_2          ':  0x02 << (skl_reserved_18 << 2),
   'knows_reserved_18_3          ':  0x03 << (skl_reserved_18 << 2),
   'knows_reserved_18_4          ':  0x04 << (skl_reserved_18 << 2),
   'knows_reserved_18_5          ':  0x05 << (skl_reserved_18 << 2),
   'knows_reserved_18_6          ':  0x06 << (skl_reserved_18 << 2),
   'knows_reserved_18_7          ':  0x07 << (skl_reserved_18 << 2),
   'knows_reserved_18_8          ':  0x08 << (skl_reserved_18 << 2),
   'knows_reserved_18_9          ':  0x09 << (skl_reserved_18 << 2),
   'knows_reserved_18_10         ':  0x0A << (skl_reserved_18 << 2),
   'knows_reserved_18_11         ':  0x0B << (skl_reserved_18 << 2),
   'knows_reserved_18_12         ':  0x0C << (skl_reserved_18 << 2),
   'knows_reserved_18_13         ':  0x0D << (skl_reserved_18 << 2),
   'knows_reserved_18_14         ':  0x0E << (skl_reserved_18 << 2),
   'knows_reserved_18_15         ':  0x0F << (skl_reserved_18 << 2),
}
troop_skills = {}
for k,v in troop_skills_old.iteritems():
    troop_skills[v] = k.replace(' ','')
    

troop_skill_combinations_old = {
    'knows_common': knows_riding_1|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1,
    'knows_common_multiplayer': knows_trade_10|knows_inventory_management_10|knows_prisoner_management_10|knows_leadership_10|knows_spotting_10|knows_pathfinding_10|knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10,
    'knows_lord_1': knows_riding_3|knows_trade_2|knows_inventory_management_2|knows_tactics_4|knows_prisoner_management_4|knows_leadership_7,
    'knows_warrior_npc': knows_weapon_master_2|knows_ironflesh_1|knows_athletics_1|knows_power_strike_2|knows_riding_2|knows_shield_1|knows_inventory_management_2,
    'knows_merchant_npc': knows_riding_2|knows_trade_3|knows_inventory_management_3,
    'knows_tracker_npc': knows_weapon_master_1|knows_athletics_2|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_ironflesh_1|knows_inventory_management_2,
    'knight_skills_1': knows_riding_3|knows_ironflesh_2|knows_power_strike_3|knows_athletics_1|knows_tactics_2|knows_prisoner_management_1|knows_leadership_3,
    'knight_skills_2': knows_riding_4|knows_ironflesh_3|knows_power_strike_4|knows_athletics_2|knows_tactics_3|knows_prisoner_management_2|knows_leadership_5,
    'knight_skills_3': knows_riding_5|knows_ironflesh_4|knows_power_strike_5|knows_athletics_3|knows_tactics_4|knows_prisoner_management_2|knows_leadership_6,
    'knight_skills_4': knows_riding_6|knows_ironflesh_5|knows_power_strike_6|knows_athletics_4|knows_tactics_5|knows_prisoner_management_3|knows_leadership_7,
    'knight_skills_5': knows_riding_7|knows_ironflesh_6|knows_power_strike_7|knows_athletics_5|knows_tactics_6|knows_prisoner_management_3|knows_leadership_9,
}
troop_skill_combinations = {}
for k,v in troop_skill_combinations_old.iteritems():
    troop_skill_combinations[v] = k.replace(' ','')
    
    
troop_faces_old = {
    'swadian_face_younger_1':  0x0000000000000001124000000020000000000000001c00800000000000000000,
    'swadian_face_young_1  ':  0x0000000400000001124000000020000000000000001c00800000000000000000,
    'swadian_face_middle_1 ':  0x0000000800000001124000000020000000000000001c00800000000000000000,
    'swadian_face_old_1    ':  0x0000000d00000001124000000020000000000000001c00800000000000000000,
    'swadian_face_older_1  ':  0x0000000fc0000001124000000020000000000000001c00800000000000000000,
    'swadian_face_younger_2':  0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000,
    'swadian_face_young_2  ':  0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000,
    'swadian_face_middle_2 ':  0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000,
    'swadian_face_old_2    ':  0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000,
    'swadian_face_older_2  ':  0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000,
    'vaegir_face_younger_1':  0x0000000000000001124000000020000000000000001c00800000000000000000,
    'vaegir_face_young_1  ':  0x0000000400000001124000000020000000000000001c00800000000000000000,
    'vaegir_face_middle_1 ':  0x0000000800000001124000000020000000000000001c00800000000000000000,
    'vaegir_face_old_1    ':  0x0000000d00000001124000000020000000000000001c00800000000000000000,
    'vaegir_face_older_1  ':  0x0000000fc0000001124000000020000000000000001c00800000000000000000,
    'vaegir_face_younger_2':  0x000000003f00230c4deeffffffffffff00000000001efff90000000000000000,
    'vaegir_face_young_2  ':  0x00000003bf00230c4deeffffffffffff00000000001efff90000000000000000,
    'vaegir_face_middle_2 ':  0x00000007bf00230c4deeffffffffffff00000000001efff90000000000000000,
    'vaegir_face_old_2    ':  0x0000000cbf00230c4deeffffffffffff00000000001efff90000000000000000,
    'vaegir_face_older_2  ':  0x0000000ff100230c4deeffffffffffff00000000001efff90000000000000000,
    'khergit_face_younger_1':  0x0000000009003109207000000000000000000000001c80470000000000000000,
    'khergit_face_young_1  ':  0x00000003c9003109207000000000000000000000001c80470000000000000000,
    'khergit_face_middle_1 ':  0x00000007c9003109207000000000000000000000001c80470000000000000000,
    'khergit_face_old_1    ':  0x0000000b89003109207000000000000000000000001c80470000000000000000,
    'khergit_face_older_1  ':  0x0000000fc9003109207000000000000000000000001c80470000000000000000,
    'khergit_face_younger_2':  0x000000003f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000,
    'khergit_face_young_2  ':  0x00000003bf0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000,
    'khergit_face_middle_2 ':  0x000000077f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000,
    'khergit_face_old_2    ':  0x0000000b3f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000,
    'khergit_face_older_2  ':  0x0000000fff0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000,
    'nord_face_younger_1':  0x0000000000000001124000000020000000000000001c00800000000000000000,
    'nord_face_young_1  ':  0x0000000400000001124000000020000000000000001c00800000000000000000,
    'nord_face_middle_1 ':  0x0000000800000001124000000020000000000000001c00800000000000000000,
    'nord_face_old_1    ':  0x0000000d00000001124000000020000000000000001c00800000000000000000,
    'nord_face_older_1  ':  0x0000000fc0000001124000000020000000000000001c00800000000000000000,
    'nord_face_younger_2':  0x00000000310023084deeffffffffffff00000000001efff90000000000000000,
    'nord_face_young_2  ':  0x00000003b10023084deeffffffffffff00000000001efff90000000000000000,
    'nord_face_middle_2 ':  0x00000008310023084deeffffffffffff00000000001efff90000000000000000,
    'nord_face_old_2    ':  0x0000000c710023084deeffffffffffff00000000001efff90000000000000000,
    'nord_face_older_2  ':  0x0000000ff10023084deeffffffffffff00000000001efff90000000000000000,
    'rhodok_face_younger_1':  0x0000000009002003140000000000000000000000001c80400000000000000000,
    'rhodok_face_young_1  ':  0x0000000449002003140000000000000000000000001c80400000000000000000,
    'rhodok_face_middle_1 ':  0x0000000849002003140000000000000000000000001c80400000000000000000,
    'rhodok_face_old_1    ':  0x0000000cc9002003140000000000000000000000001c80400000000000000000,
    'rhodok_face_older_1  ':  0x0000000fc9002003140000000000000000000000001c80400000000000000000,
    'rhodok_face_younger_2':  0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000,
    'rhodok_face_young_2  ':  0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000,
    'rhodok_face_middle_2 ':  0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000,
    'rhodok_face_old_2    ':  0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000,
    'rhodok_face_older_2  ':  0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000,
    'man_face_younger_1':  0x0000000000000001124000000020000000000000001c00800000000000000000,
    'man_face_young_1  ':  0x0000000400000001124000000020000000000000001c00800000000000000000,
    'man_face_middle_1 ':  0x0000000800000001124000000020000000000000001c00800000000000000000,
    'man_face_old_1    ':  0x0000000d00000001124000000020000000000000001c00800000000000000000,
    'man_face_older_1  ':  0x0000000fc0000001124000000020000000000000001c00800000000000000000,
    'man_face_younger_2':  0x000000003f0052064deeffffffffffff00000000001efff90000000000000000,
    'man_face_young_2  ':  0x00000003bf0052064deeffffffffffff00000000001efff90000000000000000,
    'man_face_middle_2 ':  0x00000007bf0052064deeffffffffffff00000000001efff90000000000000000,
    'man_face_old_2    ':  0x0000000bff0052064deeffffffffffff00000000001efff90000000000000000,
    'man_face_older_2  ':  0x0000000fff0052064deeffffffffffff00000000001efff90000000000000000,
    'merchant_face_1   ':  0x0000000400000001124000000020000000000000001c00800000000000000000,
    'merchant_face_2   ':  0x0000000fff0052064deeffffffffffff00000000001efff90000000000000000,
    'woman_face_1   ':  0x0000000000000001000000000000000000000000001c00000000000000000000,
    'woman_face_2   ':  0x00000003bf0030067ff7fbffefff6dff00000000001f6dbf0000000000000000,
    'swadian_woman_face_1':  0x0000000180102006124925124928924900000000001c92890000000000000000,
    'swadian_woman_face_2':  0x00000001bf1000061db6d75db6b6dbad00000000001c92890000000000000000,
    'khergit_woman_face_1':  0x0000000180103006124925124928924900000000001c92890000000000000000,
    'khergit_woman_face_2':  0x00000001af1030025b6eb6dd6db6dd6d00000000001eedae0000000000000000,
    'refugee_face1':  0x0000000000000001000000000000000000000000001c00000000000000000000,
    'refugee_face2':  0x00000003bf0030067ff7fbffefff6dff00000000001f6dbf0000000000000000,
    'girl_face1   ':  0x0000000000000001000000000000000000000000001c00000000000000000000,
    'girl_face2   ':  0x00000003bf0030067ff7fbffefff6dff00000000001f6dbf0000000000000000,
    'mercenary_face_1':  0x0000000000000000000000000000000000000000001c00000000000000000000,
    'mercenary_face_2':  0x0000000cff00730b6db6db6db7fbffff00000000001efffe0000000000000000,
    'vaegir_face1 ':  0x0000000400000001124000000020000000000000001c00800000000000000000,
    'vaegir_face2 ':  0x0000000ff100230c4deeffffffffffff00000000001efff90000000000000000,
    'bandit_face1 ':  0x0000000400000001124000000020000000000000001c00800000000000000000,
    'bandit_face2 ':  0x0000000fff0052064deeffffffffffff00000000001efff90000000000000000,
    'undead_face1 ':  0x00000000002000000000000000000000,
    'undead_face2 ':  0x000000000020010000001fffffffffff,
}
troop_faces = {}
for k,v in troop_faces_old.iteritems():
    troop_faces[v] = k.replace(' ','')
    

#-----------------------------------------------------------------------------#
#------------------------above this are constants ----------------------------#
#-----------------------------------------------------------------------------#


def get_flag_code(line):
    flag_code = ''''''
    troop_flag = int(line[4])
    
    if troop_flag==0:
        return '0'
    
    troop_flag_keys = troop_flags.keys()
    troop_flag_keys.sort()
    troop_flag_keys.reverse()
    for each_flag in troop_flag_keys:
        if troop_flag&each_flag==each_flag:
            flag_code += "|%s" %troop_flags[each_flag]
            troop_flag = troop_flag-each_flag
            
    if troop_flag==0:
        return flag_code.replace('|','',1)
    else:
        return line[4]
    
    
def get_scene_code(line):   # needs update after decompiling scene files
    troop_scene = int(line[5])
    if troop_scene==0:
        return '0'
    
    troop_entry = troop_scene>>16
    troop_scene = troop_scene&0xfff
    
    #if troop_scene in scene_ids:
    return "%s|entry(%d)" %(scene_ids[troop_scene],troop_entry)
    #else:
    #    print line[0],troop_scene


def get_fac_code(line):
    troop_fac = int(line[7])
    return faction_ids[troop_fac]


def get_skill_code(line):
    skill_code = ''''''
    troop_skill = 0
    for i in xrange(6):
        troop_skill += int(line[i]) << (32*i)
        
    if troop_skill==0:
        return '0'
    
    #troop_skill_combination_keys = troop_skill_combinations.keys()
    #troop_skill_combination_keys.sort()
    #troop_skill_combination_keys.reverse()
    #for each_skill_conbination in troop_skill_combination_keys:
    #    if troop_skill&each_skill_conbination==each_skill_conbination:
    #        skill_code += "|%s" %troop_skill_combinations[each_skill_conbination]
    #        troop_skill -= each_skill_conbination
    #    if troop_skill==0:
    #        return skill_code.replace('|','',1)
    
    troop_skill_keys = troop_skills.keys()
    troop_skill_keys.sort()
    troop_skill_keys.reverse()
    for each_skill in troop_skill_keys:
        if troop_skill&each_skill==each_skill:
            skill_code += "|%s" %troop_skills[each_skill]
            troop_skill -= each_skill
        if troop_skill==0:
            return skill_code.replace('|','',1)
    else:
        return line
    

def get_face_code(line):
    line.reverse()
    
    face_code = ''''''       
    troop_face = 0
    for i in xrange(4):
        troop_face += int(line[i]) << (64*i)
    origin_troop_face = hex(troop_face).replace('L','')
        
    if troop_face==0:
        return '0'
    
    for each_face in troop_faces:
        if troop_face==each_face:
            return troop_faces[each_face]
    else:
        return origin_troop_face


def decompile():
    ofile = open(export_dir+"troops.txt",'r')
    tfile = open(export_dir+"decompiled files/module_troops.py",'w')
    idfile = open(export_dir+"decompiled files/ID_troops.py",'w')
    
    tfile.write('''import random

from header_common import *
from header_items import *
from header_troops import *
from header_skills import *
from ID_factions import *
from ID_items import *
from ID_scenes import *

####################################################################################################################
#  Each troop contains the following fields:
#  1) Troop id (string): used for referencing troops in other files. The prefix trp_ is automatically added before each troop-id .
#  2) Toop name (string).
#  3) Plural troop name (string).
#  4) Troop flags (int). See header_troops.py for a list of available flags
#  5) Scene (int) (only applicable to heroes) For example: scn_reyvadin_castle|entry(1) puts troop in reyvadin castle's first entry point
#  6) Reserved (int). Put constant "reserved" or 0.
#  7) Faction (int)
#  8) Inventory (list): Must be a list of items
#  9) Attributes (int): Example usage:
#           str_6|agi_6|int_4|cha_5|level(5)
# 10) Weapon proficiencies (int): Example usage:
#           wp_one_handed(55)|wp_two_handed(90)|wp_polearm(36)|wp_archery(80)|wp_crossbow(24)|wp_throwing(45)
#     The function wp(x) will create random weapon proficiencies close to value x.
#     To make an expert archer with other weapon proficiencies close to 60 you can use something like:
#           wp_archery(160) | wp(60)
# 11) Skills (int): See header_skills.py to see a list of skills. Example:
#           knows_ironflesh_3|knows_power_strike_2|knows_athletics_2|knows_riding_2
# 12) Face code (int): You can obtain the face code by pressing ctrl+E in face generator screen
# 13) Face code (int)(2) (only applicable to regular troops, can be omitted for heroes):
#     The game will create random faces between Face code 1 and face code 2 for generated troops
# 14) Troop image (string): If this variable is set, the troop will use an image rather than its 3D visual during the conversations
#  town_1   Sargoth
#  town_2   Tihr
#  town_3   Veluca
#  town_4   Suno
#  town_5   Jelkala
#  town_6   Praven
#  town_7   Uxkhal
#  town_8   Reyvadin
#  town_9   Khudan
#  town_10  Tulga
#  town_11  Curaw
#  town_12  Wercheg
#  town_13  Rivacheg
#  town_14  Halmar
####################################################################################################################

# Some constant and function declarations to be used below... 
# wp_one_handed () | wp_two_handed () | wp_polearm () | wp_archery () | wp_crossbow () | wp_throwing ()
def wp(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
#  n |= wp_archery(x + random.randrange(r))
#  n |= wp_crossbow(x + random.randrange(r))
#  n |= wp_throwing(x + random.randrange(r))
  n |= wp_one_handed(x)
  n |= wp_two_handed(x)
  n |= wp_polearm(x)
  n |= wp_archery(x)
  n |= wp_crossbow(x)
  n |= wp_throwing(x)
  return n

def wpe(m,a,c,t):
   n = 0
   n |= wp_one_handed(m)
   n |= wp_two_handed(m)
   n |= wp_polearm(m)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n

def wpex(o,w,p,a,c,t):
   n = 0
   n |= wp_one_handed(o)
   n |= wp_two_handed(w)
   n |= wp_polearm(p)
   n |= wp_archery(a)
   n |= wp_crossbow(c)
   n |= wp_throwing(t)
   return n
   
def wp_melee(x):
  n = 0
  r = 10 + int(x / 10)
#  n |= wp_one_handed(x + random.randrange(r))
#  n |= wp_two_handed(x + random.randrange(r))
#  n |= wp_polearm(x + random.randrange(r))
  n |= wp_one_handed(x + 20)
  n |= wp_two_handed(x)
  n |= wp_polearm(x + 10)
  return n

#Skills
knows_common = knows_riding_1|knows_trade_2|knows_inventory_management_2|knows_prisoner_management_1|knows_leadership_1
knows_common_multiplayer = knows_trade_10|knows_inventory_management_10|knows_prisoner_management_10|knows_leadership_10|knows_spotting_10|knows_pathfinding_10|knows_tracking_10|knows_engineer_10|knows_first_aid_10|knows_surgery_10|knows_wound_treatment_10|knows_tactics_10|knows_trainer_10|knows_looting_10
def_attrib = str_7 | agi_5 | int_4 | cha_4
def_attrib_multiplayer = int_30 | cha_30



knows_lord_1 = knows_riding_3|knows_trade_2|knows_inventory_management_2|knows_tactics_4|knows_prisoner_management_4|knows_leadership_7

knows_warrior_npc = knows_weapon_master_2|knows_ironflesh_1|knows_athletics_1|knows_power_strike_2|knows_riding_2|knows_shield_1|knows_inventory_management_2
knows_merchant_npc = knows_riding_2|knows_trade_3|knows_inventory_management_3 #knows persuasion
knows_tracker_npc = knows_weapon_master_1|knows_athletics_2|knows_spotting_2|knows_pathfinding_2|knows_tracking_2|knows_ironflesh_1|knows_inventory_management_2

lord_attrib = str_20|agi_20|int_20|cha_20|level(38)

knight_attrib_1 = str_15|agi_14|int_8|cha_16|level(22)
knight_attrib_2 = str_16|agi_16|int_10|cha_18|level(26)
knight_attrib_3 = str_18|agi_17|int_12|cha_20|level(30)
knight_attrib_4 = str_19|agi_19|int_13|cha_22|level(35)
knight_attrib_5 = str_20|agi_20|int_15|cha_25|level(41)
knight_skills_1 = knows_riding_3|knows_ironflesh_2|knows_power_strike_3|knows_athletics_1|knows_tactics_2|knows_prisoner_management_1|knows_leadership_3
knight_skills_2 = knows_riding_4|knows_ironflesh_3|knows_power_strike_4|knows_athletics_2|knows_tactics_3|knows_prisoner_management_2|knows_leadership_5
knight_skills_3 = knows_riding_5|knows_ironflesh_4|knows_power_strike_5|knows_athletics_3|knows_tactics_4|knows_prisoner_management_2|knows_leadership_6
knight_skills_4 = knows_riding_6|knows_ironflesh_5|knows_power_strike_6|knows_athletics_4|knows_tactics_5|knows_prisoner_management_3|knows_leadership_7
knight_skills_5 = knows_riding_7|knows_ironflesh_6|knows_power_strike_7|knows_athletics_5|knows_tactics_6|knows_prisoner_management_3|knows_leadership_9

#These face codes are generated by the in-game face generator.
#Enable edit mode and press ctrl+E in face generator screen to obtain face codes.


reserved = 0

no_scene = 0

swadian_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
swadian_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
swadian_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
swadian_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
swadian_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

swadian_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
swadian_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

vaegir_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
vaegir_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
vaegir_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
vaegir_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
vaegir_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

vaegir_face_younger_2 = 0x000000003f00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_young_2   = 0x00000003bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_middle_2  = 0x00000007bf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_old_2     = 0x0000000cbf00230c4deeffffffffffff00000000001efff90000000000000000
vaegir_face_older_2   = 0x0000000ff100230c4deeffffffffffff00000000001efff90000000000000000

khergit_face_younger_1 = 0x0000000009003109207000000000000000000000001c80470000000000000000
khergit_face_young_1   = 0x00000003c9003109207000000000000000000000001c80470000000000000000
khergit_face_middle_1  = 0x00000007c9003109207000000000000000000000001c80470000000000000000
khergit_face_old_1     = 0x0000000b89003109207000000000000000000000001c80470000000000000000
khergit_face_older_1   = 0x0000000fc9003109207000000000000000000000001c80470000000000000000

khergit_face_younger_2 = 0x000000003f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_young_2   = 0x00000003bf0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_middle_2  = 0x000000077f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_old_2     = 0x0000000b3f0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000
khergit_face_older_2   = 0x0000000fff0061cd6d7ffbdf9df6ebee00000000001ffb7f0000000000000000

nord_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
nord_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
nord_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
nord_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
nord_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

nord_face_younger_2 = 0x00000000310023084deeffffffffffff00000000001efff90000000000000000
nord_face_young_2   = 0x00000003b10023084deeffffffffffff00000000001efff90000000000000000
nord_face_middle_2  = 0x00000008310023084deeffffffffffff00000000001efff90000000000000000
nord_face_old_2     = 0x0000000c710023084deeffffffffffff00000000001efff90000000000000000
nord_face_older_2   = 0x0000000ff10023084deeffffffffffff00000000001efff90000000000000000

rhodok_face_younger_1 = 0x0000000009002003140000000000000000000000001c80400000000000000000
rhodok_face_young_1   = 0x0000000449002003140000000000000000000000001c80400000000000000000
rhodok_face_middle_1  = 0x0000000849002003140000000000000000000000001c80400000000000000000
rhodok_face_old_1     = 0x0000000cc9002003140000000000000000000000001c80400000000000000000
rhodok_face_older_1   = 0x0000000fc9002003140000000000000000000000001c80400000000000000000

rhodok_face_younger_2 = 0x00000000000062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_young_2   = 0x00000003c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_middle_2  = 0x00000007c00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_old_2     = 0x0000000bc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000
rhodok_face_older_2   = 0x0000000fc00062c76ddcdf7feefbffff00000000001efdbc0000000000000000

man_face_younger_1 = 0x0000000000000001124000000020000000000000001c00800000000000000000
man_face_young_1   = 0x0000000400000001124000000020000000000000001c00800000000000000000
man_face_middle_1  = 0x0000000800000001124000000020000000000000001c00800000000000000000
man_face_old_1     = 0x0000000d00000001124000000020000000000000001c00800000000000000000
man_face_older_1   = 0x0000000fc0000001124000000020000000000000001c00800000000000000000

man_face_younger_2 = 0x000000003f0052064deeffffffffffff00000000001efff90000000000000000
man_face_young_2   = 0x00000003bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_middle_2  = 0x00000007bf0052064deeffffffffffff00000000001efff90000000000000000
man_face_old_2     = 0x0000000bff0052064deeffffffffffff00000000001efff90000000000000000
man_face_older_2   = 0x0000000fff0052064deeffffffffffff00000000001efff90000000000000000

merchant_face_1    = man_face_young_1
merchant_face_2    = man_face_older_2

woman_face_1    = 0x0000000000000001000000000000000000000000001c00000000000000000000
woman_face_2    = 0x00000003bf0030067ff7fbffefff6dff00000000001f6dbf0000000000000000

swadian_woman_face_1 = 0x0000000180102006124925124928924900000000001c92890000000000000000
swadian_woman_face_2 = 0x00000001bf1000061db6d75db6b6dbad00000000001c92890000000000000000

khergit_woman_face_1 = 0x0000000180103006124925124928924900000000001c92890000000000000000
khergit_woman_face_2 = 0x00000001af1030025b6eb6dd6db6dd6d00000000001eedae0000000000000000

refugee_face1 = woman_face_1
refugee_face2 = woman_face_2
girl_face1    = woman_face_1
girl_face2    = woman_face_2

mercenary_face_1 = 0x0000000000000000000000000000000000000000001c00000000000000000000
mercenary_face_2 = 0x0000000cff00730b6db6db6db7fbffff00000000001efffe0000000000000000

vaegir_face1  = vaegir_face_young_1
vaegir_face2  = vaegir_face_older_2

bandit_face1  = man_face_young_1
bandit_face2  = man_face_older_2

undead_face1  = 0x00000000002000000000000000000000
undead_face2  = 0x000000000020010000001fffffffffff

#NAMES:
#

tf_guarantee_all = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield|tf_guarantee_ranged
tf_guarantee_all_wo_ranged = tf_guarantee_boots|tf_guarantee_armor|tf_guarantee_gloves|tf_guarantee_helmet|tf_guarantee_horse|tf_guarantee_shield

''')
    
    tfile.write("troops = [\n")
    id = 0
    
    isInvtLine = 0
    isAttrLine = 0
    isWeapLine = 0
    isSkilLine = 0
    isFaceLine = 0
    isEndLine  = 0
    
    upgrade_info = []
    troop_ids = {}
    
    for line in ofile:
        if 'trp_' in line:
            line = line.split()
            troop_name = line[0]
            flag_code = get_flag_code(line)     # line[4]
            scene_code = get_scene_code(line)   # line[5]
            fac_code = get_fac_code(line)       # line[7]
            
            tfile.write('''["%s","%s","%s",%s,%s,%s,%s,\n''' %(troop_name[4:],line[1].replace('_',' '),line[2].replace('_',' '),flag_code,scene_code,'reserved',fac_code))
            idfile.write("%s = %d\n" %(line[0],id))
            troop_ids[id] = troop_name
            
            upgrade_troop1 = int(line[8])
            upgrade_troop2 = int(line[9])
            upgrade_info.append((id,upgrade_troop1,upgrade_troop2))
            
            id += 1
    
            isInvtLine = 1
            continue
            
        if isInvtLine:
            line = line.split(' 0 ')
            try:
                troop_item = [int(line[i]) for i in xrange(len(line)-1)]
            except ValueError:
                print troop_name,len(line),line
            item_code = '''  ['''
            for each_item in troop_item:
                if each_item in item_ids:
                    item_code += "%s," %item_ids[each_item]
            item_code += "],\n"
            tfile.write(item_code)
            
            isInvtLine = 0
            isAttrLine = 1
            continue
            
        if isAttrLine:
            line = line.split()
            troop_attr = [int(line[i]) for i in xrange(len(line))]
            attr_prefix = ["str_","agi_","int_","cha_"]
            attr_code = '''  '''
            for a in xrange(4):
                if troop_attr[a]>2:
                    attr_code += "|%s%d" %(attr_prefix[a],troop_attr[a])
            attr_code += "|level(%s)," %troop_attr[4]
            #attr_code = "  str_%d|agi_%d|int_%d|cha_%d|level(%d)," %tuple(troop_attr)
            tfile.write(attr_code.replace('|','',1))
            
            isAttrLine = 0
            isWeapLine = 1
            continue
            
        if isWeapLine:
            line = line.split()
            troop_weap = [int(line[i]) for i in xrange(len(line)-1)]   # exclude firearm efficiency
            weap_code = "wpex(%d,%d,%d,%d,%d,%d)," %tuple(troop_weap)
            tfile.write(weap_code)
            
            isWeapLine = 0
            isSkilLine = 1
            continue
            
        if isSkilLine:
            line = line.split()
            skill_code = get_skill_code(line)
            tfile.write("%s," %skill_code)
            
            isSkilLine = 0
            isFaceLine = 1
            continue
            
        if isFaceLine:
            line = line.split()
            face_code1 = get_face_code(line[:4])
            face_code2 = get_face_code(line[4:])
            tfile.write("%s,%s,],\n" %(face_code1,face_code2))
            
            isFaceLine = 0
            isEndLine = 1
            continue
    
        if isEndLine:
            isInvtLine = 0
            isAttrLine = 0
            isWeapLine = 0
            isSkilLine = 0
            isFaceLine = 0
            isEndLine  = 0
            continue
    
    tfile.write("]\n\n\n\n")
    
    for base_troop,upgrade_troop1,upgrade_troop2 in upgrade_info:
        if upgrade_troop1 and upgrade_troop2:
            tfile.write('''upgrade2(troops,"%s","%s","%s")\n''' %(troop_ids[base_troop][4:],troop_ids[upgrade_troop1][4:],troop_ids[upgrade_troop2][4:]))
        elif upgrade_troop1:
            tfile.write('''upgrade(troops,"%s","%s")\n''' %(troop_ids[base_troop][4:],troop_ids[upgrade_troop1][4:]))
    
    tfile.close()
    ofile.close()
    idfile.close()
    

if __name__=='__main__':
    print "Decompiling troops ..."
    decompile()