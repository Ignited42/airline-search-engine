# Author: Yuuki
# Description:
#   Purpose of file is to convert .dat files into .csv files

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
df2 = df2.drop(columns = 'Type')
df2 = df2.drop(columns = 'Source')
df2 = df2.drop(columns = 'Tz database time zone')
print(df2.head())
df3 = df3.drop(columns = 'dafif_code')
print(df3.head())
print(df4.head())
df5 = df5.drop(columns = 'Equipment')
print(df5.head())


df1.to_csv('newdata/airlines.csv', index=False)
df2.to_csv('newdata/airports.csv', index=False)
df3.to_csv('newdata/countries.csv', index=False)
df4.to_csv('newdata/planes.csv', index=False)
df5.to_csv('newdata/routes.csv', index=False)
