from N4Tools.Design import Animation
from N4Tools.Design import ThreadAnimation
from N4Tools.Design import Text
from N4Tools.Design import AnimationTools
from time import sleep
import shutil
import os
import sys
import time
import random
import socket
##################################
import os
import socket
import time
import sys
###########################################################################
mix = sys.maxsize
#############################################################################
def plist ():
    namelist = input ('\033[2;36mEnter The File Name [~] : ')
    i =int(input(' \033[2;36mNumber [~] : '))
    fd = open(namelist,'w')
    sys.stdout = fd
    rand = (random.randint(1,14))
    for i in range(i) :
        user = (r'qwertyuiopasdfghjklzxcvbnm@#_&-+(/*:;!?%[]{})1234567890QWERTYUIO')
        us = str(''.join((random.choice(user) for i in range (random.randint(8,16)))))
        print (us)

    sys.stdout = sys.__stdout__
    sleep(1)
    print('\033[1;33m[\033[1;32mDune ✓\033[1;33m]')
    print ('\033[1;32mThank \033[1;31mYoy \033[1;33mTo \033[1;34mUsed \033[1;35mMy \033[1;36mTool')
    m = '/'
    print (os.getcwd(),m,namelist)
    Hello()
########################################################################################################################
def net ():
    os.system('python tool/network_info.py')
##################################################################
def Lime():
    slowprint('\033[1;30m _     _')
    slowprint('\033[1;31m| |   (_)_ __ ____  ___')
    slowprint("\033[1;32m| |   | | '_ ` _  |/ _ | ")
    slowprint('\033[1;33m| |___| | | | | | | __/')
    slowprint('\033[1;34m|_____|_|_| |_| |_|/__|')
    Hello()
####################################################################################
T = Text()
def ls():
    i = os.listdir()
    for x in i:
        print(i)
#############################222222222222222##########################
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
 ###############################################################
def held():
    slowprint("""
   COMMAND                      DESCRIPTION
  \033[1;31m---------      ---       ----------------------------------\033[1;31m
  |  \033[1;37mcls         \033[1;32m :         \033[1;33mclear screan        \033[1;31m            |
  |  \033[1;37mexit        \033[1;32m :         \033[1;33mexit to tool          \033[1;31m          |
  |  \033[1;37mpwd         \033[1;32m :         \033[1;33mshoe directry         \033[1;31m          |
  |  \033[1;37mheight      \033[1;32m :         \033[1;33mheight numper         \033[1;31m          |
  |  \033[1;37mplist       \033[1;32m :         \033[1;33mcreat wordlist        \033[1;31m          |
  |  \033[1;37mwidth       \033[1;32m :         \033[1;33mwidth numper          \033[1;31m          |
  |  \033[1;37mip_address  \033[1;32m :         \033[1;33mget ip site           \033[1;31m          |
  |  \033[1;37mrest        \033[1;32m :         \033[1;33mrestart tool        \033[1;31m            |
  |  \033[1;37mhelp        \033[1;32m :         \033[1;33mshow command          \033[1;31m          |
  |  \033[1;37mTelgram     \033[1;32m :         \033[1;33mFollow us on Telegram\033[1;31m           |
  |  \033[1;37mFacebook    \033[1;32m :         \033[1;33mFollow us on Facebook\033[1;31m           |
  |  \033[1;37mls          \033[1;32m :         \033[1;33mshow folder           \033[1;31m          |
  |  \033[1;37mnetwork-info\033[1;32m :         \033[1;33mnetwork Scaning     \033[1;31m            |
  |  \033[1;37mGame-Snake  \033[1;32m :         \033[1;33mGame Snake          \033[1;31m            |
  |  \033[1;37mwight       \033[1;32m :         \033[1;33mwidth & height      \033[1;31m            |
  ---------      ---   \033[1;31m    ----------------------------------
     """)
    Hello()
####################################################################################
def lbs():
    ls = os.listdir()
    for i in ls :
        print (i)
##############################################################################################################
def emag ():
    from tool.main import Run_Games
    Hello()
##############################################################################################################
@ThreadAnimation(Animation=Animation().Loading, kwargs={"text":"\033[1;31mLoding... "})
def my_function(Thread):
    rand=(random.randrange(7))
    time.sleep(rand)
##################################################
@ThreadAnimation(Animation=Animation().Loading, kwargs={"text":"\033[1;31mLoding... "})
def  back (Thread):
    l = (random.randrange(3))
    time.sleep(1.5)
###################################################
def ext():
    back()    
    os.system('clear')
    print ('\033[1;32mThank \033[1;31mYoy \033[1;33mTo \033[1;34mUsed \033[1;35mMy \033[1;36mTool')
#################################################        
def restart():
    os.system('python3 figlet.py')
###################################################
dirct = (os.getcwd())
####################################################
def Hello ():
    width = (shutil.get_terminal_size().columns)
    height = (shutil.get_terminal_size().lines)
    dirct = (os.getcwd())
#    rand = (random.randint(1,7))
    numper = input ("\033[1;34m┌──\033[1;33m(\033[1;32mLime\033[1;33m)\033[1;32m~\033[1;34m[\033[1;37mRobin\033[1;34m]\n└─\033[1;31m$ \033[1;32m")
    if numper == 'Lime':
        my_function()
        Lime()
    elif numper == 'cls':
        os.system('clear')
        Hello()
    elif numper == 'max':
        print (mix)
        Hello()
    elif numper == 'width':
        print(width)
        Hello()
    elif numper == 'height':
        print (height)
        Hello()
    elif numper == 'wight':
        print ('\033[1;33mwidth is : ',width)
        print ('\033[1;33mheight is : ',height)
        Hello()
    elif numper == 'exit':
        ext()
    elif numper == 'help':
        held()
    elif numper == 'rest':
        restart()
    elif numper == 'plist':
        plist()
    elif numper == 'pwd':
        print (os.getcwd())
        Hello()
    elif numper == 'ls':
        lbs()
        Hello()
    elif numper == 'Telegram':
        os.system('xdg-open https://t.me/DrLime4110')
        Hello()
    elif numper == 'Facebook':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100086991363401')
        Hello()
    elif numper == 'm':
        os.system('micro')
        Hello()
    elif numper == 'Game-Snake':
        emag()
        Hello()
        system('python3 figlet.py')
    elif numper == 'network-info' :
        net()
        Hello()
    elif numper == 'ip_address':
        from tool.ip_addreas import main
        Hello()
    else :
        my_function()
        slowprint(T.Figlet(numper,font='big'))
        Hello()
Hello()

