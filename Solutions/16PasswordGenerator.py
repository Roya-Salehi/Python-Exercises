import random
import string
lenght = int(input("Enter the lenght of the password: "))
passw = "".join(random.choices(string.ascii_letters +
                string.digits + string.punctuation, k=lenght))
print(passw)
