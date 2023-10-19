BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
password = input("Enter a new password")
password_Repeat = input("enter the password again")

if password == password_Repeat and 8 <= len(password ) <= 12 and password not in BAD_PASSWORDS:
    print ("password set")
else:
    print ("error, password isnt valid")
