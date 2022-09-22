import pandas as pd

df1=pd.read_csv("List1.csv")
df2=pd.read_csv("List2.csv")

df_final=pd.concat([df1,df2]).drop_duplicates(subset=['Name', 'Alter', 'Geschlecht']).reset_index(drop=True)
print(df_final.shape)

df_final2=df_final.drop_duplicates(subset=['Name','Alter']).reset_index(drop=True)

df_final2.to_csv(index=False)

print(df_final2)
