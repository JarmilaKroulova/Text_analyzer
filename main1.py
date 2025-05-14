TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

print("""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Jarmila Kroulová
email: jarmilxxx@seznam.cz
""")

registrovani_uzivatele = {
    "bob": "123", 
    "ann": "pass123", 
    "mike": "password123", 
    "liz": "pass123" }

ODDELOVAC = "-" *40 

pocet_textu = len(TEXTS)

uzivatel = input("username: ")
heslo = input("password: ")

if uzivatel in registrovani_uzivatele and heslo == registrovani_uzivatele[uzivatel]:
    print(f'{ODDELOVAC}\n Welcome to the app, {uzivatel}\n We have {pocet_textu} texts to be analyzed.\n{ODDELOVAC}')
else:
    print("Unregistered user, terminating the program..")
    quit()


for _ in range(3):
    vyber_textu = input(f"Enter a number btw. 1 and {pocet_textu} to select: ")
    if vyber_textu.isdigit():
        volba = int(vyber_textu)
        if 0 < volba <= pocet_textu:
            text = TEXTS[volba-1]
            print(ODDELOVAC)
            break
        else:
            print("Try again! This is not in correct range.")
    else:
        print("Try again! This is not a number.")
else:
    print("You are failed. Terminating program.")
    quit()

ciste_slovo = [slovo.strip(",.:?!") for slovo in text.split()]

pocet_slov = len(ciste_slovo)

titlecase = []
uppercase = []
lowercase = [] 
    
for slovo in ciste_slovo: 
    if slovo.istitle():
        titlecase.append(slovo)
    elif slovo.isupper():
        uppercase.append(slovo)
    elif slovo.islower():
        lowercase.append(slovo)

zacinajici_velkym = len(titlecase)
je_velke = len(uppercase)
je_male = len(lowercase)

cisla = []
    
for cifra in ciste_slovo: 
    if cifra.isnumeric():
        cisla.append(int(cifra))

je_cislo = len(cisla)
soucet = sum(cisla)

delka_slov = [len(slovo) for slovo in ciste_slovo]


slovnik_delky = {}
for delka in set(delka_slov):
    slovnik_delky[delka] = delka_slov.count(delka)


print(f"There are {pocet_slov} words in the selected text.")
print(f"There are {zacinajici_velkym} titlecase words.")
print(f"There are {je_velke} uppercase words.")
print(f"There are {je_male} lowercase words.")
print(f"There are {je_cislo} numeric strings.")
print(f"The sum of all the numbers {soucet}.")

print(f"{ODDELOVAC}\nLEN|  OCCURENCES          |NR\n{ODDELOVAC}")

for radek in slovnik_delky.items():
    delka, vyskyt = radek
    if vyskyt > 0:
        print(f"{delka:<2} | {'*' * int(vyskyt):<30} | {vyskyt}")
