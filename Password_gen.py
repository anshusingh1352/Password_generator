import random
import string

#generating a random password length with user entered length
def gen_pass():
    string_length = int(input("Enter the length of the password: "))
    all = string.ascii_lowercase + string.ascii_uppercase + string.digits
    temp = random.sample(all,string_length)
    password = "".join(temp)
    print("Pass: ",password)
    return password



