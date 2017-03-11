#! /usr/bin/env python
#coding=utf-8

# decompile all variable (troops, items, mission_templates, etc) ids into dictionaries.
# ids of global_variables and quick_strings are also included here

from module_info import *


#-----------------------------------------------------------------------------#

def get_global_variables():
    ofile = open(export_dir+"variables.txt",'r')
    idfile2 = open("./decompiled_ID_global_variables.py",'w')
    idfile2.write("global_variable_ids = {\n")
    
    id = 0
    for line in ofile:
        if line:
            idfile2.write('''    %d: "%s",\n''' %(id,line.split()[0]))
            id += 1
    
    idfile2.write("}\n")
    idfile2.close()
    ofile.close()
    

def get_quick_strings():
    ofile = open(export_dir+"quick_strings.txt",'r')
    idfile2 = open("./decompiled_ID_quick_strings.py",'w')
    idfile2.write("quick_string_ids = {\n")
    
    id = 0
    for line in ofile:
        if 'qstr_' in line:
            str = line.split()[1].replace('_',' ')
            str2 = ''
            for c in xrange(len(str)):    # parse the string character by character
                try:
                    character = str[c].decode('utf-8')    # firstly decode this character
                except UnicodeDecodeError:
                    character = str[c].decode('ISO-8859-1')
                try:
                    str2 += character.encode('ascii')    # secondly encode this character in ascii
                except UnicodeEncodeError:
                    continue    # pass this character    # if this character cannot be encoded with ascii then pass this character
            idfile2.write("    %d: '''%s''',\n" %(id,str2))
            id += 1
    
    idfile2.write("}\n")
    idfile2.close()
    ofile.close()


def get_item_ids():
    ofile = open(export_dir+"item_kinds1.txt",'r')
    idfile2 = open("./decompiled_ID_items.py", 'w')
    idfile2.write("item_ids = {\n")
    
    id = 0
    for line in ofile:
        if 'itm_' in line:
            line = line.split()
            idfile2.write('''    %d: "%s",\n''' %(id,line[0]))
            id += 1
            
    idfile2.write("}\n")
    idfile2.close()
    ofile.close()
    
    
def get_troop_ids():
    ofile = open(export_dir+"troops.txt",'r')
    idfile2 = open("./decompiled_ID_troops.py", 'w')
    idfile2.write("troop_ids = {\n")
    
    id = 0
    for line in ofile:
        if 'trp_' in line:
            line = line.split()
            idfile2.write('''    %d: "%s",\n''' %(id,line[0]))
            id += 1
            
    idfile2.write("}\n")
    idfile2.close()
    ofile.close()
    
    
def get_animation_ids():
    ofile = open(export_dir+"actions.txt",'r')
    idfile2 = open("./decompiled_ID_animations.py", 'w')
    idfile2.write("animation_ids = {\n")
    
    id = 0
    for line in ofile:
        c = 0
        spaces = 0
        while line[c]==' ':
            spaces += 1
            c += 1
            
        if c==1:
            line = line.split()
            idfile2.write('''    %d: "%s",\n''' %(id,'anim_%s' %line[0]))
            id += 1
            
    idfile2.write("}\n")
    idfile2.close()
    ofile.close()
    
    
def get_faction_ids():
    ofile = open(export_dir+"factions.txt",'r')
    idfile2 = open("./decompiled_ID_factions.py",'w')
    idfile2.write("faction_ids = {\n")
    
    id = 0
    for line in ofile:
        if 'fac_' in line:
            line = line.split()
            if line[0]=='0':
                line = line[1:]
                
            idfile2.write("    %d:'%s',\n" %(id,line[0]))
            id += 1
    
    idfile2.write("}\n")
    idfile2.close()
    ofile.close()
    
    
def get_info_page_ids():
    ofile = open(export_dir+"info_pages.txt",'r')
    idfile2 = open("./decompiled_ID_info_pages.py",'w')
    idfile2.write("info_page_ids = {\n")
    
    id = 0
    for line in ofile:
        if 'ip_' in line:
            line = line.split()
            idfile2.write('''    %d: "%s",\n''' %(id,line[0]))
            id += 1
            
    idfile2.write("}\n")
    idfile2.close()
    ofile.close()
    
    
def get_map_icon_ids():
    ofile = open(export_dir+"map_icons.txt",'r')
    idfile2 = open("./decompiled_ID_map_icons.py",'w')
    idfile2.write("map_icon_ids = {\n")
    
    id = 0
    for line in ofile:
        if 'map_icons_file' in line:
            continue
        
        if u'\u0061'<=line[0]<=u'\u007a':   # check if the first char of the line is a lowercase English char
            line = line.split()
            idfile2.write("    %d: 'icon_%s',\n" %(id,line[0]))
            id += 1
            
    idfile2.write("}\n")
    idfile2.close()
    ofile.close()
    
    
