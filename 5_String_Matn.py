# =============================================================================
# STRING (MATN)
# =============================================================================

# STRING ma'lumot turi va uning ustida amallar

# =============================================================================
# STRING VA UNICODE
# =============================================================================

# STRING (matn) —Pythondagi eng mashxur ma'lumot turlaridan biri. Avvalgi 
# darsda ko'rganimizdek, o'zgaruvchiga matn yuklash uchun matn 
# qo'shtirnoq (" ") yoki birtirnoq (' ') ichida yozilishi kerak.

# shahar = "Қўқон"
# viloyat = 'Фарғона'



# Pythonda matnlar Unicode jadvalidagi istalgan belgilaridan iborat bo'lishi 
# mumkin (jumladan o'zbek, arab, hind, xitoy alifbosidagi harflar yoki turli 
# emoji-smayliklar). 

# unicode haqida batafsil quyidagi manzilda:
# https://unicode-table.com/en/

# matn = "Men yangi 📱 oldim®™©"
# print(matn)

# =============================================================================
# STRING USTIDA AMALLAR
# =============================================================================

# Matnlarni qo'shish operatori (+)

# Matnlarni qo'shish uchun + operatoridan foydalanmiz:

# ism = 'Ahmad'
# print("Mening ismim " + ism)

# ism = 'Ahad'
# familiya = 'Qayum'
# print(familiya + " " + ism)

# Yuqoridagi kodda ism va familiya orasiga bo'shliq belgisini qo'shmaganimiz 
# uchun ikki matn qo'shilib yozildi. Buni to'g'rilash uchun, 3-qatorni 
# quyidagicha yozamiz:

# ism = 'Ahad' # biz istagan ism. aynan Ahad emas
# familiya = 'Qayum' # biz istagan familiya. Aynan Qayum emas
# print(ism + ' ' + familiya) # ikki o'zgaruvchi orasiga bo'sh joy qo'shamiz

# =============================================================================
# f-string
# =============================================================================

# Ikki (va undan ko'p) matn ko'rinishidagi o'zgaruvchilarni birlashtirish 
# uchun f-string usulidan  f"{matn1} {matn2}" ham foydalansak bo'ladi:

# ism = "Ahad"
# familiya = 'Qayum'
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif)

# Bu usul yordamida uzun matnlarni ham yasash mumkin:

# ism = "James"
# familiya = 'Bond'
# taxallus = "Agent 007"
# print(f"Salom, mening ismim {familiya}. {ism} {familiya}!")

# print(f"Hi, my name is {familiya}. {ism} {familiya} {taxallus}")

# =============================================================================
# Mahsus belgilar
# =============================================================================

# Matnga bo'shliq qo'shish uchun \t belgisidan, 
# yangi qatordan boshlash uchun \n belgisidan foydalanamiz:

# print('Hello World!')
# print('Hello\tWorld!') # \t bilan
# print('Hello\nWorld!') # \n bilan

# =============================================================================
# STRING METODLARI
# =============================================================================

# Pythonda string ustida amalga oshirish mumkin bo'lgan tayyor amallar to'plami
# mavjud. Bunday amallar to'plami metodlar deb ataladi. 

# Metodlarni qo'llash uchun metod nomi matndan so'ng .metod_nomi() ko'rinishida 
# yoziladi. Keling shunday metodlarning ba'zilari bilan tanishaylik.

# =============================================================================
# upper() va lower() metodlari
# =============================================================================

# upper() metodi matndagi har bir harfni katta harfga o'zgartiradi. 

# ism = 'Ahad'
# familiya = 'Qayum'
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif.upper())

# lower() metodi esa aksincha, har bir harfni kichik harfga o'zgartiradi.

# ism = 'Ahad'
# familiya = 'Qayum'
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif.lower())

# =============================================================================
# title() va capitalize() metodlari
# =============================================================================

# title() metodi matndagi har bir so'zning birinchi harfini katta harf bilan yozadi.

# ism_sharif = 'james bond'
# print(ism_sharif.title())

# capitalize() esa faqatgina eng birinchi so'zning birinchi harfini 
# katta bilan yozadi.

# ism_sharif = 'james bond'
# print(ism_sharif.capitalize())


# Metodlarni faqat o'zgaruvchilarga emas, balki to'g'ridan-to'g'ri matnga 
# ham qo'llash mumkin (aslida o'zgaruvchi ham matnning (yoki boshqa ma'lumotning)
# manzili xolos)

# print('james bond'.upper())

# =============================================================================
# strip(), rstrip() va lstrip() metodlari
# =============================================================================

# Bu metodlar matnning boshi va oxiridagi bo'sh joylarni olib tashlaydi.
# lstrip() — matn boshidagi bo'shliqni,
# rstrip() – matn oxiridagi bo'shliqni,
# strip() — matn boshi va oxiridagi bo'shliqlarni olib tashlaydi

# meva = "     olma     "
# print("Men " + meva.lstrip() + " yaxshi ko'raman")
# print("Men " + meva.rstrip() + " yaxshi ko'raman")
# print("Men " + meva.strip() + " yaxshi ko'raman")
# print("Men " + meva + " yaxshi ko'raman")

# Matnlar bilan ishlaydigan metodlar ko'p. Ularning ba'zilari bilan kelajakda
# yana tanishamiz, to'liq ro'yhatni esa quyidagi sahifada ko'rishingiz mumkin:
# https://www.w3schools.com/python/python_ref_string.asp

# Metodlar o'zgaruvchi ichidagi asl matnni o'zgartirmaydi!

# =============================================================================
# INPUT —FOYDALANUVCHI BILAN MULOQOT
# =============================================================================

# Shu paytgacha biz o'zgaruvchilarning qiymatini dasturning ichida berayotgan 
# edik. Keling endi qiymatni o'zimiz emas, balki dastur foydalanuvchilariga 
# kiritish imkonini beramiz. 

# Buning uchun input() funktsyasidan foydalanamiz. 

ism = int(input("Ismingiz nima? \n"))
print(f"Assalom alaykum, + {ism}")

# Yuqoridagi dastur, avval 1-qatorda foydalanuvchining ismini so'raydi. 
# Foydalanuvchi ismini kiritib, Enter tugmasini bosgach, foydalanuvchi 
# kiritgan matnism degan o'zgaruvchiga yuklanadi va dasturining
# 2-qatori bajaradi:

# Keling yuqoridagi kod va uning natijasini chiroyliroq ko'rinishga keltiramiz.

# ism = input("Ismingiz nima?\n>>> ") # Foydalanuvchi ismini yangi qatordan kiritadi
# print("Assalom alaykum, " + ism.title())

# =============================================================================
# AMALIYOT
# =============================================================================

# Quyidagi mashqlarni bajaring:

# =============================================================================
# Quyidagi o'zgaruvchilarni yarating: 
# 
# kocha="Bog'bon"
# 
# mahalla="Sog'bon"
# 
# tuman="Bodomzor" 
# 
# viloyat="Samarqand"
# =============================================================================

# =============================================================================
# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
# =============================================================================

# =============================================================================
# Yuqoridagi o'zgaruvchilarning (kocha, mahalla, tuman, viloyat) qiymatini 
# foydalanuvchidan so'rang. Va avvalgi mashqni takrorlang.
# =============================================================================

# =============================================================================
# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi 
# qatordan yozing
# =============================================================================

# =============================================================================
# Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan 
# o'zgaruvchiga yuklang
# =============================================================================

# =============================================================================
# manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() 
# metodlarini qo'llab ko'ring.
# =============================================================================
