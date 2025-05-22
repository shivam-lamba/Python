import tkinter as tk
from components import Session
from datalayer import DBSessions
from tkinter import messagebox

class AddSession:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.grab_set()
        self.root.geometry("240x80")
        self.root.title("Session")
        self.session = tk.StringVar()
        
        self.lbl = tk.Label(self.root, text= "Enter Session")
        self.lbl.place(x = 10, y = 10)
        self.ent = tk.Entry(self.root, textvariable = self.session)
        self.ent.place(x = 100, y = 10)
        
        self.btn = tk.Button(self.root, text = "Add", command = self.addButton, width = 12)
        self.btn.place(x = 70, y = 40)
        
    def addButton(self):
        s = Session()
        s.Session = self.session.get()
        db = DBSessions()
        db.AddSession(s)
        messagebox.showinfo("Add Session", "Session was added successfully.")
        
    def showDialog(self):
        self.root.mainloop()