import random
import string

def randompwd(length):
    Lletters = string.ascii_letters
    Uletters = string.ascii_uppercase
    digits = '0123456789'
    result_str = ''.join(random.choice(Lletters) for i in range(length-3))
    result_str = result_str + ''.join(random.choice(Uletters))
    result_str = result_str + ''.join(random.choice(digits))
    result_str = result_str + ''.join(random.choice(splchar))
    print("Random string of length", length, "is:", result_str)

splchar = "!@#$%^&*()-+"
randompwd(int(input("Enter the length of the required password\n")))