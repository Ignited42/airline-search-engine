import pandas as pd

df = pd.read_csv('newdata/airlines.csv')

df_new = df[['Airline ID', 'Name', 'Country', 'IATA', 'ICAO']] # Select new rows
df_new.columns =  ['ID', 'Name', 'Country', 'IATA', 'ICAO'] # Change columns name

df_new['Code'] = df_new[['IATA', 'ICAO']].to_dict('records') # Make a new row "Code" and includes 'IATA' and 'ICAO'
df_new = df_new.drop(columns=['IATA', 'ICAO']) # Delete duplicated columns

new_json = df_new.to_json(orient='records') # Convert to JSON

print(new_json) # Testing