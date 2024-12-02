import string
import random
length = 7
ran = "".join(random.choices(string.ascii_letters + string.digits, k = length))
print("The randomly generated string is: " + str(ran))