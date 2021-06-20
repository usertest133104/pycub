<<<<<<< Updated upstream
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
import sys
sys.path.append("py.")
from api import *
from event import EventManager

def PyCub_Compil(dir , ProjectName):

    #                 _ _          __ _ _      
    #                (_) |        / _(_) |     
    #  __      ___ __ _| |_ ___  | |_ _| | ___ 
    #  \ \ /\ / / '__| | __/ _ \ |  _| | |/ _ \
    #   \ V  V /| |  | | ||  __/ | | | | |  __/
    #    \_/\_/ |_|  |_|\__\___| |_| |_|_|\___|
                                            
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
     
    #                   _                         _           _             
    #                  | |                       | |         | |            
    #   ___ _   _ _ __ | |_ __ ___  __   ___  ___| | ___  ___| |_ ___  _ __ 
    #  / __| | | | '_ \| __/ _` \ \/ /  / __|/ _ \ |/ _ \/ __| __/ _ \| '__|
    #  \__ \ |_| | | | | || (_| |>  <   \__ \  __/ |  __/ (__| || (_) | |   
    #  |___/\__, |_| |_|\__\__,_/_/\_\  |___/\___|_|\___|\___|\__\___/|_|   
    #        __/ |                                                          
    #       |___/                                                           

    print("Loading ...")

    FromFile = 'C:/PythonProject/Pycub/scripts/' + ProjectName + '.pycub'
    
    PathTargetFile = 'C:/PythonProject/Pycub/projects/' + ProjectName + '/'
    
    TargetCacheFile = 'C:/PythonProject/Pycub/scripts/.cache/test.pycub'
    
    From = open(FromFile, 'r', encoding='utf8')
    tab = "    "
    first_event = False
    Projet.createvar(From, ProjectName)
    
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
        
        # ADD 1 Lign (FOR WARN)
        
        Interpretrer.Add1Lign()
        
        if car.startswith('#'):
            Compiler.write(car)
        
        # elif car.startswith('delete file:'):
        #     AddJavaFile(car[12:])
        #     print('test changefile' + car[12:])
        
        elif car.startswith('metodfile('):
            Compiler.AddJavaFile('Main')
            
            if car[10:-1].lower == 'command' or 'commands':
                Compiler.AddListener('Main')
                print('COMMAND ADD')
            elif car[10:-1].lower == 'listeners' or 'event':
                Compiler.PyCub_AddCommand('Main')
                print('LISTENERS ADD')
            else:
                print('Method change file not exist method file (command or event)')
       
        elif car.startswith('changefile('):
            changefilearg = car[11:-2].split(',')
            clTrue = 1
            for var in changefilearg:
                if clTrue == 0:
                    cl = var
                clTrue = 0
            Compiler.AddJavaFile(changefilearg[1])
            if cl == 'command' or 'commands':
                Compiler.AddListener(cl)
                print('COMMAND ADD')
            elif cl == 'listeners' or 'event':
                Compiler.PyCub_AddCommand(cl)
                print('LISTENERS ADD')
            else:
                print('Method change file not specify method file (command or event)')

