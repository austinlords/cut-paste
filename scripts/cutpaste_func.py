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
from tkinter import messagebox, filedialog
import os
import shutil
import sqlite3
import datetime

import cutpaste_gui
import cutpaste_main


# Center module on screen
def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

# Dialog to exit program
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        self.master.destroy()
        os._exit(0)

# Dialog to select source directory on User computer
def browse1(self):
    abspath = filedialog.askdirectory()
    paste_path1(self, abspath)

# Paste selected source directory to text field in GUI
def paste_path1(self, path):
    self.txt_browse1.delete(0,END)
    self.txt_browse1.insert(0, path)

# Dialog to select destination directory on User computer
def browse2(self):
    abspath = filedialog.askdirectory()
    paste_path2(self, abspath)

# Paste selected destination directory to text field in GUI
def paste_path2(self, path):
    self.txt_browse2.delete(0,END)
    self.txt_browse2.insert(0,path)

# Create database and (1) table. Used to store cut/paste procedures
def create_database():
    conn = sqlite3.connect('DB_txtfiles.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS tbl_txtfiles (\
ID INTEGER PRIMARY KEY AUTOINCREMENT, \
File TEXT, \
LastModified TEXT, \
CutPasteTime, \
Source, \
Destination);')
    conn.commit()
    conn.close()

# Primary function of program.
# Looks for .txt files in Source Directory.
# Will prompt User to confirm cut/paste procedure 
def check_files(self):
    srcPath = self.txt_browse1.get()
    dstPath = self.txt_browse2.get()
    # Source & Destination Directories must not be empty
    if srcPath != '' and dstPath != '':
        # Try and Except(s) to make sure directories exist
        try:
            # Create a list of all files in source directory
            srcFiles = os.listdir(srcPath)
            try:
                # Create a list of all files in destination directory
                # (used for try...except only)
                dstFiles = os.listdir(dstPath)
                count = 0
                txtArray = []
                # Count number of .txt files in source directory
                for i in srcFiles:
                    if i.endswith('.txt'):
                        count += 1
                        txtArray.append(i)
                txtStr = '\n'.join(txtArray)
                if count == 0:
                    messagebox.showerror('NO FILES FOUND', 'No .txt files \
found in source directory')
                else:
                    if count > 5:
                        txtStr = '(too many files to show here)'
                    count = str(count)
                    # Ask User to confirm cut/paste procedure
                    if messagebox.askyesno('({}) files found'.format(count),
                                           'CUT ({}) .txt files from source \
directory and PASTE in destination directory?\n\n{}'.format(count,txtStr)):
                        for i in srcFiles:
                            if i.endswith('.txt'):
                                absPath = os.path.join(srcPath, i)
                                mTime = round(os.path.getmtime(absPath),0)
                                mTime = datetime.datetime.fromtimestamp(mTime)
                                print('File: {}...Modified: {}'.format(i,mTime))
                                cut_paste(self, absPath)
                                log_cut_paste(self, i, mTime)
                        messagebox.showinfo('Success', 'You have successfully \
moved {} .txt files!'.format(count))
                    else:
                        messagebox.askretrycancel('CANCELED','CUT and PASTE \
canceled. Please try again.')
                    
            except FileNotFoundError:
                messagebox.showwarning('DIRECTORY NOT FOUND',
                                       'Please select a valid destination \
directory')           
        except FileNotFoundError:
            messagebox.showwarning('DIRECTORY NOT FOUND',
                                   'Please select a valid source directory')
    else:
        messagebox.showerror('MISSING INFO',
                             'Source and destination directory is required')
            
# Cut file from Source Directory, paste in Destination Directory
# Can only handle one file at a time, given absPath of the file
def cut_paste(self, absPath):
    # Retrieve Destination Directory from text field in GUI
    dstPath = os.path.abspath(self.txt_browse2.get())
    shutil.move(absPath,dstPath)        
     
# Log cut_paste() information into SQLite3 database
def log_cut_paste(self, file, modifyDate):
    conn = sqlite3.connect('DB_txtfiles.db')
    c = conn.cursor()
    cTime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    srcPath = os.path.abspath(self.txt_browse1.get())
    dstPath = os.path.abspath(self.txt_browse2.get())
    c.execute('INSERT INTO tbl_txtfiles (File, LastModified, CutPasteTime, \
    Source, Destination) VALUES (?,?,?,?,?)',(file, modifyDate,cTime,srcPath,
                                              dstPath))
    conn.commit()
    conn.close()




if __name__ == '__main__':
    print('Please run this program from cutpaste_main.py')

