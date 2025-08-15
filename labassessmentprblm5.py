#write a python program to determine the grade based on their mark

Num=int(input("Enter the number:"))

if Num>=90 and Num<=100 :
    print("Grade A")

elif Num>=80 and Num<=89 :
    print("Grade B")


elif Num>=70 and Num<=79 :
    print("Grade C")


elif Num>=60 and Num<=69 :
    print("Grade D")

elif Num>100:
    print("The number is out of range so there will be no grade")

else:
    print("Grade F")    
