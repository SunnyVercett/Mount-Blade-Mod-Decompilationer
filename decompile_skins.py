#! /usr/bin/env python
#coding=utf-8

# decompile skins.txt to module_skins.py

from module_info import *


en_chars = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')


skin_flags_old = {
   'skf_use_morph_key_10': 0x00000001,
   'skf_use_morph_key_20': 0x00000002,
   'skf_use_morph_key_30': 0x00000003,
   'skf_use_morph_key_40': 0x00000004,
   'skf_use_morph_key_50': 0x00000005,
   'skf_use_morph_key_60': 0x00000006,
   'skf_use_morph_key_70': 0x00000007,
}
skin_flags = {}
for k,v in skin_flags_old.iteritems():
    skin_flags[v] = k.replace(' ','')
    
    
voice_flags_old = {
   'voice_die       ': 0,
   'voice_hit       ': 1,
   'voice_grunt     ': 2,
   'voice_grunt_long': 3,
   'voice_yell      ': 4,
   'voice_warcry    ': 5,
   'voice_victory   ': 6,
   'voice_stun      ': 7,
}
voice_flags = {}
for k,v in voice_flags_old.iteritems():
    voice_flags[v] = k.replace(' ','')


comp_flags_old = {
    'chin_size': 0,
    'chin_shape': 1,
    'chin_forward': 2,
    'jaw_width': 3,
    'jaw_position': 4,
    'mouth_nose_distance': 5,
    'mouth_width': 6,
    'cheeks': 7,
    'nose_height': 8,
    'nose_width': 9,
    'nose_size': 10,
    'nose_shape': 11,
    'nose_bridge': 12,
    'cheek_bones': 13,
    'eye_width': 14,
    'eye_to_eye_dist': 15,
    'eye_shape': 16,
    'eye_depth': 17,
    'eyelids': 18,
    'eyebrow_position': 19,
    'eyebrow_height': 20,
    'eyebrow_depth': 21,
    'eyebrow_shape': 22,
    'temple_width': 23,
    'face_depth': 24,
    'face_ratio': 25,
    'face_width': 26,
}
comp_flags = {}
for k,v in comp_flags_old.iteritems():
    comp_flags[v] = k.replace(' ','')


#-----------------------------------------------------------------------------#
#--------------------------- above this are constants ------------------------#
#-----------------------------------------------------------------------------#


def get_flag_code(line):
    flag_code = ''''''
    skin_flag = int(line[1])
    if skin_flag==0:
        return '0'
    
    skin_flag_keys = skin_flags.keys()
    skin_flag_keys.sort()
    skin_flag_keys.reverse()
    for each_flag in skin_flag_keys:
        if skin_flag&each_flag==each_flag:
            flag_code += "|%s" %skin_flags[each_flag]
            skin_flag -= each_flag
        if skin_flag==0:
            return flag_code.replace('|','',1)
    else:
        return line[1]


def get_face_keys_code(line):
    face_keys_code = '''[\n'''
    face_keys = line[1:]
    
    for i in xrange(int(line[1])):
        face_keys_code += '''            (%d,%d,%.2f,%.2f, '%s'),\n''' %(int(line[3+6*i]),int(line[4+6*i]),float(line[5+6*i]),float(line[6+6*i]),line[7+6*i].replace('_',' '))
        
    face_keys_code += "          ]"
    return face_keys_code


def get_comp_code(line):
    comp = int(line[1])
    if comp==1:
        return 'comp_greater_than'
    elif comp==-1:
        return 'comp_less_than'
    else:
        return 0


