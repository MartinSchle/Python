f_num = input("Napiš první číslo : ")
s_num = input("Napiš druhé číslo : ")
oper = input ("Sčítání = 1\nOdčítání = 2\nNásobení = 3\nDělení = 4\nNapiš operaci kterou chceš udělat : ")
print(oper)

oper = int(oper)
f_num = int(f_num)
s_num = int(s_num)

if oper == 1:
    print("Vaše číslo je :",f_num + s_num)
elif oper == 2:
    print("Vaše číslo je :",f_num - s_num)
elif oper == 3:
    print("Vaše číslo je :",f_num * s_num)
elif oper == 4:
    print("Vaše číslo je :",f_num / s_num)
