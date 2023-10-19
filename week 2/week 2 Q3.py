Number_Students = int(input("how many students are there"))
Group_Size = int(input("what is the group sizes"))

Full_Groups = (Number_Students // Group_Size)
Remainder_Students = (Number_Students % Group_Size)

print ("there will be", Full_Groups, "full groups")
print ("there will be", Remainder_Students, " students left over")
