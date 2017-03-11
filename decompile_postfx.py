#! /usr/bin/env python
#coding=utf-8

# decompile postfx.txt to module_postfx.py

from module_info import *

#-----------------------------------------------------------------------------#


def decompile():
    ofile = open(export_dir+"postfx.txt",'r')
    tfile = open(export_dir+"decompiled files/module_postfx.py",'w')
    idfile = open(export_dir+"decompiled files/ID_postfx_params.py",'w')
  
    tfile.write('''from header_postfx import *

####################################################################################################################
#  Each postfx_param contains the following fields:
#  1) id (string): 
#  2) flags (int). 
#  3) tonemap operator type (0,1,2,3)
#  4) shader parameters1 [ HDRRange, HDRExposureScaler, LuminanceAverageScaler, LuminanceMaxScaler ]
#  5) shader parameters2 [ BrightpassTreshold, BrightpassPostPower, BlurStrenght, BlurAmount ]
#  6) shader parameters3 [ AmbientColorCoef, SunColorCoef, SpecularCoef, -reserved ]
# 
	#define postfxParams1	(PFX1)	float4(postfx_editor_vector[1].x, postfx_editor_vector[1].y, postfx_editor_vector[1].z, postfx_editor_vector[1].w) 
	#define postfxParams2	(PFX2)	float4(postfx_editor_vector[2].x, postfx_editor_vector[2].y, postfx_editor_vector[2].z, postfx_editor_vector[2].w)
	#define postfxParams3	(PFX3)	float4(postfx_editor_vector[3].x, postfx_editor_vector[3].y, postfx_editor_vector[3].z, postfx_editor_vector[3].w)

####################################################################################################################

''')
    
    tfile.write("postfx_params = [\n")

    id = 0
    for line in ofile:
        if 'pfx_' in line:
            line = line.split()
            
            tfile.write('''  ("%s", %s, %s, [%.4f,%.4f,%.4f,%.4f], [%.4f,%.4f,%.4f,%.4f], [%.4f,%.4f,%.4f,%.4f]),\n''' %(line[0][4:],line[1],line[2],float(line[3]),float(line[4]),float(line[5]),float(line[6]),float(line[7]),float(line[8]),float(line[9]),float(line[10]),float(line[11]),float(line[12]),float(line[13]),float(line[14])))
            idfile.write("%s = %d\n" %(line[0],id))
            id += 1
            
    tfile.write("]\n")
    tfile.close()
    idfile.close()
    ofile.close()
    
    
if __name__=='__main__':
    print "Decompiling postfx ..."
    decompile()