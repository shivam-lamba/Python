import tkinter as tk
from datalayer import DBStudents, DBEnrollment
from tkinter import messagebox
from components import UpdateStudentInfo

class UpdateInfo:
    def __init__(self, roll):
        self.root = tk.Toplevel()
        self.root.geometry("620x265")
        self.root.title("Update Info")
        self.root.resizable("false","false")

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
        
        self.lbl2 = tk.Label(self.root, text = "RegistrationId")
        self.lbl2.place(x = 30 , y = 10)
        self.ent2 = tk.Entry(self.root, state = "readonly", textvariable = self.registrationid)
        self.ent2.place(x = 130, y = 10)
        
        self.lbl3 = tk.Label(self.root, text = "Registration Date")
        self.lbl3.place(x = 340, y = 10)
        self.ent3 = tk.Entry(self.root, state = "readonly", textvariable = self.redistrationdate)
        self.ent3.place(x = 460, y = 10)
        
        self.lbl4 = tk.Label(self.root, text = "Name")
        self.lbl4.place(x = 30, y = 40)
        self.ent4 = tk.Entry(self.root, textvariable = self.name)
        self.ent4.place(x = 130, y = 40)
        
        self.lbl5 = tk.Label(self.root, text = "D.O.B")
        self.lbl5.place(x = 340, y = 40)
        self.ent5 = tk.Entry(self.root, textvariable = self.dob)
        self.ent5.place(x = 460, y = 40)
        
        self.lbl6 = tk.Label(self.root, text = "Gender")
        self.lbl6.place(x = 30, y = 70)
        self.ent6 = tk.Entry(self.root, textvariable = self.gender)
        self.ent6.place(x = 130, y = 70)
        
        self.lbl7 = tk.Label(self.root, text = "Contact Number")
        self.lbl7.place(x = 340, y = 70)
        self.ent7 = tk.Entry(self.root, textvariable = self.contact)
        self.ent7.place(x = 460, y = 70)
        
        self.lbl8 = tk.Label(self.root, text = "Father Name")
        self.lbl8.place(x = 30, y = 100)
        self.ent8 = tk.Entry(self.root, textvariable = self.father)
        self.ent8.place(x = 130, y = 100)
        
        self.lbl9 = tk.Label(self.root, text = "Mother Name")
        self.lbl9.place(x = 340, y = 100)
        self.ent9 = tk.Entry(self.root, textvariable = self.mother)
        self.ent9.place(x = 460, y = 100)
        
        self.lbl10 = tk.Label(self.root, text = "City")
        self.lbl10.place(x = 30, y = 130)
        self.ent10 = tk.Entry(self.root, textvariable = self.city)
        self.ent10.place(x = 130, y = 130)
        
        self.lbl11 = tk.Label(self.root, text = "E-mail")
        self.lbl11.place(x = 340, y = 130)
        self.ent11 = tk.Entry(self.root, textvariable = self.email)
        self.ent11.place(x = 460, y = 130)
        
        self.lbl12 = tk.Label(self.root, text = "Course")
        self.lbl12.place(x = 30, y = 160)
        self.ent12 = tk.Entry(self.root, state = "readonly", textvariable = self.course)
        self.ent12.place(x = 130, y = 160)
        
        self.lbl13 = tk.Label(self.root, text = "Session")
        self.lbl13.place(x = 340, y = 160)
        self.ent13 = tk.Entry(self.root, state = "readonly", textvariable = self.session)
        self.ent13.place(x = 460, y = 160)

        self.lbl14 = tk.Label(self.root, text = "Nationality")
        self.lbl14.place(x = 30, y = 190)
        self.ent14 = tk.Entry(self.root, textvariable = self.Nationality)
        self.ent14.place(x = 130, y = 190)

        self.lbl15 = tk.Label(self.root, text = "Address")
        self.lbl15.place(x = 340, y = 190)
        self.ent15 = tk.Entry(self.root, textvariable = self.address)
        self.ent15.place(x = 460, y = 190)

        self.saveButton = tk.Button(self.root, text = "Update", width = 12, command = self.UpdateInfo)
        self.saveButton.place(x = 250, y = 230)

        # Inserting Data of Required Student into TextBoxes
        db = DBEnrollment()
        infolist = db.FindRoll(roll)

        for data in infolist:
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
            print(data.Address)

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

    def showDialog(self):
        self.root.mainloop()
