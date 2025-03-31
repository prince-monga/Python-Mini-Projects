#8- Email Slicer

#Step 1: Take input
email=input("Enter Your Email:")
#Step 2: Check @ is avilable in email
if '@' in email:
    
    parts=email.split('@')  #split email @ befor and after
    #Step 3: Check Domain [in which (.) check]
    if '.' in parts[1]:
        username=parts[0]
        domain=parts[1]
        print("User Name:",username)
        print("Domain:",domain)
    else:
        print("Invaild email format!")

else:
    print("Please enter a vaild email address.")