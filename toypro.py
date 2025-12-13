print("1 : 전원\n2 : 온도증가\n3 : 온도감소\n4 : 바람증가\n5 : 바람감소\n6 : 종류")
wind = 1
temp = 25
while True:   
    a = int(input())
    if a==1 :
        print("에어컨이 켜집니다.")
        print(f"바람은: {wind}")
        print(f"온도는: {temp}")
    elif a == 2 :
        temp += 0.5
        print(f"바람은: {wind}")
        print(f"온도는: {temp}")
    elif a == 3 :
        temp -= 0.5
        print(f"바람은: {wind}")
        print(f"온도는: {temp}")
    elif a == 4 :
        if wind < 5 :
            wind += 1
        print(f"바람은: {wind}")
        print(f"온도는: {temp}")
    elif a == 5 :
        if wind > 1 :
            wind -= 1
        print(f"바람은: {wind}")
        print(f"온도는: {temp}")
    elif a == 6 :
        break