#        elif car.startswith('import'):
#            if car.startswith('import bukkit'):
#                Write('import org.bukkit;\n')
#            
#            else: 
#                text = car + ';'
#                Write(text)
        
        elif car.startswith('event') or car.startswith('on'):
            
            # DETECT START WITH EVENT OR ON
            
            if car.startswith('on'):
                callevent = car[3:]

            elif car.startswith('event'):
                callevent = car[6:]
                
            # ADD FIRST PUBLIC CLASS
            
            if first_event == False:
                first_event = True
                global eventnumber
                eventnumber = 1
            
            # CALL EVENT

            eventnumber =+ 1
            print('NEW EVENT DETECTED :' + callevent)
            EventManager.call(callevent)             
                        
        else:        
            Compiler.write('\n')
            
            acar = car.replace(" ", "")
            
            if getvar.lign() != 1:
                if car.strip() == '':
                    print("The types is not exist PycubLign" + str(PycubLign))
    
    #                  _           _             _                        _ 
    #             | |         | |           (_)                      | |
    #    __ _  ___| |_   _ __ | |_   _  __ _ _ _ __   _   _ _ __ ___ | |
    #   / _` |/ _ \ __| | '_ \| | | | |/ _` | | '_ \ | | | | '_ ` _ \| |
    #  | (_| |  __/ |_  | |_) | | |_| | (_| | | | | || |_| | | | | | | |
    #   \__, |\___|\__| | .__/|_|\__,_|\__, |_|_| |_(_)__, |_| |_| |_|_|
    #    __/ |          | |             __/ |          __/ |            
    #   |___/           |_|            |___/          |___/             
    
    with open(dir + ProjectName + '/src/main/resources/' + 'plugin.yml', 'r') as PluginYml:
        
        numberlign = 1
        
        textlign = PluginYml.readline().rstrip()
        while textlign:
            if numberlign == 2:
                author = textlign.replace('author: ', '')
                # print('author : ' + author)
            elif numberlign == 3:
                main = textlign.replace('main: ', '').strip('.')
                # print('main : ' + main)
                maindir = main.replace('.', '/')
                mainpackage = main.split('.')
                
            numberlign += 1
            
            textlign = PluginYml.readline().rstrip()

    #                 _ _           _                  
    #                (_) |         (_)                 
    #  __      ___ __ _| |_ ___     _  __ ___   ____ _ 
    #  \ \ /\ / / '__| | __/ _ \   | |/ _` \ \ / / _` |
    #   \ V  V /| |  | | ||  __/  _| | (_| |\ V / (_| |
    #    \_/\_/ |_|  |_|\__\___| (_) |\__,_| \_/ \__,_|
    #                             _/ |                 
    #                            |__/                      
        

    for NameFile in getvar.JavaFile():
        print('Writing file ' + NameFile + '...')
        
        Target = open(dir + ProjectName + '/src/main/java/' + maindir + '/' + NameFile, 'w+', encoding='utf8')
        
        NoJavaNameFile = NameFile.replace('.java','')
        
        # WRITING PACKAGE
        
        Target.write('package fr.gonpvp.' + NoJavaNameFile.lower() + ';\n\n')
        
        # WRITING IMPORT
        
        for var in getvar.WriteImport():
            if var.startswith('key' + NameFile): 
                Target.write(var.replace('key', '').replace(NameFile, '') + '\n')
        
        Target.write('\npublic class ' + NoJavaNameFile + ' implements Listener {')
        
        # WRITING A JAVA CODE
        
        for var in getvar.WriteWrite():
            if var.startswith('key' + NameFile):
                Target.write(var.replace('key', '').replace(NameFile, ''))
        
        Target.write('\n}')
        Target.close()

    OnEnable = open(dir + ProjectName + '/src/main/java/' + maindir + '/' + 'OnEnable.java', 'w+', encoding='utf8')
    
    # WRITING PACKAGE
    OnEnable.write('package ' + mainpackage[1] + '.' + mainpackage[2] + ';\n\n')
    
    # WRITING LISTENERS
    
    for var in getvar.WriteListeners():
        # import fr.gonpvp.listeners.name of listeners;
        print('loop')
        OnEnable.write(mainpackage[1] + '.' + mainpackage[2] + '.listeners.' + var + ';\n')
    
    # for var in PyCub_Command_Write:
    #     # import fr.gonpvp.listeners.name of command;
    #     Target.write(+ mainpackage[1] + '.' + mainpackage[2] + '.command.' + var + ';\n')
    
    OnEnable.write('org.bukkit.plugin.java.JavaPlugin;\n\n')
    OnEnable.write('public final class ' + ProjectName + ' extends JavaPlugin {\n\n')
    # public final class ProjectName extends JavaPlugin {
    
    OnEnable.write(tab + 'private static ' + ProjectName + ' INSTANCE;\n\n')
    #   private static ProjectName INSTANCE;
    
    OnEnable.write(tab + '@Override\n')
    OnEnable.write(tab + 'public void onEnable() {\n')
    OnEnable.write(tab * 2 + 'INSTANCE = this;\n' + tab * 2 +'// Plugin startup logic\n')
    for var in getvar.WriteListeners():
        print('loop')
        OnEnable.write(tab * 2 + 'getServer().getPluginManager().registerEvents(new ' + var + ProjectName + 'Listener(), this);\n')
    # for var in PyCub_Command_Write:
    #     OnEnable.write(tab * 2 + var)
    OnEnable.write(tab + '}\n\n')
    
    OnEnable.write(tab + '@Override\n')
    OnEnable.write(tab + 'public void onDisable() {\n')
    OnEnable.write(tab * 2 + '// Plugin shutdown logic\n')
    OnEnable.write(tab + '}\n\n')
    
    OnEnable.write(tab + 'public ' + ProjectName + ' getInstance(){\n')
    OnEnable.write(tab * 2 + 'return INSTANCE;\n')
    OnEnable.write(tab + '}\n')
    OnEnable.write('}')

    OnEnable.close()
        
    # CLOSE ALL FILE WITH METHOD close()
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

