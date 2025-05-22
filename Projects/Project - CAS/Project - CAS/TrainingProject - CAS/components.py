class Course:
    def __init__(self):
        self.CourseId = 0
        self.CourseName = ""
        self.Description = ""
    
class Session:
    def __init__(self):
        self.SessionId = 0
        self.Session = 0
        
class Subject:
    def __init__(self):
        self.SubjectId = 0
        self.Subject = ""
        self.Description = ""
        
class Student:
    def __init__(self):
        self.RegistrationId = 0
        self.RollNo = 0
        self.RegistrationDate = ""
        self.Name = ""
        self.Dob = ""
        self.Gender = ""
        self.FatherName = ""
        self.MotherName = ""
        self.Address = ""
        self.City = ""
        self.ContactNo = 0
        self.EmailId = ""
        self.Nationality = ""
        self.CourseId = 0
        self.SessionID = 0
        
class SemesterSubjects:
    def __init__(self):
        self.SemesterSubjectId = 0
        self.Semester = ""
        self.CourseId = 0
        self.SubjectId = 0
        self.SessionId = 0

class SubjectNames:
    def __init__(self):
        self.SemesterSubjectId = 0
        self.Subject = ""
        
class AttendanceRecord:
    def __init__(self):
        self.RegistrationId = 0
        self.Name = ""
        self.Day = 0
        self.Attendance = 0