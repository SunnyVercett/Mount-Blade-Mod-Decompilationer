#! /usr/bin/env python
#coding=utf-8

# decompile parties.txt to module_parties.py

from module_info import *
from header_parties import *
from decompiled_ID_factions import *
from decompiled_ID_map_icons import *
from decompiled_ID_menus import *
from decompiled_ID_party_templates import *
from decompiled_ID_troops import *


party_flags_old = {
   'pf_icon_mask                ': 0x000000ff,
   'pf_disabled                 ': 0x00000100,
   'pf_is_ship                  ': 0x00000200,
   'pf_is_static                ': 0x00000400,
   #'pf_label_small              ': 0x00000000,
   'pf_label_medium             ': 0x00001000,
   'pf_label_large              ': 0x00002000,
   'pf_always_visible           ': 0x00004000,
   'pf_default_behavior         ': 0x00010000,
   'pf_auto_remove_in_town      ': 0x00020000,
   'pf_quest_party              ': 0x00040000,
   'pf_no_label                 ': 0x00080000,
   'pf_limit_members            ': 0x00100000,
   'pf_hide_defenders           ': 0x00200000,
   'pf_show_faction             ': 0x00400000,
    #'pf_is_hidden               ': 0x01000000, #used in the engine, do not overwrite this flag
   'pf_dont_attack_civilians    ': 0x02000000,
   'pf_civilian                 ': 0x04000000,
   'pf_town                 ':pf_is_static|pf_always_visible|pf_show_faction|pf_label_large,
   'pf_castle               ':pf_is_static|pf_always_visible|pf_show_faction|pf_label_medium,
   'pf_village              ':pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_small,
   #'pf_carry_goods_bits   ': 48,
   #'pf_carry_gold_bits    ': 56,
   #'pf_carry_gold_multiplier': 20,
   #'pf_carry_goods_mask   ': 0x00ff000000000000,
   #'pf_carry_gold_mask    ': 0xff00000000000000,
}
party_flags = {}
for k,v in party_flags_old.iteritems():
    party_flags[v] = k.replace(' ','')
    
    
ai_ids_old = {
   'ai_bhvr_hold           ': 0,
   'ai_bhvr_travel_to_party': 1,
   'ai_bhvr_patrol_location': 2,
   'ai_bhvr_patrol_party   ': 3,
   'ai_bhvr_track_party    ': 4, #deprecated, use the alias ai_bhvr_attack_party instead.
   'ai_bhvr_attack_party   ': 4,
   'ai_bhvr_avoid_party    ': 5,
   'ai_bhvr_travel_to_point': 6,
   'ai_bhvr_negotiate_party': 7,
   'ai_bhvr_in_town        ': 8,
   'ai_bhvr_travel_to_ship ': 9,
   'ai_bhvr_escort_party   ': 10,
   'ai_bhvr_driven_by_party': 11,
}
ai_ids = {}
for k,v in ai_ids_old.iteritems():
    ai_ids[v] = k.replace(' ','')
    

prsn_ids_old = {
    'courage_4 ': 0x0004,
    'courage_5 ': 0x0005,
    'courage_6 ': 0x0006,
    'courage_7 ': 0x0007,
    'courage_8 ': 0x0008,
    'courage_9 ': 0x0009,
    'courage_10': 0x000A,
    'courage_11': 0x000B,
    'courage_12': 0x000C,
    'courage_13': 0x000D,
    'courage_14': 0x000E,
    'courage_15': 0x000F,

    'aggressiveness_0 ': 0x0000,
    'aggressiveness_1 ': 0x0010,
    'aggressiveness_2 ': 0x0020,
    'aggressiveness_3 ': 0x0030,
    'aggressiveness_4 ': 0x0040,
    'aggressiveness_5 ': 0x0050,
    'aggressiveness_6 ': 0x0060,
    'aggressiveness_7 ': 0x0070,
    'aggressiveness_8 ': 0x0080,
    'aggressiveness_9 ': 0x0090,
    'aggressiveness_10': 0x00A0,
    'aggressiveness_11': 0x00B0,
    'aggressiveness_12': 0x00C0,
    'aggressiveness_13': 0x00D0,
    'aggressiveness_14': 0x00E0,
    'aggressiveness_15': 0x00F0,

    'banditness       ': 0x0100,

    'soldier_personality': aggressiveness_8 | courage_9,
    'merchant_personality': aggressiveness_0 | courage_7,
    'escorted_merchant_personality': aggressiveness_0 | courage_11,
    'bandit_personality  ': aggressiveness_3 | courage_8 | banditness,
}
prsn_ids = {}
for k,v in prsn_ids_old.iteritems():
    prsn_ids[v] = k.replace(' ','')


