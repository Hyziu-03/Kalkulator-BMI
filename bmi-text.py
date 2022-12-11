import csv
# zaimportowanie biblioteki csv


def main():
    """ funkcja main """
    with open("people.csv", "r+") as file:
        # otworzenie pliku z danymi
        reader = csv.DictReader(file)
        # szczytanie wartości z pliku używając funkcji DictReader(szczytanie zawartości jako słowników)

        for people in reader:
            people_name = people["name"]
            people_weight = people["weight"]
            weight_and_unit = people_weight.split(" ")
            weight = float(weight_and_unit[0])
            weight_unit = weight_and_unit[1]
            if "ib" in weight_unit.lower():
                weight = pound_to_kg(weight)
            # zamiana z systemu imperialnego(funty) na normalny

            people_height = people["height"]
            height_and_unit = people_height.split(" ")
            height = float(height_and_unit[0])
            height_unit = height_and_unit[1]
            if "in" in height_unit.lower():
                height = cm_to_m(inch_to_cm(height))
            # zamiana z systemu imperialnego(cale) na normalny

            if "cm" in height_unit.lower():
                height = cm_to_m(height)
            # zamiana wzrostu z centymetrów na metry

            bmi = float(weight / pow(height, 2))
            # obliczenie wartości bmi
            new_bmi = str(f"{bmi:.2f}")
            # ograniczenie cyfr po przecinku do dwóch

            file1 = open("people_bmi.csv", "a+")
            file1.write(f"met,{people_name},{weight:.2f},{height:.2f},{new_bmi}\n")
            file1.close()
            # otwarcie pliku, wpisanie wartości, które posłużą do wstawienia w wykres, zamknięcie pliku


def pound_to_kg(pound):
    return float(pound * 0.4535923)


""" funkcja konwertująca funty na kilogramy """


def inch_to_cm(inch):
    return float(inch * 2.54)


""" funkcja konwertująca cale na centymetry """


def cm_to_m(cm):
    return float(cm / 100)


""" funkcja konwertująca metry na centymetry """


if __name__ == '__main__':
    main()
# przywołanie funkcji main
