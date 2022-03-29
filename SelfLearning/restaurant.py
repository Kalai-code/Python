class Restaurant:
    """Try it yourself Resturant class"""
    
    def __init__(self,restuarant_name,cuisine_type,number_seats = 0,number_served = 0):
        """Initialize restuarant_name and cuisine_type attributes"""
        self.restuarant_name = restuarant_name
        self.cuisine_type = cuisine_type
        self.number_seats = number_seats
        self.number_served = number_served
    
    def describe_restuarant(self):
        """Print restuarant_name and cuisine_type"""
        print("Name of the restuarant:",self.restuarant_name)
        print("Cuisine Type:",self.cuisine_type)
        print("No of people can be accomodated in the restuarant:", self.number_seats)
        
    def open_restuarant(self):
        """Print that the restuarant is open"""
        print(f"The restuarant {self.restuarant_name} is open.")
        
    def set_number_served(self):
        """print the number of people server"""
        print(f"Number of the people served:", self.number_served)
        
    def increment_number_served(self):
        """increment the number of customers served"""
        print(f"Number of people served today:",self.number_served + 5)
        
restuarant = Restaurant("Asia Cafe","Chinese")

print("\nRestaurant Name:",restuarant.restuarant_name)
print(f"Cuisine :", restuarant.cuisine_type)

restuarant.describe_restuarant()
restuarant.open_restuarant()
restuarant.set_number_served()
restuarant.increment_number_served()

restuarant_thai = Restaurant("Thai Lada","Thai",15,10)

print("\nRestaurant Name:",restuarant_thai.restuarant_name)
print(f"Cuisine :", restuarant_thai.cuisine_type)

restuarant_thai.describe_restuarant()
restuarant_thai.open_restuarant()
restuarant_thai.set_number_served()
restuarant_thai.increment_number_served()

restuarant_italian = Restaurant("Mandola","Italian",50,20)

print("\nRestaurant Name:",restuarant_italian.restuarant_name)
print(f"Cuisine :", restuarant_italian.cuisine_type)

restuarant_italian.describe_restuarant()
restuarant_italian.open_restuarant()
restuarant_italian.set_number_served()
restuarant_italian.increment_number_served()
