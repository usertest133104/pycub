#                                             /^\/^\
#                                           _|_O_|  O|
#                                   \/     /~     \_/ \
#                                   \____|__________/  \
#                                           \_______      \
#                                                   `\     \                 \
#  _______     _______ _    _ ____                   |     |                  \
# |  __ \ \   / / ____| |  | |  _ \                 /      /                    \
# | |__) \ \_/ / |    | |  | | |_) |               /     /                       \\
# |  ___/ \   /| |    | |  | |  _ <              /      /                         \ \
# | |      | | | |____| |__| | |_) |            /     /                            \  \
# |_|      |_|  \_____|\____/|____/           /     /             _----_            \   \
#                                           /     /           _-~      ~-_         |   |
#  ALPHA EDITION                           (      (        _-~    _--_    ~-_     _/   |
#                                           \      ~-____-~    _-~    ~-_    ~-_-~    /
#                                               ~-_           _-~          ~-_       _-~
#                                               ~--______-~                ~-___-~

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

import os
import json

def PyCub_Compil(dir, File_name, main, author = "PyCubTranspilator"):


    # ADD WRITE AND IMPORT JAVA FILE

    #                 _ _          __ _ _      
    #                (_) |        / _(_) |     
    #  __      ___ __ _| |_ ___  | |_ _| | ___ 
    #  \ \ /\ / / '__| | __/ _ \ |  _| | |/ _ \
    #   \ V  V /| |  | | ||  __/ | | | | |  __/
    #    \_/\_/ |_|  |_|\__\___| |_| |_|_|\___|
                                            
                                        
    def PyCub_Write(var):
        PyCub_C_Write.append(var)
    def PyCub_Import(var):
        if var in PyCub_C_Import:
            pass
        else:
            PyCub_C_Import.append(var)
    
    def PyCub_DirMain(name):
        
        # CONTENT DATA.JSON FILE
            
        with open(dir + ProjectName + '/' + 'data.json', 'w') as file_json:
            data = file_json.load(f)
        
        if name == 'main' or 'maindir':            
            return DataFile[1]
        
        elif name == 'pl' or 'pldir':
            return DataFile.readlines(2)
        
        elif name == 'small' or 'package' or 'smallpackage':
            return DataFile.readlines(3)
    
    print(PyCub_DirMain(main))
    
    # ADD LISTENERS IN MAIN.JAVA
    
    def PyCub_AddListener(var):
        PyCub_Listener_Write.append('getServer().getPluginManager().registerEvents(new ' + var + 'testListener(), this);')   
        PyCub_Listener_Name.append(var)  
    
    # ADD COMMAND IN MAIN.JAVA
    
    def PyCub_AddCommand(var):
        PyCub_Command_Write.append('getCommand("' + var + 'test").setExecutor(new testCommand());')   
        PyCub_Command_Name.append(var)  
    
    # SEPARATE ESPACE    
        
    def PyCub_UnSeparteArg(arg):
        return arg.replace('||', ' ')
    def PyCub_SeparteArg(arg):
        return arg.replace(' ', '||')

    # --------------------------------------

    #             _            _       _   _                 
    #            | |          | |     | | (_)                
    #    ___ __ _| | ___ _   _| | __ _| |_ _  ___  _ __  ___ 
    #   / __/ _` | |/ __| | | | |/ _` | __| |/ _ \| '_ \/ __|
    #  | (_| (_| | | (__| |_| | | (_| | |_| | (_) | | | \__ \
    #   \___\__,_|_|\___|\__,_|_|\__,_|\__|_|\___/|_| |_|___/
                                                        
                                                       
    def PyCub_AddCalcul(car, event):
        if car in ' = ' or ' =+ ' or ' =- ' or ' invers ':
            print('no finish')
        elif car in ' =+ ':
            print('no finish')

    #                                              _       
    #                                             | |      
    #    __ _ _ __ __ _ _   _ _ __ ___   ___ _ __ | |_ ___ 
    #   / _` | '__/ _` | | | | '_ ` _ \ / _ \ '_ \| __/ __|
    #  | (_| | | | (_| | |_| | | | | | |  __/ | | | |_\__ \
    #   \__,_|_|  \__, |\__,_|_| |_| |_|\___|_| |_|\__|___/
    #              __/ |                                   
    #             |___/                                    
    
    def PyCub_ModifArg(car, expr):
        
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
    
    #         __  __          _       
    #        / _|/ _|        | |      
    #    ___| |_| |_ ___  ___| |_ ___ 
    #   / _ \  _|  _/ _ \/ __| __/ __|
    #  |  __/ | | ||  __/ (__| |_\__ \
    #   \___|_| |_| \___|\___|\__|___/
                                
    def PyCub_AddEffect(car, event):
        if car.startswith('setjoinmessage'):
            if "setjoinmessage" in From.read():
                print(f"You can't use the setjoinmessage() expression because it already exists ")
            else:
                expr = car
                expr = expr[14:]
                expr = expr[:-1]
                expr = PyCub_ModifArg(expr, "setjoinmessage")
                PyCub_Write(tab * 2 + "event.setJoinMessage(" + expr + ");\n")  
        
        elif car.startswith('broadcast'):
            expr = car
            expr = expr[10:]
            expr = expr[:-1]
            expr = PyCub_ModifArg(expr, "broadcast")
            PyCub_Write(tab * 2 + "Bukkit.broadcastMessage(" + expr + ");\n")   

    #                   _                         _           _             
    #                  | |                       | |         | |            
    #   ___ _   _ _ __ | |_ __ ___  __   ___  ___| | ___  ___| |_ ___  _ __ 
    #  / __| | | | '_ \| __/ _` \ \/ /  / __|/ _ \ |/ _ \/ __| __/ _ \| '__|
    #  \__ \ |_| | | | | || (_| |>  <   \__ \  __/ |  __/ (__| || (_) | |   
    #  |___/\__, |_| |_|\__\__,_/_/\_\  |___/\___|_|\___|\___|\__\___/|_|   
    #        __/ |                                                          
    #       |___/                                                           
      
    def PyCub_ChoiceArg(car, event):
        if " = " in car:
            PyCub_AddCalcul(car, event) 
        else:
            PyCub_AddEffect(car, event)
            
    #                        _       
    #                       | |      
    #    _____   _____ _ __ | |_ ___ 
    #   / _ \ \ / / _ \ '_ \| __/ __|
    #  |  __/\ V /  __/ | | | |_\__ \
    #   \___| \_/ \___|_| |_|\__|___/
                               
                               
    def PyCub_AddEvent(Event):
        
        # LIST OF ALL EVENT 
        
        global number_event_call
        number_event_call += 1
        if Event.startswith('on_player_join:') or Event.startswith('player join:'):
                
            # écriture de l'handler évent
                
            PyCub_Write('\n' + tab + '@EventHandler \n')
            
                
            # NAME OF PUBLIC CLASS
                
            PyCub_Write(tab + 'public void OnPlayerJoin' + str(number_event_call) + '(PlayerJoinEvent event) {\n')
            PyCub_Import("import org.bukkit.event.player.PlayerJoinEvent;")
            PyCub_Import("import org.bukkit.event.EventHandler;")
            PyCub_Import("import org.bukkit.event.Listener;")
            expr_lign = lign
            for _expr in From:
                expr_lign =+ 1
                if _expr.strip() == "stop":
                    break
                else:
                    PyCub_ChoiceArg(_expr.strip(), "on_player_join")
                
            PyCub_Write(tab * 1 + '}\n')            

                
        elif Event.startswith('on_player_leave:') or Event.startswith('player leave:'):
                
            # écriture de l'handler évent
                
            PyCub_Write('\n' + tab + '@EventHandler \n')
                
            # NAME OF PUBLIC CLASS
                
            PyCub_Write(tab + 'public void OnPlayerLeave' + str(number_event_call) + '(PlayerQuitEvent event) {\n')
            PyCub_Import("import org.bukkit.event.player.PlayerQuitEvent;")
            PyCub_Import("import org.bukkit.event.EventHandler;")
            PyCub_Import("import org.bukkit.event.Listener;")
            expr_lign = lign
            for _expr in From:
                expr_lign =+ 1
                if _expr.strip() == "stop":
                    break
                else:
                    PyCub_ChoiceArg(_expr.strip(), "on_player_leave")
                
            PyCub_Write(tab * 1 + '}\n')       

    print("Loading ...")

    FromFile = 'C:/PythonProject/Pycub/scripts/test.pycub'
    
    ProjectName = 'test/'
    PathTargetFile = 'C:/PythonProject/Pycub/projects/' + ProjectName
    
    TargetFile = PathTargetFile + 'Main/test.java'
    MainFile = PathTargetFile + 'test.java'
    TargetCacheFile = 'C:/PythonProject/Pycub/scripts/.cache/test.pycub'
    
    os.makedirs(os.path.dirname(TargetFile), exist_ok=True)
    os.makedirs(os.path.dirname(MainFile), exist_ok=True)
    From = open(FromFile, 'r', encoding='utf8')
    Target = open(TargetFile, 'w+', encoding='utf8')
    MainFile = open(TargetFile, 'w+', encoding='utf8')

    tab = "    "
    first_event = False
    global lign
    lign = 1
    PyCub_C_Write = []
    PyCub_C_Import = []
    PyCub_Listener_Name = []
    PyCub_Command_Name = []

