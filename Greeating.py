import time

Time =time.strftime("%H:%M:%S")
hur = time.strftime("%H")
min = time.strftime("%M")
sec = time.strftime("%S")

if 0 < int(hur) < 12:
    print("GOOD MORNING SIR","[",Time,"]")
elif int(hur) == 12:
    print("GOOD AFTER NOON SIR","[",Time,"]")

elif 13 <= int(hur) <= 18:
    print("GOOD EVENNING SIR","[",Time,"]")
else:
    print("GOOD NIGHT SIR","[",Time,"]")