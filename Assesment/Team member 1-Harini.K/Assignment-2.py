import random
while(True):
    a=random.randint(10,99)
    b=random.randint(10,99)
    if(a>30 and b>60):
        print("High temperature and humidity of:",a,b,"%","alarm is on")
    elif(a<35 and b<60):
        print("Normal temperature and humidity of:"a,b,"%","alarm is off")
