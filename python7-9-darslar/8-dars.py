# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 21:52:03 2023

12 - dars

@author: Solijon  Haydarov

FOR LOOP | for tsikli
"""
mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar: #mehmonlar ro'yhatini ichidagi har bir mehmon uchun manabu kodni takrorla
    print("Salom", mehmon) #for badani
    
#FOR qanday ishlaydi
    
mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
    print("Hurmat bilan, Palonchiyevlar oilasi\n")


# Sonlar ustida amallar

sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")

sonlar = list(range(11)) # 1 dan 10 gacha sonlar ro'yxatini yaratamiz
sonlar_kvadrati =[] # bo'sh ro'yxat yaratamiz
for son in sonlar:  # sonlar dagi har bir son uchun
    sonlar_kvadrati.append(son**2) # uning kv.ni hisoblab, sonlar_kvadrati ga yuklaymiz

print(sonlar)
print(sonlar_kvadrati)

# for va input

dostlar = [] # bo'sh ro'yxat
print("5 ta eng yaqin do'stingiz kim?")
for n in range(5): # n bu yerda 0 dan 4 gacha qiymatlar oladi
    dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
print(dostlar)


# Uyga Vazifa

# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing

ismlar = ['Solijon', 'Dilmurod', 'Bilolbek', 'Farruh', 'Sanjar']
for ism in ismlar:
    print("Salom", ism)
    
#Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)

print(f"Kod {len(ismlar)} marta takrorlandi!")


#10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
toqson = list(range(11, 100, 2))
for son in toqson:
    print(son**3)



# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring
kinolar = []
print("5 ta eng sevimli filmingizni kiriting ")
for kino in range(5):
    kinolar.append(input(f"{kino+1}-filmingizni kiritng:  "))
print(kinolar)

#Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
odam_soni = int(input("Bugun nechta odam bilan uchrashdingiz?>>>"))
insonlar = []
for n in range(odam_soni):
    insonlar.append(input(f"{n+1} - suhbatlashgan insonning ismini kiriting>>>"))
print(insonlar)
























