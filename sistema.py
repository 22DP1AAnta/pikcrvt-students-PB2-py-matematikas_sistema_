"""Viesturs Emerbergs DP1-1
Programma, kas palīdz matemātikas skolotājai parbaudīrt skolēna zināšanas
"""
import os


def izdarit_izveli():
    print("Ja gribi teoriju, rakstit (3)\nJa gribi trenēties pirms kontroldarbiem, raksti (2)")
    print("Lai kontroldarbus pildītu un saņemtu semestra vērtējumu, raksti (1)")
    izvele = input("No 0-3:")
    if izvele == '3':
        teorija()
    elif izvele == '2':
        izvadit_matematikas_uzd()
    elif izvele == '1':
        parbaudes_darbi()
    else:
        izdarit_izveli()
def vardi():
    global grupa
    global vards
    global uzvards

    vards = input('Vārds:')
    uzvards = input('Uzvārds:')
    grupa = input('Grupa:')
    
def parbaudes_darbi():
    print("Ir 2 varianti tēmā - Kvadrātvienādojumi")
    print("Semestra atzīmi varēsi apskatīt pēc abu darbu izpildes raskti: 3")
    izvele = input("Kuru variantu pildīsi pirmo(1/2)?")
    if izvele == '1':
        kvadratvienadojumi_pd1()
    elif izvele == '2':
        kvadratvienadojumi_pd2()
    elif izvele == '3':
        vertejums()
        
def teorija():
    kvadratvienadojums = open('kvadratvienadojums.txt', 'r', encoding='utf-8')
    print(kvadratvienadojums.read())
    kvadratvienadojums.close()
    izvele = input("Vēlies atzgriezties izvēlnē(Jā/Nē)?")
    while izvele != "Jā":
        izvele = input("Vēlies atzgriezties izvēlnē(Jā/Nē)?")

    else:
        izdarit_izveli()


def izvadit_matematikas_uzd():
    print("Dotus uzdevumus (1)\nPatstāvīgi ievadīt (2)")
    izvele = input("Tava izvēle: ")
    if izvele == '2':
        patstavigi_uzd()
    elif izvele == '1':
        doti_uzdevumi()
    else:
        izvadit_matematikas_uzd()


def doti_uzdevumi():
    print("Uzdevumi treniņam")
    print()
    pareizi = 0
    atbildes_uzdevumi = [['-2', '-1']]
    print('Aprēķini kvadrātvienādojuma x2+3x+2=0 saknes!\nraksti mazāko sakni pirmo!')

    lietotaja_atbildes1 = [input('Ievadi pirmo sakni: '), input('Ievadi otro sakni: ')]
    if lietotaja_atbildes1 == atbildes_uzdevumi[0]:
        pareizi += 1
    print("Sadali reizinātājos kvadrāttrinomu x2+8x+15!")

    lietotaja_atbildes2 = [input('(x+: '), input('(x+: ')]
    if lietotaja_atbildes2 == atbildes_uzdevumi[1]:
        pareizi += 1
    print(f'Tev bija pareizi{pareizi}no 3 jautājumiem ')
    izvele = input("Vēlies atzgriezties izvēlnē(Jā/Nē)?")
    while izvele != "Jā":
        izvele = input("Vēlies atzgriezties izvēlnē(Jā/Nē)?")

    else:
        izdarit_izveli()


def patstavigi_uzd():
    masivs = [0]
    jautajumi = [0]
    sk_atbildes = [0]
    n = int(input('Cik būs jautājumi? '))
    masivs = [0] * n  # pareizo atbilžu masīvs
    jautajumi = [0] * n  # nepareizo atbilžu masīvs
    sk_atbildes = [0] * n
    for x in range(n):
        jautajumi[x] = input(f'Skolotaja {x + 1}. Jautajums:')
        masivs[x] = input(f'Skolotaja {x + 1}. atbilde:')
    os.system('cls')
    for x in range(n):
        print(jautajumi[x])
        sk_atbildes[x] = input(f'Skolēna {x + 1}. atbilde:')

    pareizi = 0
    for i in range(n):
        if sk_atbildes[i] == masivs[i]:
            pareizi = pareizi + 1
    print("Pareizi atbildeji uz", pareizi, "jautājumiem")  # izvada pareizo atbilžu skaitu
    izvele = input("Vēlies atzgriezties izvēlnē(Jā/Nē)?")
    while izvele != "Jā":
        izvele = input("Vēlies atzgriezties izvēlnē(Jā/Nē)?")
    else:
        izdarit_izveli()


