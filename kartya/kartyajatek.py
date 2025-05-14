import random
print("Üdvözöllek a 21 kartyajatekban")
jatekmod = input("kivel szeretnéd játszani a játékot gép vagy játékos ellen:")
if jatekmod == "gép":
    robotpontszama = random.randint(2 ,30)
    jatekoskartya1 = random.randint(2 ,11)
    jatekoskartya2 = random.randint(2 ,11)
    jatekosvegsopontszam = jatekoskartya1 + jatekoskartya2
    print(f"Ez az első kártyád pontszáma: {jatekoskartya1}")
    print(f"Ez a második kártyád pontszáma: {jatekoskartya2}")
    print(f"A gép ennyi pontot szerzett összesen: {robotpontszama}")
    print(f"Ez az általad összesen elért pontszám: {jatekosvegsopontszam}")
    if jatekosvegsopontszam == 21:
        print("Gratulálok nyertél")
    elif jatekosvegsopontszam > robotpontszama:
        print("nyertél")
    elif jatekosvegsopontszam < robotpontszama:
        print("vesztettél")
    elif robotpontszama == 21:
        print("A gép nyert:(")
if jatekmod == "játékos":
    print("asdd")