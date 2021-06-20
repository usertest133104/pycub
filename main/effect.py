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

#         __  __          _       
#        / _|/ _|        | |      
#    ___| |_| |_ ___  ___| |_ ___ 
#   / _ \  _|  _/ _ \/ __| __/ __|
#  |  __/ | | ||  __/ (__| |_\__ \
#   \___|_| |_| \___|\___|\__|___/
                                
def add(car, event):
    if car.startswith('setjoinmessage'):
        if "setjoinmessage" in main.From.read():
            main.pycubprint(f"You can't use the setjoinmessage() expression because it already exists ")
        else:
            expr = main.PyCub_ModifArg(car[14:-1], "setjoinmessage")
            main.Write(main.tab * 2 + "event.setJoinMessage(" + expr + ");\n")  
        
    elif car.startswith('broadcast'):
        expr = main.PyCub_ModifArg(car[10:-1], "broadcast")
        main.Write(main.tab * 2 + "Bukkit.broadcastMessage(" + expr + ");\n")   
    else:
        main.pycubprint("The effect is not exist (lign" + str(main.PycubLign) + ")")