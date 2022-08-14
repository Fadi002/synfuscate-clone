'''
MIT License

Copyright (c) 2022 Fadi1337

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
import os
if os.name == 'nt':os.system('title synfuscate - synfuscate obfuscator')
from time import sleep
banner = '''███████╗██╗   ██╗███╗   ██╗███████╗██╗   ██╗███████╗ ██████╗ █████╗ ████████╗███████╗    
██╔════╝╚██╗ ██╔╝████╗  ██║██╔════╝██║   ██║██╔════╝██╔════╝██╔══██╗╚══██╔══╝██╔════╝    
███████╗ ╚████╔╝ ██╔██╗ ██║█████╗  ██║   ██║███████╗██║     ███████║   ██║   █████╗      
╚════██║  ╚██╔╝  ██║╚██╗██║██╔══╝  ██║   ██║╚════██║██║     ██╔══██║   ██║   ██╔══╝      
███████║   ██║   ██║ ╚████║██║     ╚██████╔╝███████║╚██████╗██║  ██║   ██║   ███████╗    
╚══════╝   ╚═╝   ╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚══════╝ ╚═════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝    
> Recreated by fadi 
> github : https://github.com/Fadi002'''
class TUI:
    def __init__(self):
        pass
    def fire(self,text):
        os.system(""); faded = ""
        green = 250
        for line in text.splitlines():
            faded += (f"\033[38;2;255;{green};0m{line}\033[0m\n")
            if not green == 0:
                green -= 25
                if green < 0:
                    green = 0
        return faded
    def banner(self):
        print(self.fire(banner))
    def fade_type(self,text):
        for c in text:
            print(c,end='',flush=True)
            sleep(0.009)
    def restart(self):
        dots = ['.','..','...','....']
        for i in dots:
            print(f'Restarting {i}',end='\r',flush=True)
            sleep(0.5)
    def exit_program(self):
        dots = ['.','..','...','....']
        for i in dots:
            print(f'exiting {i}',end='\r',flush=True)
            sleep(0.7)
        exit(-1)
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')