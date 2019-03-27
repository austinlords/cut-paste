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
import sqlite3

import cutpaste_gui
import cutpaste_func

# Create main program window
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(775,250)

        cutpaste_func.center_window(self,775,250)
        self.master.title('Move .txt files from source directory to \
destination directory')
        self.master.configure(bg='#eee')
        self.master.protocol('WM_DELETE_WINDOW', lambda:
                             cutpaste_func.ask_quit(self))
        
        cutpaste_gui.load_gui(self)
        cutpaste_func.create_database()


if __name__ == '__main__':
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()

    
