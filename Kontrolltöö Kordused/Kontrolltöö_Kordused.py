##1
#import random


#n=int(input("1 kuni 9: "))
#for i in range(n):
#    print(" ~~~~~")
#    print("/_____\ ")
#    print("| []  |")
#    print(" -----")

##2
#while True:
#    try:
#            o=int(input("Sisesta õpilaste arv ühes klassis: "))
#            o=o*2
#            s=0
#            for x in range(1, o+1):
#                h=random.randint(1,100)
#                print(f"Õpilane {x}: {h}")
#                s=s+h
#            s=s/o
#            print(f"Keskmine hinnang: {s}")
#            break
#    except:
#        print("Vale Andmetüüp")
##3﻿
#õpilased = 30 
#maksimaalne = 5
#minimmalne = 1
#for i in range(õpilased):
#    hinned = random.randint(100,500)/100
#    print(hinned)
#    if hinned > maksimaalne:
#        maksimalne = hinned
#    elif hinned < minimaalne:
#        minimaalne = hinned
#print("Maksimaalne hind on:", maksimaalne)
#print("Minimaalne hind on:", minimaalne)

##4
#s2=0
#n2=0
#for x in range(1,13):
#    S=random.randint(5,10)
#    n=random.randint(20000,50000)
#    print(f"Maakond {x}:\nElanikud: {n}\nVäljak: {S} km2")
#    print()
#    s2=s2+S
#    n2=n2+n
#p=n2//s2
#print(f"Piirkondlik rahvastikutihedus: {p}")

##5
#while True:
#    try:
#        min=int(input("Sisesta minimaalne väärtus: "))
#        max=int(input("Sisesta maksimaalne väärtus: "))
#        s=int(input("Sisesta samm: "))
#        print("y=-0.5x+x")
#        print()
#        for x in range(min, max, s):
#            y=-0.5*x+x
#            print(f"x={x}\ny={y}")
#            print()
#        break
#    except:
#        print("Vale Andmetüüp") 

#1.1
#while True:
#    try:
#        mitu=int(input("Mitu tk: "))
#        if 1<=mitu<18:
#            break
#    except ValueError:
#        print("Vale tüüp")

#for i in range(mitu):
#    print(' /V\ '.center(10,' '),end="")
#print()
#for i in range(mitu):
#    print(' / V \ '.center(10,' '),end="")
#print()

#4
#from random import *


#sum_num=0
#sum_km=0
#for i in range(12):
#    number=randint(1000,100000)
#    km=randint(1,1000)
#    sum_num+=number
#    sum_km+=km
#    print(f"{i}. maakond. \nElanikud: {number}. Pindala: {km}\n Kokku: {sum_num},{sum_km}")
#    vastus=sum_num/sum_km
#    print(f"keskmine: {vastus:.3f}")

#3
#from random import *
#N=25
#kesk1=0
#kesk2=0
#for i in range(N):
#    h1=randint(1,5)
#    h2=randint(1,5)
#    kesk1+=h1
#    kesk2+=h2
#kesk1/=N
#kesk2/=N
#print(f"Keskmine hinne 1 klassis on {kesk1}")
#print(f"Keskmine hinne 2 klassis on {kesk2}")

#5
from random import *


while True:
    try:
        k=int(input("Mitu kotleti sul on? "))
        if k>0: break
    except ValueError:
        print("Vale tüüp")
while True:
    try:
        m=int(input("Mitu kotleti ühel pannil? "))
        if m>0: break
    except ValueError:
        print("Vale tüüp")
pann=0
lisapann=0
while k>0:
    if k>=m:
        k-=m
        pann+=1
    elif k<m:
        lisapann+=1
print(f"Täispannid: {pann} ja veel on vaja {lisapann}")
print()