def decompile():
    ofile = open(export_dir+"./skins.txt",'r')
    tfile = open(export_dir+"decompiled files/module_skins.py",'w')
    
    tfile.write('''from header_skins import *
from ID_particle_systems import *
####################################################################################################################
#  Each skin record contains the following fields:
#  1) Skin id: used for referencing skins.
#  2) Skin flags. Not used yet. Should be 0.
#  3) Body mesh.
#  4) Calf mesh (left one).
#  5) Hand mesh (left one).
#  6) Head mesh.
#  7) Face keys (list)
#  8) List of hair meshes.
#  9) List of beard meshes.
# 10) List of hair textures.
# 11) List of beard textures.
# 12) List of face textures.
# 13) List of voices.
# 14) Skeleton name
# 15) Scale (doesn't fully work yet)
# 16) Blood particles 1 (do not add this if you wish to use the default particles)
# 17) Blood particles 2 (do not add this if you wish to use the default particles)
# 17) Face key constraints (do not add this if you do not wish to use it)
####################################################################################################################

man_face_keys = [
(20,0, 0.7,-0.6, "Chin Size"),
(260,0, -0.6,1.4, "Chin Shape"),
(10,0,-0.5,0.9, "Chin Forward"),
(240,0,0.9,-0.8, "Jaw Width"),
(210,0,-0.5,1.0, "Jaw Position"),
(250,0,0.8,-1.0, "Mouth-Nose Distance"),
(200,0,-0.3,1.0, "Mouth Width"),
(50,0,-1.5,1.0, "Cheeks"),

(60,0,-0.4,1.35, "Nose Height"),
(70,0,-0.6,0.7, "Nose Width"),
(80,0,1.0,-0.1, "Nose Size"),
(270,0,-0.5,1.0, "Nose Shape"),
(90,0,-0.2,1.4, "Nose Bridge"),

(100,0,-0.3,1.5, "Cheek Bones"),
(150,0,-0.2,3.0, "Eye Width"),
(110,0,1.5,-0.9, "Eye to Eye Dist"),
(120,0,1.9,-1.0, "Eye Shape"),
(130,0,-0.5, 1.1, "Eye Depth"),
(140,0,1.0,-1.2, "Eyelids"),

(160,0,1.3,-0.2, "Eyebrow Position"),
(170,0,-0.1,1.9, "Eyebrow Height"),
(220,0,-0.1,0.9, "Eyebrow Depth"),
(180,0,-1.1,1.6, "Eyebrow Shape"),
(230,0,1.2,-0.7, "Temple Width"),

(30,0,-0.6,0.9, "Face Depth"),
(40,0,0.9,-0.6, "Face Ratio"),
(190,0,0.0,0.95, "Face Width"),

(280,0,0.0,1.0, "Post-Edit"),
]
# Face width-Jaw width Temple width
woman_face_keys = [
(230,0,0.8,-1.0, "Chin Size"), 
(220,0,-1.0,1.0, "Chin Shape"), 
(10,0,-1.2,1.0, "Chin Forward"),
(20,0, -0.6, 1.2, "Jaw Width"), 
(40,0,-0.7,1.0, "Jaw Position"),
(270,0,0.9,-0.9, "Mouth-Nose Distance"),
(30,0,-0.5,1.0, "Mouth Width"),
(50,0, -0.5,1.0, "Cheeks"),

(60,0,-0.5,1.0, "Nose Height"),
(70,0,-0.5,1.1, "Nose Width"),
(80,0,1.5,-0.3, "Nose Size"),
(240,0,-1.0,0.8, "Nose Shape"),
(90,0, 0.0,1.1, "Nose Bridge"),

(100,0,-0.5,1.5, "Cheek Bones"),
(150,0,-0.4,1.0, "Eye Width"),
(110,0,1.0,0.0, "Eye to Eye Dist"),
(120,0,-0.2,1.0, "Eye Shape"),
(130,0,-0.1,1.6, "Eye Depth"),
(140,0,-0.2,1.0, "Eyelids"),


(160,0,-0.2,1.2, "Eyebrow Position"),
(170,0,-0.2,0.7, "Eyebrow Height"),
(250,0,-0.4,0.9, "Eyebrow Depth"),
(180,0,-1.5,1.2, "Eyebrow Shape"),
(260,0,1.0,-0.7, "Temple Width"),

(200,0,-0.5,1.0, "Face Depth"),
(210,0,-0.5,0.9, "Face Ratio"),
(190,0,-0.4,0.8, "Face Width"),

(280,0,0.0,1.0, "Post-Edit"),
]
undead_face_keys = []


chin_size = 0
chin_shape = 1
chin_forward = 2
jaw_width = 3
jaw_position = 4
mouth_nose_distance = 5
mouth_width = 6
cheeks = 7
nose_height = 8
nose_width = 9
nose_size = 10
nose_shape = 11
nose_bridge = 12
cheek_bones = 13
eye_width = 14
eye_to_eye_dist = 15
eye_shape = 16
eye_depth = 17
eyelids = 18
eyebrow_position = 19
eyebrow_height = 20
eyebrow_depth = 21
eyebrow_shape = 22
temple_width = 23
face_depth = 24
face_ratio = 25
face_width = 26

comp_less_than = -1
comp_greater_than = 1

''')

    tfile.write("skins = [\n")
    
    isBodyLine = 0
    isHeadLine = 0
    isHairCntLine = 0
    isHairLine = 0
    isBeardCntLine = 0
    isBeardLine = 0
    isHairTexLine = 0
    isBeardTexLine = 0
    isFaceTexLine = 0
    isSoundLine = 0
    isSkltLine = 0
    isPrtcLine = 0
    isConstrainsCntLine = 0
    isConstrainsLine = 0
    
    for line in ofile:
        if len(line)<2:
            continue   # ignore blank lines
        if 'version' in line:
            continue
        
        if line[0] in en_chars:
            line = line.split()
            
            skin_name = line[0]
            flag_code = get_flag_code(line)   # line[1]
            
            tfile.write('''  (\n    "%s", %s,''' %(line[0],flag_code))
            
            isBodyLine = 1
            continue
        
        if isBodyLine:
            line = line.split()
            
            tfile.write('''\n    "%s", "%s", "%s",''' %(line[0],line[1],line[2]))
            
            isBodyLine = 0
            isHeadLine = 1
            continue
        
        if isHeadLine:
            line = line.split()
            
            face_keys_code = get_face_keys_code(line)   # line[1]
            
            tfile.write('''\n    "%s", %s,''' %(line[0],face_keys_code))
            
            isHeadLine = 0
            isHairCntLine = 1
            continue
        
        if isHairCntLine:
            isHairCntLine = 0
            if int(line):
                isHairLine = 1
            else:
                isBeardCntLine = 1
            continue   # this line doesn't add anything to module_skins.py
        
        if isHairLine:
            line = line.split()
            tfile.write('''\n    %s,''' %str(line).replace("'",'"'))
            
            isHairLine = 0
            isBeardCntLine = 1
            continue
        
        if isBeardCntLine:
            tfile.write("\n    [")
            
            isBeardLine = int(line)
            if isBeardLine==0:
                tfile.write("],")
                isHairTexLine = 1
            isBeardCntLine = 0
            continue
        
        if isBeardLine:
            line = line.split()
            tfile.write('''"%s",''' %line[0].replace(' ',''))
            
            isBeardLine -= 1
            if isBeardLine==0:
                tfile.write("],")
                isHairTexLine = 1
            continue
        
        if isHairTexLine:
            line = line.split()
            hair_tex = line[1:]
            if int(line[0]):
                tfile.write('''\n    %s,''' %str(hair_tex).replace("'",'"'))
            else:
                tfile.write('''\n    [],''')
            
            isHairTexLine = 0
            isBeardTexLine = 1
            continue
        
        if isBeardTexLine:
            line = line.split()
            beard_tex = line[1:]
            if int(line[0]):
                tfile.write('''\n    %s,''' %str(beard_tex).replace("'",'"'))
            else:
                tfile.write('''\n    [],''')
            
            isBeardTexLine = 0
            isFaceTexLine = 1
            continue
            
        if isFaceTexLine:
            line = line.split()
            
            tfile.write('''\n    [''')
            
            pos = 0
            num_textures = int(line[pos])
            
            while num_textures:
                tfile.write("\n      (")
                
                pos += 1
                tfile.write('''"%s",''' %line[pos])
                
                pos += 1
                tfile.write("%s," %hex(int(line[pos])).replace('L',''))
                
                pos += 1
                num_hairs = int(line[pos])
                hairs = [line[j] for j in xrange(pos+2,pos+2+num_hairs)]
                tfile.write("%s," %str(hairs).replace("'",'"'))
                
                pos += 1
                num_hair_colors = int(line[pos])
                hair_colors = [hex(int(line[k])).replace('L','') for k in xrange(pos+1+num_hairs,pos+1+num_hairs+num_hair_colors)]
                tfile.write("%s)," %str(hair_colors).replace("'",''))
                
                pos = pos+num_hairs+num_hair_colors
                num_textures -= 1
            else:
                tfile.write("\n    ],")
            
            isFaceTexLine = 0
            isSoundLine = 1
            continue
        
        if isSoundLine:
            line = line.split()
            
            tfile.write('''\n    [''')
            
            for i in xrange(int(line[0])):
                voice_flag = int(line[1+2*i])
                voice_flag_code = voice_flags[voice_flag]
                voice_name = line[2+2*i]
                tfile.write('''(%s,"%s"),''' %(voice_flag_code,voice_name))
                
            tfile.write("],")
            
            isSoundLine = 0
            isSkltLine = 1
            continue
        
        if isSkltLine:
            line = line.split()
            
            tfile.write('''\n    "%s", %.2f,''' %(line[0],float(line[1])))
            
            isSkltLine = 0
            isPrtcLine = 1
            continue
        
        if isPrtcLine:
            line = line.split()
            
            tfile.write('''\n    %d, %d,''' %(int(line[0]),int(line[1])))   #TODO: Change to particle IDs
            
            isPrtcLine = 0
            isConstrainsCntLine = 1
            continue
        
        if isConstrainsCntLine:
            isConstrainsLine = int(line)
            
            tfile.write("\n    [")
            if isConstrainsLine==0:
                tfile.write("],")
                tfile.write("\n  ),\n\n")            
            isConstrainsCntLine = 0
            continue
        
        if isConstrainsLine:
            line = line.split()
            
            comp_code = get_comp_code(line)   # line[1]
            
            tfile.write('''\n        [%.1f,%s,''' %(float(line[0]),comp_code))
            
            for i in xrange(int(line[2])):
                tfile.write('''(%.1f,%s), ''' %(float(line[3+2*i]),comp_flags[int(line[4+2*i])]))
            
            tfile.write("],")
            
            isConstrainsLine -= 1
            if isConstrainsLine==0:
                tfile.write("\n    ],")
                tfile.write("\n  ),\n\n")
            continue
        
    tfile.write("\n]\n")
    tfile.close()
    ofile.close()
    
    
if __name__=='__main__':
    print "Decompiling skins ..."
    decompile()