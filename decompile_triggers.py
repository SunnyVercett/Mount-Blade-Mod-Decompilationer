#! /usr/bin/env python
#coding=utf-8

# decompile triggers.txt to module_triggers.py

from module_info import *
from decompile_operations import *


#-----------------------------------------------------------------------------#

def get_repeat_code(line):
    repeat = float(line[2])
    if repeat==100000000.0:
        return 'ti_once'
    else:
        return line[2]


def get_cdtn_csqs_code(line):
    pos = 3
    begin_pos = pos
    num_ops = int(line[pos])
    
    while num_ops:
        pos += 2
        params = int(line[pos])
        pos += params
        num_ops -= 1
        
    end_pos = pos+1
    cdtn_code = decompile_statement_block(' '.join(line[begin_pos:end_pos]))
    #if cdtn_code=='0':
    #    cdtn_code = "[]"
    #else:
    #    cdtn_code = "['%s']" %cdtn_code
    csqs_code = decompile_statement_block(' '.join(line[end_pos:]))
    #if csqs_code=='0':
    #    csqs_code = "[]"
    #else:
    #    csqs_code = "['%s']" %csqs_code
    return cdtn_code,csqs_code


def decompile():
    ofile = open(export_dir+"triggers.txt",'r')
    tfile = open(export_dir+"decompiled files/module_triggers.py",'w')
    
    tfile.write('''from header_common import *
from header_operations import *
from header_parties import *
from header_items import *
from header_skills import *
from header_triggers import *
from header_troops import *

from module_constants import *

####################################################################################################################
#  Each trigger contains the following fields:
# 1) Check interval: How frequently this trigger will be checked
# 2) Delay interval: Time to wait before applying the consequences of the trigger
#    After its conditions have been evaluated as true.
# 3) Re-arm interval. How much time must pass after applying the consequences of the trigger for the trigger to become active again.
#    You can put the constant ti_once here to make sure that the trigger never becomes active again after it fires once.
# 4) Conditions block (list). This must be a valid operation block. See header_operations.py for reference.
#    Every time the trigger is checked, the conditions block will be executed.
#    If the conditions block returns true, the consequences block will be executed.
#    If the conditions block is empty, it is assumed that it always evaluates to true.
# 5) Consequences block (list). This must be a valid operation block. See header_operations.py for reference. 
####################################################################################################################

# Some constants for use below
merchant_inventory_space = 30
num_merchandise_goods = 36

''')

    tfile.write("triggers = [\n")
    
    for line in ofile:
        if '.' in line:
            line = line.split()
            
            repeat_code = get_repeat_code(line)   # line[2]
            
            tfile.write('''    (%.1f, %.1f, %s,''' %(float(line[0]),float(line[1]),repeat_code))
            
            cdtn_code,csqs_code = get_cdtn_csqs_code(line)
            
            tfile.write("\n%s,\n%s,\n    ),\n" %(cdtn_code,csqs_code))
            
    tfile.write("]\n")
    tfile.close()
    ofile.close()
    
    
if __name__=='__main__':
    print "Decompiling triggers ..."
    decompile()