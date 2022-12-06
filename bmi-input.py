f = open("bmi_output.csv", "a")  # otwiera się plik tekstowy o nazwie bmi_output


def imperialne():  # funkcja dla wartości imperialnych
    while True:
        pseudonim = input("Podaj swój pseudonim/imię: ")
        wzrost_stopy = int(input("Ile mierzysz stóp: "))  # często ludzie pamiętają swój wzrost w danych imperialnych używając stóp i cali
        wzrost_cale = float(input("Ile mierzysz cali: "))
        waga_funty = float(input("Podaj swoją wagę w funtach: "))
        wzrost_imp = wzrost_stopy * 12 + wzrost_cale  # funkcja łączy stopy i cale dla ułatwienia obliczeń i późniejszego outputu

        bmi = (waga_funty / wzrost_imp ** 2) * 703  # wzór na bmi dla wartości imperialnych

        print(f'Twoje BMI wynosi:  {bmi}')

        print(f'imp,{pseudonim},{wzrost_imp},{waga_funty},{bmi}', file=f)  # zapisanie wartości do pliku tekstowego

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

        print(f'Twoje BMI wynosi:  {bmi}')

        print(f'met,{pseudonim},{wzrost},{waga},{bmi}', file=f)  # zapisanie wartości do pliku tekstowego

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