#                 _ _              _               _              
#                (_) |            | |             | |             
#  __      ___ __ _| |_ ___    ___| |__   ___  ___| | _____ _ __  
#  \ \ /\ / / '__| | __/ _ \  / __| '_ \ / _ \/ __| |/ / _ \ '__| 
#   \ V  V /| |  | | ||  __/ | (__| | | |  __/ (__|   <  __/ |    
#    \_/\_/ |_|  |_|\__\___|  \___|_| |_|\___|\___|_|\_\___|_|    
                                                                
#                        _                  _                             __ _ _                 _       
#                       | |                | |                           / _(_) |               | |      
#    _____   _____ _ __ | |_ ___        ___| |__   __ _ _ __   __ _  ___| |_ _| | ___        ___| |_ ___ 
#   / _ \ \ / / _ \ '_ \| __/ __|      / __| '_ \ / _` | '_ \ / _` |/ _ \  _| | |/ _ \      / _ \ __/ __|
#  |  __/\ V /  __/ | | | |_\__ \  _  | (__| | | | (_| | | | | (_| |  __/ | | | |  __/  _  |  __/ || (__ 
#   \___| \_/ \___|_| |_|\__|___/ ( )  \___|_| |_|\__,_|_| |_|\__, |\___|_| |_|_|\___| ( )  \___|\__\___|
#                                 |/                           __/ |                   |/                
#                                                             |___/                                                                                                      
                                                                
    for car in From:
        
        # Sélectionneur d'évènement
        lign =+ 1
        
        if car.startswith('package'):
            PyCub_Write(car + ';')
        if car.startswith('#'):
            PyCub_Write(car)
