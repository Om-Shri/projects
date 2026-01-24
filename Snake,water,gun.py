from random import choice

print("-------WELCOME TO SNAKE WATER GUN GAME-------")

game = ["snak","water","gun"]
youdict = {"s" : 0 ,"w" : 1 ,"g" : 2,"e" : -1}
reversedict = {0 : "Snak" , 1 : "Water",2 : "Gun"}
p_point = 0
c_point = 0
round = 1

while True:
    try:
        print(f"ROUND - {round}")
        
        you = input("chose the [snake for (s)], [water for (w)], [gun for (g)], [for exit(e)]:").lower()
        player = youdict[you]
        computer = choice(game)
        
        if player >2 or player <-1:
            print("\"ERROR\"  enter valide no (-1 to 2)")
            continue
        if player == -1 :
            break

        print(f"You chose {reversedict[player]}\nComputer chose {computer}")

        if game[player] == computer:
            print(f"Tie try again")
        elif game[player] == "snak" and computer == "water":
            p_point += 1
            c_point -= 1
            print(f"you win , you = {p_point},com = {c_point}",)
        elif game[player] == "water" and computer == "gun":
            p_point+= 1
            c_point -= 1
            print(f"you win ,you = {p_point},com = {c_point}",)
        elif game[player] == "gun" and computer == "snak":
            p_point += 1
            c_point -= 1
            print(f"you win ,you = {p_point},com = {c_point}",)
        else:
            p_point -= 1
            c_point += 1
            print(f"you lost ,you = {p_point},com = {c_point}",)
        round += 1
    except Exception:
        print("'Errer'enter valid value(s/w/g).")

print(f"Game end! your total point in  {round}-rounds: You = {p_point},Com = {c_point}")
