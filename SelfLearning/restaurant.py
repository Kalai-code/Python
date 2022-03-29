class Restaurant:
    """Try it yourself Resturant class"""
    
    def __init__(self,restuarant_name,cuisine_type):
        """Initialize restuarant_name and cuisine_type attributes"""
        self.restuarant_name = restuarant_name
        self.cuisine_type = cuisine_type
    
    def describe_restuarant(self):
        """Print restuarant_name and cuisine_type"""
        print("Name of the restuarant:",self.restuarant_name)
        print("Cuisine Type:",self.cuisine_type)
        
    def open_restuarant(self):
        """Print that the restuarant is open"""
        print(f"The restuarant {self.restuarant_name} is open.")
        
restuarant = Restaurant("Asia Cafe","Chinese")

print("\nRestaurant Name:",restuarant.restuarant_name)
print(f"Cuisine :", restuarant.cuisine_type)

restuarant.describe_restuarant()
restuarant.open_restuarant()

restuarant_thai = Restaurant("Thai Lada","Thai")

print("\nRestaurant Name:",restuarant_thai.restuarant_name)
print(f"Cuisine :", restuarant_thai.cuisine_type)

restuarant_thai.describe_restuarant()
restuarant_thai.open_restuarant()

restuarant_italian = Restaurant("Mandola","Italian")

print("\nRestaurant Name:",restuarant_italian.restuarant_name)
print(f"Cuisine :", restuarant_italian.cuisine_type)

restuarant_italian.describe_restuarant()
restuarant_italian.open_restuarant()
