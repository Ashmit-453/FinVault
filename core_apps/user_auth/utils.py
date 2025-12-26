import random,string

def generate_otp(length):
    return "".join(random.choices(string.digits,k=length))
