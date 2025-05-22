import tkinter as tk
from tkinter.ttk import Combobox, Treeview
from components import UpdateStudentInfo
from datalayer import DBCourse, DBSessions, DBEnrollment, DBStudents
from tkinter import messagebox
from UpdateStudentInfo import UpdateInfo

class ViewStudents:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.geometry("735x320")
        self.root.title("View Student")
        self.root.resizable("false","false")

        # Menu Bar  -- View all and Quick View
        self.Menu = tk.Menu(self.root)
        self.Menu.add_cascade(label = "View All", command = self.ViewAllPage)
        self.Menu.add_cascade(label = "Quick View", command = self.QuickViewPage)
        self.root.config(menu = self.Menu)
            
        # Frame for Body
        self.mainframe = tk.Frame(self.root, width = 735, height = 320)
        self.mainframe.place(x = 0, y = 0)
        self.ViewAllPage()

    # View All Defination 
    def ViewAllPage(self):
        self.mainframe.destroy()
        self.mainframe = tk.Frame(self.root, width = 735, height = 320)
        self.mainframe.place(x = 0, y = 0)

        self.lbl1 = tk.Label(self.mainframe, text = "Course")
        self.lbl1.place(x = 10 , y = 10)
        self.cmb1 = Combobox(self.mainframe, state = "readonly", width = 10)
        self.cmb1.place(x = 70, y = 10)
        
        dbcourse = DBCourse()
        self.AllCourses = dbcourse.GetCourse()
        CourseList = []
        for c in self.AllCourses:
            CourseList.append(c.CourseName)
        self.cmb1['values'] = CourseList
        
        self.lbl2 = tk.Label(self.mainframe, text = "Session")
        self.lbl2.place(x = 200, y = 10)
        self.cmb2 = Combobox(self.mainframe, state = "readonly", width = 10)
        self.cmb2.place(x = 260, y = 10)

        dbsession = DBSessions()
        self.AllSessions = dbsession.GetSession()
        SessionList = []
        for s in self.AllSessions:
            SessionList.append(s.Session)
        self.cmb2['values'] = SessionList

        self.lbl3 = tk.Label(self.mainframe, text = "Semester")
        self.lbl3.place(x = 390, y = 10)
        self.cmb3 = Combobox(self.mainframe, state = "readonly", width = 10)
        self.cmb3.place(x = 470, y = 10)

        self.cmb3['values'] = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th']
        
        self.ShowButton = tk.Button(self.mainframe, text = "Show", width = 15, command = self.ShowClicked)
        self.ShowButton.place(x = 610, y = 8)
        
        self.Tree = Treeview(self.mainframe)
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

        self.updateButton = tk.Button(self.mainframe, text= "Update", command = self.UpdateViewAll)
        self.updateButton.place(x = 200, y = 285)

        self.deleteButton = tk.Button(self.mainframe, text= "Delete", command = self.DeleteStudent)
        self.deleteButton.place(x = 450, y = 285)

    # Quick View Defination   
    def QuickViewPage(self):
        self.mainframe.destroy()
        self.mainframe = tk.Frame(self.root, width = 735, height = 320)
        self.mainframe.place(x = 0, y = 0)

        self.rollno = tk.StringVar()
        self.registrationid = tk.StringVar()
        self.redistrationdate = tk.StringVar()
        self.name = tk.StringVar()
        self.dob = tk.StringVar()
        self.gender = tk.StringVar()
        self.contact = tk.StringVar()
        self.father = tk.StringVar()
        self.mother = tk.StringVar()
        self.city = tk.StringVar()
        self.email = tk.StringVar()
        self.course = tk.StringVar()
        self.session = tk.StringVar()
        self.Nationality = tk.StringVar()
        self.address = tk.StringVar()
        
        self.lbl1 = tk.Label(self.mainframe, text = "Roll No.")
        self.lbl1.place(x = 200, y =5)
        self.ent1 = tk.Entry(self.mainframe, textvariable = self.rollno)
        self.ent1.place(x = 260, y = 5)
        
        self.FindButton = tk.Button(self.mainframe, text = "Find", width = 12, command = self.FindClicked)
        self.FindButton.place(x = 420, y = 3)
        
        self.MiddleFrame = tk.Frame(self.mainframe, width = 710, height = 230)
        self.MiddleFrame.place(x = 10, y = 45)
        self.MiddleFrame.config(highlightbackground = "Black", highlightcolor = "Black", highlightthickness = 1, bd= 0)
        
        self.lbl2 = tk.Label(self.mainframe, text = "RegistrationId")
        self.lbl2.place(x = 30 , y = 60)
        self.ent2 = tk.Entry(self.mainframe, state = "readonly", textvariable = self.registrationid)
        self.ent2.place(x = 130, y = 60)
        
        self.lbl3 = tk.Label(self.mainframe, text = "Registration Date")
        self.lbl3.place(x = 440, y = 60)
        self.ent3 = tk.Entry(self.mainframe, state = "readonly", textvariable = self.redistrationdate)
        self.ent3.place(x = 560, y = 60)
        
        self.lbl4 = tk.Label(self.mainframe, text = "Name")
        self.lbl4.place(x = 30, y = 90)
        self.ent4 = tk.Entry(self.mainframe, textvariable = self.name)
        self.ent4.place(x = 130, y = 90)
        
        self.lbl5 = tk.Label(self.mainframe, text = "D.O.B")
        self.lbl5.place(x = 440, y = 90)
        self.ent5 = tk.Entry(self.mainframe, textvariable = self.dob)
        self.ent5.place(x = 560, y = 90)
        
        self.lbl6 = tk.Label(self.mainframe, text = "Gender")
        self.lbl6.place(x = 30, y = 120)
        self.ent6 = tk.Entry(self.mainframe, textvariable = self.gender)
        self.ent6.place(x = 130, y = 120)
        
        self.lbl7 = tk.Label(self.mainframe, text = "Contact Number")
        self.lbl7.place(x = 440, y = 120)
        self.ent7 = tk.Entry(self.mainframe, textvariable = self.contact)
        self.ent7.place(x = 560, y = 120)
        
        self.lbl8 = tk.Label(self.mainframe, text = "Father Name")
        self.lbl8.place(x = 30, y = 150)
        self.ent8 = tk.Entry(self.mainframe, textvariable = self.father)
        self.ent8.place(x = 130, y = 150)
        
        self.lbl9 = tk.Label(self.mainframe, text = "Mother Name")
        self.lbl9.place(x = 440, y = 150)
        self.ent9 = tk.Entry(self.mainframe, textvariable = self.mother)
        self.ent9.place(x = 560, y = 150)
        
        self.lbl10 = tk.Label(self.mainframe, text = "City")
        self.lbl10.place(x = 30, y = 180)
        self.ent10 = tk.Entry(self.mainframe, textvariable = self.city)
        self.ent10.place(x = 130, y = 180)
        
        self.lbl11 = tk.Label(self.mainframe, text = "E-mail")
        self.lbl11.place(x = 440, y = 180)
        self.ent11 = tk.Entry(self.mainframe, textvariable = self.email)
        self.ent11.place(x = 560, y = 180)
        
        self.lbl12 = tk.Label(self.mainframe, text = "Course")
        self.lbl12.place(x = 30, y = 210)
        self.ent12 = tk.Entry(self.mainframe, state = "readonly", textvariable = self.course)
        self.ent12.place(x = 130, y = 210)
        
        self.lbl13 = tk.Label(self.mainframe, text = "Session")
        self.lbl13.place(x = 440, y = 210)
        self.ent13 = tk.Entry(self.mainframe, state = "readonly", textvariable = self.session)
        self.ent13.place(x = 560, y = 210)

        self.lbl14 = tk.Label(self.mainframe, text = "Nationality")
        self.lbl14.place(x = 30, y = 240)
        self.ent14 = tk.Entry(self.mainframe, textvariable = self.Nationality)
        self.ent14.place(x = 130, y = 240)

        self.lbl15 = tk.Label(self.mainframe, text = "Address")
        self.lbl15.place(x = 440, y = 240)
        self.ent15 = tk.Entry(self.mainframe, textvariable = self.address)
        self.ent15.place(x = 560, y = 240)

        self.saveButton = tk.Button(self.mainframe, text = "Update", width = 12, command = self.UpdateInfo)
        self.saveButton.place(x = 200, y = 285)

        self.deleteButton = tk.Button(self.mainframe, text = "Delete", width = 12, command = self.DeleteStudent)
        self.deleteButton.place(x = 450, y = 285)

    def ShowClicked(self):
        cid = self.AllCourses[self.cmb1.current()].CourseId
        sid = self.AllSessions[self.cmb2.current()].SessionId
        sem = self.cmb3.get()
        print(cid,sid,sem)

        db = DBStudents()
        StudentDetailsList = db.FindStudent(sid,cid,sem)
        i = 0
        for s in StudentDetailsList:
            self.Tree.insert("",i,text = s.RegistrationId, values=(s.Name,s.RollNo,s.RegistrationDate,s.Dob,s.ContactNo))
            i +=1

    def UpdateViewAll(self):
        key = self.Tree.focus()
        roll = int(self.Tree.item(key,"values")[1])
        
        obj = UpdateInfo(roll)
        obj.showDialog()

    def FindClicked(self):
        roll = int(self.rollno.get())
        db = DBEnrollment()
        AllData = db.FindRoll(roll)
        
        for data in AllData:
            self.registrationid.set(data.RegistrationId)
            self.redistrationdate.set(data.RegistrationDate)
            self.name.set(data.Name)
            self.dob.set(data.Dob)
            self.gender.set(data.Gender)
            self.contact.set(data.ContactNo)
            self.father.set(data.FatherName)
            self.mother.set(data.MotherName)
            self.city.set(data.City)
            self.email.set(data.EmailId)
            self.course.set(data.CourseId)
            self.session.set(data.SessionID)
            self.Nationality.set(data.Nationality)
            self.address.set(data.Address)

    def UpdateInfo(self):
        stud = UpdateStudentInfo()
        db = DBStudents()

        stud.Name = self.name.get()
        stud.Dob = self.dob.get()
        stud.Gender = self.gender.get()
        stud.ContactNo = self.contact.get()
        stud.FatherName = self.father.get()
        stud.MotherName = self.mother.get()
        stud.City = self.city.get()
        stud.Nationality = self.Nationality.get()
        stud.Address = self.address.get() 
        stud.EmailId = self.email.get()

        db.UpdateStudent(stud, self.registrationid.get())
        messagebox.showinfo("Quick View", "Information was updated successfully.")

    def DeleteStudent(self):
        db = DBStudents()

        rid = self.registrationid.get()
        db.DeleteStudent(rid)
        messagebox.showinfo("Quick View", "Student record was deleted successfully.")

    def showDialog(self):
        self.root.mainloop()