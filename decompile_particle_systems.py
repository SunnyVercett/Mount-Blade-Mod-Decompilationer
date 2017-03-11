#! /usr/bin/env python
#coding=utf-8

# decompile particle_systems.txt to module_particle_systems.py

from module_info import *


psys_flags_old = {
   'psf_always_emit        ': 0x0000000002,
   'psf_global_emit_dir    ': 0x0000000010,
   'psf_emit_at_water_level': 0x0000000020,
   'psf_billboard_2d       ': 0x0000000100, # up_vec = dir, front rotated towards camera
   'psf_billboard_3d       ': 0x0000000200, # front_vec point to camera.
   'psf_billboard_drop     ': 0x0000000300,
   'psf_turn_to_velocity   ': 0x0000000400,
   'psf_randomize_rotation ': 0x0000001000,
   'psf_randomize_size     ': 0x0000002000,
   'psf_2d_turbulance      ': 0x0000010000,
   'psf_next_effect_is_lod ': 0x0000020000,
}
psys_flags = {}
for k,v in psys_flags_old.iteritems():
    psys_flags[v] = k.replace(' ','')


#-----------------------------------------------------------------------------#
#--------------------------- above this are constants ------------------------#
#-----------------------------------------------------------------------------#

def get_flag_code(line):
    flag_code = ''''''
    psys_flag = int(line[1])
    if psys_flag==0:
        return '0'
    
    psys_flag_keys = psys_flags.keys()
    psys_flag_keys.sort()
    psys_flag_keys.reverse()
    for each_flag in psys_flag_keys:
        if psys_flag&each_flag==each_flag:
            flag_code += "|%s" %psys_flags[each_flag]
            psys_flag -= each_flag
        if psys_flag==0:
            return flag_code.replace('|','',1)
    else:
        return line[1]


def decompile():
    ofile = open(export_dir+"particle_systems.txt",'r')
    tfile = open(export_dir+"decompiled files/module_particle_systems.py",'w')
    idfile = open(export_dir+"decompiled files/ID_particle_systems.py",'w')
    
    tfile.write('''from header_particle_systems import *
#psf_always_emit         = 0x0000000002
#psf_global_emit_dir     = 0x0000000010
#psf_emit_at_water_level = 0x0000000020
#psf_billboard_2d        = 0x0000000100 # up_vec = dir, front rotated towards camera
#psf_billboard_3d        = 0x0000000200 # front_vec point to camera.
#psf_turn_to_velocity    = 0x0000000400
#psf_randomize_rotation  = 0x0000001000
#psf_randomize_size      = 0x0000002000
#psf_2d_turbulance       = 0x0000010000

####################################################################################################################
#   Each particle system contains the following fields:
#  
#  1) Particle system id (string): used for referencing particle systems in other files.
#     The prefix psys_ is automatically added before each particle system id.
#  2) Particle system flags (int). See header_particle_systems.py for a list of available flags
#  3) mesh-name.
####
#  4) Num particles per second:    Number of particles emitted per second.
#  5) Particle Life:    Each particle lives this long (in seconds).
#  6) Damping:          How much particle's speed is lost due to friction.
#  7) Gravity strength: Effect of gravity. (Negative values make the particles float upwards.)
#  8) Turbulance size:  Size of random turbulance (in meters)
#  9) Turbulance strength: How much a particle is affected by turbulance.
####
# 10,11) Alpha keys :    Each attribute is controlled by two keys and 
# 12,13) Red keys   :    each key has two fields: (time, magnitude)
# 14,15) Green keys :    For example scale key (0.3,0.6) means 
# 16,17) Blue keys  :    scale of each particle will be 0.6 at the
# 18,19) Scale keys :    time 0.3 (where time=0 means creation and time=1 means end of the particle)
#
# The magnitudes are interpolated in between the two keys and remain constant beyond the keys.
# Except the alpha always starts from 0 at time 0.
####
# 20) Emit Box Size :   The dimension of the box particles are emitted from.
# 21) Emit velocity :   Particles are initially shot with this velocity.
# 22) Emit dir randomness
# 23) Particle rotation speed: Particles start to rotate with this (angular) speed (degrees per second).
# 24) Particle rotation damping: How quickly particles stop their rotation
####################################################################################################################

''')

    tfile.write("particle_systems = [\n")
    
    isAlphaLine = 0
    isRedLine = 0
    isGreenLine = 0
    isBlueLine =  0
    isScaleLine = 0
    isEmitLine = 0
    isRotationLine = 0
    id = 0
    for line in ofile:
        if 'psys_' in line:
            line = line.split()
            
            flag_code = get_flag_code(line)
            
            tfile.write('''  ("%s", %s, "%s",\n    %d,%.2f,%.2f,%.2f,%.2f,%.2f,''' %(line[0][5:],flag_code,line[2],int(line[3]),float(line[4]),float(line[5]),float(line[6]),float(line[7]),float(line[8])))
            idfile.write("%s = %d\n" %(line[0],id))
            id += 1
            
            isAlphaLine = 1
            continue
        
        if isAlphaLine:
            line = line.split()
            
            tfile.write('''\n    (%.2f,%.2f), (%.2f,%.2f),''' %(float(line[0]),float(line[1]),float(line[2]),float(line[3])))
            
            isAlphaLine = 0
            isRedLine = 1
            continue
        
        if isRedLine:
            line = line.split()
            
            tfile.write('''\n    (%.2f,%.2f), (%.2f,%.2f),''' %(float(line[0]),float(line[1]),float(line[2]),float(line[3])))
            
            isRedLine = 0
            isGreenLine = 1
            continue
        
        if isGreenLine:
            line = line.split()
            
            tfile.write('''\n    (%.2f,%.2f), (%.2f,%.2f),''' %(float(line[0]),float(line[1]),float(line[2]),float(line[3])))
            
            isGreenLine = 0
            isBlueLine = 1
            continue
        
        if isBlueLine:
            line = line.split()
            
            tfile.write('''\n    (%.2f,%.2f), (%.2f,%.2f),''' %(float(line[0]),float(line[1]),float(line[2]),float(line[3])))
            
            isBlueLine = 0
            isScaleLine = 1
            continue
        
        if isScaleLine:
            line = line.split()
            
            tfile.write('''\n    (%.2f,%.2f), (%.2f,%.2f),''' %(float(line[0]),float(line[1]),float(line[2]),float(line[3])))
            
            isScaleLine = 0
            isEmitLine = 1
            continue
        
        if isEmitLine:
            line = line.split()
            
            tfile.write('''\n    (%.2f, %.2f, %.2f),\n    (%.2f, %.2f, %.2f),\n    %.2f,''' %(float(line[0]),float(line[1]),float(line[2]),float(line[3]),float(line[4]),float(line[5]),float(line[6])))
            
            isEmitLine = 0
            isRotationLine = 1
            continue
        
        if isRotationLine:
            line = line.split()
            
            tfile.write('''\n    %d,\n    %.2f\n  ),\n''' %(int(float(line[0])),float(line[1])))
            
            isRotationLine = 0
            continue
        
    tfile.write("]\n")
    tfile.close()
    idfile.close()
    ofile.close()
    
    
if __name__=='__main__':
    print "Decompiling particle systems ..."
    decompile()