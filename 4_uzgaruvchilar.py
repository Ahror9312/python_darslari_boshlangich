# =============================================================================
# O'ZGARUVCHILAR
# =============================================================================

# Pythonda o'zgaruvchilar bilan ishlashni o'rganamiz

# =============================================================================
# O'ZGARUVCHI (VARIABLE)
# =============================================================================

# O'zgaruvchi —kompyuter xotirasida ma'lum bir qiymatni saqlash uchun ajratilgan 
# joy. Soddaroq qilib tushuntirsak, o'zgaruvchini quti, quti ichidagi narsani esa 
# qiymat deb tasavvur qilish mumkin. Pythonda qiymatlar son, matn, ro'yxat va 
# hokazo ko'rinishida bo'lishi mumkin.

# ctrl+c       kopirovat      (nusxalash)
# ctrl+v       vistavit       (qo'yish)

# Quyidagi misolga e'tibor bering, biz 2 ta o'zgaruvchi yaratdik (ism va yosh) 
# va ularga qiymatlar yukladik (Pythonda boshqa tillardagi ka'bi o'zgaruvchilarni 
# avvaldan e'lon qilish yo'q):

# ism = "Abdulloh"
# yosh = 25
# print(ism)
# print(yosh)

# O'zgaruvchi (variable) bunday deyilishiga sabab, uning qiymati istalgan vaqt 
# o'zgartirilishi mumkin:

# ism = "Abdulloh"
# print(ism)
# ism="Muhammad"
# ism="Nurbek"
# print(ism)


# xotdog=25000            # 1-amal
# print(xotdog)           # 2-amal
# xotdog=xotdog+10000     # 3-amal
# print(xotdog)           # 4-amal
# Yuqoridagi misolda ism nomli o'zgaruvchiga avval Abdulloh keyin esa Muhammad 
# qiymatlarini berdik.

# =============================================================================
# O'ZGARUVCHILARNI NOMLASH
# =============================================================================

# =============================================================================
# O'zgaruvchilarga nom berishda quyidagi qoidalarga amal qiling:
# 
# O'zgaruvchi nomi harf yoki pastki chiziq (_) bilan boshlanishi kerak
# 
# O'zgaruvchi nomi raqam bilan boshlanishi mumkin emas. raqam bilan tugatish mumkin
# 
# O'zgaruvchi nomida faqatgina lotin alifbosi harflari (A-z), raqamlar (0-9) 
# va pastki chiziq (_) qatnashishi mumkin
# 
# O'zgaruvchi nomida bo'shliq (пробел) bo'lishi mumkin emas
# 
# O'zgaruvchi nomida katta-kichik harflar turlicha talqin qilinadi 
# (ism, ISM, va Ism uchta turli o'zgaruvchi)
# =============================================================================

# Qo'shimcha qoida sifatida: 
# O'zgaruvchi nomini kichik harflar bilan yozing. 

# O'zgaruvchi nomida 2 va undan ortiq so'z qatnashsa ularning orasini pastki 
# chiziq (_) bilan ajrating (ism_sharif="Ahror Ahmedov")

# O'zgaruvchiga tushunarli nom bering (y=20 emas yosh=20, 
# d="Korea" emas davlat = "Korea" va hokazo)

# =============================================================================
# Shuningdek o'zgaruvchilarga Pythonda ishlatiladigan funktsiyalar va 
# maxsus kalit so'zlarning (keywords) nomini bermang. Kalit so'zlar
# ro'yhatini ko'rish uchun Spyder konsolida avval help() deb yozing va 
# Enter tugmasini bosing. Keyin esa keywords deb kiritib, yana Enter bosing. 
# Marhamat, ekraningizda Pythondagi maxsus kalit so'zlar ro'yhatini ko'ryapsiz:
#     
# False               class               from                or
# None                continue            global              pass
# True                def                 if                  raise
# and                 del                 import              return
# as                  elif                in                  try
# assert              else                is                  while
# async               except              lambda              with
# await               finally             nonlocal            yield
# break               for                 not   
# =============================================================================


# =============================================================================
# AMALIYOT
# =============================================================================

# Quyidagi mashqlarni bajaring:

# "Hello World!" matnini yangi o'zgaruvchiga yuklang va print() yordamida 
# konsolga chiqaring

# xabar deb nomlangan o'zgaruvchiga biror matn yuklang va konsolga chiqaring, 
# keyin esa o'zgaruvchiga yangi qiymat berib uni ham konsolga chiqaring.

# class den nomlangan o'zgaruvchi yarating, unga biror qiymat bering va 
# konsolga chiqaring (siz kutgan natija chiqdimi?)

# Quyidagi kodni bajaring:
# radius = 5
# pi = 3.14159
# aylana_yuzi = pi * radius**2
# print("Radiusi" , radius, "ga teng aylananing yuzi=", aylana_yuzi)


# import math

# print(math.sqrt(64))
# print(64**(1/2))




