znamky = [[3,1], [3,2], [3,1], [10,3], [4,4]]
prvni_cisla = []

for z in znamky:
    prvni_cisla.append(z[0])

pocet_vah = sum(prvni_cisla)

nasobek = [x * y for x, y in znamky]
nasobek = sum(nasobek)

prumer = nasobek / pocet_vah
prumer = round(prumer, 2)

print("Průměr je :",prumer)