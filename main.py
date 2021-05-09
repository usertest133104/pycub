
# IMPORTS

import string

# BASE NON COMPILED FUNCTION

def PyCub_Compil():

    # LIST OF ALL EXPRESSION 

    def PyCub_AddExpr(car, event):
        if car.contains("player"):
            if event == "on_player_join":
                Target.write(tab * 2 + "Bukkit.broascastMessage(" + reason + ") ;\n")

    # LIST OF ALL EFFECT

    def PyCub_AddEffect(car, event):
        if car.startswith('setjoinmessage'):
            expr = car
            if "setjoinmessage" in From.read():
                print(f"You can't use the setjoinmessage() expression because it already exists ")
            else:
                reason = expr
                reason = reason.replace("+ player +", '+ event.getPlayer().getName() +')
                reason = reason.replace("player +", 'event.getPlayer().getName() +')
                reason = reason.replace("+ player", '+ event.getPlayer().getName()')
                Target.write(tab * 2 + "Bukkit.broascastMessage(" + reason + ");\n")  
        elif car.startswith('broadcast'):
            expr = car
            expr = expr[10:]
            expr = expr[:-1]
            reason = expr
            reason = reason.replace("+ player +", '+ event.getPlayer().getName() +')
            reason = reason.replace("player +", 'event.getPlayer().getName() +')
            reason = reason.replace("+ player", '+ event.getPlayer().getName()')
            Target.write(tab * 2 + "Bukkit.broascastMessage(" + reason + ");\n")   

    print("Loading ...")

    From = 'C:/PythonProject/Pycub/test.pycub'
    Target = 'C:/PythonProject/Pycub/test.txt'

    From = open(From, 'r', encoding='utf8')
    Target = open(Target, 'w', encoding='utf8')

    tab = "    "
    first_event = False
    global lign
    lign = 1
    eventplayerjoin = 0

    for car in From:
        
        # Sélectionneur d'évènement
        lign =+ 1
        
        if car.startswith('package'):
            Target.write(car + ';')
        if car.startswith('#'):
            Target.write(car)
        elif car.startswith('import'):
            if car.startswith('import bukkit'):
                Target.write('import org.bukkit;\n')
            
            else: 
                text = car + ';'
                Target.write(text)
        
        elif car.startswith('event') or car.startswith('on'):
            
            # DETECT START WITH EVENT OR ON
            
            if car.startswith('on'):
                event = car[3:]

            elif car.startswith('event'):
                event = car[6:]
                
            # ADD FIRST PUBLIC CLASS
            
            if first_event == False:
                Target.write('public class PycubEvent implements Listener {\n')
                first_event = True
            
            # LIST OF ALL EVENT 
            

            if event.startswith('on_player_join:') or event.startswith('player join:'):
                
                # écriture de l'handler évent
                
                Target.write('\n' + tab + '@EventHandler \n')
                
                # NAME OF PUBLIC CLASS
                
                Target.write(tab + 'public void OnPlayerJoin' + str(eventplayerjoin) + '(PlayerJoinEvent event) {\n')
                expr_lign = lign
                for _expr in From:
                    expr = _expr.strip()
                    expr_lign =+ 1
                    if expr == "stop":
                        eventplayerjoin += 1
                        break
                    else:
                        PyCub_AddEffect(expr, "on_player_join")
                
                Target.write(tab * 1 + '}\n')                    
                        
        else:        
            Target.write('\n')
            
            acar = car
            acar.replace(" ", "")
            
            if lign != 1:
                if car.strip() == '':
                    print("The event is not exist lign" + str(lign))

    if first_event == True:
        Target.write('}\n')

    # fermeture du fichier avec la méthode close()
    Target.close()
    From.close()

    print("Compiled !")

PyCub_Compil()