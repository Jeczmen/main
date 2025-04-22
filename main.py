"""
Autor: Tomáš Ječmínek
Email: jecminek.tomas@gmail.com
Projekt: Tic-tac-toe
"""

def pozdrav():
    print("Vítej ve hře Piškvorky!")
    print("Hrajeme na poli 3x3. Hráč 1 má symbol X, hráč 2 má symbol O.")
    print("Cílem hry je umístit 3 své symboly vedle sebe (horizontálně, vertikálně nebo diagonálně).")
    print("Pro výběr pole napiš číslo od 1 do 9 podle následujícího rozložení:")
    zobraz_pole([str(i) for i in range(1, 10)])

def zobraz_pole(pole):
    print()
    for i in range(0, 9, 3):
        print(f" {pole[i]} | {pole[i+1]} | {pole[i+2]} ")
        if i < 6:
            print("---|---|---")
    print()

def je_vitez(pole, znak):
    kombinace = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # řádky
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # sloupce
        [0, 4, 8], [2, 4, 6]              # diagonály
    ]
    for kombinace_tahu in kombinace:
        if all(pole[i] == znak for i in kombinace_tahu):
            return True
    return False

def je_remiza(pole):
    return all(p in ['X', 'O'] for p in pole)

def vyber_pole(pole, hrac):
    while True:
        try:
            volba = int(input(f"Hráč {hrac} ({'X' if hrac == 1 else 'O'}), zvol číslo pole (1–9): "))
            if volba < 1 or volba > 9:
                print("Zadej číslo od 1 do 9.")
            elif pole[volba - 1] in ['X', 'O']:
                print("Toto pole je již obsazené. Zvol jiné.")
            else:
                return volba - 1
        except ValueError:
            print("Neplatný vstup! Zadej číslo od 1 do 9.")

def hlavni():
    pozdrav()
    pole = [str(i) for i in range(1, 10)]
    aktualni_hrac = 1
    znak_hrace = {1: 'X', 2: 'O'}

    while True:
        zobraz_pole(pole)
        index = vyber_pole(pole, aktualni_hrac)
        pole[index] = znak_hrace[aktualni_hrac]

        if je_vitez(pole, znak_hrace[aktualni_hrac]):
            zobraz_pole(pole)
            print(f"Hráč {aktualni_hrac} vyhrál! Gratulujeme!")
            break
        elif je_remiza(pole):
            zobraz_pole(pole)
            print("Remíza! Nikdo nevyhrál.")
            break

        aktualni_hrac = 2 if aktualni_hrac == 1 else 1

if __name__ == "__main__":
    hlavni()