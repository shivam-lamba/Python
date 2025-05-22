import tkinter as tk
from datalayer import DBSubjects
from components import Subject
from tkinter import messagebox

class AddSubject:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.grab_set()
        
        self.SubjectName = tk.StringVar()
        self.Description = tk.StringVar()
        
        self.root.geometry("250x100")
        self.root.title("Add Subject")
        
        self.lbl1 = tk.Label(self.root, text = "Subject")
        self.lbl1.place(x = 10, y = 10)
        
        self.ent1 = tk.Entry(self.root, textvariable = self.SubjectName)
        self.ent1.place(x = 110, y = 10)
        
        self.lbl3 = tk.Label(self.root, text="Description")
        self.lbl3.place(x = 10, y = 40)
        
        self.ent3 = tk.Entry(self.root, textvariable = self.Description)
        self.ent3.place(x = 110, y =40)
        
        self.btn1 = tk.Button(self.root, text = "Save", command = self.SaveClicked, width = 12)
        self.btn1.place(x = 90, y =70)
        
    def SaveClicked(self):
        p = Subject()
        
        p.Subject = self.SubjectName.get()
        p.Description = self.Description.get()
        obj=DBSubjects()
        obj.AddSubject(p)       
        messagebox.showinfo("AddSubject","Subject has been Added successfully.")
        
    def showDialog(self):
        self.root.mainloop()