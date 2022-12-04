def main():
    with open("people.csv", "r+") as file:
        # otwarcie pliku z danymi
        people = []
        i = 0
        # deklaracja list i zmiennych

        for line in file:
            new_item = line.split(",")
            people.append(new_item)
        # szczytanie wartości z pliku, dodanie elementów do listy

        for i in range(len(people)):
            w = people[i][1]
            w_p = w.split(" ")
            weight = float(w_p[0])
            weight_unit = w_p[1]
            if "ib" in weight_unit.lower():
                weight = pound_to_kg(weight)
            # zamiana z systemu imperialnego(funty) na normalny

            h = people[i][2]
            h_p = h.split(" ")
            height = float(h_p[0])
            height_unit = h_p[1]
            if "in" in height_unit.lower():
                height = cm_to_m(inch_to_cm(height))
            # zamiana z systemu imperialnego(cale) na normalny

            if "cm" in height_unit.lower():
            # warunek być może trochę naiwny, ale ludzie nie mają z reguły więcej niż 2.5 metra wzrostu
                height = cm_to_m(height)
            # zamiana wzrostu z centymetrów na metry

            bmi = float(weight / pow(height, 2))
            # obliczenie wartości bmi
            new_bmi = str(f"{bmi:.2f}")
            # ograniczenie cyfr po przecinku do dwóch

            file1 = open("file_to_plot.csv", "a+")
            file1.write(f"{people[i][0]},{weight:.2f},{height:.2f}\n")
            file1.close()
            # otwarcie pliku, wpisanie wartości, które posłużą do wstawienia w wykres, zamknięcie pliku

            file2 = open("bmi.csv", "a+")
            file2.write(f"{people[i][0]},{new_bmi}\n")
            file2.close()
            # otwarcie pliku, wpisanie imion i odpowiadającemu im bmi, zamknięcie pliku

            i += 1
            # inkrementacja zmiennej i służącej do określenia indexu w liście


def pound_to_kg(pound):
    return float(pound * 0.4535923)
# funkcja konwertująca funty na kilogramy


def inch_to_cm(inch):
    return float(inch * 2.54)
# funkcja konwertująca cale na centymetry


def cm_to_m(cm):
    return float(cm / 100)
# funkcja konwertująca metry na centymetry


if __name__ == '__main__':
    main()
# przywołanie funkcji main
