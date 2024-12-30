import pandas as pd
df = pd.read_csv(r"C:\Users\User\Downloads\Python\SA Companies.csv")
specific_companies = ['Sasol', 'Eskom']
fdf = df[df['Company'].str.contains("Group")]
print(fdf)