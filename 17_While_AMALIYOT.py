# =============================================================================
# Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. 
# Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating
# =============================================================================

# savol = "Sevgan kitobingizni kiriting"
# savol += "(barcha kitoblarni kiritib bo'lgach 'exit' deb yozing): "

# while True:
#     kitob = input(savol)
#     if kitob == 'exit':
#         break
# print('Rahmat!')       



# =============================================================================
# Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan
#   yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 
#   dan kattalarga bepul. Shunday while tsikl yozingki, dastur foydalanuvchi 
#   yoshini so'rasin va chipta narhini chiqarsin. Foydalanuvchi exit yoki quit deb 
#   yozganda dastur to'xtasin (ikkita shartni ham tekshiring).
# =============================================================================

# Muzeyga chipta narhi foydalanuvchining 
# yoshiga bog'liq: 
# 7 dan yoshlarga - 2000 so'm, 
# 7-18 gacha 3000 so'm, 
# 18-65 gacha 10000 so'm, 
# 65 dan kattalarga bepul. 
# Shunday while tsikl yozingki, 
# dastur foydalanuvchi yoshini so'rasin 
# va chipta narhini chiqarsin. 
#Foydalanuvchi exit yoki quit deb yozganda 
#dastur to'xtasin (ikkita shartni ham tekshiring).

# savol = "Yoshingizni kiriting: "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
    
#     if yosh<7:
#         narh = 2000
#     elif 7<=yosh<18:
#         narh = 3000
#     elif 18<=yosh<65:
#         narh = 10000
#     else: narh = 0
    
#     if narh==0:
#         print("Sizga chipta bepul")
#     else:
#         print(f"Chipta {narh} so'm")






# =============================================================================
# Yuqoridagi dasturni turli usullarda yozib ko'ring (break, ishora, 
# yoki shart tekshirish)
# =============================================================================


# =============================================================================
# Quyidagi dasturda bir nechta mantiqiy xatolar bor. Jumladan, xusisiy 
# holatlarda tsikl abadiy qaytarilib qolmoqda. Xatolarni to'g'rilay olasizmi?
# =============================================================================



# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat=='exit':
#         break
#     elif float(qiymat)<0:
#         continue # agar foydalanuvchi manfiy son kiritsa tsiklni takrorlaymiz
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")