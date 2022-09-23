import pandas as pd

df1 = pd.read_csv(r"/home/conny/Documents/List1.csv")
df2 = pd.read_csv(r"/home/conny/Documents/List2.csv")

df_final = pd.concat([df1, df2]).drop_duplicates(subset=['Name', 'Alter', 'Geschlecht']).reset_index(drop=True)

df_final2 = df_final.drop_duplicates(subset=['Name', 'Alter']).reset_index(drop=True)

df_final2.to_csv('merged12.csv', index=False)

print(df_final2)
