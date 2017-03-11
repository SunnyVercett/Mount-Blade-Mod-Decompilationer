#! /usr/bin/env python
#coding=utf-8

# decompile party_templates.txt to module_party_templates.py

from module_info import *
from header_parties import *
from decompiled_ID_troops import *
from decompiled_ID_map_icons import *
from decompiled_ID_factions import *
from decompiled_ID_menus import *


pttmp_flags_old = {
   #'pf_icon_mask                ': 0x000000ff,
   'pf_disabled                 ': 0x00000100,
   'pf_is_ship                  ': 0x00000200,
   'pf_is_static                ': 0x00000400,

   #'pf_label_small              ': 0x00000000,   # 0x00 means nothing
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
    #pf_is_hidden               ': 0x01000000, #used in the engine, do not overwrite this flag
   'pf_dont_attack_civilians    ': 0x02000000,
   'pf_civilian                 ': 0x04000000,

   #'pf_carry_goods_bits   ': 48,
   #'pf_carry_gold_bits    ': 56,
   #'pf_carry_gold_multiplier': 20,
   #'pf_carry_goods_mask   ': 0x00ff000000000000,
   #'pf_carry_gold_mask    ': 0xff00000000000000,
}
pttmp_flags = {}
for k,v in pttmp_flags_old.iteritems():
    pttmp_flags[v] = k.replace(' ','')


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
#------------------------- above this are constants --------------------------#
#-----------------------------------------------------------------------------#


def get_flag_code(line):
    flag_code = ''''''
    pttmp_flag = int(line[2])
    if pttmp_flag==0:
        return '0'
    
    for each_icon in map_icon_ids:
        if pttmp_flag&pf_icon_mask==each_icon:
            flag_code += "|%s" %map_icon_ids[each_icon]
            pttmp_flag -= each_icon
        if pttmp_flag==0:
            return flag_code.replace('|','',1)
    
    pttmp_goods = (pttmp_flag&0x00ff000000000000) >> 48
    pttmp_golds = ((pttmp_flag&0xff00000000000000) >> 56) *20
    if pttmp_goods:
        flag_code += "|carries_goods(%d)" %pttmp_goods
        pttmp_flag -= (pttmp_flag&0x00ff000000000000)
        if pttmp_flag==0:
            return flag_code.replace('|','',1)        
    if pttmp_golds:
        flag_code += "|carries_golds(%d)" %pttmp_golds
        pttmp_flag -= (pttmp_flag&0xff00000000000000)
        if pttmp_flag==0:
            return flag_code.replace('|','',1)        
                
    pttmp_flag_keys = pttmp_flags.keys()
    pttmp_flag_keys.sort()
    pttmp_flag_keys.reverse()
    for each_flag in pttmp_flag_keys:
        if pttmp_flag&each_flag==each_flag:
            flag_code += "|%s" %pttmp_flags[each_flag]
            pttmp_flag -= each_flag
        if pttmp_flag==0:
            return flag_code.replace('|','',1)
    else:
        return line[2]
    
    
def get_menu_code(line):
    menu_code = ''''''
    pttmp_menu = int(line[3])
    if pttmp_menu==0:
        return '0'
    
    menu_id_keys = menu_ids.keys()
    menu_id_keys.sort()
    menu_id_keys.reverse()
    for each_menu in menu_id_keys:
        if pttmp_menu%each_menu==each_menu:
            menu_code += "|%s" %menu_ids[each_menu]
            pttmp_menu -= each_menu
        if pttmp_menu==0:
            return menu_code.replace('|','',1)
    else:
        return line[3]
    
    
def get_personality_code(line):
    prsn_code = ''''''
    pttmp_prsn = int(line[5])
    if pttmp_prsn==0:
        return '0'
    
    prsn_id_keys = prsn_ids.keys()
    prsn_id_keys.sort()
    prsn_id_keys.reverse()
    for each_prsn in prsn_id_keys:
        if pttmp_prsn&each_prsn==each_prsn:
            prsn_code += "|%s" %prsn_ids[each_prsn]
            pttmp_prsn -= each_prsn
        if pttmp_prsn==0:
            return prsn_code.replace('|','',1)
    else:
        return line[5]
    

def decompile():
    ofile = open(export_dir+"party_templates.txt",'r')
    tfile = open(export_dir+"decompiled files/module_party_templates.py",'w')
    idfile = open(export_dir+"decompiled files/ID_party_templates.py",'w')
    
    tfile.write('''from header_common import *
from header_parties import *
from ID_troops import *
from ID_factions import *
from ID_map_icons import *

pmf_is_prisoner = 0x0001

####################################################################################################################
#  Each party template record contains the following fields:
#  1) Party-template id: used for referencing party-templates in other files.
#     The prefix pt_ is automatically added before each party-template id.
#  2) Party-template name.
#  3) Party flags. See header_parties.py for a list of available flags
#  4) Menu. ID of the menu to use when this party is met. The value 0 uses the default party encounter system.
#  5) Faction
#  6) Personality. See header_parties.py for an explanation of personality flags.
#  7) List of stacks. Each stack record is a tuple that contains the following fields:
#    7.1) Troop-id. 
#    7.2) Minimum number of troops in the stack. 
#    7.3) Maximum number of troops in the stack. 
#    7.4) Member flags(optional). Use pmf_is_prisoner to note that this member is a prisoner.
#     Note: There can be at most 6 stacks.
####################################################################################################################

''')

    tfile.write("party_templates = [\n")
    
    id = 0
    for line in ofile:
        if 'pt_' in line:
            line = line.split()
            
            pttmp_name = line[0]
            flag_code = get_flag_code(line)   # line[2]
            menu_code = get_menu_code(line)   # line[3]
            prsn_code = get_personality_code(line)   # line[5]
            
            tfile.write('''  ("%s","%s", %s, %s, %s, %s,\n    [''' %(pttmp_name[3:],line[1].replace('_',' '),flag_code,menu_code,faction_ids[int(line[4])],prsn_code))
            
            pttmp_stack = line[6:]
            pttmp_member_number = (len(pttmp_stack)-6)/3   # empty party has 6 slots, each non-empty slot adds 3 slots
            for i in xrange(pttmp_member_number):
                this_member = (int(line[6+4*i]),int(line[7+4*i]),int(line[8+4*i]),int(line[9+4*i]))
                if this_member[3]==1:
                    prison_flag = 'pmf_is_prisoner'
                else:
                    prison_flag = '0'
                this_member_code = "(%s,%d,%d,%s)," %(troop_ids[this_member[0]],this_member[1],this_member[2],prison_flag)
                tfile.write(this_member_code)
            tfile.write("]\n  ),\n")
                
            idfile.write("%s = %d\n" %(pttmp_name,id))
            id += 1
            
    tfile.write("]\n")
    tfile.close()
    idfile.close()
    ofile.close()
    
    
if __name__=='__main__':
    print "Decompiling party templates ..."
    decompile()