def get_menu_ids():
    ofile = open(export_dir+"menus.txt",'r')
    idfile2 = open("./decompiled_ID_menus.py",'w')
    idfile2.write("menu_ids = {\n")
    
    id = 0
    for line in ofile:
        if 'menu_' in line:
            line = line.split()
            idfile2.write('''    %d: "%s",\n''' %(id,'mnu_%s' %line[0][5:]))
            id += 1
            
    idfile2.write("}\n")
    idfile2.close()
    ofile.close()
    
    
def get_mesh_ids():
    ofile = open(export_dir+"meshes.txt",'r')
    idfile2 = open("./decompiled_ID_meshes.py",'w')
    idfile2.write("mesh_ids = {\n")
    
    id = 0
    for line in ofile:
        if 'mesh_' in line:
            line = line.split()
            idfile2.write('''    %d: "%s",\n''' %(id,line[0]))    
            id += 1
            
    idfile2.write("}\n")
    idfile2.close()
    ofile.close()
    
    
def get_mission_template_ids():
    ofile = open(export_dir+"mission_templates.txt",'r')
    idfile2 = open("./decompiled_ID_mission_templates.py",'w')
    idfile2.write("mission_template_ids = {\n")
    
    id = 0
    for line in ofile:
        if len(line)<2:
            continue
        
        if 'mst_' in line:
            line = line.split()
            idfile2.write('''    %d: "%s",\n''' %(id,'mt_%s' %line[0][4:]))
            id += 1

    idfile2.write("}\n")
    idfile2.close()
    ofile.close()
    
    
def get_music_ids():
    ofile = open(export_dir+"music.txt",'r')
    idfile2 = open("./decompiled_ID_music.py",'w')
    idfile2.write("track_ids = {\n")
    
    id = 0
    for line in ofile:
        if 0<len(line)<5:
            continue
        
        line = line.split()
        idfile2.write('''    %d: "%s",\n''' %(id,'track_%s' %line[0].split('.')[0]))
        id += 1
        
    idfile2.write("}\n")
    idfile2.close()    
    ofile.close()
    
    
def get_particle_system_ids():
    ofile = open(export_dir+"particle_systems.txt",'r')
    idfile2 = open("./decompiled_ID_particle_systems.py",'w')
    idfile2.write("particle_system_ids = {\n")
    
    id = 0
    for line in ofile:
        if 'psys_' in line:
            line = line.split()
            idfile2.write('''    %d: "%s",\n''' %(id,line[0]))
            id += 1
            
    idfile2.write("}\n")
    idfile2.close()
    ofile.close()
    
    
def get_party_ids():
    ofile = open(export_dir+"parties.txt",'r')
    idfile2 = open("./decompiled_ID_parties.py",'w')
    idfile2.write("party_ids = {\n")
    
    id = 0
    for line in ofile:
        if 'p_' in line:
            line = line.split()
            idfile2.write('''    %d: "%s",\n''' %(id,line[3]))
            id += 1
    
    idfile2.write("}\n")
    idfile2.close()
    ofile.close()
    
    
def get_party_template_ids():
    ofile = open(export_dir+"party_templates.txt",'r')
    idfile2 = open("./decompiled_ID_party_templates.py",'w')
    idfile2.write("party_template_ids = {\n")
    
    id = 0
    for line in ofile:
        if 'pt_' in line:
            line = line.split()
            idfile2.write("    %d:'%s',\n" %(id,line[0]))
            id += 1
            
    idfile2.write("}\n")
    idfile2.close()
    ofile.close()
    
    
def get_postfx_ids():
    ofile = open(export_dir+"postfx.txt",'r')
    idfile2 = open("./decompiled_ID_postfx_params.py",'w')
    idfile2.write("postfx_param_ids = {\n")
    
    id = 0
    for line in ofile:
        if 'pfx_' in line:
            line = line.split()
            idfile2.write('''    %d: "%s",\n''' %(id,line[0]))
            id += 1
            
    idfile2.write("}\n")
    idfile2.close()
    ofile.close()
    
    
def get_presentation_ids():
    ofile = open(export_dir+"presentations.txt",'r')
    idfile2 = open("./decompiled_ID_presentations.py",'w')
    idfile2.write("presentation_ids = {\n")
    
    id = 0
    for line in ofile:
        if 'prsnt_' in line:
            line = line.split()
            idfile2.write('''    %d: "%s",\n''' %(id,line[0]))
            id += 1
            
    idfile2.write("}\n")
    idfile2.close()
    ofile.close()
    
    
