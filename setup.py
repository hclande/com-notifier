import os
import time
import win32com.client
from win32com.shell import shell, shellcon
import pythoncom
import ctypes, sys
import threading

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def startupdirectory():
    return shell.SHGetFolderPath(
        0,
        shellcon.CSIDL_STARTUP,
        0,# null access token (no impersonation)
        0 # want current value, shellcon.SHGFP_TYPE_CURRENT isn't available, this seems to work
        )


def install():
    pth = os.path.dirname(os.path.realpath(__file__))
    s_name = "com-notifier.lnk"
    com_name = "\com-notifier.exe"
    frompath = '"'+ pth + com_name +'"'

    print("\n Creating shortcut in startup folder for COM")
    print("\n shortcut target : %s\n" %frompath)
    print("\n copying shortcut to Windows Startup folder:")

    # pythoncom.CoInitialize() # remove the '#' at the beginning of the line if running in a thread.
    desktop = startupdirectory()  #r'C:\Users\hcl23810p.WESTCON\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' # path to where you want to put the .lnk
    path = os.path.join(desktop , s_name) #(desktop +  s_name)
    print(path)
    target = frompath
    #icon = r'C:\Users\XXXXX\Desktop\muell\icons8-link-512.ico'  # not needed, but nice

    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    #shortcut.IconLocation = icon
    shortcut.WindowStyle = 7  # 7 - Minimized, 3 - Maximized, 1 - Normal
    shortcut.save()

    time.sleep(2)
    print("\n \nRestart or double click COM.EXE to run script")
    time.sleep(5)
    #b = input("Do you want to run script?(y/n)")

    if b == "y":
        print("starting script..")
        print( frompath )
        os.system(frompath)

    else:
        print("Exiting")
        time.sleep(2)
        pass

if __name__ == "__main__":
    if is_admin():
        a = input("do you want to add COM to Windows startup?(y/n)")
        if a == "y":
            install()
        else:
            print("Exiting without adding to Windows startup")
            time.sleep(2)
            pass
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)

