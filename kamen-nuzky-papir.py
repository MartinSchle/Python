import random

def kamen_nuzky_papir():
    moznosti = ["kámen", "nůžky", "papír"]

    while True:
        print("Vyber kámen, nůžky nebo papír (nebo zadej 'konec' pro ukončení hry):")
        volba_hrace = input().lower()

        if volba_hrace == 'konec':
            break  

        if volba_hrace not in moznosti:
            print("Neplatná volba. Zkus to znovu.")
            continue  

        volba_pocitace = random.choice(moznosti)

        print(f"Tvá volba: {volba_hrace}")
        print(f"Volba počítače: {volba_pocitace}")

        if volba_hrace == volba_pocitace:
            print("Remíza!")
        elif (volba_hrace == "kámen" and volba_pocitace == "nůžky") or \
             (volba_hrace == "nůžky" and volba_pocitace == "papír") or \
             (volba_hrace == "papír" and volba_pocitace == "kámen"):
            print("Vyhrál jsi!")
        else:
            print("Počítač vyhrál!")

kamen_nuzky_papir()