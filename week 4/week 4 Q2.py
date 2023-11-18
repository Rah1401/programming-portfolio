def case_count(string):
    upper_char = 0
    lower_char = 0

    for char in string:
        if char .isupper():
            upper_char = upper_char + 1
        elif char .islower():
            lower_char = lower_char + 1
    return upper_char, lower_char

string = input("enter sentence with only characters")

upper_char, lower_char = case_count(string)

print ("there are", upper_char, " uppercase characters in this string")
print ("there are", lower_char, " lowercase characters in this string")


