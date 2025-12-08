**Chicago vs New York City Food Inspections**

**Contributors**:

* Samantha Sy, ORCID: 0009-0002-3181-5731  
* Andres Gomez

**Summary**:  
Food service is an essential part of modern society, shaping how people eat, socialize, and build community. With the rise of delivery apps like DoorDash, Uber Eats, Fantuan, etc., the restaurant industry is more popular than ever. This convenience makes dining out or ordering in a central part of everyday life. These technologies have shaped the way people eat their meals, spend time with friends/family, celebrate events, etc. It is important for restaurants to make sure that their customers are happy and healthy. This includes keeping their food safe for consumption. Health inspections are an important way to make sure that restaurants are maintaining healthy environments for their customers. This is an important aspect of public health, as maintaining health codes ensures that foodborne illnesses do not spread across communities. 

This project focuses on two cities: Chicago and New York City, to analyze the relationship between the two cities' inspection data in a way that aligns with data management/curation/reproductibility principles. Chicago and New York City are two large and diverse urban centers with a plethora of available data for research. This makes these two cities a great source of information to study and develop insights.

Our goal for this project is to gain a better understanding of food safety and health violations so we can better recommend practices/raise awareness for businesses and consumers so they can continue using these services. Foodborne illnesses affect millions of people each year, which leads to medical costs, lost productivity, and sometimes long-term health complications. Restaurants should take inspections seriously, as failure can result in temporarily or permanently closing down the business. Inspection data reveals different issues like temperature control, contamination, or insufficient hygiene practices. By analyzing inspection data, we can identify how well restaurants actually adhere to safety standards and see which violations are occurring. This project will follow the USGS Science Data Lifecycle, as we planned this project, acquired data, processed/cleaned data, analyzed/created visualizations, preserved data (+ findings), and shared it for further enrichment for teaching staff.

Research Questions

1. *How do restaurant inspection outcomes (NYC’s grades vs. Chicago’s results) compare in terms of failure rate across years?*

This question helps us get a grasp of where failure rates are happening in different cities. If this information is cross-referenced with other pieces of data, we can get a data story. For example, if Chicago’s inspection failure rate increased more than usual in one year, we can look at news or other data that may have caused a large number of failed inspections. Therefore, we can predict health inspection scores in different cities that may encounter similar events.

What we found in our analysis is that Chicago has had a higher proportion of passing inspections each year since 2010 compared to New York City. However, there have been no significant rises or falls within each city, as the pass rate looks fairly consistent across the years. Chicago pass rates ranged from 70% to 80% while New York City pass rates ranged from 50% to 60%.

2. *How have average inspection scores (NYC) and pass rates (Chicago) changed from 2015 to 2025?*

This question will help us understand if businesses are improving their pass rates. If there is an increasing trend of passes, what improvements have been made in the past few years that have led to this improvement? If restaurants have been failing more in the past few years, what has been happening in these cities, and what improvements can be made?

What we found interesting in this analysis is that there are a few months (2015-11, 2015-12, and 2021-02), where New York City has a pass rate of nearly (if not) 1.0. This seems impossible, and would require a deeper dive into the dataset to see what events occurred (or did not occur) during these months. It may also require some cross-referencing of new/media outlets to understand the context. There are also a few months where data from New York City is absent. Apart from those outliers, Chicago has had a higher pass rate than New York City over the past ten years. 

**Data profile**:

* For the New York City Inspections dataset  
  * This dataset contains every sustained or not yet adjudicated violation citation from every full or special program inspection conducted up to three years prior to the most recent inspection for restaurants and college cafeterias in an active status on the date of the data pull. This contains all inspected restaurants; ones that pass inspections have one entry, while sustained violations have multiple entries.

