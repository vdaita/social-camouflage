import pandas as pd

df = pd.read_csv("data/0721-month-analysis-data.csv")
print(df.columns)

df = df[df['Researcher Classification'] == 'Hong Kong']
researchers = df['Researcher Cleaned Name'].unique().tolist()

new_df = pd.DataFrame(researchers, columns=['Name'])
new_df.to_csv("homepage_data_2.csv", index=False)

print(researchers, "Length: ", len(researchers))
