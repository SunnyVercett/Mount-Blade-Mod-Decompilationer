#! /usr/bin/env python
#coding=utf-8

# decompile menus.txt to module_game_menus.py

from module_info import *
from header_game_menus import *
from decompile_operations import *


menu_flags_old = {
   'mnf_join_battle           ': 0x00000001, #Consider this menu when the player joins a battle
   'mnf_auto_enter            ': 0x00000010, #Automatically enter the town with the first menu option. 
   'mnf_enable_hot_keys       ': 0x00000100, #Enables P,I,C keys
   'mnf_disable_all_keys      ': 0x00000200, #Disables all keys
   'mnf_scale_picture         ': 0x00001000, #Scale menu picture to offest screen aspect ratio
}
menu_flags = {}
for k,v in menu_flags_old.iteritems():
    menu_flags[v] = k.replace(' ','')
    

#-----------------------------------------------------------------------------#
#-------------------------- above this are constants -------------------------#
#-----------------------------------------------------------------------------#


def get_flag_code(line):
    flag_code = ''''''
    menu_flag = int(line[1])
    if menu_flag==0:
        return '0'
    
    menu_color = menu_flag >> 32
    if menu_color:
        flag_code += "|menu_text_color(%d)" %menu_color
        menu_flag -= (menu_color << 32)
        if menu_flag==0:
            return flag_code.replace('|','',1)
        
    for each_flag in menu_flags:
        if menu_flag&each_flag==each_flag:
            flag_code += "|%s" %menu_flags[each_flag]
            menu_flag -= each_flag
        if menu_flag==0:
            return flag_code.replace('|','',1)
    else:
        return line[1]


def decompile():
    ofile = open(export_dir+"menus.txt",'r')
    tfile = open(export_dir+"decompiled files/module_game_menus.py",'w')
    idfile = open(export_dir+"decompiled files/ID_menus.py",'w')
    
    tfile.write('''from header_game_menus import *
from header_parties import *
from header_items import *
from header_mission_templates import *
from header_music import *
from header_terrain_types import *

from module_constants import *

####################################################################################################################
#  (menu-id, menu-flags, menu_text, mesh-name, [<operations>], [<options>]),
#
#   Each game menu is a tuple that contains the following fields:
#  
#  1) Game-menu id (string): used for referencing game-menus in other files.
#     The prefix menu_ is automatically added before each game-menu-id
#
#  2) Game-menu flags (int). See header_game_menus.py for a list of available flags.
#     You can also specify menu text color here, with the menu_text_color macro
#  3) Game-menu text (string).
#  4) mesh-name (string). Not currently used. Must be the string "none"
#  5) Operations block (list). A list of operations. See header_operations.py for reference.
#     The operations block is executed when the game menu is activated.
#  6) List of Menu options (List).
#     Each menu-option record is a tuple containing the following fields:
#   6.1) Menu-option-id (string) used for referencing game-menus in other files.
#        The prefix mno_ is automatically added before each menu-option.
#   6.2) Conditions block (list). This must be a valid operation block. See header_operations.py for reference. 
#        The conditions are executed for each menu option to decide whether the option will be shown to the player or not.
#   6.3) Menu-option text (string).
#   6.4) Consequences block (list). This must be a valid operation block. See header_operations.py for reference. 
#        The consequences are executed for the menu option that has been selected by the player.
#
#
# Note: The first Menu is the initial character creation menu.
####################################################################################################################

''')

    tfile.write("game_menus = [\n")

    id = 0
    isItemLine = 0
    for line in ofile:
        if ('menu_' in line) and ('mno_' not in line):
            line = line.split()
            
            menu_name = line[0]
            flag_code = get_flag_code(line)   # line[1]
            
            tfile.write('''  ("%s", %s, \n    "%s",\n    "%s",\n''' %(menu_name[5:],flag_code,line[2].replace('_',' '),line[3]))
            
            operations_block = ' '.join(line[4:len(line)-1])
            operations_block = decompile_statement_block(operations_block)

            tfile.write('''%s,\n    [''' %operations_block)
            idfile.write("%s = %d\n" %(menu_name,id))
            id += 1
            
            num_menu_items = int(line[-1])
            isItemLine = 1
            continue
            
        if isItemLine:
            line = line.split(' mno_')
            for eachMenuItem in line:
                if len(eachMenuItem)<2:
                    continue
                menuItem = eachMenuItem.split()
                #menuItem[0] = "mno_%s" %menuItem[0]
                
                pos = 0
                mno_name = menuItem[pos]
                
                pos += 1
                num_ops = int(menuItem[pos])
                while num_ops:
                    pos += 2
                    num_params = int(menuItem[pos])
                    pos += num_params
                    num_ops -= 1
                ops_block = ' '.join(menuItem[1:pos+1])
                ops_block = decompile_statement_block(ops_block)
                
                pos += 1
                mno_text = menuItem[pos].replace('_',' ')
                
                pos += 1
                num_csqs = int(menuItem[pos])
                begin_pos = pos
                while num_csqs:
                    pos += 2
                    num_params = int(menuItem[pos])
                    pos += num_params
                    num_csqs -= 1
                csqs_block = ' '.join(menuItem[begin_pos:pos+1])
                csqs_block = decompile_statement_block(csqs_block)
                
                mno_door = menuItem[-1]
                
                tfile.write('''\n      ("%s",\n%s,\n        "%s",\n%s,\n        "%s",\n      ),\n''' %(mno_name,ops_block,mno_text,csqs_block,mno_door))
                
            tfile.write( "    ]\n  ),\n\n")

            isItemLine = 0
            continue
    
    tfile.write("]\n")
    tfile.close()
    ofile.close()
    idfile.close()
  
    
if __name__=='__main__':
    print "Decompiling menus ..."
    decompile()