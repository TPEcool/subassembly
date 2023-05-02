import os
import webbrowser as web
import tkinter.messagebox as msg
import sys
from playsound import playsound as snd

global acc
global dat

dat = 'This is a general-purpose register to use for whatever you want. This register is independent of ACC.'
acc = 'This is a general-purpose and mathematical register. When performing mathematical operations, the first parameter will be ACC and the result will also be saved to ACC.'

lic = '''
Copyright (c) 2023 electrovoyage.#9148

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

version = '1.0'

def help_():
    web.open('https://docs.google.com/document/d/1wrAH8cXmieUfTHcIkoJr7vji-Fu_-S30l_8m7yNnLGk/edit?usp=sharing')

def info():
    print('--- SUBASSEMBLY ---\r\nVersion '+version+'\r\nby electrovoyage.#9148'+('\r\nNot for production use' if ('Development' in version) else ''))
    print('Type "help" to open the help page, "info" to see this screen again or "license" to see the official license.\r\n')

inf = 'Subassembly is a tool that allows you to execute basic Assembly programs in the command prompt. Developed by electrovoyage.#9148 in May of 2023.'

print('--- SUBASSEMBLY ---')
print('Subassembly v.'+version+' \r\nBy electrovoyage.#9148.\r\nMade in 2023\r\n'+('\r\nNot for production use' if 'Development' in version else ''))
print('Type "help" to open the help page, "info" to see this screen again or "license" to see the official license.\n')

commands = ' quit q exit ! ex  help ?  info inf  about @  license lic © (c) (C)  return <- << -> >> back echo  mov ] --  add sub div mul idiv pow  show  apd  psd  mde'
helps = {
    'quit': 'Close the application.',
    'q': 'Close the application.',
    'exit': 'Close the application.',
    '!': 'Close the application.',
    'ex': 'Close the application.',

    'help': 'Gives help on a specific topic or lists the commands, depending on the parameters given.',
    '?': 'Gives help on a specific topic or lists the commands, depending on the parameters given.',

    'info': 'Prints information about the current version of Subassembly.',
    'inf': 'Prints information about the current version of Subassembly.',

    'about': 'Prints general information about Subassembly.',
    '@': 'Prints general information about Subassembly.',

    'add': 'Add acc to an operand and save result in acc.',
    'sub': 'Subtract an operand from acc and save result in acc.',
    'div': 'Divide acc by an operand and save result to acc.',
    'mul': 'Multiply acc by an operand and save result to acc.',
    'idiv': 'Integer division. Divides acc by an operand, removes everything after the point and saves result to acc.',
    'pow': 'Calculate the power of acc^operand, and save result to acc.',
    'mod': 'Divide acc by an operand and save remainder to acc.',

    'show':'Display a messagebox to the user. Accepts three operands: type (info/warn/error), title and text.',

    'mde':'Set interpretation mode. Use operand "set" to enable separation with | characters, "default" to enable separation with spaces. This is useful for making multi-word strings.',

    'apd':'Append an operand to ACC and save result there.',

    'psd':'Play a sound from the "resource/sound/" folder. For filenames with spaces, first use the "mde sep" mode and then type "psd|[filename]".'
}
cmds = commands.split(' ')

compare1 = ''
compare2 = ''

os.makedirs(os.getcwd()+'/resource',exist_ok=True)
os.makedirs(os.getcwd()+'/resource/sound',exist_ok=True)

sep = ' '

def operandList():
    ind = 0
    out = []
    for i in act:
        if ind!=0:
            out.append(i)
        ind+=1
    return out

while True:
    command = input('subassembly.exe/')
    act = command.strip().split(sep)
    cmd = act[0]
    if cmd == 'quit' or cmd == 'q' or cmd == 'exit' or cmd == '!' or cmd == 'ex':
        print('Thank you for using Subassembly '+version+'!')
        confirm = input('Are you sure you want to close Subassembly? (Y/N)')
        if confirm == 'y' or confirm == 'Y':
            break
        else:
            print('Subassembly quit command cancelled')
            info()
    elif cmd == 'help' or cmd == '?':
        if len(act)>1:
            if act[1]=='commands':
                for i in cmds:
                    print(i)
            else:
                for i in cmds:
                    if act[1]==i:
                        print(helps[act[1]])
        else:
             help_()
    elif cmd == 'info' or cmd == 'inf':
        info()
    elif cmd=='about' or cmd == '@':
        print(inf)
    elif cmd == 'license' or cmd == 'lic' or cmd == '©' or cmd == '(c)' or cmd == '(C)':
        print(lic)
    elif cmd  == 'return' or cmd =='<-' or cmd == '<<' or cmd == '->' or cmd == '>>' or cmd == 'back' or cmd == 'echo':
        if len(act) < 2:
            print('Error in '+cmd+' statement: no value provided!')
        else:
            print('')
            for i in operandList():
                if i == 'dat':
                 print(dat)
                elif i == 'acc':
                    print(acc)
                else:
                 print(i)
                print('')
    elif cmd == 'mov' or cmd == ']' or cmd == '<>' or cmd == '--':
        if len(act)==3:
            if act[1]=='acc':
                if act[2]=='acc':
                    acc = acc
                    print('Warning: acc set to itself!')
                elif act[2] == 'dat':
                    dat = acc
                else:
                    print('Unable to execute '+cmd+' statement: operand 2 must be of type Register!')
            elif act[1]=='dat':
                if act[2]=='dat':
                    dat = dat
                    print('Warning: dat set to itself!')
                elif act[2] == 'acc':
                    acc = dat
                else:
                    print('Unable to execute '+cmd+' statement: operand 2 must be of type Register!')
            else:
                if act[2]=='acc':
                    acc=act[1]
                elif act[2]=='dat':
                    dat=act[1]
                else:
                    print('Unable to execute '+cmd+' statement: operand 2 must be of type Register!')
        else:
            print('Unable to execute '+cmd+' statement: too '+('few' if len(act)<3 else 'many')+' operands provided!')
    elif cmd == 'add':
        if len(act)!=2:
            print('Unable to execute add statement: too '+('few' if len(act)<3 else 'many')+' operands provided!')
        else:
            try:
                acc = float(acc)+float(act[1])
            except ArithmeticError:
                print('Critical runtime exception: number division failed: number overflow!')
            except:
                print('Critical runtime exception: number addition failed: failed to convert either value to float!')
    elif cmd == 'sub':
        if len(act)!=2:
            print('Unable to execute sub statement: too '+('few' if len(act)<3 else 'many')+' operands provided!')
        else:
            try:
                acc = float(acc)-float(act[1])
            except ArithmeticError:
                print('Critical runtime exception: number division failed: number overflow!')
            except:
                print('Critical runtime exception: number subtraction failed: failed to convert either value to float!')
    elif cmd == 'mul':
        if len(act)!=2:
            print('Unable to execute sub statement: too '+('few' if len(act)<3 else 'many')+' operands provided!')
        else:
            try:
                acc = float(acc)*float(act[1])
            except ArithmeticError:
                print('Critical runtime exception: number division failed: number overflow!')
            except:
                print('Critical runtime exception: number multiplication failed: failed to convert either value to float!')
    elif cmd == 'div':
        if len(act)!=2:
            print('Unable to execute sub statement: too '+('few' if len(act)<3 else 'many')+' operands provided!')
        else:
            try:
                acc = float(acc)/float(act[1])
            except ArithmeticError:
                print('Critical runtime exception: number division failed: mathematical error! (divison by zero or overflow)')
            except:
                print('Critical runtime exception: number division failed: failed to convert either value to float!')
    elif cmd == 'pow':
        if len(act)!=2:
            print('Unable to execute sub statement: too '+('few' if len(act)<3 else 'many')+' operands provided!')
        else:
            try:
                acc = float(acc)**float(act[1])
            except ArithmeticError:
                print('Critical runtime exception: number division failed: number overflow!')
            except:
                print('Critical runtime exception: number power calculation failed: failed to convert either value to float!')
    elif cmd == 'idiv':
        if len(act)!=2:
            print('Unable to execute sub statement: too '+('few' if len(act)<3 else 'many')+' operands provided!')
        else:
            try:
                acc = float(acc)//float(act[1])
            except ArithmeticError:
                print('Critical runtime exception: number division failed: number overflow or division by zero!')
            except:
                print('Critical runtime exception: number power calculation failed: failed to convert either value to float!')
    elif cmd == 'show':
        if len(act)!=4:
            print('Unable to execute show statement: wrong number of operands!')
        else:
            match act[1]:
                case 'info':
                    msg.showinfo(title = act[2],message = act[3])
                case 'warn':
                    msg.showwarning(title = act[2],message = act[3])
                case 'error':
                    msg.showerror(title = act[2],message = act[3])
                case _:
                    print('Error in show statement: failed to match window type!')
    elif cmd == 'apd':
        if len(act)!=2:
            print('Unable to execute append statement: wrong number of operands provided!')
        else:
            acc = str(acc)+act[1]
    elif cmd == 'mde':
        if len(act)!=2:
            print('Unable to execute mode command: wrong number of operands!')
        else:
            if act[1] == 'default' or act[1] == 'def':
                sep = ' '
            else:
                sep = '|'
    elif cmd == 'mod':
        if len(act)!=2:
            print('Unable to execute modulo statement: wrong number of operands!')
        else:
            try:
                acc = float(acc)%float(act[1])
            except ArithmeticError:
                print('Critical runtime exception: module statement failed: division by zero or number overflow!')
            except:
                print('Unable to execute modulo statement: failed to convert either value to float!')
    elif cmd=='psd':
        if len(act)!=2:
            print('Unable to execute psd statement: wrong argument count!')
        else:
            try:
                snd(os.getcwd()+'/resource/sound/'+act[1])
            except:
                print('Failed to load audio file!')
    else:
            print("Error in '"+cmd+"' statement: unable to interpret statement due to unknown command! Please enter 'help commands' to list all available commands or 'help [command]' to get help on a specific command.")

print('Quitting Subassembly...')
sys.exit()