def kvadratvienadojumi_pd2():
    vardi()
    global punkti2
    punkti2 = 0
    uzd_skaits = 4
    print('Kontroldarbs. II variants')
    print()

    print('1.uzdevums')
    print()

    atbildes_kd = [['0', '2'], ['-7', '0'], ['-4','-2'], ['4','3']]
    print("Nosaki saknes nepilnajam kvadrātvienādojumam 4x2−8x=0!\n(Pirmo ievadi mazāko sakni!)")
    lietotaja_atbildes2 = [input("Ievadi pirmo sakni: "),input('Ievadi otro sakni: ')]
    if lietotaja_atbildes2 == atbildes_kd[0]:
        punkti2+=1
    print('2.uzdevums')
    print()
    print("Atrisini nepilno vienādojumu 3x2+21x=0!\n(Pirmo ievadi mazāko sakni!)")
    lietotaja_atbildes4 = [input("Ievadi pirmo sakni: "), input('Ievadi otro sakni: ')]
    if lietotaja_atbildes4 == atbildes_kd[1]:
        punkti2+=1
    print('3.uzdevums')
    print()
    print("Aprēķini kvadrātvienādojuma x2+6x+8=0 saknes!\(Pirmo ievadi mazāko sakni!)")
    lietotaja_atbildes4 = [input("Ievadi pirmo sakni: "), input('Ievadi otro sakni: ')]
    if lietotaja_atbildes4 == atbildes_kd[2]:
        punkti2 += 1
    print('4.uzdevums')
    print()
    print("Sadali reizinātājos kvadrāttrinomu x2+7x+12!\n(Pirmo raksti lielāko skaitli!)")
    lietotaja_atbildes4 = [input("(x+ "), input('(x+ ')]
    if lietotaja_atbildes4 == atbildes_kd[3]:
        punkti2 += 1
    if punkti2 < 1:
        print(f"Tavs vērtējums ir {punkti2+1}")
    else:
        print("Tavs vērtējums ir: ", round(punkti1 / uzd_skaits * 10))
    izvele = input("Vēlies atzgriezties izvēlnē(Jā/Nē)?")
    while izvele != "Jā":
        izvele = input("Vēlies atzgriezties izvēlnē(Jā/Nē)?")

    else:
        izdarit_izveli()
def kvadratvienadojumi_pd1():
    vardi()
    global punkti1
    punkti1 = 0
    uzd_skaits = 4
    print('1. variants kontroldarbs Kvadrātvienādojumi.')
    print()

    print('1.uzdevums')
    print()

    atbildes_kd = [['0', '7'], ['-4', '-1'], ['-5', '5'], ['1', '2']]
    print("Nosaki saknes nepilnajam kvadrātvienādojumam 7x2−49x=0\nraksti mazāko sakni pirmo!")
    print()

    lietotaja_atbildes1 = [input('Ievadi pirmo sakni: '), input('Ievadi otro sakni: ')]

    if lietotaja_atbildes1 == atbildes_kd[0]:
        punkti1 += 1
    print('2. uzdevums')
    print()

    print("Aprēķini kvadrātvienādojuma x2+5x+4=0 saknes!\nraksti mazāko sakni pirmo!")

    lietotaja_atbildes2 = [input('Ievadi pirmo sakni: '), input('Ievadi otro sakni: ')]
    print()
    if lietotaja_atbildes2 == atbildes_kd[1]:
        punkti1 += 1
    print("3. uzdevums")
    print("Kādas ir nepilnā kvadrātvienādojuma 3x2−75=0 saknes?\nraksti mazāko sakni pirmo!")

    lietotaja_atbildes3 = [input('Ievadi pirmo sakni: '), input('Ievadi otro sakni: ')]
    print()
    if lietotaja_atbildes3 == atbildes_kd[2]:
        punkti1 += 1
    print("4. uzdevums")
    print("Atrisini kvadrātvienādojumu 2x2−6x+4=0!\nraksti mazāko sakni pirmo!")

    lietotaja_atbildes4 = [input('Ievadi pirmo sakni: '), input('Ievadi otro sakni: ')]
    print()
    if lietotaja_atbildes4 == atbildes_kd[3]:
        punkti1 += 1
    if punkti1 < 1:
        print(f"Tavs vērtējums ir {punkti1+1}")
    else:
        print("Tavs vērtējums ir: ", round(punkti1 / uzd_skaits * 10))
    izvele = input("Vēlies atzgriezties izvēlnē(Jā/Nē)?")
    while izvele != "Jā":
        izvele = input("Vēlies atzgriezties izvēlnē(Jā/Nē)?")

    else:
        izdarit_izveli()
def vertejums():
    vert = open('Atzimes.txt', 'w', encoding = 'utf-8')
    vert.write(f'{vards, uzvards} grupa {grupa} dabūja semestra atzīmi {round((punkti1+punkti2)*2.5/2)} no . Tēmā - Kvadrātvienādojums un kvadrāttrinoms.')
    vert.close()
    atzime = open('Atzimes.txt', 'r', encoding='utf-8')
    print(atzime.read())
    atzime.close()

izdarit_izveli()
os.system("pause")


