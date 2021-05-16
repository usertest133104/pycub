
# IMPORTS

import os
import time

# BASE NON COMPILED FUNCTION

global number_event_call
number_event_call = 0

def PyCub_Compil(dir, File_name, main, author = "PyCubTranspilator"):


    # ADD WRITE AND IMPORT JAVA FILE

    def PyCub_Write(var):
        PyCub_C_Write.append(var)
    def PyCub_Import(var):
        if var in PyCub_C_Import:
            pass
        else:
            PyCub_C_Import.append(var)
    
    # ADD LISTENERS AND COMMAND IN Main.java
    
    def PyCub_AddListener(var):
        PyCub_Listener_Write.append('getServer().getPluginManager().registerEvents(new ' + var + 'testListener(), this);')   
        PyCub_Listener_Name.append(var)  
    
    def PyCub_AddCommand(var):
        PyCub_Command_Write.append('getCommand("' + var + 'test").setExecutor(new testCommand());')   
        PyCub_Command_Name.append(var)  
    
    # SEPARATE ESPACE    
        
    def PyCub_UnSeparteArg(arg):
        return arg.replace('||', ' ')
    def PyCub_SeparteArg(arg):
        return arg.replace(' ', '||')

            
    # LIST OF ALL EXPRESSION 

    def PyCub_AddExpr(car, event):
        if car.contains("player"):
            if event == "on_player_join":
                PyCub_Write(tab * 2 + "Bukkit.broascastMessage(" + reason + ") ;\n")

    def PyCub_AddCalcul(car, event):
        if car in ' = ' or ' =+ ' or ' =- ' or ' invers ':
            print('no finish')
        elif car in ' =+ ':
            print('no finish')

    
    def PyCub_ModifArg(car, expr):
#        print("call :" + car)
        if '"' and '+' in car:
            arg = PyCub_SeparteArg(car)
#            print("yes '" + car)
            if 'player' in arg:
#                print(arg)
                if 'player||name' in arg:
                    arg = arg.replace('player||name', 'event.getPlayer().getName()')
                if 'player' or '||player||' or '||player' or 'player||' in arg:
                    arg = arg.replace('player', 'event.getPlayer()')    
                return PyCub_UnSeparteArg(arg)
        elif '"' and '+' not in car:
#            print("not '" + car)
            if 'player' in car:
#                print(car)
                if 'player name' in car:
                    arg = car.replace('player name', 'event.getPlayer().getName()')
                if 'player' in arg:
                    arg = car.replace('player', 'event.getPlayer()')    
                return PyCub_UnSeparteArg(arg)
        else:
            return car 
    
    # LIST OF ALL EFFECT

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

    def PyCub_ChoiceArg(car, event):
        if " = " in car:
            PyCub_AddCalcul(car, event) 
        else:
            PyCub_AddEffect(car, event)
            
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
            
            # LIST OF ALL EVENT 
            
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

def PyCub_CreateProject(dir, File_name, main, author = "PyCubTranspilator"):
    
    # CREATE PLUGINS.YML
    
    pl_yml = dir + File_name + '/src/main/resources/plugin.yml'
    print(pl_yml)
    os.makedirs(os.path.dirname(pl_yml), exist_ok=True)
    pl_yml = open(pl_yml, 'w+', encoding='utf8')
    
    
    pl_yml.write('name: ' + File_name + '\n')
    pl_yml.write('author: ' + author + '\n')
    
    # fr.gonpvp.pycub
    
    pl_yml.write('main: ' + main + '\n')
    pl_yml.write('version: ' + '0.1' + '\n')
    pl_yml.write('commands:' + '\n')
    pl_yml.close()
    
    
    # CREATE MAIN DIR
    
    maindir = main.replace('.', '/')
    main_dir = dir + File_name + '/src/main/java/' + maindir + '/'
    os.makedirs(os.path.dirname(main_dir), exist_ok=True)
    
    
PyCub_CreateProject('C:/PythonProject/Pycub/projects/test/', 'test', 'fr.gonpvp.pycub')
PyCub_Compil('C:/PythonProject/Pycub/projects/test/', 'test', 'fr.gonpvp')

#os.system('cd C:\PythonProject\Pycub\jar-ressource')
#os.system('gradlew.bat')