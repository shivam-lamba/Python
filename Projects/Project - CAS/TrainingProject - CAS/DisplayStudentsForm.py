import tkinter as tk
from tkinter.ttk import Combobox, Treeview
from datalayer import DBSessions, DBCourse, DBStudents, DBMarks
from MarksForm import MarksForm
from UpdateMarksForms import UpdateMarksForm
from ViewMarksForm import ViewMarksForm

class DisplayStudentForm:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.geometry("855x350")
        self.root.title("Marks")
        
        self.lbl1 = tk.Label(self.root, text = "Session")
        self.lbl1.place(x = 10 , y = 10)
        self.cmb1 = Combobox(self.root, state = "readonly")
        self.cmb1.place(x = 70, y = 10)
        dbsessions = DBSessions()
        self.AllSessions = dbsessions.GetSession()
        SessionList = []
        for sess in self.AllSessions:
            SessionList.append(sess.Session)
        self.cmb1['values'] = SessionList
        
        self.lbl2 = tk.Label(self.root, text = "Course")
        self.lbl2.place(x = 250 , y =10)
        self.cmb2 = Combobox(self.root, state = "readonly")
        self.cmb2.place(x = 310, y = 10)
        dbcourses = DBCourse()
        self.AllCourses = dbcourses.GetCourse()
        CourseList = []
        for cour in self.AllCourses:
            CourseList.append(cour.CourseName)
        self.cmb2['values'] = CourseList
        
        self.lbl3 = tk.Label(self.root, text = "Semester")
        self.lbl3.place(x = 490 , y =10)
        self.cmb3 = Combobox(self.root, state = "readonly")
        self.cmb3.place(x = 560, y = 10)
        self.cmb3['values'] = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th']
        
        self.ShowButton = tk.Button(self.root, text = "Show", command = self.ShowClicked, width = 12)
        self.ShowButton.place(x = 750, y = 10)
        
        self.Tree = Treeview(self.root)
        self.Tree.place(x = 10, y = 70)
        self.Tree['columns'] = ['c1','c2','c3','c4','c5']
        self.Tree.heading("#0", text = "RegId")
        self.Tree.heading("c1",text = "Name")
        self.Tree.heading("c2",text = "Roll No.")
        self.Tree.heading("c3",text = "DOB")
        self.Tree.heading("c4",text = "Gender")
        self.Tree.heading("c5",text = "Contact No.")
        
        self.Tree.column("#0", width = 50)
        self.Tree.column("c2", width = 130)
        self.Tree.column("c3", width = 130)
        self.Tree.column("c4", width = 120)
        
        self.MarksButton = tk.Button(self.root, text = "Marks", command = self.MarksClicked, width = 12)
        self.MarksButton.place(x = 300, y = 310)
        
        self.ViewMarksButton = tk.Button(self.root, text = "View Marks", command = self.ViewMarksClicked, width = 12)
        self.ViewMarksButton.place(x = 460, y = 310)
        
    def ShowClicked(self):
        sessid = self.AllSessions[self.cmb1.current()].SessionId
        cid = self.AllCourses[self.cmb2.current()].CourseId
        sem = self.cmb3.get()
        
        db = DBStudents()
        AllDetails = db.FindStudent(sessid,cid,sem)
        
        i = 0
        for ad in AllDetails:
            self.Tree.insert("",i,text = ad.RegistrationId, values = (ad.Name, ad.RollNo, ad.Dob, ad.Gender, ad.ContactNo))
            i += 1
    
    def MarksClicked(self):
        key = self.Tree.focus()
        regid = int(self.Tree.item(key,"text"))
        name = self.Tree.item(key,"values")[0]
        
        sessid = self.AllSessions[self.cmb1.current()].SessionId
        cid = self.AllCourses[self.cmb2.current()].CourseId
        sem = self.cmb3.get()
    
        db = DBMarks()
        MarksList = db.CheckMarks(regid,sem)
        
        if MarksList != []:
            obj = UpdateMarksForm(regid,sessid,cid,sem,name, MarksList)
            obj.showDialog()
            
        else:
            obj = MarksForm(regid,sessid,cid,sem,name)
            obj.showDialog()
    
    def ViewMarksClicked(self):
        key = self.Tree.focus()
        regid = int(self.Tree.item(key,"text"))
        name = self.Tree.item(key,"values")[0]
        
        sessid = self.AllSessions[self.cmb1.current()].SessionId
        cid = self.AllCourses[self.cmb2.current()].CourseId
        sem = self.cmb3.get()
        
        db = DBMarks()
        MarksList = db.CheckMarks(regid,sem)
        
        obj = ViewMarksForm(sem,regid,name,sessid,cid,MarksList)
        obj.showDialog()
        
    def showDialog(self):
        self.root.mainloop()