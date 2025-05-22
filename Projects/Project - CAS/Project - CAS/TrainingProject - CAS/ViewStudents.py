import tkinter as tk
from tkinter.ttk import Combobox, Treeview
from datalayer import DBCourse, DBSessions, DBStudents

class ViewStudents:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.geometry("735x290")
        self.root.title("View Student")
            
        self.lbl1 = tk.Label(self.root, text = "Course")
        self.lbl1.place(x = 10 , y = 10)
        self.cmb1 = Combobox(self.root, state = "readonly")
        self.cmb1.place(x = 70, y = 10)
        
        dbcourse = DBCourse()
        self.AllCourses = dbcourse.GetCourse()
        CourseList = []
        for c in self.AllCourses:
            CourseList.append(c.CourseName)
        self.cmb1['values'] = CourseList
        
        self.lbl2 = tk.Label(self.root, text = "Session")
        self.lbl2.place(x = 310, y = 10)
        self.cmb2 = Combobox(self.root, state = "readonly")
        self.cmb2.place(x = 370, y = 10)
        
        dbsession = DBSessions()
        self.AllSessions = dbsession.GetSession()
        SessionList = []
        for s in self.AllSessions:
            SessionList.append(s.Session)
        self.cmb2['values'] = SessionList
        
        self.ShowButton = tk.Button(self.root, text = "Show", width = 15, command = self.ShowClicked)
        self.ShowButton.place(x = 610, y = 10)
        
        self.Tree = Treeview(self.root)
        self.Tree.place(x = 10, y = 50)
        self.Tree['columns'] = ("c1","c2","c3","c4","c5")
        self.Tree.heading("c1",text = "Name")
        self.Tree.heading("c2", text = "Roll Number")
        self.Tree.heading("c3", text = "Registration Date")
        self.Tree.heading("c4", text = "D.O.B")
        self.Tree.heading("c5", text = "Contact Number")
        
        self.Tree.column("#0", width = 50)
        self.Tree.column("c1", width = 180)
        self.Tree.column("c2", width = 100)
        self.Tree.column("c3", width = 100)
        self.Tree.column("c4", width = 100)
        self.Tree.column("c5", width = 180)
        
    def ShowClicked(self):
        cid = self.AllCourses[self.cmb1.current()].CourseId
        sid = self.AllSessions[self.cmb2.current()].SessionId
        db = DBStudents()
        StudentDetailsList = db.ViewStudents(cid,sid)
        i = 0
        for s in StudentDetailsList:
            self.Tree.insert("",i,text = s.RegistrationId, values=(s.Name,s.RollNo,s.RegistrationDate,s.Dob,s.ContactNo))
            i +=1
            
    def showDialog(self):
        self.root.mainloop()