# Error message:
# Syntax Error: unterminated string literal
# line 1
#    print(My age is:", age)
# Name Error: name 'age' is not defined
#
# What caused the error:
# I tried to print the variable age before assigning it a value. Also, I forget to put My age is in double quotation as a string.
#
# How I fixed it:
# I defined age =25 before using it in the print statement. Also, put double quotation beginning and ending the statement "My age is:"

age = 25
print("My age is:" , age)