def get_quest_ids():
    ofile = open(export_dir+"quests.txt",'r')
    idfile2 = open("./decompiled_ID_quests.py",'w')
    idfile2.write("quest_ids = {\n")
    
    id = 0
    for line in ofile:
        if 'qst_' in line:
            line = line.split()
            idfile2.write('''    %d: "%s",\n''' %(id,line[0]))
            id += 1
            
    idfile2.write("}\n")
    idfile2.close()
    ofile.close()
    
    
def get_scene_prop_ids():
    ofile = open(export_dir+"scene_props.txt",'r')
    idfile2 = open("./decompiled_ID_scene_props.py",'w')
    idfile2.write("scene_prop_ids = {\n")
    
    id = 0
    for line in ofile:
        if 'spr_' in line:
            line = line.split()
            idfile2.write('''    %d: "%s",\n''' %(id,line[0]))
            id += 1
            
    idfile2.write("}\n")
    idfile2.close()
    ofile.close()
    
    
def get_scene_ids():
    ofile = open(export_dir+"scenes.txt",'r')
    idfile2 = open("./decompiled_ID_scenes.py",'w')
    idfile2.write("scene_ids = {\n")
    
    id = 0
    for line in ofile:
        if 'scn_' in line:
            line = line.split()
            idfile2.write("%d:'%s',\n" %(id,line[0]))
            id += 1
            
    idfile2.write("}\n")
    idfile2.close()
    ofile.close()
    
    
def get_script_ids():
    ofile = open(export_dir+"scripts.txt",'r')
    idfile2 = open("./decompiled_ID_scripts.py",'w')
    idfile2.write("script_ids = {\n")
    
    id = 0
    for line in ofile:
        if '_' in line:
            line = line.split()
            idfile2.write('''    %d: "%s",\n''' %(id, 'script_%s' %line[0]))
            id += 1
            
    idfile2.write("}\n")
    idfile2.close()
    ofile.close()
    
    
def get_skill_ids():
    ofile = open(export_dir+"skills.txt",'r')
    idfile2 = open("./decompiled_ID_skills.py",'w')
    idfile2.write("skill_ids = {\n")
    
    id = 0
    for line in ofile:
        if 'skl_' in line:
            line = line.split()
            idfile2.write("    %d:'%s',\n" %(id,line[0]))
            id += 1
            
    idfile2.write("}\n")
    idfile2.close()
    ofile.close()
    
    
def get_sound_ids():
    ofile = open(export_dir+"sounds.txt",'r')
    idfile2 = open("./decompiled_ID_sounds.py",'w')
    idfile2.write("sound_ids = {\n")
    
    id = 0
    for line in ofile:
        if 'snd_' in line:
            line = line.split()
            idfile2.write('''    %d: "%s",\n''' %(id,line[0]))
            id += 1
            
    idfile2.write("}\n")
    idfile2.close()
    ofile.close()
    
    
def get_string_ids():
    ofile = open(export_dir+"strings.txt",'r')
    idfile2 = open("./decompiled_ID_strings.py",'w')
    idfile2.write("string_ids = {\n")

    id = 0
    for line in ofile:
        if 'str_' in line:
            line = line.split()
            idfile2.write('''    %d: "%s",\n''' %(id,line[0]))
            id += 1
            
    idfile2.write("}\n")
    idfile2.close()
    ofile.close()
    
    
def get_tableau_material_ids():
    ofile = open(export_dir+"tableau_materials.txt",'r')
    idfile2 = open("./decompiled_ID_tableau_materials.py",'w')
    idfile2.write("tableau_material_ids = {\n")

    id = 0
    for line in ofile:
        if 'tab_' in line:
            line = line.split()
            idfile2.write('''    %d: "%s",\n''' %(id,'tableau_%s' %line[0][4:]))
            id += 1
            
    idfile2.write("}\n")
    idfile2.close()
    ofile.close()
    
    
if __name__=='__main__':
    get_global_variables()
    get_quick_strings()
    get_animation_ids()
    get_faction_ids()
    get_info_page_ids()
    get_item_ids()
    get_map_icon_ids()
    get_menu_ids()
    get_mesh_ids()
    get_mission_template_ids()
    get_music_ids()
    get_particle_system_ids()
    get_party_ids()
    get_party_template_ids()
    get_postfx_ids()
    get_presentation_ids()
    get_quest_ids()
    get_scene_ids()
    get_scene_prop_ids()
    get_script_ids()
    get_skill_ids()
    get_sound_ids()
    get_string_ids()
    get_tableau_material_ids()
    get_troop_ids()