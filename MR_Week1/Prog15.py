""" 
create 3 variables your name, age and country , make 
sure that your age is of an integer value not string , 
print the following statement using the new formatting method
name = "Ali"
age = 20 
country = "Egypt"  

My Name Is Ali, And My Age Is 20, And My Country Is Egypt
"""
# --------------------------------------------------------------#
name = "Ali"
age = 20
country = "Egypt"

print("My name is {}, And my Age is {} ,\
And my country is {}".format(name, age, country))

# or

print("\nMy name is {1}, And my Age is {0} ,\
And my country is {2}".format(age, name, country))

