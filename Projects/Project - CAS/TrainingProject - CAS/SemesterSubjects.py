import tkinter as tk
from tkinter.ttk import Combobox, Treeview
from datalayer import DBSessions, DBCourse, DBSubjects, DBSemesterSubjects
from components import SemesterSubjects

class SemesterSubjectsForm:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.geometry("625x330")
        
        self.lbl1 = tk.Label(self.root, text = "Session")
        self.lbl1.place(x = 10 , y =10)
        self.cmb1 = Combobox(self.root, state = "readonly")
        self.cmb1.place(x = 70, y = 10)
        dbsessions = DBSessions()
        self.AllSessions = dbsessions.GetSession()
        SessionList = []
        for sess in self.AllSessions:
            SessionList.append(sess.Session)
        self.cmb1['values'] = SessionList
        
        self.lbl2 = tk.Label(self.root, text = "Semester")
        self.lbl2.place(x = 270 , y =10)
        self.cmb2 = Combobox(self.root, state = "readonly")
        self.cmb2.place(x = 330, y = 10)
        self.cmb2['values'] = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th']
        
        self.lbl3 = tk.Label(self.root, text = "Course")
        self.lbl3.place(x = 10 , y =40)
        self.cmb3 = Combobox(self.root, state = "readonly")
        self.cmb3.place(x = 70, y = 40)
        dbcourses = DBCourse()
        self.AllCourses = dbcourses.GetCourse()
        CourseList = []
        for cour in self.AllCourses:
            CourseList.append(cour.CourseName)
        self.cmb3['values'] = CourseList
        
        self.lbl4 = tk.Label(self.root, text = "Subject")
        self.lbl4.place(x = 270 , y =40)
        self.cmb4 = Combobox(self.root, state = "readonly")
        self.cmb4.place(x = 330, y = 40)
        dbsubjects = DBSubjects()
        self.AllSubjects = dbsubjects.GetSubjects()
        SubjectList = []    
        for sub in self.AllSubjects:
            SubjectList.append(sub.Subject)
        self.cmb4['values'] = SubjectList
        
        self.AddButton = tk.Button(self.root, text = "Show" , width = 12, command = self.ShowClicked)
        self.AddButton.place(x = 520, y = 10)
        
        self.AddButton = tk.Button(self.root, text = "Add" , width = 12, command = self.AddClicked)
        self.AddButton.place(x = 520, y = 40)
        
        self.Tree = Treeview(self.root)
        self.Tree.place(x = 10, y = 90)
        self.Tree['columns'] = ['c1','c2']
        self.Tree.heading("#0", text = "SemesterSubjectId")
        self.Tree.heading("c1",text = "Semester")
        self.Tree.heading("c2",text = "Subject")
    
    def ShowClicked(self):
        self.Tree.delete(*self.Tree.get_children())
        sessid = self.AllSessions[self.cmb1.current()].SessionId
        cid = self.AllCourses[self.cmb3.current()].CourseId
        subid = self.AllSubjects[self.cmb4.current()].SubjectId
        ss = SemesterSubjects()
        ss.SessionId = sessid
        ss.CourseId  = cid
        ss.SubjectId = subid
        ss.Semester = self.cmb2.get()
        
        db = DBSemesterSubjects()
        AllSemesterSubjects = db.Getdata(ss)
        
        i = 0
        for allss in AllSemesterSubjects:
            self.Tree.insert("",i,text = allss.SemesterSubjectId, values = (allss.Semester, allss.SubjectId))
            i += 1
            
    def AddClicked(self):
        sessid = self.AllSessions[self.cmb1.current()].SessionId
        cid = self.AllCourses[self.cmb3.current()].CourseId
        subid = self.AllSubjects[self.cmb4.current()].SubjectId
        ss = SemesterSubjects()
        ss.SessionId = sessid
        ss.CourseId  = cid
        ss.SubjectId = subid
        ss.Semester = self.cmb2.get()
        
        db = DBSemesterSubjects()
        db.StoreValues(ss)
        
        self.Tree.delete(*self.Tree.get_children())
        AllSemesterSubjects = db.Getdata(ss)
        
        i = 0
        for allss in AllSemesterSubjects:
            self.Tree.insert("", i, text = allss.SemesterSubjectId, values = (allss.Semester, allss.SubjectId))
            i += 1
        
    def showDialog(self):
        self.root.mainloop()