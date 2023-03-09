import pandas as pd

df = pd.read_csv('data/synthetic_listing.csv')
df["ID"] = df.index

df['Kunto'] = df['Kunto'].fillna("Unknown")
df['Kunto'] = df['Kunto'].replace(['huono'], 'bad')
df['Kunto'] = df['Kunto'].replace(['hyvä'], 'good')
df['Kunto'] = df['Kunto'].replace(['tyyd.'], 'satisfactory')


df['Asunnon tyyppi'] = df['Asunnon tyyppi'].replace(['Yksiö'], 'Studio apartment')
df['Asunnon tyyppi'] = df['Asunnon tyyppi'].replace(['Kaksi huonetta'], 'Two rooms')
df['Asunnon tyyppi'] = df['Asunnon tyyppi'].replace(['Kolme huonetta'], 'Three rooms')
df['Asunnon tyyppi'] = df['Asunnon tyyppi'].replace(['Neljä huonetta tai enemmän'], 'Four rooms or more')


print(df['Kunto'].unique())
print(df['Asunnon tyyppi'].unique())


print(df.head())
print(df.columns)