def PyCub_CreateProject(dir, country = "fr", author = "PyCubTranspilator", ProjectName = 'None'):
    
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
    
    
    pl_yml.write('name: ' + ProjectName.lower() + '\n')
    pl_yml.write('author: ' + author + '\n')
    
    main = country + '.' + author + '.' + ProjectName.lower()
    pl_yml.write('main: ' + main + '\n')
    pl_yml.write('version: ' + '0.1' + '\n')
    pl_yml.write('commands:' + '\n')
    pl_yml.close()
    
    
    # CREATE MAIN DIR
    
    maindir = main.replace('.', '/')
    main_dir = dir + ProjectName + '/src/main/java/' + maindir + '/'
    os.makedirs(os.path.dirname(main_dir), exist_ok=True)
    

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
            print('')
            print('--------------------')
            print('')
            print(' - c(reate)p(rojet) <dir> <country> <author> <name>')
            print('Allows you to create a script project')
            print('Exemple: cp C:/PythonProject/Pycub/projects/ fr gonpvp test')
            print('')
            print(' - rl <dir> <name>')
            print('Allows you to create a script project')
            print('Exemple: rl C:/PythonProject/Pycub/projects/ test')
            print('')
            print(' - clear')
            print('Clear the terminal')
            print('')
            print('Support: discord.gg/hm8VXyVx5u')
            print('')
        
        elif command_input.startswith('cp') or command_input.startswith('cr'):
            commands = command_input.split(' ')
            for var in commands:
                print(var)
            PyCub_CreateProject(commands[1], commands[2], commands[3], commands[4])
        
        elif command_input.startswith('rl'):
            command_strip = command_input.split(' ')
            PyCub_Compil(command_strip[1], command_strip[2])
        
        elif command_input == 'close':
            print('Good bye :)')
            break
        elif command_input == 'pause':
            clear = lambda: os.system('pause')
            clear()
        elif command_input == 'clear':
            clear = lambda: os.system('cls')
            clear()
        else:
            print('command not exist')
    exit()
    

#   _                  _       _   _                          _       _   
#  | |                | |     | | | |                        (_)     | |  
#  | | __ _ _ __   ___| |__   | |_| |__   ___   ___  ___ _ __ _ _ __ | |_ 
#  | |/ _` | '_ \ / __| '_ \  | __| '_ \ / _ \ / __|/ __| '__| | '_ \| __|
#  | | (_| | | | | (__| | | | | |_| | | |  __/ \__ \ (__| |  | | |_) | |_ 
#  |_|\__,_|_| |_|\___|_| |_|  \__|_| |_|\___| |___/\___|_|  |_| .__/ \__|
#                                                              | |        
#                                                              |_|            
      
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
=======
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

