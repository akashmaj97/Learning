def add(*args): # The *args syntax allows the function to accept a variable number of arguments as a tuple.
    print(type(args)) # Output: <class 'tuple'>     
    
    total = 0
    for num in args:
        total += num
    return total


print(add(1, 2, 3)) # Output: 6
print(add(4, 5))    # Output: 9

print("\n") # Just to add a newline for better readability of the output


#**************************************************************************************
#***************using **kwargs to accept variable number of keyword arguments**********
#**************************************************************************************

def print_info(**kwargs): # The **kwargs syntax allows the function to accept a variable number of keyword arguments as a dictionary.
    print(type(kwargs)) # Output: <class 'dict'>     
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")    

print_info(name="Alice", age=30, city="New York")
# Output:      

print("\n") # Just to add a newline for better readability of the output

#*******************************************************************************************************************
#***************using **kwargs to accept variable number of keyword arguments along with normal parameters**********
#*******************************************************************************************************************

def print_info(name, age, **kwargs): # The **kwargs syntax allows the function to accept a variable number of keyword arguments as a dictionary.
    print(f"Name: {name}, Age: {age}")
    
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    
print_info("Alice", 30, city="New York", profession="Engineer")



#*******************************************************************************************************************
#***************using **kwargs to set attributes dynamically in a class**********   
#*******************************************************************************************************************

class Person:
    def __init__(self, name, age, **kwargs):
        self.name = name
        self.age = age
        
        self.city = kwargs.get("city", "Unknown") # Set city attribute if provided, otherwise default to "Unknown"
        self.profession = kwargs.get("profession", "Unknown") # Set profession attribute if provided

person1 = Person("Alice", 30, city="New York", profession="Engineer")
print(person1.name)        # Output: Alice  
print(person1.city)        # Output: New York
print("\n") # Just to add a newline for better readability of the output
person2 = Person("Bob", 25) # No city or profession provided, will use default values
print(person2.name)        # Output: Bob
print(person2.city)       # Output: Unknown    