import winreg

'''
def getMicrosoftWordVersion():
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Office", 0, winreg.KEY_READ)
    versionNum = 0
    i = 0
    while True:
        try:
            subkey = winreg.EnumKey(key, i)
            i+=1
            if versionNum < float(subkey):
                versionNum = float(subkey)
        except: #relies on error handling WindowsError as e as well as type conversion when we run out of numbers
            break
    return versionNum'''
'''
def getMicrosofAccessVersion():
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Microsoft\\Office", 0, winreg.KEY_READ)
    versionNum = 0
    i = 0
    while True:
        try:
            subkey = winreg.EnumKey(key, i)
            i+=1
            if versionNum < float(subkey):
                versionNum = float(subkey)
        except: #relies on error handling WindowsError as e as well as type conversion when we run out of numbers
            break
    return versionNum
print(getMicrosofAccessVersion())'''


'''from win32com.client.dynamic import Dispatch

access = Dispatch("MicrosoftAccess.Application")
print (access)
access_version = access.version
print (access_version)'''

import win32com.client

'''xl = win32com.client.Dispatch("access.Application")
access_version = xl.version
print(access_version)


if access_version <= "16.0":
    print("number")
else:
    print("string")
#end if'''
print(win32com.client.Dispatch("access.Application").version)
