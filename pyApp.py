from ast import Pass


class IBM:
    def get_processor_speed(self):
        print("16GHz")

    def register_user(self, email, password, otp=None, key_code=None):
        if (keycode!=None):
            print(f"Your Email Addres is: {email}")


    def login(self, username, password):
        print("Login is in Progress...")

    def login(self, username, password, otp=None):
        print("Login with OTP in Progress...")

class Nyawira(IBM):
    def get_processor_speed(self):
        # email,password and OTP
        print("32GHz")

ibm =IBM()
ibm.get_processor_speed()
nyawira = Nyawira()
nyawira.get_processor_speed()

# ibm.login("username", "password")