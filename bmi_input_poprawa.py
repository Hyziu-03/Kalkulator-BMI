f = open("bmi_output.csv", "a")  # otwiera się plik tekstowy o nazwie bmi_output


def imperialne():  # funkcja dla wartości imperialnych
    while True:
        pseudonim = input("Podaj swój pseudonim/imię: ")
        wzrost_stopy = int(input("Ile mierzysz stóp: "))  # często ludzie pamiętają swój wzrost w danych imperialnych używając stóp i cali
        wzrost_cale = float(input("Ile mierzysz cali: "))
        waga_funty = float(input("Podaj swoją wagę w funtach: "))
        wzrost_imp = wzrost_stopy * 12 + wzrost_cale  # funkcja łączy stopy i cale dla ułatwienia obliczeń i późniejszego outputu

        bmi = (waga_funty / wzrost_imp ** 2) * 703  # wzór na bmi dla wartości imperialnych
        zwrot = ''  #przez błąd musiałem to zrobić tak, że zwrot jest pusty a po zbadaniu wartości bmi program przypisuje mu odpowiednią nazwę
        if bmi < 16:
            print(f'Twoje BMI wynosi: {bmi} Oznacza to: wygłodzenie')
            zwrot = 'wygłodzenie'
        if 16.99 > bmi > 16:
            print(f'Twoje BMI wynosi: {bmi} Oznacza to: wychudzenie ')
            zwrot = 'wychudzenie'
        if 18.49 > bmi > 17:
            print(f'Twoje BMI wynosi: {bmi} Oznacza to: niedowage')
            zwrot = 'niedowaga'
        if 24.99 > bmi > 18.5:
            print(f'Twoje BMI wynosi: {bmi} Oznacza to: poprawną mase ciała')
            zwrot = 'poprawna'
        if 19.99 > bmi > 25:
            print(f'Twoje BMI wynosi: {bmi} Oznacza to: nadwage')
            zwrot = 'nadwaga'
        if 34.99 > bmi > 30:
            print(f'Twoje BMI wynosi: {bmi} Oznacza to: otyłość pierwszego stopnia')
            zwrot = 'otyłość1'
        if 39.99 > bmi > 35:
            print(f'Twoje BMI wynosi: {bmi} Oznacza to: otyłość drugiego stopnia')
            zwrot = 'otyłość2'
        if bmi >= 40:
            print(f'Twoje BMI wynosi: {bmi} Oznacza to: otyłość trzeciego stopnia')
            zwrot = 'otyłość3'

        print(f'imp,{pseudonim},{wzrost_imp},{waga_funty},{bmi},{zwrot}', file=f)  # zapisanie wartości do pliku tekstowego

        kolejna = input("Czy chciałbyś dodać kolejną osobę używając jednostek imperialnych? (tak lub nie): ")
        if kolejna == 'tak':  # jeśli ktoś chce dalej dodawać osoby w tym samym formacie danych to może to robić wpisując tak
            continue
        if kolejna == 'nie':  # jeśli chce zmienić dane na metryczne albo całkowicie opuścić program to wpisuje nie
            kolejnamet = input("Czy chciałbyś dodać kolejną osobę używając jednostek metrycznych? (tak lub nie): ")
            if kolejnamet == 'tak':
                metryczne()
            elif kolejnamet == 'nie':  # po dwukrotnym wpisaniu 'nie' zamyka się plik tekstowy a następnie program
                f.close()
                exit()


def metryczne():  # funkcja dla wartości metrycznych
    while True:
        pseudonim = input("Podaj swój pseudonim/imię: ")
        wzrost = float(input("Podaj swój wzrost w metrach: "))
        waga = float(input("Podaj swoją wagę w kilogramach: "))

        bmi = waga / wzrost ** 2
        zwrot = ''
        if bmi < 16:
            print(f'Twoje BMI wynosi: {bmi} Oznacza to: wygłodzenie')
            zwrot = 'wygłodzenie'
        if 16.99 > bmi > 16:
            print(f'Twoje BMI wynosi: {bmi} Oznacza to: wychudzenie ')
            zwrot = 'wychudzenie'
        if 18.49 > bmi > 17:
            print(f'Twoje BMI wynosi: {bmi} Oznacza to: niedowage')
            zwrot = 'niedowaga'
        if 24.99 > bmi > 18.5:
            print(f'Twoje BMI wynosi: {bmi} Oznacza to: poprawną mase ciała')
            zwrot = 'poprawna'
        if 19.99 > bmi > 25:
            print(f'Twoje BMI wynosi: {bmi} Oznacza to: nadwage')
            zwrot = 'nadwaga'
        if 34.99 > bmi > 30:
            print(f'Twoje BMI wynosi: {bmi} Oznacza to: otyłość pierwszego stopnia')
            zwrot = 'otyłość1'
        if 39.99 > bmi > 35:
            print(f'Twoje BMI wynosi: {bmi} Oznacza to: otyłość drugiego stopnia')
            zwrot = 'otyłość2'
        if bmi >= 40:
            print(f'Twoje BMI wynosi: {bmi} Oznacza to: otyłość trzeciego stopnia')
            zwrot = 'otyłość3'

        print(f'met,{pseudonim},{wzrost},{waga},{bmi},{zwrot}', file=f)  # zapisanie wartości do pliku tekstowego

        kolejna = input("Czy chciałbyś dodać kolejną osobę używając jednostek metrycznych? (tak lub nie): ")  # te pętle działają tak samo jak poprzednie
        if kolejna == 'tak':
            continue
        if kolejna == 'nie':
            kolejnaimp = input("Czy chciałbyś dodać kolejną osobę używając jednostek imperialnych? (tak lub nie): ")
            if kolejnaimp == 'tak':
                imperialne()
            elif kolejnaimp == 'nie':
                f.close()
                exit()

q = input("Chcesz podawać dane w jednostkach imperialnych czy metrycznych?: ")  # pytanie początkowe do użytkownika jakich wartości chciałby używać
if q == 'imperialnych':
    imperialne()
if q == 'metrycznych':
    metryczne()
