#  //
# PROJECT CREATED BY GONPVP
# ALL RIGHTS TO POSETION ARE FORBIDDEN
# CONTRIBUTOR: NONE :'/
# /

#  _                            _   
# (_)                          | |  
#  _ _ __ ___  _ __   ___  _ __| |_ 
# | | '_ ` _ \| '_ \ / _ \| '__| __|
# | | | | | | | |_) | (_) | |  | |_ 
# |_|_| |_| |_| .__/ \___/|_|   \__|
#             | |                   
#             |_|                

import sys
sys.path.append("..")
from api import *

#         __  __          _       
#        / _|/ _|        | |      
#    ___| |_| |_ ___  ___| |_ ___ 
#   / _ \  _|  _/ _ \/ __| __/ __|
#  |  __/ | | ||  __/ (__| |_\__ \
#   \___|_| |_| \___|\___|\__|___/

# SEPARATE ESPACE 
        
def PyCub_UnSeparteArg(arg):
    return arg.replace('||', ' ')
def PyCub_SeparteArg(arg):
    return arg.replace(' ', '||')

# REPLACE ARGUMENT IN TEXT

def PyCub_ModifArg(car, expr):

    return car    
    if '"' and '+' in car:
        arg = PyCub_SeparteArg(car)
            
        if 'player' in arg:
            if 'player||name' in arg:
                arg = arg.replace('player||name', 'event.getPlayer().getName()')
            if 'player' or '||player||' or '||player' or 'player||' in arg:
                arg = arg.replace('player', 'event.getPlayer()')    
            return PyCub_UnSeparteArg(arg)
        
    elif '"' and '+' not in car:
            
        if 'player' in car:
            if 'player name' in car:
                arg = car.replace('player name', 'event.getPlayer().getName()')
            if 'player' in arg:
                arg = car.replace('player', 'event.getPlayer()')    
            return PyCub_UnSeparteArg(arg)
        
    else:
        return car       
                                
class EffectManager:
    def __init__(self):
        pass

    def call(car, event):
        if car.startswith('setjoinmessage'):
            if "setjoinmessage" in getvar.readfile():
                print(f"You can't use the setjoinmessage() expression because it already exists ")
            else:
                expr = PyCub_ModifArg(car[14:-1], "setjoinmessage")
                Compiler.write(getvar.tab() * 2 + "event.setJoinMessage(" + expr + ");\n")  

        elif car.startswith('broadcast'):
            expr = PyCub_ModifArg(car[10:-1], "broadcast")
            print(expr)
            print(getvar.tab() * 2 + 'blabla')
            Compiler.write(getvar.tab() * 2 + "Bukkit.broadcastMessage(" + expr + ");\n")   
        else:
            print("The effect is not exist (lign" + str(getvar.lign()) + ")")