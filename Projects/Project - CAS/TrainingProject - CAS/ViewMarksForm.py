import tkinter as tk
from tkinter.ttk import Combobox
from datalayer import DBMarks
from functools import partial

class ViewMarksForm:
    def __init__(self,sem,regid,name,sessid,cid,Marks):
        self.root = tk.Toplevel()
        self.root.geometry("530x385")
        self.root.title("View Marks")
        self.y = 5
        self.rid = tk.StringVar()
        self.Name = tk.StringVar()
        
        self.lbl2 = tk.Label(self.root, text = "RegistrationId")
        self.lbl2.place(x = 10, y = 10)
        self.ent2 = tk.Entry(self.root, textvariable = self.rid, state = "readonly")
        self.ent2.place(x = 110, y = 10)
        self.rid.set(regid)
        
        self.lbl3 = tk.Label(self.root, text = "Name")
        self.lbl3.place(x = 250, y = 10)
        self.ent3 = tk.Entry(self.root, textvariable = self.Name, state = "readonly")
        self.ent3.place(x = 350, y = 10)
        self.Name.set(name)
        
        self.lbl1 = tk.Label(self.root, text = "Semester")
        self.lbl1.place(x = 10, y = 50)
        self.cmb = Combobox(self.root)
        self.cmb.place(x = 110, y = 50)
        self.cmb['values'] = ['1st','2nd','3rd','4th','5th','6th','7th','8th']
        
        self.ShowButton = tk.Button(self.root, text = "Show", command = partial(self.ShowClicked,sessid,cid,regid))
        self.ShowButton.place(x = 350, y = 50)
        
        self.frame = tk.Frame(self.root, width = 400, height = 400)
        self.frame.place(x = 105, y = 100)
        
        self.GetMarks(sessid,cid,sem,Marks)
        omarks = 0
        for mark in Marks:
            omarks += mark
            
        if Marks != []:
            obt = tk.Label(self.frame, text = "Obtained Marks")
            obt.place(x = 25, y = self.y + 20)
            obtlbl = tk.Label(self.frame, text = omarks).place(x = 125, y = self.y + 20)
            
            total = tk.Label(self.frame, text = "Total Marks")
            total.place(x = 25, y = self.y + 50)
            totallbl = tk.Label(self.frame, text = len(Marks)*100).place(x = 125, y = self.y + 50)
            
            per = tk.Label(self.frame, text = "Percentage")
            per.place(x = 25, y = self.y + 80)
            perlbl = tk.Label(self.frame, text = (omarks/len(Marks))).place(x = 125, y = self.y + 80)
            
    def ShowClicked(self,sessid,cid,regid):
        self.y = 5
        self.frame.destroy()
        self.frame = tk.Frame(self.root, width = 400, height = 400)
        self.frame.place(x = 105, y = 100)
        sem = self.cmb.get()
        db = DBMarks()
        Marks = db.CheckMarks(regid,sem)
        self.GetMarks(sessid,cid,sem,Marks)
        
        if Marks != []:
            omarks = 0
            for mark in Marks:
                omarks += mark
            obt = tk.Label(self.frame, text = "Obtained Marks")
            obt.place(x = 25, y = self.y + 20)
            obtlbl = tk.Label(self.frame, text = omarks).place(x = 125, y = self.y + 20)
            
            total = tk.Label(self.frame, text = "Total Marks")
            total.place(x = 25, y = self.y + 50)
            totallbl = tk.Label(self.frame, text = len(Marks)*100).place(x = 125, y = self.y + 50)
            
            per = tk.Label(self.frame, text = "Percentage")
            per.place(x = 25, y = self.y + 80)
            perlbl = tk.Label(self.frame, text = (omarks/len(Marks))).place(x = 125, y = self.y + 80)
            
    def GetMarks(self,sessid,cid,sem,Marks):
        db = DBMarks()
        self.AllSubjects = db.GetSubjects(sessid,cid,sem)
        self.MarksList = []
       
        if Marks == []:
            Marks = ["NULL"] * len(self.AllSubjects)
            
        for a,m in zip(self.AllSubjects,Marks):
            listvar = tk.StringVar()
            self.MarksList.append((listvar,a.SemesterSubjectId))
            lbl = tk.Label(self.frame, text = a.Subject)
            lbl.place(x = 5, y = self.y)
            ent = tk.Entry(self.frame, textvariable = listvar, state = "readonly")
            ent.place(x = 95, y = self.y)
            self.y += 40
            listvar.set(m)
            
        
    def showDialog(self):

        self.root.mainloop()