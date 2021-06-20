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

import main

# FUNCTION
 
def eventhandler():
    main.Write('\n' + main.tab + '@EventHandler \n') 
 
def endevent():
    main.Write(main.tab * 1 + '}\n')                              

def analysexpr(event):   
    expr_PycubLign = main.PycubLign
    for _expr in main.From:
        expr_PycubLign =+ 1
        if _expr.strip() == "stop":
            break
        else:
            main.PyCub_ChoiceArg(_expr.strip(), event)
   
   
#                        _       
#                       | |      
#    _____   _____ _ __ | |_ ___ 
#   / _ \ \ / / _ \ '_ \| __/ __|
#  |  __/\ V /  __/ | | | |_\__ \
#   \___| \_/ \___|_| |_|\__|___/   
                            
def add(Event):
        
    # LIST OF ALL EVENT 
        
    global number_event_call
    number_event_call = 0
    number_event_call += 1
    if Event.startswith('on_player_join:') or Event.startswith('player join:'):
                
        # WRITE EVENT HANDLER
                
        eventhandler()
              
        # NAME OF PUBLIC CLASS
                
        main.Write(main.tab + 'public void OnPlayerJoin' + str(number_event_call) + '(PlayerJoinEvent event) {\n')
        
        # ADD IMPORT
        
        main.Import("import org.bukkit.event.EventHandler;")
        main.Import("import org.bukkit.event.Listener;")
        main.Import("import org.bukkit.event.player.PlayerJoinEvent;")
        analysexpr(Event)
        endevent()            

                
    elif Event.startswith('on_player_leave:') or Event.startswith('player leave:'):
                
        eventhandler()
                 
        main.Write(main.tab + 'public void OnPlayerLeave' + str(number_event_call) + '(PlayerQuitEvent event) {\n')
        main.Import("import org.bukkit.event.player.PlayerQuitEvent;")
        main.Import("import org.bukkit.event.EventHandler;")
        main.Import("import org.bukkit.event.Listener;")
        analysexpr(Event)
                
        endevent()      
        
    else:
        main.pycubprint("The event is not exist (lign" + str(main.PycubLign) + ")")