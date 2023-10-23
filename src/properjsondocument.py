# Author: Steven
# Description:
#   Purpose of file is to output proper JSON files to be ingested into a NoSQL document DB

def create_airline_collection(airline_df, country_df):
    for x in airline_df.index:
        entry = country_df.loc[country_df['Name'] == airline_df.iloc[x]['Country']].to_dict('records')
        
        try:
            airline_df.at[x, "Country"] = entry[0]
        except:
            continue

def create_airports_collection(airport_df, country_df):
    for x in airport_df.index:
        entry = country_df.loc[country_df['Name'] == airport_df.iloc[x]['Country']].to_dict('records')
        
        try:
            airport_df.at[x, "Country"] = entry[0]
        except:
            continue
    return


def create_routes_collection(routes_df, airport_df):
    for x in routes_df.index:
        try:
            source_id = int(routes_df.iloc[x]['Airports']['Source ID'])
            destination_id = int(routes_df.iloc[x]['Airports']['Destination ID'])
        except:
            continue
        

        source = airport_df.loc[airport_df['ID'] == source_id].to_dict('records')
        destination = airport_df.loc[airport_df['ID'] == destination_id].to_dict('records')

        try:
            source_dict = {
                "ID": source[0]["ID"],
                "Name": source[0]["Name"],
                "City": source[0]["City"],
                "Country": source[0]["Country"]["Name"]
            }
            
            destination_dict = {
                "ID": destination[0]["ID"],
                "Name": destination[0]["Name"],
                "City": destination[0]["City"],
                "Country": destination[0]["Country"]["Name"]
            }

            routes_df.at[x, 'Airports'] = {
                "Source": source_dict,
                "Destination": destination_dict
            }
        except:
            pass

    return