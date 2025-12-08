# this code performs data integration between the NYC and Chicago Datasets

import pandas as pd
import numpy as np
import sys
import os

chicago_file = sys.argv[1]
nyc_file = sys.argv[2]
output_file_full = sys.argv[3]
output_file_reduced = sys.argv[4]


chicago = pd.read_csv(chicago_file)
nyc = pd.read_csv(nyc_file)

#chicago = pd.read_csv("Data/Cleaned Datasets/Chicago_Inspections_Data/11.7_Chicago_Food_Inspections_Cleaned_Reduced.csv")
#nyc = pd.read_csv("Data/Cleaned Datasets/NYC_Inspections_Data/11.16_NYC_Inspections_Cleaned_Reduced.csv")

chicago['Zip'] = chicago['Zip'].astype('Int64')
chicago['License #'] = chicago['License #'].astype('Int64')

chicago['DBA Name'] = chicago['DBA Name'].str.upper()

chicago = chicago[["License #", "DBA Name", "Risk", "Address", "City", "State", "Zip", "Inspection Date", "Facility Type", "Violations", "Results"]]

nyc["City"] = "NEW YORK CITY"
nyc["State"] = "NY"

nyc = nyc.rename(
    columns={"DBA": "DBA Name", "BORO": "Boro", "STREET": "Street", "ZIPCODE": "Zip", "CUISINE DESCRIPTION": "Cuisine Description", "INSPECTION DATE": "Inspection Date", "VIOLATION DESCRIPTION": "Violations", "CRITICAL FLAG": "Critical Flag"}
)

nyc = nyc[["CAMIS", "DBA Name", "Boro", "Critical Flag", "Street", "City", "State", "Zip", "Cuisine Description", "Inspection Date", "Violations"]]
nyc['Violations'] = nyc['Violations'].str.upper()

final_df = pd.concat([nyc, chicago], ignore_index=True)
final_df.index = range(1, len(final_df) + 1)
final_df['RecordID'] = final_df.index

final_df = final_df[['RecordID', 'DBA Name', 'CAMIS', 'License #', 'Address', 'Street', 'City', 'Boro', 'State', 'Zip', 'Inspection Date', 'Risk', 'Critical Flag', 'Facility Type', 'Cuisine Description', 'Violations', 'Results']]
final_df['CAMIS'] = final_df['CAMIS'].astype('Int64')

os.makedirs(os.path.dirname(sys.argv[3]), exist_ok=True)
os.makedirs(os.path.dirname(sys.argv[4]), exist_ok=True)

final_df.to_csv("Data/Data Integration/11.16_Inspections.csv", index=False)

final_red = final_df.sample(frac = .75, random_state=477)

final_red.to_csv("Data/Data Integration/11.16_Inspections_Reduced.csv", index=False)