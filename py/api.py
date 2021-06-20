test = "test"

class Projet:
    
    def __init__(self):
        pass

    def createvar(FromFile, ProjectName):
        global number_event_call
        number_event_call = 0
        global tab
        tab = "    "
        global NameFile
        NameFile = FromFile
        global PycubLign
        PycubLign = 1
        global PyCub_C_Write
        PyCub_C_Write = []
        global PyCub_C_Import
        PyCub_C_Import = []
        global PyCub_Listener_Write
        PyCub_Listener_Write = []
        global PyCub_Command_Write
        PyCub_Command_Write = []
        global PyCub_JavaFile
        PyCub_JavaFile = ['Main.java']
        global ActuelFileModif
        ActuelFileModif = 'Main.java'
        global ActualProjectName
        ActualProjectName = ProjectName

class getvar:
    def __init__():
        pass
    
    def WriteImport():
        return PyCub_C_Import

    def WriteWrite():
        return PyCub_C_Write

    def namefile():
        return NameFile

    def readfile():
        return NameFile.read()

    def lign():
        return PycubLign

    def JavaFile():
        return PyCub_JavaFile

    def tab():
        return tab

    def WriteListeners():
        return PyCub_Listener_Write
    
    def WriteCommand():
        return PyCub_Command_Write

    def NumberCallEvent():
        return number_event_call

class Interpretrer:
    def __init__(self):
        pass
    
    def Add1Lign():
        PycubLign =+ 1
    
    def AddLign(self, number):
        PycubLign =+ number

    def RemoveLign(self, number):
        PycubLign =- var 
    
    
    def Add1CallEvent():
        number_event_call =+ 1
    
    def AddCallEvent(self, number):
        number_event_call =+ number

    def RemoveCallEvent(self, number):
        number_event_call =- var 


class setvar:
    def __init__(self):
        pass
    
    def JavaFile(var):
        ActuelFileModif = var
    
    def ProjetName(var):
        ActualProjectName = var 


class Compiler:
    def __init__(self):
        pass
    
    def write(var):
        PyCub_C_Write.append('key' + PyCub_JavaFile[-1] + var)

    def Import(var):
        if 'key' + PyCub_JavaFile[-1] + var in PyCub_C_Import:
            pass
        else:
            PyCub_C_Import.append('key' + PyCub_JavaFile[-1] + var)
    
    def AddJavaFile(self, name):
        PyCub_JavaFile.append(name.rstrip() + '.java')
        print('add file' + str(PyCub_JavaFile) + ActuelFileModif)

    def AddListener(self, var):
        ListenerText = var
        PyCub_Listener_Write.append(var)  
    
    def PyCub_AddCommand(self, var):
        ListenerText = var
        # PyCub_Command_Write.append('getCommand("' + var + 'test").setExecutor(new testCommand());')   
        PyCub_Command_Write.append(var)  


# class var:
#     def __init__(self):
#         pass

#     def get(self, var):
#         return var

#     def add(self, var, add):
#         var = 
    