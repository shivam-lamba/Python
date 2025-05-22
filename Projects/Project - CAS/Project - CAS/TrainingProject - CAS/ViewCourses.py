import tkinter as tk
from tkinter.ttk import Treeview
from tkinter import messagebox
from datalayer import DBCourse
from components import Course

class ViewCourses:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.grab_set()
        
        self.tree = Treeview(self.root)
        self.tree.pack()
        
        self.tree['columns'] = ("c1","c2")
        self.tree.heading("c1", text = "Course")
        self.tree.heading("c2", text = "Description")
        
        db = DBCourse()
        AllCourses = db.GetCourse()
        
        i = 1
        
        for c in AllCourses:
            self.tree.insert("",i,text = c.CourseId, values=  (c.CourseName, c.Description))
            i = i+1
       
        self.DeleteButton = tk.Button(self.root,text="Delete", command = self.DeleteClicked)
        self.DeleteButton.pack()
        
    def DeleteClicked(self):
        ret = messagebox.askyesno("Courses","Do you want to delete the course?")
        if ret == True:
            key = self.tree.focus()
            cid = int(self.tree.item(key,"text"))
            c = Course()
            db = DBCourse()
            c.CourseId = cid
            db.DeleteCourse(c)
            self.tree.delete(key)
        
    def showDialog(self):
        self.root.mainloop()
        