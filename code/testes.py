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
#print(win32com.client.Dispatch("access.Application").version)

'''def is_64bit_elf(filename):
    with open(filename, "rb") as f:
        return f.read(5)[-1] == 2

print(is_64bit_elf(r"C:\Program Files\obs-studio\bin\64bit\obs64.exe"))
'''
'''from win32com.client import Dispatch

ver_parser = Dispatch('Scripting.FileSystemObject')
info = ver_parser.GetFileVersion(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE")
print(ver_parser.GetFileVersion(r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE"))
if info == 'No Version Information Available':
    info = None

print(info)'''

import win32api

#==============================================================================
'''def getFileProperties(fname):
#==============================================================================
    """
    Read all properties of the given file return them as a dictionary.
    """
    propNames = ('Comments', 'InternalName', 'ProductName',
        'CompanyName', 'LegalCopyright', 'ProductVersion',
        'FileDescription', 'LegalTrademarks', 'PrivateBuild',
        'FileVersion', 'OriginalFilename', 'SpecialBuild')

    props = {'FixedFileInfo': None, 'StringFileInfo': None, 'FileVersion': None}

    try:
        # backslash as parm returns dictionary of numeric info corresponding to VS_FIXEDFILEINFO struc
        fixedInfo = win32api.GetFileVersionInfo(fname, '\\')
        props['FixedFileInfo'] = fixedInfo
        props['FileVersion'] = "%d.%d.%d.%d" % (fixedInfo['FileVersionMS'] / 65536,
                fixedInfo['FileVersionMS'] % 65536, fixedInfo['FileVersionLS'] / 65536,
                fixedInfo['FileVersionLS'] % 65536)

        # \VarFileInfo\Translation returns list of available (language, codepage)
        # pairs that can be used to retreive string info. We are using only the first pair.
        lang, codepage = win32api.GetFileVersionInfo(fname, '\\VarFileInfo\\Translation')[0]

        # any other must be of the form \StringfileInfo\%04X%04X\parm_name, middle
        # two are language/codepage pair returned from above

        strInfo = {}
        for propName in propNames:
            strInfoPath = u'\\StringFileInfo\\%04X%04X\\%s' % (lang, codepage, propName)
            ## print str_info
            strInfo[propName] = win32api.GetFileVersionInfo(fname, strInfoPath)

        props['StringFileInfo'] = strInfo
    except:
        pass

    return props 


print(getFileProperties("C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe"))'''



'''from win32api import GetFileVersionInfo, LOWORD, HIWORD
def get_version_number(filename):
    try:
        info = GetFileVersionInfo (filename, "\\")
        ms = info['FileVersionMS']
        ls = info['FileVersionLS']
        return HIWORD (ms), LOWORD (ms), HIWORD (ls), LOWORD (ls)
    except:
        return "Unknown version"
if __name__ == "__main__":
    version = ".".join([str (i) for i in get_version_number (r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE')])
    print(version)

print(get_version_number(r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE'))'''

'return f.read(5)[-1] == 2'

'''def is_64bit_elf(filename):
    with open(filename, "rb") as f:
        return f.read(5)[-1]


print(is_64bit_elf(r'C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE'))   '''

def is_64bit_pe(filename):
    import win32file
    return win32file.GetBinaryType(filename) == 6


print(is_64bit_pe(r'C:\Program Files\Microsoft Office\root\Office16\MSACCESS.EXE')) #  64 bits
print(is_64bit_pe(r"C:\Program Files (x86)\Notepad++\notepad++.exe") ) ## 32 bits


if is_64bit_pe(r'C:\Program Files\Microsoft Office\root\Office16\MSACCESS.EXE') == False:
    print("e 32 bits parca")
else:
    print("e 64 bro")