import pandas
import matplotlib.pyplot as plt

# WCZYTYWANIE DANYCH

file = open("bmi.csv", "r")
# przykładowy plik dla testów

contents = file.read()
records_list = contents.split("\n")
# \n to znak nowej linii
records_size = len(records_list)
for i in range(records_size):
    records_list[i] = records_list[i].split(",")
# wczytywanie danych z pliku do listy

systems = []
names = []
weights = []
heights = []
bmis = []

for i in range(records_size):
    systems.append(records_list[i][0])
    names.append(records_list[i][1])
    weights.append(records_list[i][2])
    heights.append(records_list[i][3])
    bmis.append(records_list[i][4])
# przepisywanie danych z jednej listy do trzech
# każda lista to osobne dane, każdy indeks odpowiada jednej osobie
# to znaczy systems[0], names[0], weights[0], heights[0] i bmis[0]...
# ...odpowiadają tej samej osobie

# WIZUALIZACJA DANYCH

# wczytanie danych
people = pandas.read_csv("bmi.csv")
# wykres robiony w pyplot, bez seaborna
g = plt.bar(people["name"], people["bmi"])

# ustawienie kolorów poszczególnych kolumn
for i in range(len(people)):
    color = ""
    bmi = people["bmi"][i]
    if bmi < 16:
        color = "darkblue"
    elif bmi < 17:
        color = "blue"
    elif bmi < 18.5:
        color = "paleturquoise"
    elif bmi < 25:
        color = "lightgreen"
    elif bmi < 30:
        color = "khaki"
    elif bmi < 35:
        color = "gold"
    elif bmi < 40:
        color = "crimson"
    else:
        color = "firebrick"
    g[i].set_color(color)

# ustawienie żeby ładnie wyglądało
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# file.close()
