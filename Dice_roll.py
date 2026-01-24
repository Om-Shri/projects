import random

dice = [1,2,3,4,5,6]
result = []
times = 0

while True:
    choice = input("Roll the dice (y/n):")

    if choice.lower() == "y":
        num = int(input("Enter how many dice you want to roll:"))
        for i in range(1,num+1):
            a = random.choice(dice)   
            result.append(a)
        print(result)
        result.clear()
        times += 1

    elif choice.lower() == "n" :
        break

    else:
        print("invalid choice!")
        
print("Thanks for using.")
print(f"You roll dice {times} times.")