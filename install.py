import os, winshell
from win32com.client import Dispatch

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
      INSTALLATION ...                        (      (        _-~    _--_    ~-_     _/   |
                                               \      ~-____-~    _-~    ~-_    ~-_-~    /
                                                   ~-_           _-~          ~-_       _-~
                                                   ~--______-~                ~-___-~      
            """)

os.system('cd ' + os.getcwd())
print('Installing dependance ...')
os.system('pip install -r requirements.txt')

os.system('cls')
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
      Create shortcut ...                     (      (        _-~    _--_    ~-_     _/   |
                                               \      ~-____-~    _-~    ~-_    ~-_-~    /
                                                   ~-_           _-~          ~-_       _-~
                                                   ~--______-~                ~-___-~      
            """)

print("Create shortcut name 'PyCubTerminal' in desktop for starting PyCub ...")

desktop = winshell.desktop()
path = os.path.join(desktop, "PyCubTerminal.lnk")
target = os.getcwd() + '\main\main.py'
wDir = os.getcwd()
icon = os.getcwd() + '\main\logo.ico'
shell = Dispatch('WScript.Shell')
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
shortcut.WorkingDirectory = wDir
shortcut.IconLocation = icon
shortcut.save()

os.system('cls')
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
      INSTALLATION IS FINISH !                (      (        _-~    _--_    ~-_     _/   |
                                               \      ~-____-~    _-~    ~-_    ~-_-~    /
                                                   ~-_           _-~          ~-_       _-~
                                                   ~--______-~                ~-___-~      
            """)