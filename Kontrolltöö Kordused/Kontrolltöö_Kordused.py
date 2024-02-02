#1
import random


n=int(input("1 kuni 9:"))
for i in range(n):
    print(" ~~~~~")
    print("/_____\ ")
    print("| []  |")
    print(" -----")
#2
while True:
    try:
            o=int(input("Sisesta õpilaste arv ühes klassis: "))
            o=o*2
            s=0
            for x in range(1, o+1):
                h=random.randint(1,100)
                print(f"Õpilane {x}: {h}")
                s=s+h
            s=s/o
            print(f"Keskmine hinnang: {s}")
            break
    except:
        print("Vale Andmetüüp")
#3﻿
õpilased = 30 
maksimaalne = 5
minimmalne = 1
for i in range(õpilased):
    hinned = random.randint(100,500)/100
    print(hinned)
    if hinned > maksimaalne:
        maksimalne = hinned
    elif hinned < minimaalne:
        minimaalne = hinned
print("Maksimaalne hind on:", maksimaalne)
print("Minimaalne hind on:", minimaalne)

#4
s2=0
n2=0
for x in range(1,13):
    S=random.randint(5,10)
    n=random.randint(20000,50000)
    print(f"Maakond {x}:\nElanikud: {n}\nVäljak: {S} km2")
    print()
    s2=s2+S
    n2=n2+n
p=n2//s2
print(f"Piirkondlik rahvastikutihedus: {p}")

#5
while True:
    try:
        min=int(input("Sisesta minimaalne väärtus: "))
        max=int(input("Sisesta maksimaalne väärtus: "))
        s=int(input("Sisesta samm: "))
        print("y=-0.5x+x")
        print()
        for x in range(min, max, s):
            y=-0.5*x+x
            print(f"x={x}\ny={y}")
            print()
        break
    except:
        print("Vale Andmetüüp") 
 
