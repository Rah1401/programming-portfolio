Sweets = int(input("how many sweets are in the box"))
Students = int(input("how many students are in the class"))

Average_Sweets = (Sweets // Students)
Sweets_Remaining = (Sweets % Students)

print ("each student will get", Average_Sweets, "and there will be", Sweets_Remaining, "sweets left")

