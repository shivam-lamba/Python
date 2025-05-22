import tkinter as tk
from tkinter.ttk import Treeview
from tkinter import messagebox
from datalayer import DBSubjects
from components import Subject

class ViewSubjects:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.grab_set()
        self.root.title("View Subject")
        
        self.tree = Treeview(self.root)
        self.tree.pack()
        
        self.tree['columns'] = ("c1","c2")
        self.tree.heading("c1", text = "Course")
        self.tree.heading("c2", text = "Description")
        
        db = DBSubjects()
        AllSubjects = db.GetSubjects()
        
        i = 1
        
        for c in AllSubjects:
            self.tree.insert("",i,text = c.SubjectId, values=  (c.Subject, c.Description))
            i = i+1
       
        self.DeleteButton = tk.Button(self.root,text="Delete", command = self.DeleteClicked)
        self.DeleteButton.pack()
        
    def DeleteClicked(self):
        ret = messagebox.askyesno("Courses","Do you want to delete the subject?")
        if ret == True:
            key = self.tree.focus()
            sid = int(self.tree.item(key,"text"))
            c = Subject()
            db = DBSubjects()
            c.SubjectId = sid
            db.DeleteSubjects(c)
            self.tree.delete(key)
            
    def showDialog(self):
        self.root.mainloop()
        