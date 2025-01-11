import pandas as pd

df = pd.read_csv("data/0721-month-analysis-data.csv")
print(df.columns)

df = df[df['Pre-2014 School'].isin(['CityU', 'CUHK', 'HKU', 'HKUST'])]
pre_2014_school_researchers = df['Researcher Cleaned Name'].unique().tolist()

df = df[df['Researcher Classification'] == 'Hong Kong']
researcher_classification_researchers = df['Researcher Cleaned Name'].unique().tolist()

researchers = list(set(pre_2014_school_researchers) - set(researcher_classification_researchers))

new_df = pd.DataFrame(researchers, columns=['Name'])
new_df.to_csv("homepage_data_3.csv", index=False)

print(researchers, "Length: ", len(researchers))
