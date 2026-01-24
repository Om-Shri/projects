print("WELCOME TO SECRATE COAD CENTER ` `")
while True:
    a = int(input("code(1) or decode(0) :"))


    if a == 1:
        message = input("enter your message :")

        replacement = { "a":"'0+1'" , "e":"'3+1'" , "i":"'1+1'" , "o":"'8+1'" , "u":"'4+1'" ,
        "2":"'a-1'" , "5":"'u+1'" , "6":"'u+2'" , "7":"'o-1'" , "9":"'o+1'" }


        for old,new in replacement.items():
            message = message.replace(old,new)

        list = message.split(" ")
        list.reverse()
        finaly = " ".join(list)

        with open ("message.txt","w") as f:
            f.write(finaly)

    elif a == 0:

        with open("message.txt","r") as f: 
                finaly = f.read()

        replacement = { "a":"'0+1'" , "e":"'3+1'" , "i":"'1+1'" , "o":"'8+1'" , "u":"'4+1'" ,
        "2":"'a-1'" , "5":"'u+1'" , "6":"'u+2'" , "7":"'o-1'" , "9":"'o+1'" }
        for old,new in replacement.items():
            finaly = finaly.replace(new,old)

        list = finaly.split(" ")
        list.reverse()
        message = " ".join(list)

        print(message)       
