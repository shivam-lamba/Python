import tkinter as tk
from datalayer import DBCourse
from components import Course
from tkinter import messagebox

class AddCourse:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.grab_set()
        self.root.title("Add Course")
        
        self.CourseName = tk.StringVar()
        self.Description = tk.StringVar()
        
        self.root.geometry("245x115")
        
        self.lbl1 = tk.Label(self.root, text = "Course Name")
        self.lbl1.place(x = 10, y = 10)
        
        self.ent1 = tk.Entry(self.root, textvariable = self.CourseName)
        self.ent1.place(x = 110, y = 10)
        
        self.lbl3 = tk.Label(self.root, text="Description")
        self.lbl3.place(x = 10, y = 40)
        
        self.ent3 = tk.Entry(self.root, textvariable = self.Description)
        self.ent3.place(x = 110, y =40)
        
        self.btn1 = tk.Button(self.root, text = "Save", command = self.SaveClicked, width = 12)
        self.btn1.place(x = 70, y =80)
        
    def SaveClicked(self):
        p = Course()
        
        p.CourseName = self.CourseName.get()
        p.Description = self.Description.get()
        obj=DBCourse()
        obj.AddCourse(p)       
        messagebox.showinfo("Add Course", "Course was added successfully.")
     
    def showDialog(self):
        self.root.mainloop()
