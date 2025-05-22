import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox
from components import Student,Course, Session
from datalayer import DBStudents, DBCourse, DBSessions

class RegistrationForm:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.geometry("650x390")
        self.root.title("Registration")
        
        self.CourseId = 0
        self.SessionID = 0
        self.RegistrationDate = tk.StringVar()
        self.RollNo = tk.StringVar()
        self.Name = tk.StringVar()
        self.Dob = tk.StringVar()
        self.Gender = tk.StringVar()
        self.FatherName = tk.StringVar()
        self.MotherName = tk.StringVar()
        self.Address = tk.StringVar()
        self.City = tk.StringVar()
        self.Nationality = tk.StringVar()
        self.ContactNo = tk.StringVar()
        self.EmailId = tk.StringVar()
        
        
        self.lbl1 = tk.Label(self.root, text = "Course")
        self.lbl1.place(x = 10 , y = 10)
  
        self.cmb1 = Combobox(self.root, state = "readonly", width = 20)
        self.cmb1.place(x = 110, y = 10)
        
        
        dbcourse = DBCourse()
        self.AllCourses = dbcourse.GetCourse()
        
        courseslist = []
        for c in self.AllCourses:
            courseslist.append(c.CourseName)
        
        self.cmb1['values'] = courseslist
        
        self.lbl2 = tk.Label(self.root, text = "Session")
        self.lbl2.place(x = 350 , y = 10)

        self.cmb2 = Combobox(self.root, state = "readonly", width = 20)
        self.cmb2.place(x = 460, y = 10)


        dbsession = DBSessions()
        self.AllSessions = dbsession.GetSession()
        
        sessionlist = []
        
        for s in self.AllSessions:
            sessionlist.append(s.Session)
        
        self.cmb2['values'] = sessionlist
        
        
        self.lbl13 = tk.Label(self.root, text = "Registration Date")
        self.lbl13.place(x = 10 , y = 70)
        self.ent13 = tk.Entry(self.root , textvariable = self.RegistrationDate, width = 25)
        self.ent13.place(x = 110, y = 70)
        
        self.lbl14 = tk.Label(self.root, text = "Name")
        self.lbl14.place(x = 350 , y = 70)
        self.ent14 = tk.Entry(self.root, textvariable = self.Name, width = 25)
        self.ent14.place(x = 460, y = 70)
        
        self.lbl3 = tk.Label(self.root, text = "Roll Number")
        self.lbl3.place(x = 10 , y = 110)
        self.ent3 = tk.Entry(self.root, textvariable = self.RollNo, width = 25)
        self.ent3.place(x = 110, y = 110)
        
        self.lbl4 = tk.Label(self.root, text = "D.O.B")
        self.lbl4.place(x = 350 , y = 110)
        self.ent4 = tk.Entry(self.root, textvariable = self.Dob, width = 25)
        self.ent4.place(x = 460, y = 110)
        
        self.lbl5 = tk.Label(self.root, text = "Gender")
        self.lbl5.place(x = 10, y = 150)
        self.rbn1 = tk.Radiobutton(self.root, text = "Male", variable = self.Gender, value = "Male")
        self.rbn1.place(x = 110, y = 150)
        self.rbn2 = tk.Radiobutton(self.root, text = "Female", variable = self.Gender, value = "Female")
        self.rbn2.place(x = 210, y = 150)
        self.rbn3 = tk.Radiobutton(self.root, text = "Others", variable = self.Gender, value = "Others")
        self.rbn3.place(x = 310, y = 150)
        
        self.lbl6 = tk.Label(self.root, text = "Father Name")
        self.lbl6.place(x = 10 , y = 190)
        self.ent6 = tk.Entry(self.root, textvariable = self.FatherName, width = 25)
        self.ent6.place(x = 110, y = 190)
        
        self.lbl7 = tk.Label(self.root, text = "Mother Name")
        self.lbl7.place(x = 350 , y = 190)
        self.ent7 = tk.Entry(self.root, textvariable = self.MotherName, width = 25)
        self.ent7.place(x = 460, y = 190)
        
        self.lbl8 = tk.Label(self.root, text = "Address")
        self.lbl8.place(x = 10 , y = 230)
        self.ent8 = tk.Entry(self.root, textvariable = self.Address, width = 25)
        self.ent8.place(x = 110, y = 230)
        
        self.lbl9 = tk.Label(self.root, text = "City")
        self.lbl9.place(x = 350 , y = 230)
        self.ent9 = tk.Entry(self.root, textvariable = self.City, width = 25)
        self.ent9.place(x = 460, y = 230)
        
        self.lbl10 = tk.Label(self.root, text = "Nationality")
        self.lbl10.place(x = 10 , y = 270)
        self.ent10 = tk.Entry(self.root, textvariable = self.Nationality, width = 25)
        self.ent10.place(x = 110, y = 270)
        
        self.lbl11 = tk.Label(self.root, text = "Contact Number")
        self.lbl11.place(x = 350 , y = 270)
        self.ent11 = tk.Entry(self.root, textvariable = self.ContactNo, width = 25)
        self.ent11.place(x = 460, y = 270)
        
        self.lbl12 = tk.Label(self.root, text = "Email Id")
        self.lbl12.place(x = 10 , y = 310)
        self.ent12 = tk.Entry(self.root, textvariable = self.EmailId, width = 25)
        self.ent12.place(x = 110, y = 310)
        
        self.btn = tk.Button(self.root, text = "Submit", width = 20, command = self.SubmitClicked)
        self.btn.place(x = 250 , y = 350)
    
    
    def SubmitClicked(self):

        comp = Student()
        comp.CourseId = self.AllCourses[self.cmb1.current()].CourseId
        comp.SessionID = self.AllSessions[self.cmb2.current()].SessionId
        comp.RegistrationDate = self.RegistrationDate.get()
        comp.RollNo = self.RollNo.get()
        comp.Name = self.Name.get()
        comp.Dob = self.Dob.get()
        comp.Gender = self.Gender.get()
        comp.FatherName = self.FatherName.get()
        comp.MotherName = self.MotherName.get()
        comp.Address = self.Address.get()
        comp.City = self.City.get()
        comp.Nationality = self.Nationality.get()
        comp.ContactNo = self.ContactNo.get()
        comp.EmailId = self.EmailId.get()
        db = DBStudents()
        db.AddStudent(comp)
        messagebox.showinfo("Registration", "Registration successful.")
    
    def showDialog(self):
        self.root.mainloop()