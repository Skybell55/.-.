z = int(input("ведите температуру "))
if z < -40:
    print("возьмите шубу")
elif z < 0:
    print("возьмите шапку")
elif z < 40:
    print("вам ничего не нужно")
else:
    print("возьмите крем")
