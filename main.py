#1-misol
i = 1
while i < 11:
    print(i)
    i = i + 1
    
#2-misol
while True:
    son = int(input("Son kiriting (chiqish uchun 0): "))
    if son == 0:
        break
    print(son)

#3-misol
while True:
    son = int(input("Musbat son kiriting: "))

    if son > 0:
        print("Rahmat! Siz musbat son kiritdingiz:", son)
        break
    else:
        print("Noto‘g‘ri, qaytadan kiriting")

#4-misol
i = 1
while i <= 5:
    print("Salom Dunyo")
    i = i + 1

#5-misol
i = 2
while i <= 100:
    print(i)
    i = i + 2

#6-misol
n = int(input("N sonini kriting: "))

yigindi = 0
i = 1

while i <= n:
    yigindi += i
    i += 1

print("1 dan", n, "gacha bo'lgan sonlar yig'indisi:", yigindi)
