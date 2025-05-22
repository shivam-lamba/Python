# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 20:42:53 2020

@author: slamb
"""

class Account:
    def __init__(self,username,password):
        self._username = username
        self._password = password
        
    def validateLength(self):
        if len(self._password) < 6:
            return False
        return True

    def validateDigit(self):
        if self._password.isalpha():
            return False
        return True

    def addUsername(self):
        self._username = input("Enter a username 6 characters long:")

        while len(self._username) != 6 and len(self._username) <=  6 :
            self._username = input("Enter a username 6 characters long:")
        return self._username

    def getUsername(self):
        return self._username

    def addPassword(self):
        self._password = input("Enter a 6 character long password having atleast 1 digit:")

        while not self.validateLength() or not self.validateDigit():
            self._password = input("Enter a password :")
        return self._password 

    

class Student:
    def __init__(self,name,Birthyear,Countryorigin):
        self._year = 2018 
        self._name = name
        self._birthYear = Birthyear
        self._country = Countryorigin
        self._previousCourses = []
        self._currentCourses = []

    def getYear(self):
        self._year = input("Enter the year of admission:")
        return self._year

    def addPreviousCourses(self,courses):
        self._previousCourses.append(courses)
        self._courses = self._previousCourses

    def addCurrentCourses(self,newCourses):
        self._currentCourses.append(newCourses)
        self._newCourses = self._currentCourses
        
    def getStudentName(self):
        return self._name

    def getBirthYear(self):
        return self._birthYear

    def getCountryOrigin(self):
        return self._country
        
    def getPreviousCourses(self):
        return self._courses

    def getCurrentCourses(self):
        return self._newCourses


class StudentProfile:
    def __init__(self,id,firstName,lastName,gender,address,country,age):
        self._studentId = id
        self._firstName = firstName
        self._lastName = lastName
        self._gender = gender
        self._address = address
        self._countryOfOrigin = country
        self._age = age

    def getStudentId(self):
        return self._studentId

    def getFirstName(self):
        self._firstName = input("Enter your first name:")
        return self._firstName

    def getLastName(self):
        self._lastName = input("Enter your last name:")
        return self._lastName

    def addGender(self):
        self._gender = input("Enter your gender:")
     
    def getGender(self):
        return self._gender

    def getAddress(self):
        return self._address

    def addCountry(self):
        self._countryOfOrigin = input("Enter your country of origin:")
       
    def getCountry(self):
        return self._countryOfOrigin

    def addAge(self):
        self._age = input("Enter your age:")
        
    def getAge(self):
        return self._age
    
class Transcript:
    _totalCourses = 0
    def __init__(self,courses,names,code,grade,unit,semester):
        Transcript._totalCourses = Transcript._totalCourses + 1
        self._courses = courses
        self._name = names
        self._code = code
        self._grade = grade
        self._unit = unit
        self._semester = semester
        self._totalCourses = Transcript._totalCourses

    def getCourses(self):
        return self._courses

    def getName(self):
        return self._name

    def getCode(self):
        return self._code

    def getGrade(self):
        return self._grade

    def getUnit(self):
        return self._unit

    def getSemester(self):
        return self._semester

    def getTotalCourses(self):
        return self._totalCourses 

class GeneralTranscript(Transcript):
    def __init__(self,courses,names,code,grade,unit,semester):
        super().__init__(self,courses,names,code,grade,unit,semester)

    def getCourses(self):
        return self._courses

    def getName(self):
        return self._name

    def getCode(self):
        return self._code

    def getGrade(self):
        return self._grade

    def getUnit(self):
        return self._unit

    def getSemester(self):
        return self._semester


class CurrentSemesterTranscript(Transcript):

    def __init__(self,courses,names,code,grade,unit,semester):
        super().__init__(self,courses,names,code,grade,unit,semester)
   
    def getCurrentSemsCourses(self):
        return self._courses    

    def getCurrentName(self):
        return self._name

    def getCurrentCode(self):
        return self._code

    def getCurrentGrade(self):
        return self._grade

    def getCurrentUnit(self):
        return self._unit

    def getCurrentSemester(self):
        return self._semester 

class Manager:
    def __init__(self,firstName,lastName,title):
        self._Managerftname = firstName
        self._Managerltname = lastName
        self._title = title
    
    def getMangerFirstName(self):
        return self._Managerftname
    
    def getManagerLastName(self):
        return self._Managerltname
    
    def getTitle(self):
        return self._title
    
class CollegeCourses:
    def __init__(self,allCourses,Namesofthem,Unitsofthem):
        self._allCourses = allCourses
        self._coursesNames = Namesofthem
        self._coursesUnits = Unitsofthem
        
    def getAllCourses(self):
        return self._allCourses
    
    def getAllCoursesNames(self):
        return self._coursesNames
    
    def getAllCoursesUnits(self):
        return self._coursesUnits

class StudentsInCollege:
    def __init__(self,nameOfStudent,Studentid):
        self._nameOfStudent = nameOfStudent
        self._Studentid = Studentid
        
    def getStudentName(self):
        return self._nameOfStudent
    
    def getIdOfStudent(self):
        return self._Studentid
    
def testColllege():
    collegeCrs1 = CollegeCourses("CSCI101", "Python", 3)
    collegeCrs2 = CollegeCourses("CSCI102","Object-Oriented Programming",2)
    collegeCrs3 = CollegeCourses("CSCI201", "Problem-Solving", 2)
    collegeCrs4 = CollegeCourses("CSCI202","Project-Management",3)
    collegeCrs5 = CollegeCourses("CSCI301", "Java Programming", 3)
    collegeCrs6 = CollegeCourses("CSCI302", "Web Development",2)
    collegeCrs7 = CollegeCourses("CSCI401","Android Programming",2)
    collegeCrs8 = CollegeCourses("CSCI402", "ioS Applications", 3)
    
    crs1 = collegeCrs1.getAllCourses()
    crs2 = collegeCrs2.getAllCourses()
    crs3 = collegeCrs3.getAllCourses()
    crs4 = collegeCrs4.getAllCourses()
    crs5 = collegeCrs5.getAllCourses()
    crs6 = collegeCrs6.getAllCourses()    
    crs7 = collegeCrs7.getAllCourses()
    crs8 = collegeCrs8.getAllCourses()
    
    cnm1 = collegeCrs1.getAllCoursesNames()
    cnm2 = collegeCrs2.getAllCoursesNames()
    cnm3 = collegeCrs3.getAllCoursesNames()
    cnm4 = collegeCrs4.getAllCoursesNames()
    cnm5 = collegeCrs5.getAllCoursesNames()
    cnm6 = collegeCrs6.getAllCoursesNames()
    cnm7 = collegeCrs7.getAllCoursesNames()        
    cnm8 = collegeCrs8.getAllCoursesNames()
    
    cun1 = collegeCrs1.getAllCoursesUnits()
    cun2 = collegeCrs2.getAllCoursesUnits()    
    cun3 = collegeCrs3.getAllCoursesUnits()
    cun4 = collegeCrs4.getAllCoursesUnits()
    cun5 = collegeCrs5.getAllCoursesUnits() 
    cun6 = collegeCrs6.getAllCoursesUnits()  
    cun7 = collegeCrs7.getAllCoursesUnits() 
    cun8 = collegeCrs8.getAllCoursesUnits() 
    
    print("1)",crs1,":",cnm1,":",cun1,"[Not Taken]")
    print("2)",crs2,":",cnm2,":",cun2,"[Not Taken]")
    print("3)",crs3,":",cnm3,":",cun3,"[Not Taken]")
    print("4)",crs4,":",cnm4,":",cun4,"[]Not Taken")
    print("5)",crs5,":",cnm5,":",cun5,"[Taken at semester 1]")
    print("6)",crs6,":",cnm6,":",cun6,"[Taken at semester 2]")
    print("7)",crs7,":",cnm7,":",cun7,"[Taken at semester 4]")
    print("8)",crs8,":",cnm8,":",cun8,"[Taken at semester 3]")
    
def testCollegeStudents():
    Students1 = StudentsInCollege("William Walker", 898745)
    Students2 = StudentsInCollege("Mike Wheeler", 8222333)
    Students3 = StudentsInCollege("Clay Jensen", 9812756)
    
    name1 = Students1.getStudentName()
    name2 = Students2.getStudentName()
    name3= Students3.getStudentName()
    
    id1 = Students1.getIdOfStudent()
    id2 = Students2.getIdOfStudent()
    id3 = Students3.getIdOfStudent()
     
    print("2)",name1,":",id1)
    print("3)",name2,":",id2)
    print("4)",name3,":",id3)
 
        
    
    
    
    
def StudentPortal():
    

    print("Please Enter your account to login")
    account = Account("login","Password")
    account.addUsername()
    acc = account.getUsername()
    account.validateLength()
    acc1 = account.validateDigit()
    psd = account.addPassword()
    print("Not registered yet? ")
    user = input("Type 'Register' or  Press enter to start registration process!")    
    
    student = StudentProfile("7813007","Peter","Brown","Male","Vancouver","CANADA","21")
    firstName = student.getFirstName()
    lastName = student.getLastName()
    print("\n"+firstName)
    print(lastName)
    name = firstName + " " + lastName
    
    student.addGender()
    gender = student.getGender()
    print(gender)
    student.addCountry()
    country = student.getCountry()
    student.addAge()
    age = student.getAge()
    studentId  = student.getStudentId()
    address = student.getAddress()
    
    s = Student("Archit Arora" , "2000" , "India")
    year = s.getYear()
    print(year)
    
    account = Account("login","Password")
    account.addUsername()
    acc1 = account.getUsername()
    account.validateLength()
    acc2 = account.validateDigit()
    psdd2 = account.addPassword()
    
    print("Username:",acc1)
    print("Password:",psdd2)
    
    print("Thanks, your account has  been created successfully. Welcome Abroad...!")
    print(name)
    print(input())
    
    print("Select from the options:")
    print("[1] -Print my enrolment certificate")
    print("[2] -Print my courses")
    print("[3] -Print my transcript")
    print("[4] -Print my GPA")
    print("[5] -Print my ranking among all students in the college")
    print("[6] -List all available courses")
    print("[7] -List all students")
    print("[8] -Show my profile")
    print("[9] -Logout" )
    print("[10]-Exit")
    print("________________________________________________________")


    
        
    
    trans1 = Transcript("CSCI101", "Python", 101, 86, 3, 1)
    trans2 = Transcript("CSCI202", "Project Management", 202, 82, 3, 1)
    trans3 = Transcript("CSCI301", "Java Programming", 301, 64, 3, 2)
    trans4 = Transcript("CSCI401", "Android Programming", 401, 76, 2,3 )
    
    gc1 = trans1.getCourses()
    gc2 = trans2.getCourses()
    gc3 = trans3.getCourses()
    gc4 = trans4.getCourses()
    
    nm1 = trans1.getName()
    nm2 = trans2.getName()
    nm3 = trans3.getName()
    nm4 = trans4.getName()
    
    gd1 = trans1.getGrade()
    gd2 = trans2.getGrade()
    gd3 = trans3.getGrade()
    gd4 = trans4.getGrade()
    
    co1 = trans1.getCode()
    co2 = trans2.getCode()
    co3 = trans3.getCode()
    co4 = trans4.getCode()
    
    un1 = trans1.getUnit()
    un2 = trans2.getUnit()
    un3 = trans3.getUnit()
    un4 = trans4.getUnit()
    
    gpa = (gd1*un1 + gd2*un2 + gd3*un3 + gd4*un4)/(un1+un2+un3+un4)
    currentGPA = (gd4*un4) /un4
         
    tt4 = trans4.getTotalCourses()
    
    sem1 = trans1.getSemester()
    sem2 = trans2.getSemester()
    sem3 = trans3.getSemester()
    sem4 = trans4.getSemester()
    
    manager = Manager("Peter", "Jackson", "Manager")
    firstnm = manager.getMangerFirstName()
    lastnm = manager.getManagerLastName()
    fullName = firstnm + "" + lastnm   
    title = manager.getTitle()
    
    collegeC1 = CollegeCourses("CSCI101", "Python", 3)
    collegeC2 = CollegeCourses("CSCI102","Object-Oriented Programming",2)
    collegeC3 = CollegeCourses("CSCI201", "Problem-Solving", 2)
    collegeC4 = CollegeCourses("CSCI202","Project-Management",3)
    collegeC5 = CollegeCourses("CSCI301", "Java Programming", 3)
    collegeC6 = CollegeCourses("CSCI302", "Web Development",2)
    collegeC7 = CollegeCourses("CSCI401","Android Programming",2)
    collegeC8 = CollegeCourses("CSCI402", "ioS Applications", 3)
    
  
    choice = input("Enter your choice...Proceed :")
            
    if choice == "1" :
        print("DearSir/Madam,")
        print("This is to certify that",name," with studentId",studentId," is student in semester",sem4," at Columbia.")
        print("He was admitted to our College in", year, "and has taken", tt4, "courses so far.")
        print("Currently he resides at",address,".")
        print("[",title,":",fullName,"]")

            
    elif choice == "2":
        print("Hi Mr.",name,",")
        print("You have taken the following courses so far:")
        print("1)",gc1)
        print("2",gc2)
        print("3)",gc3)
        print("4)",gc4,"[Current Semester]")
          
    elif choice =="3":
        print("Hi Mr.",name,",")
        print("Here is your general transcript:")
        print("1)",gc1,":",nm1,":",gd1)
        print("2)",gc2,":",nm2,":",gd2)
        print("3)",gc3,":",nm3,":",gd3)
        print("4)",gc4,":",nm4,":",gd4,"[Current Semester]")
        print("YOUR GPA IS:",gpa)

        print("Here is your current semester transcript:")
        print("1)", gc4, ":", nm4,":",gd4)
        print("YOUR current semester GPA IS:", currentGPA)
        
    elif choice == "4":
        print("Hi Mr.", name)
        print("Your overall GPA is:", gpa)
        print("Your current semester's GPA is:", currentGPA)
           
    elif choice == "5":
        print("Hi Mr.",name)
        
        if gpa >=90 :
            rank = "1"
        elif gpa >=70 and gpa<90:
            rank = "2"
        elif gpa>=60 and gpa<70:
            rank = "3"
        else:
            rank = "4"
            
        print("Your overall GPA is",gpa,"and therefore your rank is",rank)
        
            
        
    elif choice == "6":
        print("The following courses are offered in Columbia College:")
        testColllege()  
           
        
    elif choice == "7":
        print("There are 4 students in Columbia College as following:")
        print("1)", name,":",studentId)
        testCollegeStudents()
              
    elif choice == "8":
        print("Name: Mr.",name)
        print("Student Id:", studentId)
        print("Gender:", gender )
        print("Address:", student.getAddress())
        print("Country Of Origin:", country)
        print("Age:", age )
        print("Year Of Admission:", year)
        print("Overall GPA:", gpa)
        print("Courses taken so far:", gc1,":",nm1, gc2,":",nm2, gc3,":",nm3, gc4,nm4 , "[current semester]")
        
    elif choice == "9":
       
            
            StudentPortal()
                             
    return 
        
        
def main():
    StudentPortal()
    
main()
