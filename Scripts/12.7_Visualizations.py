import pandas as pd
import numpy as np
import os
import sys
import matplotlib.pyplot as plt

chicago_file = sys.argv[1]   
nyc_file = sys.argv[2]       
integrated_file = sys.argv[3]  
output_year = sys.argv[4]      
output_yearmonth = sys.argv[5] 

os.makedirs('Visualizations', exist_ok = True)
os.makedirs(os.path.dirname(output_year), exist_ok=True)
os.makedirs(os.path.dirname(output_yearmonth), exist_ok=True)

chicago = pd.read_csv(chicago_file)
nyc = pd.read_csv(nyc_file)
integrated = pd.read_csv(integrated_file)

#script_dir = os.getcwd()
#chicago_path = os.path.join(script_dir, '..', 'Data', 'Data Integration', '11.16_Chicago_Inspections_Reduced.csv')
#newYork_path = os.path.join(script_dir, '..', 'Data', 'Data Integration', '11.16_NYC_Inspections_Reduced.csv')
#integrated_path = os.path.join(script_dir, '..', 'Data', 'Data Integration', '11.16_Inspections_Reduced.csv')

#chicago = pd.read_csv('11.16_Chicago_Inspections_Reduced.csv')
#nyc = pd.read_csv('11.16_NYC_Inspections_Reduced.csv')
#integrated = pd.read_csv('11.16_Inspections_Reduced.csv')

chicago['Results'].unique()

print(f"Business Not Located Results: {round(len(chicago[chicago.Results == 'Business Not Located']) / len(chicago) * 100, 2)}%")
print(f"Not Ready Results: {round(len(chicago[chicago.Results == 'Not Ready']) / len(chicago) * 100, 2)}%")
print(f"No Entry Results: {round(len(chicago[chicago.Results == 'No Entry']) / len(chicago) * 100, 2)}%")
print(f"Out of Business Results: {round(len(chicago[chicago.Results == 'Out of Business']) / len(chicago) * 100, 2)}%")

chicagoFiltered = chicago[~chicago.Results.isin(['Business Not Located', 'Not Ready', 'No Entry', 'Out of Business'])]

nyc['Critical Flag'].unique()

nycFiltered = nyc[nyc['Critical Flag'].isin(['Critical', 'Not Critical'])]

chicagoFiltered['Year'] = pd.to_datetime(chicagoFiltered['Inspection Date']).dt.year
nycFiltered['Year'] = pd.to_datetime(nycFiltered['Inspection Date']).dt.year

chicagoFiltered['Pass Y/N'] = chicagoFiltered['Results'].apply(lambda x: 'Y' if 'Pass' in x else 'N')
nycFiltered['Pass Y/N'] = nycFiltered['Critical Flag'].apply(lambda x: 'N' if 'Not' in x else 'Y')

chicagoPassProp = chicagoFiltered[['Year', 'Pass Y/N']].groupby('Year').value_counts(normalize = True).reset_index()[['Year', 'proportion']]
nycPassProp = nycFiltered[['Year', 'Pass Y/N']].groupby('Year').value_counts(normalize = True).reset_index()[['Year', 'proportion']]

plt.bar(chicagoPassProp['Year'], chicagoPassProp['proportion'], label='Chicago')
plt.bar(nycPassProp['Year'], nycPassProp['proportion'], label='NYC')

plt.title('Proportion of Passing Inspections by Year')
plt.xlabel('Year')
plt.ylabel('Proportion of Passing Inspections')

plt.legend(loc = 'upper left', bbox_to_anchor=(1, .6))
#plt.savefig("passing_inspections_year.png")
plt.savefig(output_year)
plt.show()

chicagoFiltered = chicagoFiltered[chicagoFiltered.Year >= 2015]
nycFiltered = nycFiltered[nycFiltered.Year >= 2015]

chicagoFiltered.loc[:, 'YearMonth'] = pd.to_datetime(chicagoFiltered.loc[:, 'Inspection Date']).dt.to_period('M')
nycFiltered.loc[:, 'YearMonth'] = pd.to_datetime(nycFiltered.loc[:, 'Inspection Date']).dt.to_period('M')

chicagoPassPropYM = chicagoFiltered[['YearMonth', 'Pass Y/N']].groupby(['YearMonth']).value_counts(normalize=True).reset_index()
nycPassPropYM = nycFiltered[['YearMonth', 'Pass Y/N']].groupby(['YearMonth']).value_counts(normalize=True).reset_index()

fig, ax = plt.subplots(figsize = (15, 8))
plt.bar(chicagoPassPropYM['YearMonth'].astype(str), chicagoPassPropYM['proportion'], label='Chicago')
plt.bar(nycPassPropYM['YearMonth'].astype(str), nycPassPropYM['proportion'], label='NYC')

plt.xticks(chicagoPassPropYM['YearMonth'].astype('str')[::12], rotation=45)
plt.savefig(output_yearmonth)
#plt.savefig("passing_inspections_yearmonth.png") 
plt.show()