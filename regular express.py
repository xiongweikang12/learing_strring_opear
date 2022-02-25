import re
import pyperclip
import tkinter
from tkinter import messagebox

# TODO 用正则表达式查找，匹配文本（不同模式）
# re.DOTALL
# re.VERBOSE

# TODO 项目：电话号码和邮箱地址的提取程序

# Create phone regex

phoneRexgex = re.compile(r'''((\d{3}|\(\d{3}\))?
                           (\s|-|\.)?
                           (\d{3})
                           (\s|-|\.)
                           (\d{4})
                           (\s*(ext|x|ext.)\s*(\d{2,6}))?)

                            ''', re.VERBOSE)  # 表示可以有注释

# Create email regax

emailRexgex = re.compile(r'''([a-zA-Z0-9.%+-]+)
                           @
                           ([a-zA-Z0-9.-]+)
                           (\.[a-zA-Z0-9]{2,4})

                            ''', re.VERBOSE)

# Find matches inclipboard text
text = str(pyperclip.paste())
window=tkinter.Tk()
window.title('从粘贴板得到电话或邮箱')
window.geometry('200x200')


def get_phonenumber():
    matches_1=[]
    for groups in phoneRexgex.findall(text):
        phonenumber = '-'.join(groups[1], groups[3], groups[5])
        if grounp[8] != '':
            phonenumber += 'x' + groups[8]
        matches_1.append(phonenumber)

    if len(matches_1)!=0:
        pyperclip.copy('\n'.join(matches_1))
        print('copied to clipboard')
        print('\n'.join(matches_1))
    else:
        print('no find out phonenumber')



def get_email():
    matches_2=[]
    for groups in emailRexgex.findall(text):
        matches_2.append(groups[0]+'@'+groups[1]+groups[2])#str(groups[0])+str(groups[1])
    if len(matches_2) != 0:
        pyperclip.copy('\n'.join(matches_2))
        print('copied to clipboard')
        print('\n'.join(matches_2))
    else:
        print('no find out phonenumber')

def judge():
    if len(text)==0:
        messagebox.showerror(title='judge',message='there is not any thing in clipboard')
    else:
        messagebox.showinfo(title='judge',message='no problem and continue')


#copy result to clipboard
tkinter.Button(window,text='get_phonenumber',command=get_phonenumber,height=2,width=15).pack()
tkinter.Button(window,text='get_email',command=get_email,height=2,width=15).pack()
tkinter.Button(window,text='judge',command=judge,height=2,width=15).pack()
tkinter.Button(window,text='quit',command=quit,height=2,width=15).pack()

if __name__=='__main__':
    window.mainloop()





