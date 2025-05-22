import tkinter as tk
from tkinter.ttk import Combobox, Treeview
from datalayer import DBSessions, DBCourse, DBStudents, DBAttendance

class ViewAttendance:
    def __init__ (self):
        self.root=tk.Toplevel()
        self.root.geometry("1055x340")
        self.root.title("ViewAttendance")
        self.root.resizable("false","false")
        
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
        self.lbl2.place(x = 260 , y =10)
        self.cmb2 = Combobox(self.root, state = "readonly")
        self.cmb2.place(x = 330, y = 10)
        dbcourses = DBCourse()
        self.AllCourses = dbcourses.GetCourse()
        CourseList = []
        for cour in self.AllCourses:
            CourseList.append(cour.CourseName)
        self.cmb2['values'] = CourseList
        
        self.lbl3 = tk.Label(self.root, text = "Semester")
        self.lbl3.place(x = 540 , y = 10)
        self.cmb3 = Combobox(self.root, state = "readonly")
        self.cmb3.place(x = 620, y = 10)
        self.cmb3['values'] = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th']
        self.cmb3.bind("<<ComboboxSelected>>", self.SemesterChanged)
        
        
        self.lbl4 = tk.Label(self.root, text = "Month")
        self.lbl4.place(x = 820 , y = 10)
        self.cmb4 = Combobox(self.root, state = "readonly")
        self.cmb4.place(x = 900, y = 10)
        
        self.btn = tk.Button(self.root, text = "Show", command = self.ShowClicked, width = 12)
        self.btn.place(x = 350, y = 50)
        
        self.btn1 = tk.Button(self.root, text = "Exit", command = self.root.destroy, width = 12)
        self.btn1.place(x = 650, y = 50)
        
        self.Tree = Treeview(self.root)
        self.Tree.place(x = 10, y = 100, width = 1035)
        
    
    def SemesterChanged(self, event):
        semesterindex = self.cmb3.current()+1
        
        if semesterindex%2==0:
            self.cmb4['values']=["Aug","Sept","Oct","Nov","Dec"]
        else:
            self.cmb4['values']=["Jan","Feb","Mar","Apr","May"]
            
    def ShowClicked(self):
        self.Tree.column("#0",width=100)
        semesterindex = self.cmb3.current()+1

        month = 0
        
        if semesterindex%2==0:
            month = self.cmb4.current()+7
        else:
            month = self.cmb4.current()+1
        
        headings = []
        
        if month==2:
            for i in range(1,29):
                headings.append(str(i))

        elif month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
            for i in range(1,32):
                headings.append(str(i))
                
        else:
            for i in range(1,31):
                headings.append(str(i))
            
        
        self.Tree["columns"] =  headings           
        
        
        for heading in headings:
            self.Tree.heading(heading, text=heading)
        
        if len(headings) == 28:
            print("28")
            self.Set28Widths()
        elif len(headings) == 30:
            self.Set30Widths()
        else:
            self.Set31Widths()
        
        sid = self.AllSessions[self.cmb1.current()].SessionId
        cid = self.AllCourses[self.cmb2.current()].CourseId
        sem = self.cmb3.get()
        
        db = DBAttendance()
        records = db.GetAttendance(sem, cid ,sid)
        
        i = 0
        att = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','']
        
        
        regid =  records[0].RegistrationId
        Name = ""
        
        for record in records: 
            
            if record.RegistrationId==regid:
                att[record.Day-1] = record.Attendance
            else:
                self.Tree.insert("", i, text = Name , values= (att))
                att = ['','','','','','','','','','','','','','','','','','','','','','','','','','','','']
                att[record.Day-1] = record.Attendance

                regid=record.RegistrationId

            Name=record.Name
            
            i += 1
            
            if i==len(records):
                self.Tree.insert("", i, text = Name , values= (att))
    
    def Set31Widths(self):
        
        self.Tree.column("1",width=30)
        self.Tree.column("2",width=30)
        self.Tree.column("3",width=30)
        self.Tree.column("4",width=30)
        self.Tree.column("5",width=30)
        self.Tree.column("6",width=30)
        self.Tree.column("7",width=30)
        self.Tree.column("8",width=30)
        self.Tree.column("9",width=30)
        self.Tree.column("10",width=30)
        self.Tree.column("11",width=30)
        self.Tree.column("12",width=30)
        self.Tree.column("13",width=30)
        self.Tree.column("14",width=30)
        self.Tree.column("15",width=30)
        self.Tree.column("16",width=30)
        self.Tree.column("17",width=30)
        self.Tree.column("18",width=30)
        self.Tree.column("19",width=30)
        self.Tree.column("20",width=30)
        self.Tree.column("21",width=30)
        self.Tree.column("22",width=30)
        self.Tree.column("23",width=30)
        self.Tree.column("24",width=30)
        self.Tree.column("25",width=30)
        self.Tree.column("26",width=30)
        self.Tree.column("27",width=30)
        self.Tree.column("28",width=30)
        self.Tree.column("29",width=30)
        self.Tree.column("30",width=30)
        self.Tree.column("31",width=30)
        
    def Set30Widths(self):
        self.Tree.column("1",width=30)
        self.Tree.column("2",width=30)
        self.Tree.column("3",width=30)
        self.Tree.column("4",width=30)
        self.Tree.column("5",width=30)
        self.Tree.column("6",width=30)
        self.Tree.column("7",width=30)
        self.Tree.column("8",width=30)
        self.Tree.column("9",width=30)
        self.Tree.column("10",width=30)
        self.Tree.column("11",width=30)
        self.Tree.column("12",width=30)
        self.Tree.column("13",width=30)
        self.Tree.column("14",width=30)
        self.Tree.column("15",width=30)
        self.Tree.column("16",width=30)
        self.Tree.column("17",width=30)
        self.Tree.column("18",width=30)
        self.Tree.column("19",width=30)
        self.Tree.column("20",width=30)
        self.Tree.column("21",width=30)
        self.Tree.column("22",width=30)
        self.Tree.column("23",width=30)
        self.Tree.column("24",width=30)
        self.Tree.column("25",width=30)
        self.Tree.column("26",width=30)
        self.Tree.column("27",width=30)
        self.Tree.column("28",width=30)
        self.Tree.column("29",width=30)
        self.Tree.column("30",width=30)
        
    def Set28Widths(self):
        self.Tree.column("1",width=30)
        self.Tree.column("2",width=30)
        self.Tree.column("3",width=30)
        self.Tree.column("4",width=30)
        self.Tree.column("5",width=30)
        self.Tree.column("6",width=30)
        self.Tree.column("7",width=30)
        self.Tree.column("8",width=30)
        self.Tree.column("9",width=30)
        self.Tree.column("10",width=30)
        self.Tree.column("11",width=30)
        self.Tree.column("12",width=30)
        self.Tree.column("13",width=30)
        self.Tree.column("14",width=30)
        self.Tree.column("15",width=30)
        self.Tree.column("16",width=30)
        self.Tree.column("17",width=30)
        self.Tree.column("18",width=30)
        self.Tree.column("19",width=30)
        self.Tree.column("20",width=30)
        self.Tree.column("21",width=30)
        self.Tree.column("22",width=30)
        self.Tree.column("23",width=30)
        self.Tree.column("24",width=30)
        self.Tree.column("25",width=30)
        self.Tree.column("26",width=30)
        self.Tree.column("27",width=30)
        self.Tree.column("28",width=30)
    
    def showDialog(self):
        self.root.mainloop()