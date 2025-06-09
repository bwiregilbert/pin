# Python Inheritance Example: Person and Student Classes

##Description
This project demonstrates fundamental object -oriented programming (oop)
concepts in python, specifically inheritance. It defines a "Person" class
and a "Student" class that inherits from the "Person" class. The "Student" class
extends the "Person" class by adding attributes like 'graduationyear','course','mark' and
overrides or extends the 'printName' method to provide more detailed student information.

##features

### "Person" class
'__init__'method: Initializes fname(first name) and lname(last name).
'printName'method: Retuns the full name of the person.

### "Student" class(Inherits from "Person" class)
'__init__'method: Calls the parent class's '__init__' and 
adds 'year','course','mark' attributes specific to a student.
'printName' method: Extends the parent's printName to include the graduationyear,course,mark
providing a comprehensive student overview.