#-----------------------------------------------------------------------------#
#------------------------ above this are constants ---------------------------#
#-----------------------------------------------------------------------------#


def get_flag_code(line):
    flag_code = ''''''
    party_flag = int(line[5])
    
    party_icon = party_flag&0xff
    if party_icon in map_icon_ids:
        flag_code += "|%s" %map_icon_ids[party_icon]
        party_flag -= party_icon
    if party_flag==0:
        return flag_code.replace('|','',1)
    
    party_flag_keys = party_flags.keys()
    party_flag_keys.sort()
    party_flag_keys.reverse()
    for each_flag in party_flag_keys:
        if party_flag&each_flag==each_flag:
            flag_code += "|%s" %party_flags[each_flag]
            party_flag -= each_flag
        if party_flag==0:
            return flag_code.replace('|','',1)
    else:
        return line[5]


def get_menu_code(line):
    menu_code = ''''''
    party_menu = int(line[6])
    if party_menu==0:
        return '0'
    
    menu_id_keys = menu_ids.keys()
    menu_id_keys.sort()
    menu_id_keys.reverse()
    for each_menu in menu_id_keys:
        if party_menu%each_menu==each_menu:
            menu_code += "|%s" %menu_ids[each_menu]
            party_menu -= each_menu
        if party_menu==0:
            return menu_code.replace('|','',1)
    else:
        return line[6]


def get_template_code(line):
    party_tmpt = int(line[7])
    if party_tmpt in party_template_ids:
        return party_template_ids[party_tmpt]
    else:
        return line[7]


def get_faction_code(line):
    party_fac = int(line[8])
    if party_fac in faction_ids:
        return faction_ids[party_fac]
    else:
        return line[8]


def get_prsn_code(line):
    prsn_code = ''''''
    party_prsn = int(line[9])
    if party_prsn==0:
        return '0'
    
    prsn_id_keys = prsn_ids.keys()
    prsn_id_keys.sort()
    prsn_id_keys.reverse()
    for each_prsn in prsn_id_keys:
        if party_prsn&each_prsn==each_prsn:
            prsn_code += "|%s" %prsn_ids[each_prsn]
            party_prsn -= each_prsn
        if party_prsn==0:
            return prsn_code.replace('|','',1)
    else:
        return line[9]
    

def get_ai_code(line):
    ai_code = ''''''
    party_ai = int(line[11])
    
    ai_id_keys = ai_ids.keys()
    ai_id_keys.sort()
    ai_id_keys.reverse()
    for each_ai in ai_id_keys:
        if party_ai&each_ai==each_ai:
            ai_code += "|%s" %ai_ids[each_ai]
            party_ai -= each_ai
        if party_ai==0:
            ai_code += "|ai_bhvr_hold"
            return ai_code.replace('|','',1)
    else:
        return line[11]
    
    
def get_ai_target_code(line):
    ai_target_code = ''''''
    party_ai_target = int(line[12])
    if party_ai_target==0:
        return '0'
    elif party_ai_target in party_ids:
        return party_ids[party_ai_target]
    else:
        return line[12]
    
    
def get_member_code(line):
    member_code = '''['''
    party_member = line[21:]
    
    for i_member in xrange(int(line[21])):
        member_id = int(line[22+4*i_member])
        if member_id in troop_ids:
            member_name = troop_ids[member_id]
        else:
            member_name = str(member_id)
        member_num = int(line[23+4*i_member])
        member_flag = int(line[25+4*i_member])
        if member_flag==1:
            member_flag = 'pmf_is_prisoner'
        elif member_flag==0:
            member_flag = '0'
        member_code += "(%s,%d,%s)," %(member_name,member_num,member_flag)
    member_code += "]"
    return member_code


