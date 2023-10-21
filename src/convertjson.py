import pandas as pd
from json import loads, dumps

df_airline = pd.read_csv('newdata/airlines.csv')
df_airports = pd.read_csv('newdata/airports.csv')
df_countries = pd.read_csv('newdata/countries.csv')
df_planes = pd.read_csv('newdata/planes.csv')
df_routes = pd.read_csv('newdata/airlines.csv')

#======================================================================
df_new1 = df_airline[['Airline ID', 'Name', 'Country', 'IATA', 'ICAO']] # Select new rows
df_new1.columns =  ['ID', 'Name', 'Country', 'IATA', 'ICAO'] # Change columns name

df_new1['Code'] = df_new1[['IATA', 'ICAO']].to_dict('records') # Make a new row "Code" and includes 'IATA' and 'ICAO'
df_new1 = df_new1.drop(columns=['IATA', 'ICAO']) # Delete duplicated columns

airline_json = df_new1.to_json(orient='records') # Convert to JSON

parsed = loads(airline_json)
#print(dumps(parsed, indent=4) ) # Printing
#==============================

#======================================================================
df_new2 = df_airports[['Airport ID', 'Name', 'City', 'Country', 'IATA', 'ICAO', 'Latitude', 'Longitude', 'TimeZone', 'DST']] # Select new rows
df_new2.columns =  ['ID', 'Name', 'City', 'Country', 'IATA', 'ICAO', 'Latitude', 'Longitude', 'TimeZone', 'DST'] # Change columns name

df_new2['Code'] = df_new2[['IATA', 'ICAO']].to_dict('records') # Make a new row "Code" and includes 'IATA' and 'ICAO'
df_new2['Location'] = df_new2[['Latitude', 'Longitude']].to_dict('records')
df_new2['Time'] = df_new2[['TimeZone', 'DST']].to_dict('records')

df_new2 = df_new2.drop(columns=['IATA', 'ICAO', 'Latitude', 'Longitude', 'TimeZone', 'DST']) # Delete duplicated columns

airports_json = df_new2.to_json(orient='records') # Convert to JSON

parsed = loads(airports_json)
print(dumps(parsed, indent=4) ) # Printing
#==============================