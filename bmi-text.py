import csv
# zaimportowanie biblioteki csv


def main():
    """ funkcja main """
    with open("people.csv", "r+") as file:
        # otworzenie pliku z danymi
        reader = csv.DictReader(file)
        # szczytanie wartości z pliku używając funkcji DictReader(szczytanie zawartości jako słowników)
        list_of_weights = []
        list_of_heights = []
        list_of_bmi = []
        list_of_names = []
        # deklaracja list
        for people in reader:
            people_name = people["imie"]
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
            list_of_weights.append(f"{weight:.2f}")
            list_of_heights.append(f"{height:.2f}")
            list_of_bmi.append(new_bmi)
            list_of_names.append(people_name)

        with open("people_bmi.csv", "a+") as file1:
            writer = csv.DictWriter(
                file1, fieldnames=["system", "imie", "wzrost", "waga", "bmi"])
            writer.writeheader()
            for i in range(20):
                writer.writerow({
                    "system": "met", 
                    "imie": list_of_names[i],
                    "wzrost": list_of_heights[i], 
                    "waga": list_of_weights[i], 
                    "bmi": list_of_bmi[i]
                })
                i += 1
        # wpisanie danych o osobach do pliku używając funckji DictWriter
        # niestety funkcja ta automatycznie dodaje nowe linie na koniec, dlatego też potrzebne będzie ich usunięcie
        with open("people_bmi.csv", "r") as file2:
            for line in file2:
                if line == "\n":
                    line = line.replace("\n", "")
                with open("bmi.csv", "a") as file3:
                    file3.write(line)
        # usunięcie zbędnych linii w pliku csv


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
