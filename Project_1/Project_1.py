data = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}

oddelovac = '-' * 35
print(oddelovac)
print('Welcome to the app. Please log in.')
print(oddelovac)

username = str(input('USERNAME: '))
password = str(input('PASSWORD: '))

if data.get(username) != password:
    print('Incorrect username or password')
    quit()

TEXTS = ['''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley ''',

'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick. ''',

'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present. ''']

print(oddelovac)
print('We have 3 texts to be analyzed.')

num = str(input('Enter a number btw. 1 and 3 to select: '))

if not num.isnumeric():
    print('Wrong, enter a number btw. 1 and 3.')
    quit()

correct = {'1': '1', '2': '2', '3': '3'}
if correct.get(num) != num:
    print('Wrong, enter a number btw. 1 and 3.')
    quit()

num = int(num)
print(oddelovac)
text = TEXTS[num-1]
slova = []
for slovo in text.split():
    slovo = slovo.strip(',:/;')
    slova.append(slovo)

titlecase = 0
lowercase = 0
uppercase = 0
numeric   = 0
pocet     = {}
all_numb  = 0

x = 0
while x < len(slova):
    if slova[x].istitle():
        titlecase = titlecase + 1
    elif slova[x].isupper():
        uppercase = uppercase + 1
    elif slova[x].islower():
        lowercase = lowercase + 1
    elif slova[x].isnumeric():
        numeric = numeric + 1
        all_numb = all_numb + float(slova[x])

    l = len(slova[x])
    pocet[l] = pocet.get(l, 0) + 1
    x = x + 1
print(oddelovac)
print(f'There are {len(slova)} words in the text.')
print(f'There are {titlecase:>2} titlecase words.')
print(f'There are {uppercase:>2} uppercase words.')
print(f'There are {lowercase} lowercase words.')
print(f'There are {numeric:>2} numeric strings.')
print(oddelovac)

delka = sorted(pocet)
x = 0
while x < len(delka):
    lg = delka[x]
    freq = pocet[lg]

    if len(str(lg)) == 1:
        index = ' ' + str(lg)
    else:
        index = str(lg)

    print(index, '*' * freq, freq)
    x = x + 1
print(oddelovac)
print(f'If we summed all the numbers in this text we would get: {all_numb}')
print(oddelovac)