from time import *
import random as r

def mistake(peretest,usertest):
    error = 0
    for i in range(len(peretest)):
        try:
            if peretest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error

def speed_time(time_s,time_e,userinput):
    time_taken = round(time_e - time_s,2)
    letters_len = len(userinput)
    speed = round(letters_len/time_taken)
    return speed


test = ["Our life is also a story in which we face many ups and downs and at certain.",
"He saw that Ant and begged for food, but she said, When I worked hard, you enjoyed."]

print("********SPEED TEST*********","\n")

paragraph = r.choice(test)
print(paragraph,"\n")
time1 = time()
typed = input("**STARTED** \n")
time2 = time()

print(f"speed : {speed_time(time1,time2,typed)}letter/sec")
print(f"Mistakes : {mistake(paragraph,typed)}")