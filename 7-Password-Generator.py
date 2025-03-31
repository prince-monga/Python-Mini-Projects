#7- Password generater

#Step 1: import modules
import string
import random
#Step 2: Create function for Password length and generate
def Pass_Generator(length):
    lower=string.ascii_lowercase    # a-z
    upper=string.ascii_uppercase    # A-Z
    digit=string.digits              # 0-9
    special=string.punctuation      # special characters
    
    #Step 3: Create empty list and combine all string 
    S=[]
    S.extend(lower)
    S.extend(upper)
    S.extend(digit)
    S.extend(special)
    # print(S)
    random.shuffle(S)
    print("".join(S[0:length]))
    
# Get desired password length from user
Pass_Generator(int(input("Enter length of Password:")))
    
