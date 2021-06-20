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
from effect import EffectManager


tab = '     '

def PyCub_ChoiceArg(car, event):
    test = car
    print('Choice Arg' + test + event)
    # print('Read File' + str(getvar.readfile())
    if " = " in car:
        PyCub_AddCalcul(car, event) 
    else:
        EffectManager.call(car, event)

class EventManager:
    
    print('test 1')
    def __init__(self):
        pass

    def call(event):
        
        # OPEN FILE

        # FUNCTION WRITE

        def eventhandler():
            Compiler.write('\n' + getvar.tab() + '@eventHandler \n') 

        def endevent():
            Compiler.write('\n' + getvar.tab() * 1 + '}\n')                              

        def analysexpr(event):   
            expr_PycubLign = getvar.lign()
            print(getvar.namefile())
            for _expr in getvar.namefile():
                expr_PycubLign =+ 1
                if _expr.strip() == "":
                    break
                else:
                    PyCub_ChoiceArg(_expr.strip(), event)

        # LIST OF ALL event 
            
        Interpretrer.Add1CallEvent()
        print(event)
        if event.startswith('on_player_join:') or event.startswith('player join:'):
                    
            # WRITE event HANDLER
                    
            eventhandler()
                
            # NAME OF PUBLIC CLASS
                    
            Compiler.write(getvar.tab() + 'public void OnPlayerJoin' + str(getvar.NumberCallEvent()) + '(PlayerJoinevent event) {\n')
            
            # ADD IMPORT
            
            Compiler.Import("import org.bukkit.event.eventHandler;")
            Compiler.Import("import org.bukkit.event.Listener;")
            Compiler.Import("import org.bukkit.event.player.PlayerJoinevent;")
            analysexpr(event)
            endevent()            

                    
        elif event.startswith('on_player_leave:') or event.startswith('player leave:'):
                    
            eventhandler()
                    
            Compiler.write(getvar.tab() + 'public void OnPlayerLeave' + str(getvar.NumberCallEvent()) + '(PlayerQuitevent event) {\n')
            Compiler.Import("import org.bukkit.event.player.PlayerQuitevent;")
            Compiler.Import("import org.bukkit.event.eventHandler;")
            Compiler.Import("import org.bukkit.event.Listener;")
            analysexpr(event)
                    
            endevent()      
            
        else:
            print("The event is not exist (lign" + str(getvar.lign) + ")")
