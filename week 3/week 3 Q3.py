password = input("Enter a new password")
password_Repeat = input("enter the password again")

if password == password_Repeat and 8 <= len(password ) <= 12:
    print ("password set")
else:
    print ("error, password must be between 8 and 12 characters")
