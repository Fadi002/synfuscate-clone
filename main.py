import os
from src import *
from src.codes import anti_debug
UI = TUI()
UI.clear()
def main():
    UI.banner()
    UI.fade_type('The only licence is Fadi1337 : ')
    licence = str(input())
    if licence != 'Fadi1337':
        UI.fade_type('Are you stupid ? I said the only fucking license that exists is Fadi1337\n')
        UI.restart()
        UI.clear()
        main()
    UI.clear()
    UI.banner()
    UI.fade_type('Enter file name to obfuscate : ')
    file = input()
    if os.path.exists(file):
        pass
    else:
        print('Files dose not exists')
    name = file.split('/')[-1]
    name = file.split('\\')[-1]
    name = name.split('.')[0]
    UI.fade_type('do you want anti debug ? [y/n] : ')
    anti_debugie = str(input())
    UI.fade_type('do you want anti decode ? [y/n] : ')
    anti_dedecodeie = str(input())
    if anti_debugie == 'Y' or anti_debugie == 'y':
        anti_debugie = True
    else:
        anti_debugie = False
    if anti_dedecodeie == 'Y' or anti_dedecodeie == 'y':
        anti_dedecodeie = True
    else:
        anti_dedecodeie = False
    file = open(file,'r',encoding='utf8').read()
    x=obff(file,antid=anti_debugie,antide=anti_dedecodeie)
    with open(name+'-syn.py','w',encoding='utf8') as f:
        f.write(x)
        f.close()
    UI.clear()
    UI.fade_type('Done !!!!!!!!\n')
    UI.exit_program()
        
while True:
    main()