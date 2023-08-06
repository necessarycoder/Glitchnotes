import os
try:
    file = open("/.glitchnotes/installer", "r")
    file.close()
    start = input("are you sure you want to uninstall GlitchNotes? (your notes will be deleted!) [y/n]")
    start = start.lower()
    if start == "y":
        print("uninstalling...")
        os.system("rm -r /.notes/ && rm /bin/GlitchNotes")
    else:
        pass
except FileNotFoundError:
    start = input("are you sure you want to install GlitchNotes? (for installer to work you need these packages: git) (only works on linux) [y/n] ")
    start = start.lower()
    if start == "y":
        print("starting installation...")
        os.system("mkdir /.glitchnotes/ && mkdir /.glitchnotes/notes && touch /.glitchnotesnotes/installer && echo \"python /.glitchnotes/main.py\" > /bin/glitchnotes && chmod +x /bin/notes && git clone https://github.com/CurrentlyIsGlitching/Glitchnotes/ && cp Glitchnotes/main.py /.glitchnotes/ && rm -r Glitchnotes &&echo \"installation succesful! if you want to launch GlitchNotes just type glitchnotes, and if you want to remove this app open this installer again.\"")
    else:
[admin@localhost заметки]$ cat installer.py
import oscalhost заметки]$ cat installer.py
try:
    file = open("/.glitchnotes/installer", "r")
    file.close()
    start = input("are you sure you want to uninstall GlitchNotes? (your notes will be deleted!) [y/n]")
    start = start.lower()
    if start == "y":
        print("uninstalling...")
        os.system("rm -r /.notes/ && rm /bin/GlitchNotes")
    else:
        pass
except FileNotFoundError:
    start = input("are you sure you want to install GlitchNotes? (for installer to work you need these packages: git) (only works on linux) [y/n] ")
    start = start.lower()
    if start == "y":
        print("starting installation...")
        os.system("mkdir /.glitchnotes/ && mkdir /.glitchnotes/notes && touch /.glitchnotesnotes/installer && echo \"python /.glitchnotes/main.py\" > /bin/glitchnotes && chmod +x /bin/notes && git clone https://github.com/CurrentlyIsGlitching/Glitchnotes/ && cp Glitchnotes/main.py /.glitchnotes/ && rm -r Glitchnotes &&echo \"installation succesful! if you want to launch GlitchNotes just type glitchnotes, and if you want to remove this app open this installer again.\"")
    else:
        print("cancelling...")
