import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
from datalayer import DBEnrollment
from datetime import date

class Enrollments:
    def __init__(self):
        self.root = tk.Toplevel()
        self.root.geometry("590x340")
        self.root.title("Enrollment")
        
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
        
        self.lbl1 = tk.Label(self.root, text = "Roll No.")
        self.lbl1.place(x = 140, y =10)
        self.ent1 = tk.Entry(self.root, textvariable = self.rollno)
        self.ent1.place(x = 200, y = 10)
        
        self.FindButton = tk.Button(self.root, text = "Find", width = 12, command = self.FindClicked)
        self.FindButton.place(x = 360, y = 10)
        
        self.MiddleFrame = tk.Frame(self.root, width = 570, height = 210)
        self.MiddleFrame.place(x = 10, y = 60)
        self.MiddleFrame.config(highlightbackground = "Black", highlightcolor = "Black", highlightthickness = 1, bd= 0)
        
        self.lbl2 = tk.Label(self.root, text = "RegistrationId")
        self.lbl2.place(x = 30 , y = 80)
        self.ent2 = tk.Entry(self.root, state = "readonly", textvariable = self.registrationid)
        self.ent2.place(x = 130, y = 80)
        
        self.lbl3 = tk.Label(self.root, text = "Registration Date")
        self.lbl3.place(x = 330, y = 80)
        self.ent3 = tk.Entry(self.root, state = "readonly", textvariable = self.redistrationdate)
        self.ent3.place(x = 430, y = 80)
        
        self.lbl4 = tk.Label(self.root, text = "Name")
        self.lbl4.place(x = 30, y = 110)
        self.ent4 = tk.Entry(self.root, state = "readonly", textvariable = self.name)
        self.ent4.place(x = 130, y = 110)
        
        self.lbl5 = tk.Label(self.root, text = "D.O.B")
        self.lbl5.place(x = 330, y = 110)
        self.ent5 = tk.Entry(self.root, state = "readonly", textvariable = self.dob)
        self.ent5.place(x = 430, y = 110)
        
        self.lbl6 = tk.Label(self.root, text = "Gender")
        self.lbl6.place(x = 30, y = 140)
        self.ent6 = tk.Entry(self.root, state = "readonly", textvariable = self.gender)
        self.ent6.place(x = 130, y = 140)
        
        self.lbl7 = tk.Label(self.root, text = "Contact Number")
        self.lbl7.place(x = 330, y = 140)
        self.ent7 = tk.Entry(self.root, state = "readonly", textvariable = self.contact)
        self.ent7.place(x = 430, y = 140)
        
        self.lbl8 = tk.Label(self.root, text = "Father Name")
        self.lbl8.place(x = 30, y = 170)
        self.ent8 = tk.Entry(self.root, state = "readonly", textvariable = self.father)
        self.ent8.place(x = 130, y = 170)
        
        self.lbl9 = tk.Label(self.root, text = "Mother Name")
        self.lbl9.place(x = 330, y = 170)
        self.ent9 = tk.Entry(self.root, state = "readonly", textvariable = self.mother)
        self.ent9.place(x = 430, y = 170)
        
        self.lbl10 = tk.Label(self.root, text = "City")
        self.lbl10.place(x = 30, y = 200)
        self.ent10 = tk.Entry(self.root, state = "readonly", textvariable = self.city)
        self.ent10.place(x = 130, y = 200)
        
        self.lbl11 = tk.Label(self.root, text = "E-mail")
        self.lbl11.place(x = 330, y = 200)
        self.ent11 = tk.Entry(self.root, state = "readonly", textvariable = self.email)
        self.ent11.place(x = 430, y = 200)
        
        self.lbl12 = tk.Label(self.root, text = "Course")
        self.lbl12.place(x = 30, y = 230)
        self.ent12 = tk.Entry(self.root, state = "readonly", textvariable = self.course)
        self.ent12.place(x = 130, y = 230)
        
        self.lbl13 = tk.Label(self.root, text = "Session")
        self.lbl13.place(x = 330, y = 230)
        self.ent13 = tk.Entry(self.root, state = "readonly", textvariable = self.session)
        self.ent13.place(x = 430, y = 230)
        
        self.lbl14 = tk.Label(self.root, text = "Semester")
        self.lbl14.place(x = 140, y = 300)
        self.cmb1 = Combobox(self.root)
        self.cmb1.place(x = 200, y = 300)
        self.cmb1['values'] = ['1st', '2nd', '3rd','4th','5th','6th','7th','8th']
        
        self.RegisterButton = tk.Button(self.root, text = "Register", width = 12, command = self.RegisterClicked)
        self.RegisterButton.place(x = 360, y = 300)
    
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
    
    def RegisterClicked(self):
        sem = self.cmb1.get()
        rid = int(self.registrationid.get())
        today = str(date.today())
        db = DBEnrollment()
        db.Register(today,sem,rid)
        
        messagebox.showinfo("Enrollment", "Student was enrolled successfully.")
        
    def showDialog(self):
        self.root.mainloop()