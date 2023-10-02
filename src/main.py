import pandas as pd

df1 = pd.read_csv('data/raw/airlines.dat')
df2 = pd.read_csv('data/raw/airports.dat')
df3 = pd.read_csv('data/raw/countries.dat')
df4 = pd.read_csv('data/raw/planes.dat')
df5 = pd.read_csv('data/raw/routes.dat')

df1 = df1.fillna(r'\N')
df2 = df2.fillna(r'\N')
df3 = df3.fillna(r'\N')
df4 = df4.fillna(r'\N')
df5 = df5.fillna(r'\N')

df1 = df1[df1['Active'] == 'Y']
df1 = df1.drop(columns = 'Callsign')
df1 = df1.drop(columns = 'Active')
print(df1.head())
#print(df1.isnull().sum())

df2 = df2.drop(columns = 'Type')
df2 = df2.drop(columns = 'Source')
df2 = df2.drop(columns = 'Tz database time zone')
print(df2.head())
#print(df2.isnull().sum())

df3 = df3.drop(columns = 'dafif_code')
print(df3.head())
#print(df3.isnull().sum())

print(df4.head())
#print(df4.isnull().sum())

print(df5.head()) # Checking
#print(df5.isnull().sum()) # Print total num of NaN

#print(df.isnull().sum())
