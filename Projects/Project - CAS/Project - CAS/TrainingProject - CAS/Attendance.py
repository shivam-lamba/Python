import tkinter as tk
from tkinter import Canvas, Scrollbar,messagebox
from tkinter.ttk import Combobox
from datalayer import DBSessions, DBCourse, DBStudents, DBAttendance

class Attendance:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.geometry("505x480")
        self.root.title("Marks")
        self.Date = tk.StringVar()
        
        self.topframe = tk.Frame(self.root, width = 505 , height = 120)
        self.lbl1 = tk.Label(self.topframe, text = "Session")
        self.lbl1.place(x = 10 , y = 10)
        self.cmb1 = Combobox(self.topframe, state = "readonly")
        self.cmb1.place(x = 70, y = 10)
        dbsessions = DBSessions()
        self.AllSessions = dbsessions.GetSession()
        SessionList = []
        for sess in self.AllSessions:
            SessionList.append(sess.Session)
        self.cmb1['values'] = SessionList
        
        self.lbl2 = tk.Label(self.topframe, text = "Course")
        self.lbl2.place(x = 290 , y =10)
        self.cmb2 = Combobox(self.topframe, state = "readonly")
        self.cmb2.place(x = 350, y = 10)
        dbcourses = DBCourse()
        self.AllCourses = dbcourses.GetCourse()
        CourseList = []
        for cour in self.AllCourses:
            CourseList.append(cour.CourseName)
        self.cmb2['values'] = CourseList
        
        self.lbl3 = tk.Label(self.topframe, text = "Semester")
        self.lbl3.place(x = 10 , y = 40)
        self.cmb3 = Combobox(self.topframe, state = "readonly")
        self.cmb3.place(x = 70, y = 40)
        self.cmb3['values'] = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th']
        
        self.lbl4 = tk.Label(self.topframe, text = "Date")
        self.lbl4.place(x = 290, y = 40)
        self.ent4 = tk.Entry(self.topframe, textvariable = self.Date, width = 23)
        self.ent4.place(x = 350, y = 40)
        self.errlbl = tk.Label(self.topframe, text = "", fg = "Gray")
        self.errlbl.place(x = 350, y = 60)
        
        self.ShowButton = tk.Button(self.topframe, text = "Show",command = self.ShowClicked, width = 12)
        self.ShowButton.place(x = 205, y = 80)
        
        self.topframe.pack(side = "top")
        
        self.myframe = tk.Frame(self.root, width = 400, height = 100, bd = 1)
        self.myframe.place(x = 10 , y = 140)
        self.scrollableframe()
        
        self.btn= tk.Button(self.root, text = "Mark Attendence", command = self.MarkAttendance)
        self.btn.place(x = 200, y = 445)
        
    def ShowClicked(self):
        self.r = 1
        sessid = self.AllSessions[self.cmb1.current()].SessionId
        cid = self.AllCourses[self.cmb2.current()].CourseId
        sem = self.cmb3.get()
        
        db = DBStudents()
        StudentsList = db.FindStudent(sessid,cid,sem)
        self.AttendanceList = []
        self.EnrollmentIdList = []
        
        self.frame.destroy()
        self.myframe = tk.Frame(self.root, width = 465, height = 100, bd = 1)
        self.myframe.place(x = 10 , y = 140) 
        self.scrollableframe()
        
        for Student in StudentsList:
            listvar = tk.StringVar()
            listvar.set(0)
            lbl5 = tk.Label(self.frame, text = Student.RegistrationId, bg = "White")
            lbl5.grid(row = self.r, column = 0)
            lbl6 = tk.Label(self.frame, text = Student.Name, bg = "White")
            lbl6.grid(row = self.r, column = 1)
            lbl7 = tk.Label(self.frame, text = Student.RollNo, bg = "White")
            lbl7.grid(row = self.r, column = 2)
            chk = tk.Checkbutton(self.frame, variable = listvar, text = "", bg = "White")
            chk.grid(row = self.r, column = 3)
            self.r += 1
    
            self.AttendanceList.append((listvar,Student.RegistrationId))
            db = DBAttendance()
            EIL = db.GetEnrollmentId(Student.RegistrationId)
            self.EnrollmentIdList.append(EIL)     

    def MarkAttendance(self):
        Check = self.CheckEntries()
        if Check == True:
            db = DBAttendance()
            for a,m in zip(self.AttendanceList, self.EnrollmentIdList):
                att = a[0].get()
                rid = a[1]
                eid = m[0]
                date = self.Date.get()
                db.SaveAttendance(rid,eid,att,date)
            messagebox.showinfo("Attendance", "Attendance has been Marked")
        
    def CheckEntries(self):
        Err = True
        self.errlbl.config(text = "")
        
        if self.Date.get() == "":
            self.errlbl.config(text = "*Field cannot be empty.")
            messagebox.showerror("Attendence", "Fill the required fields!")
            Err = False
            
        return Err
        
    def scrollableframe(self):
        self.canvas = Canvas(self.myframe, bg = "White")
        self.frame = tk.Frame(self.canvas, bg = "White")
        self.myscrollbar = Scrollbar(self.myframe, orient = "vertical", command = self.canvas.yview)
        self.canvas.configure(yscrollcommand = self.myscrollbar.set)
        
        self.myscrollbar.pack(side = "right", fill = "y")
        self.canvas.pack(side = "left")
        self.canvas.create_window((0,0),window = self.frame, anchor = 'nw')
        self.frame.bind("<Configure>", self.myfunction)
        
        self.lbl1 = tk.Label(self.frame, text = "RegistrationId" , bg = "White")
        self.lbl1.grid(row = 0, column = 0)
        self.lbl2 = tk.Label(self.frame, text = "Name" , bg = "White")
        self.lbl2.grid(row = 0, column = 1)    
        self.lbl3 = tk.Label(self.frame, text = "Roll No." , bg = "White")
        self.lbl3.grid(row = 0, column = 2)
        self.lbl4 = tk.Label(self.frame, text = "Attendance" , bg = "White")
        self.lbl4.grid(row = 0, column = 3)
        self.frame.grid_columnconfigure(0, minsize =80)
        self.frame.grid_columnconfigure(1, minsize =180)
        self.frame.grid_columnconfigure(2, minsize =100)
        self.frame.grid_columnconfigure(3, minsize =100)
        
    def myfunction(self,event):
        self.canvas.configure(scrollregion = self.canvas.bbox("all"), width = 465, height = 270)
        
    def showDiaog(self):
        self.root.mainloop()