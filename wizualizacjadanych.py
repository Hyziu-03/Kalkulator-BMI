import seaborn as sns
sns.set_theme(style="whitegrid")

ludzie = sns.load_dataset("ludzie")


g = sns.catplot(
    data=ludzie, kind="bar",
    x="species", y="wartosc BMI", hue="sex",
    errorbar="sd", palette="dark", alpha=.6, height=6
)
g.despine(left=True)
g.set_axis_labels("", "Wartosc BMI")
g.legend.set_title("")
