import Password_gen
import User_input_password

generated_pass = Password_gen.gen_pass()

user_input = User_input_password.user_input()

def verify_pass():
    if generated_pass == user_input:
        return True

    else:
        return False
