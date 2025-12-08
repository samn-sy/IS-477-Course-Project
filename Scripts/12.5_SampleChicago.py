# this code reads the Chicago Dataset into a csv and takes a sample for analysis

import pandas as pd
import numpy as np
import os
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

#script_dir = os.getcwd()
#chicago_path = os.path.join(script_dir, '..', 'Data', 'Original Datasets', '11.7_Chicago_Food_Inspections.csv')
#chicago_cleaned_path = os.path.join(script_dir, '..', 'Data', 'Cleaned Datasets', 'Chicago_Inspections_Data', '11-7-Chicago-Food-Inspections.csv')
chi_cleandf = pd.read_csv(input_file)

chi_cleandf.sample(frac = .27, random_state = 477).to_csv('11.7_Chicago_Food_Inspections_Cleaned_Reduced.csv', index=False)
