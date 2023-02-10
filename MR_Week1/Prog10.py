""" 
10-create variables of type string, and add “@” to the 
string but with one condition that is the string mustn’t be 
more than 20 letters take the following as an example  
name_one = "Ali" 
name_two = "Ali_Ahmed" 
# Needed Output 
# @@@@@@@@@@@@@@@@@Ali 
# @@@@@@@@@@@Ali_Ahmed

"""
#--------------------------------------------------------------#
name_one = "Ali" 
name_two = "Ali_Ahmed"
name_one = name_one.center(30,"@")
name_two = name_two.center(30,"@")
print(name_one.rstrip("@"))
print(name_two.rstrip("@"))


