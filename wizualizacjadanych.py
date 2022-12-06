import seaborn as sns
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

sns.set_theme(style="whitegrid")

people = pandas.read_csv("bmi.csv")

g = sns.catplot(
    data=people, kind="bar", errorbar="sd",
    x="imie", y="bmi",
    palette="dark", alpha=.6, height=6
)
g.despine(left=True)
g.set_axis_labels("Osoba", "Wartość BMI")
plt.show()

file.close()
