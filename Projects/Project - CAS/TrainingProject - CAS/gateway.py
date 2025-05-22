import tkinter as tk
from tkinter.ttk import Treeview
from datalayer import DBSessions
from RegistrationForm import RegistrationForm
from ViewStudents import ViewStudents
from Enrollments import Enrollments
from DisplayStudentsForm import DisplayStudentForm
from Attendance import Attendance
from AddSession import AddSession
from ViewSessions import ViewSessions
from AddSubject import AddSubject
from ViewSubjects import ViewSubjects
from AddCourse import AddCourse
from ViewCourses import ViewCourses
from SemesterSubjects import SemesterSubjectsForm
from datalayer import DBCourse, DBStudents
from ViewAttendance import ViewAttendance
from datetime import date

class Gateway:
    def __init__(self,username):
        self.root = tk.Toplevel()

        self.root.geometry("625x450")
        self.root.title("CAS")
        self.root.resizable('false','false')
        
        self.Menu = tk.Menu(self.root)
        
        dt = date.today()
        self.welcomeuser = tk.Label(self.root, text = "Welcome, " + username)
        self.welcomeuser.place(x = 10 , y = 425)
        self.datetimelabel = tk.Label(self.root, text = dt)
        self.datetimelabel.place(x = 550, y = 425)
        
        studentmenu = tk.Menu(self.Menu, tearoff = 0) 
        studentmenu.add_command(label = "New Registration", command = self.NewRegistrationClick)
        studentmenu.add_command(label = "View Students", command = self.ViewStudentsClick)
        studentmenu.add_separator()
        studentmenu.add_command(label= "Semester Registration", command = self.SemesterRegistrationClick)
        
        self.Menu.add_cascade(label = "Students", menu = studentmenu)
        
        marksmenu = tk.Menu(self.Menu, tearoff = 0)
        marksmenu.add_command(label= "Add/View/Update", command = self.MarksClick)
        self.Menu.add_cascade(label = "Marks", menu = marksmenu)
        
        attendancemenu = tk.Menu(self.Menu, tearoff = 0)
        attendancemenu.add_command(label = "Mark Attendance", command = self.AttendanceClick)
        attendancemenu.add_command(label = "View Attendance", command = self.ViewAttendanceClick)
        self.Menu.add_cascade(label = "Attendance", menu = attendancemenu)
        
        master = tk.Menu(self.Menu, tearoff = 0)
        
        session = tk.Menu(master, tearoff = 0)
        session.add_command(label = "Add Session", command = self.AddSessionClick)
        session.add_command(label = "View Session", command = self.ViewSessionClick)
        master.add_cascade(label = "Session", menu = session)
        
        course = tk.Menu(master, tearoff = 0)
        course.add_command(label = "Add Course", command = self.AddCourseClick)
        course.add_command(label = "View Course", command = self.ViewCourseClick)
        master.add_cascade(label = "Course", menu = course)
        
        subject = tk.Menu(master, tearoff = 0)
        subject.add_command(label = "Add Subject", command = self.AddSubjectClick)
        subject.add_command(label = "View Subject", command = self.ViewSubjectClick)
        master.add_cascade(label = "Subject", menu = subject)
        master.add_separator()
        master.add_command(label = "Semester Subject", command = self.SemesterSubjectClick)
        self.Menu.add_cascade(label = "Masters Record", menu = master)

        self.Menu.add_cascade(label = "Refresh", command = self.Refresh)
        
        self.root.config(menu = self.Menu)
        
        
        self.Tree = Treeview(self.root)
        self.Tree['columns'] = ['col1', 'col2']
        self.Tree.place(x = 10, y = 20, height=400)
        
        dbsession = DBSessions()
        allcourses = DBCourse().GetCourse()
        objDALStudent = DBStudents()
        
        sessioncounter = 1
        coursecounter=1
        studentcounter = 1
        
        for session in dbsession.GetSession():
            sessionnode = self.Tree.insert("", sessioncounter, text=session.Session, values=("",""))
            
            coursecounter=1
            for course in allcourses:
                coursenode = self.Tree.insert(sessionnode, coursecounter, text=course.CourseName, values=("",""))
                coursecounter+=1
                
                studentcounter = 1
                for student in objDALStudent.ViewStudents(course.CourseId, session.SessionId):
                    self.Tree.insert(coursenode, studentcounter, text=str(studentcounter), values=(student.RollNo, student.Name))
                    studentcounter+=1
                    
                    
            sessioncounter+=1

    def Refresh(self):
        self.Tree.delete(*self.Tree.get_children())
        dbsession = DBSessions()
        allcourses = DBCourse().GetCourse()
        objDALStudent = DBStudents()
        
        sessioncounter = 1
        coursecounter=1
        studentcounter = 1
        
        for session in dbsession.GetSession():
            sessionnode = self.Tree.insert("", sessioncounter, text=session.Session, values=("",""))
            
            coursecounter=1
            for course in allcourses:
                coursenode = self.Tree.insert(sessionnode, coursecounter, text=course.CourseName, values=("",""))
                coursecounter+=1
                
                studentcounter = 1
                for student in objDALStudent.ViewStudents(course.CourseId, session.SessionId):
                    self.Tree.insert(coursenode, studentcounter, text=str(studentcounter), values=(student.RollNo, student.Name))
                    studentcounter+=1
                    
                    
            sessioncounter+=1

    def NewRegistrationClick(self):
        obj = RegistrationForm()
        obj.showDialog()
        
    def ViewStudentsClick(self):
        obj = ViewStudents()
        obj.showDialog()
    
    def SemesterRegistrationClick(self):
        obj = Enrollments()
        obj.showDialog()
    
    def MarksClick(self):
        obj = DisplayStudentForm()
        obj.showDialog()
        
    def AttendanceClick(self):
        obj = Attendance()
        obj.showDiaog()
        
    def ViewAttendanceClick(self):
        obj = ViewAttendance()
        obj.showDialog()
        
    def AddSessionClick(self):
        obj = AddSession()
        obj.showDialog()
        
    def ViewSessionClick(self):
        obj = ViewSessions()
        obj.showDialog()
        
    def AddSubjectClick(self):
        obj = AddSubject()
        obj.showDialog()
        
    def ViewSubjectClick(self):
        obj = ViewSubjects()
        obj.showDialog()
    
    def AddCourseClick(self):
        obj = AddCourse()
        obj.showDialog()
        
    def ViewCourseClick(self):
        obj = ViewCourses()
        obj.showDialog()
        
    def SemesterSubjectClick(self):
        obj = SemesterSubjectsForm()
        obj.showDialog()
        
    def showDialog(self):
        self.root.mainloop()