The license for this dataset was not found on [Data.gov](http://Data.gov), where this dataset was originally discovered. A quick search through the NYC Data Portal details the following:

“By accessing datasets and feeds available through the NYC.gov Data Mine (or the "Site"), the user agrees to all of the terms of use outlined below as well as the Privacy Policy for NYC.gov. The user also agrees to any additional terms of use defined by entities providing data or feeds through the Site. Entities providing data include, without limitation, agencies, bureaus, offices, departments, and other discrete entities of the City of New York ("City"). Where additional terms apply for a specific entity, dataset, or feed, a link to those terms is provided.”

* The NYC Open Data portal has no restrictions on using the public data, but by accessing it, users agree to the NYC.gov Terms of Use and the NYC.gov Privacy Policy. This means that while the data is free to use, we must also adhere to the terms and policies of the overall NYC.gov website

* For the Chicago Food Inspection dataset  
  * This information is derived from inspections of restaurants and other food establishments in Chicago from January 1, 2010, to the present. Inspections are performed by staff from the Chicago Department of Public Health’s Food Protection Program using a standardized procedure. The results of the inspection are inputted into a database, then reviewed and approved by a State of Illinois Licensed Environmental Health Practitioner (LEHP).

The Chicago Data Portal details the following information about Terms of Use:

“This site provides applications using data that has been modified for use from its source, www.cityofchicago.org, the official website of the City of Chicago.  The City of Chicago makes no claims as to the content, accuracy, timeliness, or completeness of any of the data provided at this site.  The data provided at this site is subject to change at any time.  It is understood that the data provided at this site is being used at one’s own risk.” (Chicago.gov)

* Chicago’s Data Portal seems to act like a bridge between the user and access to the data. It states multiple times that Chicago makes “no warranty, representation, or guaranty as to the content, accuracy, timeliness, or completeness of any of the data” (Chicago.gov).

Both of the datasets we found were available on open data portals, maintaining accessibility for research and use. The NYC Open Data Portal states that “Open Data is free public data published by New York City agencies and other partners.” Meanwhile, the Chicago Data Portal is “required under an Executive Order signed by Mayor Rahm Emanuel on December 10, 2012.” These portals allow for open access and responsible use by users, with care to ensure that bigger city government policies are still being followed.

**Data quality**:

Upon assessment of our datasets, they both looked fairly clean. Using OpenRefine and various types of facets, we observed that a significant portion of the data was consistently formatted. The dataset has a lot of information that we don’t need for analysis. The most important information we need is information on the restaurant and inspection information. There was a lot of extra information on longitude and latitude that was not helpful for our study.

There were a few errors/outliers to point out:

* There were a few qualitative differences between observations in the datasets. Upon analysis in OpenRefine, there were many different ways of formatting street names. This included different syntaxes for numbered street names (i.e., First Street, 1 Street, 1st Street), inconsistent street abbreviations (i.e., ave vs avenue, dr vs drive, pkwy vs parkway), some spelling errors (“Beverly” instead of “Beverley”), and even some other outlier notations for streets. This was especially apparent for establishments in certain buildings, such as JFK International Airport or malls, which noted floor numbers in the street address.

* Quantitative data quality issues were also present in our datasets. In the New York City dataset documentation, it describes that records “are also included for each restaurant that has applied for a permit but has not yet been inspected and for inspections resulting in no violations. Establishments with an inspection date of 1/1/1900 are new establishments that have not yet received an inspection.” This made the analysis confusing as the datetime information did not align with additional data, and was removed for our analysis. Additionally, many values were not considered to be numerical in columns like License and Zip Code.

* Documentation in the Chicago Food Inspections dataset contains a disclaimer that describes that attempts have been made to minimize duplicate inspection reports. Although the dataset may still contain duplicates and appropriate precautions should be exercised when viewing or analyzing this data.

Based on these observations, the New York City and Chicago food inspection datasets were deemed of good quality, although some data cleaning was necessary to prepare them for use in this project. With cleaning, these are the attributes we chose for our integrated dataset:

- **RecordID \[Int\]:** Unique identifier for each observation.  
- **DBA Name \[str\]:** Legal/public business name of the establishment.  
- **CAMIS \[Int64\]:** Unique NYC health inspection ID (NYC only).  
- **License Number \[Int64\]:** Unique establishment license number (Chicago only).  
- **Address \[str\]:** Full address of the establishment.  
- **Street \[str\]:** Street of the establishment (NYC only).  
- **City \[str\]:** Chicago or New York City.  
- **Boro \[str\]:** Borough (NYC only).  
- **State \[str\]:** State of the establishment (IL or NY).  
- **Zip \[Int\]:** Zip code of establishment.  
- **Inspection Date \[datetime\]:** Date of inspection.  
- **Risk \[str\]:** Risk category of establishment (1–3; Chicago only).  
- **Critical Flag \[str\]:** Indicates critical violation (Critical / Not Critical / Not Applicable; NYC only).  
- **Facility Type \[str\]:** Type of establishment (e.g., restaurant, grocery, bakery).  
- Cuisine Description \[str\]: Cuisine type (optional).  
- **Violations \[str\]:** Description of violations noted during inspection.  
- **Results \[str\]:** Outcome of inspection (Pass / Pass with Conditions / Fail / Not Located / Out of Business; Chicago only).

* **Findings**:

In preparation for our data visualizations, we found the following results from the Chicago “Results” attribute:

* Business Not Located Results: 0.03%  
* Not Ready Results: 1.37%  
* No Entry Results: 4.48%  
* Out of Business Results: 8.34%

These categories represent inspections where either the business was inaccessible, had not received an inspection, or was not operational. Given our research question regards an establishment’s inspection pass/fail rate, we opted to exclude/disregard these results. One thing that stands out is the number of “Out of Business” results. Although it is not the focus of our research question, it is definitely something that should be flagged and further looked into in future works.

Additionally, we found this result comparing the NYC “Critical Flag” results:

* Not Applicable Results: 1.41%

We are treating the Critical Flag column as the same as the Results column in the Chicago dataset, as it will tell us similar information about risks and concerns that we should have over an establishment.

Upon looking at our visualizations, we observed that the proportion of establishments passing inspections was fairly stable. We found in our analysis that Chicago has had a higher proportion of passing inspections each year since 2010 compared to New York City. However, there have been no significant rises or falls within each city, as the pass rate looks fairly consistent across the years. Chicago pass rates ranged from 70% to 80% while New York City pass rates ranged from 50% to 60%. There is a general uniformity between the cities, reflecting an overall higher level of compliance among food establishments. This suggests that businesses seem to understand the importance of health codes and do their best to abide by health standards, positively impacting public/community health. While the data is slightly different, it also reflects some baseline consistency in food inspection standards. Further research would be necessary to get a better understanding of each city’s standards and inspection logistics. With that information, public health establishments across the United States can make better-informed decisions for their communities.

We also found that there are a few months (2015-11, 2015-12, and 2021-02), where New York City has a pass rate of nearly (if not) 1.0. This seems improbable because every inspection during those months would have to pass. Given the sheer size and diversity of New York City, this data seems like an outlier. There are questions raised about the number of inspections conducted during these months, as a lower number during that month could yield a higher pass rate. It may also require some cross-referencing of new/media outlets to understand the context. 

There are also a few months where data from New York City is absent. This absence could be for numerous reasons: reporting gaps, technical issues in data collection, or other events.

Apart from those outliers, Chicago has had a higher pass rate than New York City over the past ten years. Although the difference is not extreme, this pattern suggests that Chicago, on average, has fewer critical violations during inspections. There can be further research into Chicago’s public health policies and food inspection standards to find out why the rate is higher. Is it a higher rate of compliance? Is it because of a smaller pool of restaurants?

* **Future work**:

For future work, we recommend looking at external data to continue the integration process and develop a better understanding of the passing rates. For this project, it was realized that combining the two datasets is not as straightforward as it initially seemed. There were different data collection methods and different column variables. In order to combine, we had to decide which columns to keep, which to rename, and to what, and what the implications were of each decision made for integration. It would be recommended that, for future data collection, there be a standardization for data. For example, each data collection on food inspections, let there be a minimum standard to have whether or not the inspection resulted in a pass or failure, the risk, an ID, address, business name, and alias, etc. So, while this project helped uncover insights on pass rates for both Chicago and New York City, it also uncovered other opportunities for deeper analysis. 

Our analysis demonstrated stable pass/fail patterns over time, but several unexpected findings, like near-perfect pass rates for the NYC data, suggest that either external events may have influenced inspection trends, a data entry error, or a simple lack of inspections made for a given month (i.e., if only two inspections were made in a month and both pass). However, introducing contextual datasets such as COVID-19 shutdown and reopening periods may align with periods when inspections were paused or reduced due to public health emergencies. Contextual analysis could convert simple descriptive trends into quality narratives, which is what we are trying to achieve.

Another path to take with this data is shifting the narrative to looking at violation level patterns instead of only pass/fail outcomes. Although both datasets had different ways to express if the inspection resulted in a pass or a fail, both datasets have detailed violation codes that reveal specific food safety hazards. It is also possible to look at spatial analysis since both datasets have some sort of geographic information. Work can include looking at whether socioeconomic variables correlate with inspection outcomes or mapping failure hotspots using other tools like GIS. There are also ways to analyze unstructured textual data. By understanding what words/violations are commonly mentioned, we can gather new recommendations for establishments to prevent failing inspections from commonly violated codes.

A more direct work that could be done is predictive modeling. It would be useful to build a model to predict inspection outcomes based on factors such as facility type, inspection frequency, geographic location, or time of year. Doing this while integrating more quality data from other urban hubs, like from Los Angeles or Miami, could eventually support a nationwide analysis of restaurant food safety.

Overall, this project established a strong foundation for comparing two major cities' inspection systems, but also highlighted the difficulty of integrating public datasets. Future work should focus on standardization, contextual/external sources, spatial and violation level analysis, and predictive modeling. This future work has the potential to not only increase the scientific value of the project but also contribute to practical insights for public health departments, policymakers, and food establishments.

* **Reproducibility**

1\. Acquire Data

Google Drive was an easy way to store our information for asynchronous use remotely. This method proved to be useful as well because Git has a maximum allowed file size of 100 MB, and our datasets are both over that limit. Google Drive helps mitigate our file size limitation. The files downloaded on November 7th, as well as other files that were too large for GitHub, are contained and **can be downloaded from there.**

[https://drive.google.com/drive/u/2/folders/1GyPrGygC1G9P3-tIosZeoEGwUJfcxy0I](https://drive.google.com/drive/u/2/folders/1GyPrGygC1G9P3-tIosZeoEGwUJfcxy0I)

Download links from the respective data portals: (\*Note that our datasets were retrieved on 11/7)

* NYC: Download from [NYC Open Data Portal](https://data.cityofnewyork.us/d/43nn-pn8j) (API: https://data.cityofnewyork.us/api/v3/views/43nn-pn8j/query.json)  
* Chicago: Download from [Chicago Data Portal](https://data.cityofchicago.org/Health-Human-Services/Food-Inspections/4ijn-s7e5/about_data) (API: https://data.cityofchicago.org/api/v3/views/4ijn-s7e5/query.json).

* Save files locally using naming convention: \[date\]\_\[city\]\_Inspections.csv.

2\. Verify Data Integrity

* Use 12.5\_SHA256.ipynb (or 12.5\_SHA256.py) to generate SHA-256 hashes for each dataset.

3\. Clean Data

* Tools: OpenRefine \+ Python  
* Steps for NYC:  
  * Convert columns to datetime.  
  * Correct spelling errors and standardize street names.

  * Remove invalid or outlier dates (e.g., 1/1/1900).  
  * Keep key columns for analysis: DBA, BORO, STREET, ZIPCODE, CUISINE DESCRIPTION, INSPECTION DATE, VIOLATION DESCRIPTION, CRITICAL FLAG.

* Steps for Chicago:  
  * Convert data types as needed.  
  * Standardize string columns (capitalization, punctuation).  
  * Clean categorical values using clustering/merging.  
  * Keep key columns: License \#, Facility Type, Risk, Address, Results.

4\. Sample Data  
Reduce dataset size using the Pandas sample function for easier analysis:

df.sample(frac=0.50, random\_state=477)  \# NYC  
df.sample(frac=0.75, random\_state=477)  \# Merged

5\. Merge Datasets  
Align columns and rename NYC columns to match Chicago:

 nyc \= nyc.rename(  
    columns={  
"DBA": "DBA Name",   
"BORO": "Boro",  
"STREET": "Street",   
"ZIPCODE": "Zip",   
"CUISINE DESCRIPTION": "Cuisine Description",   
"INSPECTION DATE": "Inspection Date",   
"VIOLATION DESCRIPTION": "Violations",   
"CRITICAL FLAG": "Critical Flag"}  
)

* Convert DBA Name and Violations to uppercase for consistency.  
* Concatenate datasets using pd.concat.  
* Add a unique RecordID for each row.

6\. Save Merged Dataset

* Full merged dataset: 11.16\_Inspections.csv.

* Reduced dataset (75%): 11.16\_Inspections\_Reduced.csv.

7\. Visualize Data

* Filter out irrelevant values:  
  * Chicago: Business Not Located, Not Ready, No Entry, Out of Business.  
  * NYC: Not Applicable.

* Treat Critical Flag (NYC) as equivalent to Results (Chicago).  
* Generate bar plots:  
  * Proportion of passing inspections by year.  
  * Proportion of passing inspections by year-month.

8\. Automation

* All steps are scripted in the Snakemake workflow:  
  * 12.5\_SHA256.py → Data integrity  
  * 12.5\_SampleChicago → Sampling  
  * 12.5\_SampleNYC.py → Sampling  
  * 12.5\_DataIntegration.py → Data merging  
  * 12.7\_Visualizations.py → Plotting  
  * Input/output paths and sampling steps are documented in the Snakefile.

**Licenses for Data & Software**  
Python software and documentation are licensed under the Python Software Foundation License Version 2\.

The numpy license is as follows:  
This software is provided by the copyright holders and contributors "as is" and any express or implied warranties, including, but not limited to, the implied warranties of merchantability and fitness for a particular purpose are disclaimed. in no event shall the copyright owner or contributors be liable for any direct, indirect, incidental, special, exemplary, or consequential damages (including, but not limited to, procurement of substitute goods or services; loss of use, data, or profits; or business interruption) however caused and on any theory of liability, whether in contract, strict liability, or tort (including negligence or otherwise) arising in any way out of the use of this software, even if advised of the possibility of such damage.

Pandas is released under a permissive BSD license, meaning people can freely use, modify, and distribute it for any purpose, including commercial applications, as long as they retain the original copyright notice, conditions, and disclaimer, and clearly mark any modified source code.

Matplotlib is distributed under a BSD-style license, which is also compatible with the Python Software Foundation (PSF) license. This license is considered permissive, meaning it has similar permissions to packages like Pandas.

For the New York City Inspections dataset, there is no license information provided on Data.gov. However, the NYC Open Data FAQ details the terms and conditions related to information collected from the NYC OpenData portal

By accessing datasets and feeds available through the NYC.gov Data Mine (or the "Site"), the user agrees to all of the terms of use outlined below as well as the Privacy Policy for NYC.gov. The user also agrees to any additional terms of use defined by entities providing data or feeds through the Site. Entities providing data include, without limitation, agencies, bureaus, offices, departments and other discrete entities of the City of New York ("City"). Where additional terms apply for a specific entity, dataset or feed, a link to those terms is provided.

The NYC Open Data portal has no restrictions on using the public data, but by accessing it, users agree to the NYC.gov Terms of Use and the NYC.gov Privacy Policy. This means that while the data is free to use, we must also adhere to the terms and policies of the overall NYC.gov website

For the Chicago Food Inspection dataset, there was no direct link to find the licensing details on the website where you download the data. There was only an indication to “See Terms of Use” and after a quick Google Search, “Chicago Data Portal Terms of Use” it was the first link that popped up. Chicago’s Data Portal seems to act like a bridge between the user and access to the data. It states multiple times that Chicago makes “no warranty, representation, or guaranty as to the content, accuracy, timeliness, or completeness of any of the data” ([Chicago.gov](http://Chicago.gov)). 

**References**

### **Datasets**

City of Chicago. (2024). *Food Inspections* \[Data set\]. Chicago Data Portal. https://data.cityofchicago.org/Health-Human-Services/Food-Inspections/4ijn-s7e5

City of New York. (2024). *DOHMH New York City Restaurant Inspection Results* \[Data set\]. NYC OpenData. https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/43nn-pn8j

### **Software & Code**

Harris, C.R., Millman, K.J., van der Walt, S.J. et al. *Array programming with NumPy*. Nature 585, 357–362 (2020). DOI: 10.1038/s41586-020-2649-2.

Köster, J., & Rahmann, S. (2012). *Snakemake*. https://snakemake.readthedocs.io/

pandas development team. (2024). *pandas* (v2.2.2). https://pandas.pydata.org

Python Software Foundation. (2024). *Python* (v3.12) \[Computer software\]. https://www.python.org/