#        elif car.startswith('import'):
#            if car.startswith('import bukkit'):
#                PyCub_Write('import org.bukkit;\n')
#            
#            else: 
#                text = car + ';'
#                PyCub_Write(text)
        
        elif car.startswith('event') or car.startswith('on'):
            
            # DETECT START WITH EVENT OR ON
            
            if car.startswith('on'):
                callevent = car[3:]

            elif car.startswith('event'):
                callevent = car[6:]
                
            # ADD FIRST PUBLIC CLASS
            
            if first_event == False:
                PyCub_Write('public class PycubEvent implements Listener {\n')
                first_event = True
                global eventnumber
                eventnumber = 1
            
            # CALL EVENT
            
            eventnumber =+ 1
            PyCub_AddEvent(callevent)               
                        
        else:        
            PyCub_Write('\n')
            
            acar = car
            acar.replace(" ", "")
            
            if lign != 1:
                if car.strip() == '':
                    print("The event is not exist lign" + str(lign))

    if first_event == True:
        PyCub_Write('}\n')

#    Target.write('package fr.' + ProjectName + ''.listeners;')
    PyCub_Import(' ')
    for var in PyCub_C_Import:
        Target.write(var + "\n")
    for var in PyCub_C_Write:
        Target.write(var)


    # ADD LISTENERS, COMMAND IN Main.java

    MainFile.write('package fr.gonpvp;' + '\n')
    for var in PyCub_Listener_Name:
        Target.write('fr.gonpvp.listeners.' + var + ';\n')
    for var in PyCub_Command_Name:
        Target.write('fr.gonpvp.command.' + var + ';\n')    
        
    # CLOSE ALL FILE WITH METHOD close()
    Target.close()
    From.close()

    print("Compiled !")

