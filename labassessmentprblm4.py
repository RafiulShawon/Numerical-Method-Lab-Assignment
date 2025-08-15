#check a Uppercase and lowercase 

character=input("Enter a character:")

if len(character)!=1 :
    print ("Enter only one character")
else:
    if character.isupper():
        print("the letter is uppercase")

    elif character.islower():
        print("The letter is lowerCase")   

    else:
        print("Special Character")     
