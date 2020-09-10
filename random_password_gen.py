import random
password = ""

for i in range(2):
    upper_case = chr(random.randint(65, 90))
    password += upper_case
for i in range(2):
    lower_case = chr(random.randint(97, 122))
    password += lower_case
for i in range(2):
    numbers = chr(random.randint(48, 57))
    password += numbers
for i in range(2):
    symbols = chr(random.randint(32, 47) or random.randint(58, 64) or random.randint(91, 96) or random.randint(123, 126) or random.randint(145, 149) or random.randint(152))
    password += symbols
random.randint = password
print(password)
