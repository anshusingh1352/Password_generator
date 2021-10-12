import Password_gen
import User_input_password
import verify_pass



if __name__ == '__main__':
    Password_gen.gen_pass()
    User_input_password.user_input()
    final_result = verify_pass.verify_pass()

if final_result == True:
    print("You are successfully login")

else:
    print("Wrong OTP")