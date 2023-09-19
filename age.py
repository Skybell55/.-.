x = int(input("ведите возраст "))
year = x % 10
if x == 11:
    print("вам 11 лет")    
elif year == 1:
    print("вам", x, "год")
elif year < 5:
    print("вам", x, "года")
else:
    print("вам", x, "лет")
