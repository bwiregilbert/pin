import os 
os.system("cls")

class Person:
    def __init__(self ,fname, lname):
        self.fname = fname
        self.lname =lname
    def __str__(self):
        return f'{self.fname} {self.lname} ' 

class Student(Person):
    
    def __init__(self,fname,lname,year,course,mark):
        super().__init__(fname,lname)
        self.Graduationyear = year
        self.course = course
        self.mark = mark
    
    def __str__(self):
        return ( f' Name: {super().__str__()},  Year: {self.Graduationyear}, ' f'Course: {self.course},  Mark: {self.mark}') 
      
student1 = Student('Akullu Bella ','Prossy',2009,'Information Technology',60) 

print(student1)          
    
















     