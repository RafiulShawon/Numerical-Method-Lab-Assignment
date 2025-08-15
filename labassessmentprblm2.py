#Reverse a string using a loop
string=input("Enter the string:")

reversed_str=" "

for char in string:
    reversed_str=char+reversed_str

print("The reversed string is:",reversed_str)