def PyCub_Compil(dir , ProjectName):

    #                 _ _          __ _ _      
    #                (_) |        / _(_) |     
    #  __      ___ __ _| |_ ___  | |_ _| | ___ 
    #  \ \ /\ / / '__| | __/ _ \ |  _| | |/ _ \
    #   \ V  V /| |  | | ||  __/ | | | | |  __/
    #    \_/\_/ |_|  |_|\__\___| |_| |_|_|\___|
                                            
                                
    def PyCub_Write(var):
        PyCub_C_Write.append('key' + PyCub_JavaFile[-1] + var)
    
    def PyCub_Import(var):
        if 'key' + PyCub_JavaFile[-1] + var in PyCub_C_Import:
            pass
        else:
            PyCub_C_Import.append('key' + PyCub_JavaFile[-1] + var)
    
    def PyCub_AddJavaFile(name):
        PyCub_JavaFile.append(name.rstrip() + '.java')
        print('add file' + str(PyCub_JavaFile) + ActuelFileModif)
    
    # ADD LISTENERS IN OnEnable.java
    
    def PyCub_AddListener(var):
        ListenerText = var
        PyCub_Listener_Write.append(var)  
    
    # # ADD COMMAND IN OnEnable.java
    
    # def PyCub_AddCommand(var):
    #     ListenerText = var
    #     # PyCub_Command_Write.append('getCommand("' + var + 'test").setExecutor(new testCommand());')   
    #     PyCub_Command_Write.append(var)  
    
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
                expr = PyCub_ModifArg(car[14:-1], "setjoinmessage")
                PyCub_Write(tab * 2 + "event.setJoinMessage(" + expr + ");\n")  
        
        elif car.startswith('broadcast'):
            expr = PyCub_ModifArg(car[10:-1], "broadcast")
            PyCub_Write(tab * 2 + "Bukkit.broadcastMessage(" + expr + ");\n")   

        else:
            print("The effect is not exist (lign" + str(PycubLign) + ")")
   
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
            PyCub_Import("import org.bukkit.event.EventHandler;")
            PyCub_Import("import org.bukkit.event.Listener;")
            PyCub_Import("import org.bukkit.event.player.PlayerJoinEvent;")
            expr_PycubLign = PycubLign
            for _expr in From:
                expr_PycubLign =+ 1
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
            expr_PycubLign = PycubLign
            for _expr in From:
                expr_PycubLign =+ 1
                if _expr.strip() == "stop":
                    break
                else:
                    PyCub_ChoiceArg(_expr.strip(), "on_player_leave")
                
            PyCub_Write(tab * 1 + '}\n')       
        
        else:
            print("The event is not exist (lign" + str(PycubLign) + ")")
    
    print("Loading ...")

    FromFile = 'C:/PythonProject/Pycub/scripts/' + ProjectName + '.pycub'
    
    PathTargetFile = 'C:/PythonProject/Pycub/projects/' + ProjectName + '/'
    
    TargetCacheFile = 'C:/PythonProject/Pycub/scripts/.cache/test.pycub'
    
    From = open(FromFile, 'r', encoding='utf8')

    tab = "    "
    first_event = False
    global PycubLign
    PycubLign = 1
    PyCub_C_Write = []
    PyCub_C_Import = []
    PyCub_Listener_Write = []
    PyCub_Command_Write = []
    PyCub_JavaFile = ['OnEnable.java']
    ActuelFileModif = 'OnEnable.java'
    
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
        
        # ADD 1 Lign (FOR WARN)
        
        PycubLign =+ 1
        
        if car.startswith('#'):
            PyCub_Write(car)
        # elif car.startswith('delete file:'):
        #     PyCub_AddJavaFile(car[12:])
        #     print('test changefile' + car[12:])
        elif car.startswith('start file:'):
            PyCub_AddJavaFile(car[12:])
        elif car.startswith('change file:') or car.startswith('moove file:'):
            PyCub_Write('}\n')
            PyCub_AddJavaFile(car[13:])
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
                first_event = True
                global eventnumber
                eventnumber = 1
            
            # CALL EVENT
            
            eventnumber =+ 1
            PyCub_AddEvent(callevent)               
                        
        else:        
            PyCub_Write('\n')
            
            acar = car.replace(" ", "")
            
            if PycubLign != 1:
                if car.strip() == '':
                    print("The types is not exist PycubLign" + str(PycubLign))

    if first_event == True:
        PyCub_Write('}\n')
    
    #                  _           _             _                        _ 
    #             | |         | |           (_)                      | |
    #    __ _  ___| |_   _ __ | |_   _  __ _ _ _ __   _   _ _ __ ___ | |
    #   / _` |/ _ \ __| | '_ \| | | | |/ _` | | '_ \ | | | | '_ ` _ \| |
    #  | (_| |  __/ |_  | |_) | | |_| | (_| | | | | || |_| | | | | | | |
    #   \__, |\___|\__| | .__/|_|\__,_|\__, |_|_| |_(_)__, |_| |_| |_|_|
    #    __/ |          | |             __/ |          __/ |            
    #   |___/           |_|            |___/          |___/             
    
    with open(dir + ProjectName + '/src/main/resources/' + 'plugin.yml', 'r') as PluginYml:
        
        numberlign = 1
        
        textlign = PluginYml.readline().rstrip()
        while textlign:
            if numberlign == 2:
                author = textlign.replace('author: ', '')
                print('author : ' + author)
            elif numberlign == 3:
                main = textlign.replace('main: ', '').strip('.')
                print('main : ' + main)
                maindir = main.replace('.', '/')
                mainpackage = main.split('.')
                
            numberlign += 1
            
            textlign = PluginYml.readline().rstrip()

    #                 _ _           _                  
    #                (_) |         (_)                 
    #  __      ___ __ _| |_ ___     _  __ ___   ____ _ 
    #  \ \ /\ / / '__| | __/ _ \   | |/ _` \ \ / / _` |
    #   \ V  V /| |  | | ||  __/  _| | (_| |\ V / (_| |
    #    \_/\_/ |_|  |_|\__\___| (_) |\__,_| \_/ \__,_|
    #                             _/ |                 
    #                            |__/                      
        

    for NameFile in PyCub_JavaFile:
        print('Writing file ' + NameFile + '...')
        
        Target = open(dir + ProjectName + '/src/main/java/' + maindir + '/' + NameFile, 'w+', encoding='utf8')
        
        NoJavaNameFile = NameFile.replace('.java','')
        Target.write('package fr.gonpvp.' + NoJavaNameFile.lower() + ';\n\n')
        for var in PyCub_C_Import:
            # print('import (in file ' + NameFile + ')' + var)
            if var.startswith('key' + NameFile):
                filtervar = var.replace('key', '')    
                filtervar = filtervar.replace(NameFile, '')    
                Target.write(filtervar + '\n')
        Target.write('\npublic class ' + NoJavaNameFile + ' implements Listener {')
        for var in PyCub_C_Write:
            # print('write (in file ' + NameFile + ')' + var)
            if var.startswith('key' + NameFile):
                filtervar = var
                filtervar = var.replace('key', '')    
                filtervar = filtervar.replace(NameFile, '')    
                Target.write(filtervar)
        Target.close()

    OnEnable = open(dir + ProjectName + '/src/main/java/' + maindir + '/' + 'OnEnable.java', 'w+', encoding='utf8')
    
    OnEnable.write('package ' + mainpackage[1] + '.' + mainpackage[2] + ';\n')
    for var in PyCub_Listener_Write:
        # import fr.gonpvp.listeners.name of listeners;
        Target.write(+ mainpackage[1] + '.' + mainpackage[2] + '.listeners.' + var + ';\n')
    
    # for var in PyCub_Command_Write:
    #     # import fr.gonpvp.listeners.name of command;
    #     Target.write(+ mainpackage[1] + '.' + mainpackage[2] + '.command.' + var + ';\n')
    
    OnEnable.write('org.bukkit.plugin.java.JavaPlugin;\n\n')
    OnEnable.write('public final class ' + ProjectName + ' extends JavaPlugin {\n\n')
    # public final class ProjectName extends JavaPlugin {
    
    OnEnable.write(tab + 'private static ' + ProjectName + ' INSTANCE;\n\n')
    #   private static ProjectName INSTANCE;
    
    OnEnable.write(tab + '@Override\n')
    OnEnable.write(tab + 'public void onEnable() {\n')
    OnEnable.write(tab * 2 + 'INSTANCE = this;\n' + tab * 2 +'// Plugin startup logic\n')
    for var in PyCub_Listener_Write:
        OnEnable.write(tab * 2 + 'getServer().getPluginManager().registerEvents(new ' + var + ProjectName + 'Listener(), this);\n')
    # for var in PyCub_Command_Write:
    #     OnEnable.write(tab * 2 + var)
    OnEnable.write(tab + '}\n\n')
    
    OnEnable.write(tab + '@Override\n')
    OnEnable.write(tab + 'public void onDisable() {\n')
    OnEnable.write(tab * 2 + '// Plugin shutdown logic\n')
    OnEnable.write(tab + '}\n\n')
    
    OnEnable.write(tab + 'public ' + ProjectName + ' getInstance(){\n')
    OnEnable.write(tab * 2 + 'return INSTANCE;\n')
    OnEnable.write(tab + '}\n')
    OnEnable.write('}')

    OnEnable.close()
        
    # CLOSE ALL FILE WITH METHOD close()
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

