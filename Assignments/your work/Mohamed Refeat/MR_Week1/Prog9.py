""" 
9-create variables of type string containing any number 
you want of size not more than 4 digits , now you have to 
print these numbers but with added zeros to make the 
variable of 4 digits and if the variable is already of 4 digits 
then it should stay like this without adding zeros Take the following as an example     
num1 = "9"
num2 = "15"
num3= "130"
num4 = "1500"
# Needed Output 
# 0009
# 0015 
# 0130 
# 1500 
"""
#--------------------------------------------------------------#
num1 = "9"
num2 = "15"
num3= "130"
num4 = "1500"

print(num1.zfill(4))
print(num2.zfill(4))
print(num3.zfill(4))
print(num4.zfill(4))