#                       _                         _           _   
#                      | |                       (_)         | |  
#    ___ _ __ ___  __ _| |_ ___   _ __  _ __ ___  _  ___  ___| |_ 
#   / __| '__/ _ \/ _` | __/ _ \ | '_ \| '__/ _ \| |/ _ \/ __| __|
#  | (__| | |  __/ (_| | ||  __/ | |_) | | | (_) | |  __/ (__| |_ 
#   \___|_|  \___|\__,_|\__\___| | .__/|_|  \___/| |\___|\___|\__|
#                                | |            _/ |              
#                                |_|           |__/               

def PyCub_CreateProject(dir, ProjectName, main, smallpackage = "fr.gonpvp", author = "PyCubTranspilator"):
    
    print('Project ' + ProjectName + ' is being created ...')
    
    #                       _               _             _                        _ 
    #                      | |             | |           (_)                      | |
    #    ___ _ __ ___  __ _| |_ ___   _ __ | |_   _  __ _ _ _ __   _   _ _ __ ___ | |
    #   / __| '__/ _ \/ _` | __/ _ \ | '_ \| | | | |/ _` | | '_ \ | | | | '_ ` _ \| |
    #  | (__| | |  __/ (_| | ||  __/ | |_) | | |_| | (_| | | | | || |_| | | | | | | |
    #   \___|_|  \___|\__,_|\__\___| | .__/|_|\__,_|\__, |_|_| |_(_)__, |_| |_| |_|_|
    #                                | |             __/ |          __/ |            
    #                                |_|            |___/          |___/             
    
    PlYmlFile = dir + ProjectName + '/src/main/resources/plugin.yml'
    os.makedirs(os.path.dirname(PlYmlFile), exist_ok=True)
    pl_yml = open(PlYmlFile, 'w+', encoding='utf8')
    
    
    pl_yml.write('name: ' + ProjectName + '\n')
    pl_yml.write('author: ' + author + '\n')
    
    pl_yml.write('main: ' + main + '\n')
    pl_yml.write('version: ' + '0.1' + '\n')
    pl_yml.write('commands:' + '\n')
    pl_yml.close()
    
    
    # CREATE MAIN DIR
    
    
    maindir = main.replace('.', '/')
    main_dir = dir + ProjectName + '/src/main/java/' + maindir + '/'
    os.makedirs(os.path.dirname(main_dir), exist_ok=True)
    
        
    #                       _             _       _          _                 
    #                      | |           | |     | |        (_)                
    #    ___ _ __ ___  __ _| |_ ___    __| | __ _| |_ __ _   _ ___  ___  _ __  
    #   / __| '__/ _ \/ _` | __/ _ \  / _` |/ _` | __/ _` | | / __|/ _ \| '_ \ 
    #  | (__| | |  __/ (_| | ||  __/ | (_| | (_| | || (_| |_| \__ \ (_) | | | |
    #   \___|_|  \___|\__,_|\__\___|  \__,_|\__,_|\__\__,_(_) |___/\___/|_| |_|
    #                                                      _/ |                
    #                                                     |__/                 
        
    ContentData = {
    'main dir': main_dir,
    'plugins.yml dir': PlYmlFile,
    'small package': smallpackage,
    }
    
    with open(dir + ProjectName + '/' + 'data.json', 'w') as file_json:
        json.dump(ContentData, file_json)
    
    print('Successfully created project!')
    
    