def PyCub_CreateProject(dir, ProjectName, country = "fr", author = "PyCubTranspilator"):
    
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
    
    
    pl_yml.write('name: ' + ProjectName.lower() + '\n')
    pl_yml.write('author: ' + author + '\n')
    
    main = country + '.' + author + '.' + ProjectName.lower()
    pl_yml.write('main: ' + main + '\n')
    pl_yml.write('version: ' + '0.1' + '\n')
    pl_yml.write('commands:' + '\n')
    pl_yml.close()
    
    
    # CREATE MAIN DIR
    
    maindir = main.replace('.', '/')
    main_dir = dir + ProjectName + '/src/main/java/' + maindir + '/'
    os.makedirs(os.path.dirname(main_dir), exist_ok=True)
    

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
            print('')
            print('--------------------')
            print('')
            print(' - c(reate)p(rojet) <dir> <country> <author> <name>')
            print('Allows you to create a script project')
            print('Exemple: cp C:/PythonProject/Pycub/projects/ test fr gonpvp')
            print('')
            print(' - rl <dir> <name>')
            print('Allows you to create a script project')
            print('Exemple: rl C:/PythonProject/Pycub/projects/ test')
            print('')
            print('Support: discord.gg/hm8VXyVx5u')
            print('')
        
        elif command_input.startswith('cp') or command_input.startswith('cr'):
            commands = command_input.split(' ')
            package = commands[1].split('.')
            PyCub_CreateProject(package[0], package[4], package[3], package[2])
        
        elif command_input.startswith('rl'):
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
>>>>>>> Stashed changes
