import tkinter
from tkinter import *


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width = False, height=False)
        self.master.geometry("425x200")
        self.master.title('Check Files')
        self.master.config(bg="#F9F7F6")

        self.varSearch1 = StringVar()
        self.varSearch2 = StringVar()


        self.btnSearch1 = Button(self.master,text="Browse...", width=15, height=1)
        self.btnSearch1.grid(row=0, column=0, padx=(10,0), pady=(50,0))

        self.btnSearch2 = Button(self.master,text="Browse...", width=15, height=1)
        self.btnSearch2.grid(row=1, column=0, padx=(10,0), pady=(10,0) )

        self.btnCheck = Button(self.master,text="Check for files...", width=15, height=2)
        self.btnCheck.grid(row=2, column=0, padx=(10,0), pady=(10,0))

        self.txtSearch1 = Entry(self.master,text=self.varSearch1, font=("Helvetica", 16), fg="black", bg="white")
        self.txtSearch1.grid(row=0, column=1, padx=(30,0), pady=(50,0))

        
        self.txtSearch2 = Entry(self.master,text=self.varSearch2, font=("Helvetica", 16), fg="black", bg="white")
        self.txtSearch2.grid(row=1, column=1, padx=(30,0), pady=(10,0))
        
        self.btnClose = Button(self.master, text="Close Program", width= 15, height = 2)
        self.btnClose.grid(row=2, column=1, padx=(0,0), pady=(10,0), sticky=E)


        
    

















if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()
