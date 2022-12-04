<<<<<<< HEAD
import seaborn as sns
import pandas
import matplotlib as plt

# WCZYTYWANIE DANYCH

file = open("dane.csv", "r")
# przykładowy plik dla testów

contents = file.read()
records_list = contents.split("\n")
# \n to znak nowej linii
records_size = len(records_list)
for i in range(records_size):
    records_list[i] = records_list[i].split(",")
# wczytywanie danych z pliku do listy

names = []
weights = []
heights = []
for i in range(records_size):
    names.append(records_list[i][0])
    weights.append(records_list[i][1])
    heights.append(records_list[i][2])
# przepisywanie danych z jednej listy do trzech
# każda lista to osobne dane, każdy indeks odpowiada jednej osobie
# to znaczy names[0], weights[0] i heights[0] odpowiadają tej samej osobie

# WIZUALIZACJA DANYCH

sns.set_theme(style="whitegrid")

people = pandas.read_csv("dane.csv")

g = sns.barplot(data=people, x=people.index, y="BMI", kind="bar",
    errorbar="sd", palette="dark", alpha=.6, height=6)
# o co chodzi, wyskakuje błąd ValueError: Could not interpret input 'species'

g.set_axis_labels("", "Wartość BMI")
g.set_xticklabels("", "Osoby badane")
g.legend.set_title("")
g.despine(left=True)

plt.show()
file.close()
=======
import seaborn as sns
import pandas

# WCZYTYWANIE DANYCH

file = open("dane.csv", "r")
# przykładowy plik dla testów

contents = file.read()
records_list = contents.split("\n")
# \n to znak nowej linii
records_size = len(records_list)
for i in range(records_size):
    records_list[i] = records_list[i].split(",")
# wczytywanie danych z pliku do listy

names = []
weights = []
heights = []
for i in range(records_size):
    names.append(records_list[i][0])
    weights.append(records_list[i][1])
    heights.append(records_list[i][2])
# przepisywanie danych z jednej listy do trzech
# każda lista to osobne dane, każdy indeks odpowiada jednej osobie
# to znaczy names[0], weights[0] i heights[0] odpowiadają tej samej osobie

# WIZUALIZACJA DANYCH

sns.set_theme(style="whitegrid")

people = pandas.read_csv("dane.csv")

g = sns.catplot(
    data=people, kind="bar",
    x="species", y="wartość BMI", hue="sex",
    errorbar="sd", palette="dark", alpha=.6, height=6
)
# o co chodzi, wyskakuje błąd ValueError: Could not interpret input 'species'
g.despine(left=True)
g.set_axis_labels("", "Wartość BMI")
g.legend.set_title("")

file.close()
>>>>>>> 3e38b9adf984a3f0f75adef4a55bf80a47b2a8c2
