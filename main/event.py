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
#             | |                   s
#             |_|                

# from main import Compiler
import main

# FUNCTION
 
tab = '     '

class PyCub_ChoiceArg(object):
    print('test')

    # if " = " in car:
    #     PyCub_AddCalcul(car, event) 
    # else:
    #     effect.add(car, event)

class EventManager(object):
    
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


    #                        _       
    #                       | |      
    #    _____   _____ _ __ | |_ ___ 
    #   / _ \ \ / / _ \ '_ \| __/ __|
    #  |  __/\ V /  __/ | | | |_\__ \
    #   \___| \_/ \___|_| |_|\__|___/   

    def test():
        print('tezst')    

    def callevent(Event):
        
        # OPEN FILE

        dir = 'C:/PythonProject/Pycub/.cache/' + ActualProjectName + '.txt'
        file = open(dir, 'w+', encoding='utf8')
        dir = 'C:/PythonProject/Pycub/.cache/' + ActualProjectName + 'import.txt'
        ifile = open(dir, 'w+', encoding='utf8')

        # FUNCTION WRITE

        def eventhandler():
            file.write('\n' + ' ' + '@EventHandler \n') 

        def endevent():
            file.write(tab * 1 + '}\n')                              

        def analysexpr(event):   
            expr_PycubLign = PycubLign
            for _expr in PyCub_From:
                expr_PycubLign =+ 1
                if _expr.strip() == "stop":
                    break
                else:
                    PyCub_ChoiceArg(_expr.strip(), event)

        def Write(var):
            file.write('key' + PyCub_JavaFile[-1] + var)

        def Import(var):
            if 'key' + PyCub_JavaFile[-1] + var in ifile:
                pass
            else:
                ifile.write('key' + main.PyCub_JavaFile[-1] + var)


        # LIST OF ALL EVENT 
            
        global number_event_call
        number_event_call = 0
        number_event_call += 1
        if Event.startswith('on_player_join:') or Event.startswith('player join:'):
                    
            # WRITE EVENT HANDLER
                    
            eventhandler()
                
            # NAME OF PUBLIC CLASS
                    
            Write(tab + 'public void OnPlayerJoin' + str(number_event_call) + '(PlayerJoinEvent event) {\n')
            
            # ADD IMPORT
            
            Import("import org.bukkit.event.EventHandler;")
            Import("import org.bukkit.event.Listener;")
            Import("import org.bukkit.event.player.PlayerJoinEvent;")
            analysexpr(Event)
            endevent()            

                    
        elif Event.startswith('on_player_leave:') or Event.startswith('player leave:'):
                    
            eventhandler()
                    
            Write(tab + 'public void OnPlayerLeave' + str(number_event_call) + '(PlayerQuitEvent event) {\n')
            Import("import org.bukkit.event.player.PlayerQuitEvent;")
            Import("import org.bukkit.event.EventHandler;")
            Import("import org.bukkit.event.Listener;")
            analysexpr(Event)
                    
            endevent()      
            
        else:
            pycubprint("The event is not exist (lign" + str(PycubLign) + ")")
   
                           