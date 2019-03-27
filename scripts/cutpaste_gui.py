##
##Python Ver:     3.7.2
##
##Author:         Austin Lords
##
##Purpose:        Cut all .txt files from a source directory and paste in
##                a destination directory. The Tech Academy Tkinter project.
##
##Tested OS:      Written and tested in Windows 10


from tkinter import *

import cutpaste_func
import cutpaste_main

def load_gui(self):
    # Lables for text fields (directory paths)
    self.lbl_browse1 = Label(self.master,text='Please select source directory')
    self.lbl_browse1.grid(row=0, column=1, padx=(20,20), pady=(20,5),
                          ipadx=(10), sticky=NW)
    self.lbl_browse2 = Label(self.master,text='Please select destination \
directory')
    self.lbl_browse2.grid(row=2, column=1, padx=(20,20), pady=(20,5),
                          ipadx=(10), sticky=NW)  
    
    # Browse... text fields (directory paths)
    self.txt_browse1 = Entry(self.master,text='',width=100)
    self.txt_browse1.grid(row=1,column=1,padx=(30,20),pady=(0,0),sticky=NE)
    self.txt_browse2 = Entry(self.master,text='', width=100)
    self.txt_browse2.grid(row=3,column=1,padx=(30,20),pady=(0,0),sticky=NE)

    # Browse... Buttons
    self.btn_browse1 = Button(self.master,width=12,height=1,text='Browse...',
                              command=lambda:cutpaste_func.browse1(self))
    self.btn_browse1.grid(row=1,column=0,padx=(20,0),pady=(0,0),sticky=NW)
    self.btn_browse2 = Button(self.master,width=12,height=1,text='Browse...',
                              command=lambda:cutpaste_func.browse2(self))
    self.btn_browse2.grid(row=3,column=0,padx=(20,0),pady=(0,0),sticky=NW)


    # Check for .txt files... Button
    self.btn_checkfiles = Button(self.master,width=12,height=2,text='Check \
for .txt files...',wraplength=100,command=lambda:cutpaste_func.check_files(self))
    self.btn_checkfiles.grid(row=4,column=0,padx=(20,0),pady=(30,20),sticky=NW)

    # Close Button
    self.btn_close = Button(self.master,width=12,height=2,text='Close \
Program', command=lambda: cutpaste_func.ask_quit(self))
    self.btn_close.grid(row=4,column=1,padx=(30,20),pady=(30,20),sticky=NE)


if __name__ == '__main__':
    print('Please run this program from cutpaste_main.py')
