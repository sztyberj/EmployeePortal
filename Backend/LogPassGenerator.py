import string
import random
def GeneratePassword():
    lenght = 10

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    all = lower + upper + num + symbols

    temp = random.sample(all, lenght)

    password = "".join(temp)

    return password

def GenerateLogin(first_name, last_name):
    login = first_name[0].lower() + last_name.lower()

    print(login)

GenerateLogin()