def panel():
    print(" ")
    print("PYCUB - ALPHA EDITION")
    print(" ")
    print("- Type the help command to get the list of commands")
    print(" ")
    
#                                                   _     
#                                                  | |    
#      ___ ___  _ __ ___  _ __ ___   __ _ _ __   __| |___ 
#     / __/ _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` / __|
#    | (_| (_) | | | | | | | | | | | (_| | | | | (_| \__ \
#     \___\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_|___/
                                                      
                                                      
                                                  
    while True: 
        command_input = input("Type the command : ")
        if command_input == 'help':
            print(' - c(reate)p(rojet) <dir> <name> <main> <smallpackage> <author>')
            print('Allows you to create a script project')
            print('Exemple: cp C:/PythonProject/Pycub/projects/ test fr.exemple.author fr.exemple')
            print('')
            print(' - p(roject)r(eload) <dir> <name>')
            print('Allows you to create a script project')
            print('Exemple: pr C:/PythonProject/Pycub/projects/ test')
            print('')
        
        elif command_input.startswith('cp') or command_input.startswith('cr'):
            command_strip = command_input.split(' ')
            PyCub_CreateProject(command_strip[1], command_strip[2], command_strip[3], command_strip[4])
        
        elif command_input.startswith('pr'):
            command_strip = command_input.split(' ')
            PyCub_Compil(command_strip[1], command_strip[2])
        
        elif command_input == 'close':
            print('Good bye :)')
            break

    exit()
    

#   _                  _       _   _                          _       _   
#  | |                | |     | | | |                        (_)     | |  
#  | | __ _ _ __   ___| |__   | |_| |__   ___   ___  ___ _ __ _ _ __ | |_ 
#  | |/ _` | '_ \ / __| '_ \  | __| '_ \ / _ \ / __|/ __| '__| | '_ \| __|
#  | | (_| | | | | (__| | | | | |_| | | |  __/ \__ \ (__| |  | | |_) | |_ 
#  |_|\__,_|_| |_|\___|_| |_|  \__|_| |_|\___| |___/\___|_|  |_| .__/ \__|
#                                                              | |        
#                                                              |_|            
    
if __name__ == '__main__':
    
    global number_event_call
    number_event_call = 0
    
    print(r"""
          
                                                 /^\/^\
                                               _|_O_|  O|
                                       \/     /~     \_/ \
                                       \____|__________/  \
                                               \_______      \
                                                       `\     \                 \
      _______     _______ _    _ ____                   |     |                  \
     |  __ \ \   / / ____| |  | |  _ \                 /      /                    \
     | |__) \ \_/ / |    | |  | | |_) |               /     /                       \\
     |  ___/ \   /| |    | |  | |  _ <              /      /                         \ \
     | |      | | | |____| |__| | |_) |            /     /                            \  \
     |_|      |_|  \_____|\____/|____/           /     /             _----_            \   \
                                               /     /           _-~      ~-_         |   |
      ALPHA EDITION                           (      (        _-~    _--_    ~-_     _/   |
                                               \      ~-____-~    _-~    ~-_    ~-_-~    /
                                                   ~-_           _-~          ~-_       _-~
                                                   ~--______-~                ~-___-~      
            """)
    panel()
