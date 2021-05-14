
# IMPORTS

import os
import time

# BASE NON COMPILED FUNCTION

global number_event_call
number_event_call = 0

def PyCub_Compil():

    def PyCub_Write(var):
        PyCub_C_Write.append(var)
    def PyCub_Import(var):
        if var in PyCub_C_Import:
            pass
        else:
            PyCub_C_Import.append(var)
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
    
    TargetFile = PathTargetFile + '/test.txt'
    TargetCacheFile = 'C:/PythonProject/Pycub/scripts/.cache/test.pycub'
    
    os.makedirs(os.path.dirname(PathTargetFile), exist_ok=True)
    From = open(FromFile, 'r', encoding='utf8')
    Target = open(TargetFile, 'w+', encoding='utf8')

    tab = "    "
    first_event = False
    global lign
    lign = 1
    PyCub_C_Write = []
    PyCub_C_Import = []
    
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

        
    # fermeture du fichier avec la méthode close()
    Target.close()
    From.close()

    print("Compiled !")

PyCub_Compil()
#os.system('cd C:\PythonProject\Pycub\jar-ressource')
#os.system('gradlew.bat')