class User:
    """Try it yourself Users"""
    
    def __init__(self,first_name,last_name,age,location):
        """Initialize the attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0
    
    def describe_user(self):
        print("Here is the user information\n")
        print(f"Name:{self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name} !! Welcome to the world of Python")
    
    def increment_login_attempts(self):
        self.login_attempts = self.login_attempts + 1
        return self.login_attempts
        
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Login attempt has been reset to {self.login_attempts}.")

user = User("David","John",37,"Washington")

user.describe_user()
user.greet_user()
print("Login attempt:", user.increment_login_attempts())
print("Login attempt:", user.increment_login_attempts())
print("Login attempt:", user.increment_login_attempts())
user.reset_login_attempts()
print("Login attempt after reset:", user.increment_login_attempts())