def decompile():
    ofile = open(export_dir+"parties.txt",'r')
    idfile = open(export_dir+"decompiled files/ID_parties.py",'w')

    id = 0
    party_ids = {}
    for line in ofile:
        if 'p_' in line:
            line = line.split()
            party_name = line[3]
            party_ids[id] = party_name[2:]
            idfile.write("%s = %d\n" %(party_name,id))
            id += 1
    idfile.close()
    ofile.close()
    
    ofile = open(export_dir+"parties.txt",'r')
    tfile = open(export_dir+"decompiled files/module_parties.py",'w')
    
    tfile.write('''from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_party_templates import *
from ID_map_icons import *

####################################################################################################################
#  Each party record contains the following fields:
#  1) Party id: used for referencing parties in other files.
#     The prefix p_ is automatically added before each party id.
#  2) Party name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Party-template. ID of the party template this party belongs to. Use pt_none as the default value.
#  6) Faction.
#  7) Personality. See header_parties.py for an explanation of personality flags.
#  8) Ai-behavior
#  9) Ai-target party
# 10) Initial coordinates.
# 11) List of stacks. Each stack record is a triple that contains the following fields:
#   11.1) Troop-id. 
#   11.2) Number of troops in this stack. 
#   11.3) Member flags. Use pmf_is_prisoner to note that this member is a prisoner.
# 12) Party direction in degrees [optional]
####################################################################################################################

no_menu = 0
#pf_town = pf_is_static|pf_always_visible|pf_hide_defenders|pf_show_faction
pf_town = pf_is_static|pf_always_visible|pf_show_faction|pf_label_large
pf_castle = pf_is_static|pf_always_visible|pf_show_faction|pf_label_medium
pf_village = pf_is_static|pf_always_visible|pf_hide_defenders|pf_label_small

#sample_party = [(trp_swadian_knight,1,0), (trp_swadian_peasant,10,0), (trp_swadian_crossbowman,1,0), (trp_swadian_man_at_arms, 1, 0), (trp_swadian_footman, 1, 0), (trp_swadian_militia,1,0)]

# NEW TOWNS:
# NORMANDY: Rouen, Caen, Bayeux, Coutances, Evreux, Avranches
# Brittany: Rennes, Nantes,
# Maine: Le Mans
# Anjou: Angers

''')

    tfile.write("parties = [\n")
    
    isBearingLine = 0
    for line in ofile:
        if 'p_' in line:
            line = line.split()
            
            id = int(line[1])
            party_name = line[3]
            flag_code = get_flag_code(line)      # line[5]
            menu_code = get_menu_code(line)      # line[6]
            tmpl_code = get_template_code(line)  # line[7]
            fac_code = get_faction_code(line)    # line[8]
            prsn_code = get_prsn_code(line)      # line[9] and line[10]
            ai_code = get_ai_code(line)          # line[11]
            ai_target_code = get_ai_target_code(line)   #line[12] and line[13]
            init_pos = (float('%.1f'%float(line[14])),float('%.1f'%float(line[15])))   # line[14], line[15], line[16], line[17], line[18], line[19], line[20]
            member_code = get_member_code(line)   # line[21:]
            
            tfile.write('''  ("%s","%s", %s, %s, %s, %s,%s, %s, %s, (%.2f,%.2f), %s,''' %(party_name[2:],line[4].replace('_',' '),flag_code,menu_code,tmpl_code,fac_code,prsn_code,ai_code,ai_target_code,init_pos[0],init_pos[1],member_code))
            
            isBearingLine = 1
            continue
        
        if isBearingLine:
            bearing = int(float(line)*180.0/3.1415926)
            tfile.write(" %d),\n" %bearing)
            
            isBearingLine = 0
            continue
    
    tfile.write("]\n")
    tfile.close()
    ofile.close()
    
    
if __name__=='__main__':
    print "Decompiling parties ..."
    decompile()