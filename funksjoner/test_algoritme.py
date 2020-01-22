print("Diamant eksempel")
storrelse = int(input("Størrelse: "))
for y in range(storrelse):
    for x in range(storrelse):
        if x == storrelse-y-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
