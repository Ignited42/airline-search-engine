# Author: Yuuki
# Co-author: Steven
# Description:
#   Purpose of file is to convert .csv files into .json files.

import pandas as pd
from json import loads, dumps
from data_cleaning import properjsondocument
import time

start_time = time.time()

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

airline_json = df_new1.to_json(orient='records') # Convert to JSON

parsed = loads(airline_json)
#print(dumps(parsed, indent=4) ) # Printing
#==============================

#======================================================================
df_new2 = df_airports[['Airport ID', 'Name', 'City', 'Country', 'IATA', 'ICAO', 'Latitude', 'Longitude', 'TimeZone', 'DST']] # Select new rows
df_new2.columns =  ['ID', 'Name', 'City', 'Country', 'IATA', 'ICAO', 'Latitude', 'Longitude', 'TimeZone', 'DST'] # Change columns name

df_new2['Code'] = df_new2[['IATA', 'ICAO']].to_dict('records')
df_new2['Location'] = df_new2[['Latitude', 'Longitude']].to_dict('records')
df_new2['Time'] = df_new2[['TimeZone', 'DST']].to_dict('records')

df_new2 = df_new2.drop(columns=['IATA', 'ICAO', 'Latitude', 'Longitude', 'TimeZone', 'DST']) # Delete duplicated columns

airports_json = df_new2.to_json(orient='records') # Convert to JSON

parsed = loads(airports_json)
#print(dumps(parsed, indent=4) ) # Printing
#==============================

#======================================================================
df_new3 = df_countries[['name','iso_code']] # Select new rows
df_new3.columns =  ['Name','ISO'] # Change columns name

df_new3['Code'] = df_new3[['ISO']].to_dict('records')

df_new3 = df_new3.drop(columns=['ISO']) # Delete duplicated columns

countries_json = df_new3.to_json(orient='records') # Convert to JSON

parsed = loads(airports_json)
#print(dumps(parsed, indent=4) ) # Printing
#==============================

#======================================================================
df_new4 = df_planes[['Name','IATA code', 'ICAO code']] # Select new rows
df_new4.columns =  ['Name','IATA', 'ICAO'] # Change columns name

df_new4['Code'] = df_new4[['IATA', 'ICAO']].to_dict('records')

df_new4 = df_new4.drop(columns=['IATA', 'ICAO']) # Delete duplicated columns

planes_json = df_new4.to_json(orient='records') # Convert to JSON

parsed = loads(airports_json)
#print(dumps(parsed, indent=4) ) # Printing
#==============================

#======================================================================
df_new5 = df_routes[['Airline', 'Airline ID', 'Source airport', 'Source airport ID', 'Destination airport', 'Destination airport ID', 'Codeshare', 'Stops']] # Select new rows
df_new5.columns =  ['Name', 'ID', 'Source Name', 'Source ID', 'Destination Name', 'Destination ID', 'Codeshare', 'Stops'] # Change columns name

df_new5['Airline'] = df_new5[['Name', 'ID']].to_dict('records')
df_new5['Airports'] = df_new5[['Source Name', 'Source ID', 'Destination Name', 'Destination ID']].to_dict('records')

df_new5 = df_new5.drop(columns=['Name', 'ID', 'Source Name', 'Source ID', 'Destination Name', 'Destination ID']) # Delete duplicated columns

routes_json = df_new5.to_json(orient='records') # Convert to JSON

parsed = loads(airports_json)
#print(dumps(parsed, indent=4) ) # Printing
#==============================

#df_new1.to_json('JSONdata/airlines.json', orient='records')
#df_new2.to_json('JSONdata/airports.json', orient='records')
#df_new3.to_json('JSONdata/countries.json', orient='records')
#df_new4.to_json('JSONdata/planes.json', orient='records')
#df_new5.to_json('JSONdata/routes.json', orient='records')

#entry = df_new3.loc[df_new3['Name'] == df_new1.iloc[1]['Country']].to_dict('records')[0]
#df_new1.at[1, "Country"] = entry

print("Creating airlines collection")
properjsondocument.create_airline_collection(df_new1, df_new3)

print("Creating airports collection")
properjsondocument.create_airports_collection(df_new2, df_new3)

print("Creating routes collection")
properjsondocument.create_routes_collection(df_new5, df_new2)

end_time = time.time()

print("Elapsed time for JSON conversion: " + str(end_time - start_time))

#print("Done.")