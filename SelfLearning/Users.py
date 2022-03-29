class User:
    """Try it yourself Users"""
    
    def __init__(self,first_name,last_name,age,location):
        """Initialize the attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
    
    def describe_user(self):
        print("Here is the user information\n")
        print(f"Name:{self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name} !! Welcome to the world of Python")

user = User("David","John",37,"Washington")

user.describe_user()
user.greet_user()