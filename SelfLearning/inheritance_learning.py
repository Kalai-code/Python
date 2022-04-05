class Person:
      
    # Constructor
    def __init__(self, name):
        self.name = name
  
    # To get name
    def getName(self):
        return self.name
  
    # To check if this person is an employee
    def isEmployee(self):
        return False
  
  
# Inherited Person base class (Note Person in bracket)
class Employee(Person):
  
    # Here we return true
    def isEmployee(self):
        return True
  
# Driver code
emp = Person("John")  # An Object of Person
print("Base class - Name:",emp.getName(),",Isemployee:", emp.isEmployee())
  
emp = Employee("Jan") # An Object of Employee
print("Child class - Name:" , emp.getName(),",Isemployee:", emp.isEmployee())