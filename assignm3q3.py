
string = str(input("Enter the string "))
def lowercaseanduppercase(string):
    lowercase=0
    uppercase=0
    for i in string:
        if i.isupper():
            uppercase+=1
        elif i.islower():
            lowercase+=1
    print("No. of Upper case characters :",uppercase)
    print("No. of Lower case characters :",lowercase)
    

lowercaseanduppercase(string)







