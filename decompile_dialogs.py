#! /usr/bin/env python
#coding=utf-8

# decompile dialog_states.txt and conversations.txt to module_dialogs.py

from module_info import *
from decompile_operations import *


speakers_old = {
    'anyone             ': 0x00000fff,
    'repeat_for_factions': 0x00001000,
    'repeat_for_parties ': 0x00002000,
    'repeat_for_troops  ': 0x00003000,
    'repeat_for_100     ': 0x00004000,
    'repeat_for_1000    ': 0x00005000,

    'plyr               ': 0x00010000,
    'party_tpl          ': 0x00020000,
    'auto_proceed       ': 0x00040000,
    'multi_line         ': 0x00080000,
}
speakers = {}
for k,v in speakers_old.iteritems():
    speakers[v] = k.replace(' ','')


#-----------------------------------------------------------------------------#


def get_speaker(line):
    speaker_code = ''''''
    speaker = int(line[1])
    if speaker==0:
        return '0'
    
    speaker_keys = speakers.keys()
    speaker_keys.sort()
    speaker_keys.reverse()
    for each_speaker in speaker_keys:
        if speaker&each_speaker==each_speaker:
            speaker_code += "|%s" %speakers[each_speaker]
            speaker -= each_speaker
        if speaker==0:
            return speaker_code.replace('|','',1)
    else:
        return line[1]
    
    
def get_text(line):
    pos = 3
    num_ops = int(line[pos])
    
    while num_ops:
        pos += 2   # skip the operator id position
        params = int(line[pos])   # get the number of parameters of this operator
        
        pos += params   # get to the last parameter position
        num_ops -= 1
    
    cdtn_code = ' '.join(line[3:pos+1])
    #if cdtn_code=='0':
    #    cdtn_code = "[]"
    #else:
    #    cdtn_code = "['%s']" %cdtn_code
    cdtn_code = decompile_statement_block(cdtn_code)
    text = line[pos+1].replace('_',' ')
    csqs_code = ' '.join(line[pos+3:len(line)-1])
    #if csqs_code=='0':
    #    csqs_code = "[]"
    #else:
    #    csqs_code = "['%s']" %csqs_code
    csqs_code = decompile_statement_block(csqs_code)
    
    return cdtn_code,text,csqs_code


def get_voice_over(line):
    return line[-1]

def decompile():
    ofile = open(export_dir+"conversation.txt",'r')
    tfile = open(export_dir+"decompiled files/module_dialogs.py",'w')
    
    tfile.write('''
from header_common import *
from header_dialogs import *
from header_operations import *
from header_parties import *
from header_item_modifiers import *
from header_skills import *
from header_triggers import *
from ID_troops import *
from ID_party_templates import *

from module_constants import *


####################################################################################################################
# During a dialog, the dialog lines are scanned from top to bottom.
# If the dialog-line is spoken by the player, all the matching lines are displayed for the player to pick from.
# If the dialog-line is spoken by another, the first (top-most) matching line is selected.
#
#  Each dialog line contains the following fields:
# 1) Dialogue partner: This should match the person player is talking to.
#    Usually this is a troop-id.
#    You can also use a party-template-id by appending '|party_tpl' to this field.
#    Use the constant 'anyone' if you'd like the line to match anybody.
#    Appending '|plyr' to this field means that the actual line is spoken by the player
#    Appending '|other(troop_id)' means that this line is spoken by a third person on the scene.
#       (You must make sure that this third person is present on the scene)
#
# 2) Starting dialog-state:
#    During a dialog there's always an active Dialog-state.
#    A dialog-line's starting dialog state must be the same as the active dialog state, for the line to be a possible candidate.
#    If the dialog is started by meeting a party on the map, initially, the active dialog state is "start"
#    If the dialog is started by speaking to an NPC in a town, initially, the active dialog state is "start"
#    If the dialog is started by helping a party defeat another party, initially, the active dialog state is "party_relieved"
#    If the dialog is started by liberating a prisoner, initially, the active dialog state is "prisoner_liberated"
#    If the dialog is started by defeating a party led by a hero, initially, the active dialog state is "enemy_defeated"
#    If the dialog is started by a trigger, initially, the active dialog state is "event_triggered"
# 3) Conditions block (list): This must be a valid operation block. See header_operations.py for reference.  
# 4) Dialog Text (string):
# 5) Ending dialog-state:
#    If a dialog line is picked, the active dialog-state will become the picked line's ending dialog-state.
# 6) Consequences block (list): This must be a valid operation block. See header_operations.py for reference.
# 7) Voice-over (string): sound filename for the voice over. Leave here empty for no voice over
####################################################################################################################

''')

    tfile.write("dialogs = [\n")
    
    for line in ofile:
        if 'dlga_' in line:
            line = line.split()
            
            ipt_token = line[0].split(':')[0][5:]
            opt_token = line[0].split(':')[1].split('.')[0]
            speaker = get_speaker(line)   # line[1]
            cdtn_code,text,csqs_code = get_text(line)   # line[3:-1]
            voice_over = get_voice_over(line)   # line[-1]
            
            tfile.write('''  (%s,"%s",\n%s,\n    """%s""",\n    "%s",\n%s,\n    "%s"\n  ),\n''' %(speaker,ipt_token,cdtn_code,text,opt_token,csqs_code,voice_over))
            
    tfile.write("]\n")
    tfile.close()
    ofile.close()
    
    
if __name__=='__main__':
    print "Decompiling dialogs ..."
    decompile()