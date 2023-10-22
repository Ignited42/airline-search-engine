import pandas as pd
from json import loads, dumps
import properjsondocument

df_airline = pd.read_csv('newdata/airlines.csv')
df_airports = pd.read_csv('newdata/airports.csv')
df_countries = pd.read_csv('newdata/countries.csv')
df_planes = pd.read_csv('newdata/planes.csv')
df_routes = pd.read_csv('newdata/routes.csv')

#======================================================================
df_new1 = df_airline[['Airline ID', 'Name', 'Country', 'IATA', 'ICAO']] # Select new rows
df_new1.columns =  ['ID', 'Name', 'Country', 'IATA', 'ICAO'] # Change columns name

df_new1['Code'] = df_new1[['IATA', 'ICAO']].to_dict('records') # Make a new row "Code" and includes 'IATA' and 'ICAO'
df_new1 = df_new1.drop(columns=['IATA', 'ICAO']) # Delete duplicated columns


entry = df_new1.iloc[1]

entry['Country'] = df_countries.loc[df_countries["name"] == entry["Country"]].to_dict('records')[0]

print(entry)

#=====================================================================

#print(df_new1.head(5))


#entry = df_new1.iloc[1].to_dict()

#for x in entry.keys():
#    print(str(x) +  " = " + str(entry[x]))

#properjsondocument.create_airline_collection(df_new1, df_countries)