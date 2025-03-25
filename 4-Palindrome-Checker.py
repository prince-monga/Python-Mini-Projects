#Palindrome Checker 

#step1: Ask the user to enter a word or phrase.
value=input("Enter a word or phrase:").lower()

#step 2: Reverse the string using string slicing 
Reverse_value=value[::-1]

#step 3: Compaer reverse vale and original value 
if Reverse_value == value:
    print("It is Palindrome.")
else:
    print("It is Not Palindrome.")
