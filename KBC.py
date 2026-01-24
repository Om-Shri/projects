list = ["1)Who is the father of physics?\nA)Geleogelile,B)AARYABATH,C)Mendal,D)Thomas alwa adition ",
"2)who is the CM of bihar ?\nA)Modi,B)Nitesh,C)Murmu,D)NOTE",
"3)who is the national bird of india?\nA)Peacock,B)Dog,C)Lion,D)Cow",
"4)what is the formula of Xcom for two masses?\nA)M/A,B)D*L,C)w/D,D)NOTA",
"5)what is colour of sky?\nA)BLUE,B)BLACK,C)WHITE,D)RANBOW"
]

to_ans = ("A","B","A","D","A")

print("------------AApka swagat hai kon banega karor pati mai------------")
print("------------aapka pehla question hai yeh---------------")


total = 0
i = 0
while i < len(list):
    print(list[i])
    ans = str(input("CHOOSE THE CORRECT ANS (A,B,C,D) :"))
    if ans.upper() == to_ans[i]:
        total += 2000000
        print("aap jeet cuke hai 20L RS  tatal amount =",total)
        i += 1
    else:
        print(" Affsos hai ke aapka jawab galat hai aap sab paise haar cuke hai", "RS = 000")
        break

if total == 10000000:
    print("----------------Badhaye ho aap jeet cuke 'KBC'---------------total amount =",total)

