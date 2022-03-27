#Try it yourself Dictionary learning

person = {"first_name":"Arunkumar","last_name":"Gurusamy","Age":36,"city":"Austin"}
print("Name:",person["first_name"],person["last_name"])
print("Age:",person["Age"])
print("City:",person["city"])

#Try it yourself Favorite Numbers
favorite_numbers = {"John":2,"Ram":5,"Arun":7,"Jan":9,"August":3}
for name,number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")

#Try it yourself learning with dictionaries inside list

people = [{"first_name":"Arunkumar","last_name":"Gurusamy","Age":36,"city":"Austin"},
            {"first_name":"Shatvik","last_name":"Arunkumar","Age":9,"city":"Austin"},
            {"first_name":"Mithra","last_name":"Arunkumar","Age":6,"city":"Austin"}]
if len(people) > 0:
    for person in people:
        print("Name:",person["first_name"],person["last_name"])
        print("Age:",person["Age"])
        print("City:",person["city"])
        print("\n")
        
#Try it yourself Favorite Numbers - list inside dictionary
favorite_numbers = {"John":[2,3],"Ram":5,"Arun":[5,7],"Jan":[9,1,5],"August":3}
for name,number in favorite_numbers.items():
    print(f"{name}'s favorite number is {number}.")
    
#Add values to dictionary
person = {}
person["first_name"] = "Jan"
person["last_name"] = "Paul"
print(person)
