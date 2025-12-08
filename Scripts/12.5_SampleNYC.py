# this code takes the cleaned nyc inspections and takes a sample of it for easier analysis

import pandas as pd

df = pd.read_csv("11.12_NYC_Inspections_CLEANED.csv")
df = df[['CAMIS', 'DBA', 'BORO', 'STREET', 'ZIPCODE', 'CUISINE DESCRIPTION', 'INSPECTION DATE', 'ACTION', 'VIOLATION DESCRIPTION', 'CRITICAL FLAG']]
df = df.sample(frac = 0.50, random_state = 477)
df.to_csv('11.16_NYC_Inspections_Cleaned_Reduced.csv', index = False)