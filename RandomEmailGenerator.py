import random

email_services = ["yopmail","gmail","yahoo","outlook","protonmail"]
letters = "qwertyuiopasdfghjklzxcvbnm1234567890._-"
email_name=""
length = int(input("ENter length of email name:-"))
count=0
if length>0:
    for i in range(length):
        email_name  = email_name+random.choice(letters)
        count=count+1
else:
    exit(0)


print("Email Name",email_name)

email_services = random.choice(email_services)
email_id = email_name+"@"+email_services+".com"

print(email_id)