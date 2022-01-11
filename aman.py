import random

print("random")
print()

connect = True

while connect == True:
    a = input("1 num:")
    print()
    b = input("2 num")
    print()
    if b < a:
        print("b cant be less than a")
        continue

    finish = random.randint(int(a), int(b))

    print("random num:", int(finish))
    print()

input()
