### Interim Status Report

For the New York City Inspections dataset, there is no license information provided on [Data.gov](http://Data.gov). However, the [NYC.gov](http://NYC.gov) website details the terms and conditions related to information collected from the NYC OpenData portal in the Intellectual Property section.

The City respects the intellectual property of others and it asks its users to do the same. Service marks and trademarks contained in or displayed on NYC.gov, and the contents of linked sites operated by third parties, are the property of their respective owners (which may be the City). All other design, information, text, graphics, images, pages, interfaces, links, software, and other items and materials contained in or displayed on NYC.gov, and the selection and arrangements thereof, are the property of the City of New York. All rights are reserved (NYC.gov). 

It also details the Digital Millennium Copyright Act (“DMCA”) Notice/Takedown Request, discussing data owner’s copyright infringement.

For the Chicago Food Inspection dataset, there was no direct link to find the licensing details on the website where you download the data. There was only an indication to “See Terms of Use” and after a quick Google Search “chicago data portal terms of use” it was the [first link](https://www.chicago.gov/city/en/narr/foia/data_disclaimer.html) that popped up. Chicago’s Data Portal seems to act like a bridge between the user and access to the data. It states multiple times that Chicago makes “no warranty, representation, or guaranty as to the content, accuracy, timeliness, or completeness of any of the data” ([Chicago.gov](http://Chicago.gov)). The following is a disclaimer that any user that uses data from their website should include in their reports:

“This site provides applications using data that has been modified for use from its original source, www.cityofchicago.org, the official website of the City of Chicago.  The City of Chicago makes no claims as to the content, accuracy, timeliness, or completeness of any of the data provided at this site.  The data provided at this site is subject to change at any time.  It is understood that the data provided at this site is being used at one’s own risk.” (Chicago.gov)

The Chicago government also hold reservation rights for the data and may discontinue availability of data at any time for any reason and also has indemnity terms and conditions as well.

**Storage and organization:**  
We found that Google Drive would be an easy way to remotely store our information for asynchronous use between the two of us, as our schedules are different. This method proved to be useful as well because Git has a maximum allowed file size of 100 MB, and our datasets are both over that limit. So, choosing Google Drive helps mitigate that limitation. Managing the data would also be much easier with a remote filesystem. We used similar naming conventions \[date\]\_\[city\]\_Inspections.csv  
Our CSV files are considered tabular and structured data, but can also be considered semi-structured in different contexts based on their predefined schema/datatypes at the file level.

**Data quality:**   
Upon assessment of our datasets, they both looked fairly clean. Using OpenRefine and many different types of facets, we could see that a lot of the data was consistently formatted. The dataset has a lot of information that we don’t need for analysis. The most important information we need is information on the restaurant and inspection information. There was a lot of extra information on longitude and latitude that was not helpful for our study.

There were a few errors/outliers to point out:  
Qualitative

* Noticed many different ways of formatting street names, some examples of different formatting include  
  * Different ways of writing out numeric streets (first, 1st, or 1\)  
  * Inconsistent abbreviations (ave vs avenue, dr vs drive, pkwy vs parkway)  
  * Some spelling errors (“Beverly” instead of “Beverley”)

Quantitative

* Many of the restaurants had an inspection date of 1/1/1900  
  * This was stated in the description of the dataset that these are new establishments that have not yet received an inspection.  
* Many values were not considered to be numerical in columns like License and zip code.

Generally, our datasets contained a lot of typos and different syntaxes that we wanted to make sure were cleaned so our data was formatted in a similar manner.

**Note:** The dataset CSV files were downloaded from their respective portals on November 7th, 2025\. Although these datasets are continuously and automatically updated. This fulfills the data quality requirement of timeliness.

**Data cleaning (cf. Module 10):** 

Sam used OpenRefine for the initial data cleaning stage. She spent a lot of time reviewing the addresses in the New York City dataset to ensure they were accurate and had a consistent format. This included converting columns to datetime, fixing spelling errors, reformatting street names, etc. Another thing that was done was removing outliers. Establishments with an inspection date of 1/1/1900 are new establishments that have not yet received an inspection; this created an interesting outlier in our data. As our research question is focused on food quality and safety, she opted to exclude them from the cleaned dataset.

Using Visual Studio Code and Python, she took the OpenRefine cleaned dataset and obtained 50% in a random sample (random\_state \= 477). 

	Andres took a similar approach to cleaning the Chicago dataset. He initially was going to use Python, but realized OpenRefine had really useful tools for data cleaning, such as data type formatting and combining multiple string values that vary by punctuation, capitalization, or typos. Clustering and merging values were the bulk of the cleaning, as the dataset has a lot of string values and values that are subject to typos and inconsistencies due to there not being a clear structure for each category. It seems as though there would be a list of categories to choose from, and occasionally the category would change based on either a typo or additional information added to the category, like “1223” with no clear indication of the meaning of the number.

**Data integration:**  
Since we are combining data from two different cities, there are various conventions for naming/schemas. There are many columns related to the violations that did not match any column/attribute in the other dataset. However, we still thought that they would be insightful for our work, so we opted to include them, even if there was no equivalent value. This includes columns like:

* Chicago Dataset: License \#, Facility Type, Risk, Address (similar to street in the NYC dataset, but slightly different), Results  
* New York City Dataset: CAMIS, Boro, Critical Flag, Street, Cuisine Description

We utilized the concat function in pandas to match column names/attributes. Initially, there were columns in both datasets that communicated the same information (i.e., DBA in the NYC Dataset and DBA Name in the Chicago Dataset). We wanted to make sure that the information in the same columns had the same syntax, so for columns like DBA Name and Violations, we used the .str.upper() function to make sure that all of our entries had the same syntax.

To fit the constraints of GitHub, our dataset was reduced using the sample function, taking 75% of the observations with a random state of 477 once again.

Due to scheduling constraints present mainly in October, we did not have as much time to dedicate to our extraction and enrichment. In the next few weeks, we would like to look at our dataset(s) and visualize some of our data based on different patterns like inspection dates, extract text to find out more about violations, etc.

**Updated Timeline:**

11/17-11/21 \-\> Analyze our dataset, create visualizations as necessary, and work on the automated end-to-end workflow using Python and Snakemake

- As mentioned above, we would like to create visualizations on the spread of data across our datasets  
- Additionally, based on some of the information on Python we have learned in class, we would like to analyze unstructured text data in the “Violations” column  
  - What are some commonly used words in this column? What information can we learn?  
  - There are many different violations, and to different degrees of severity. It would be interesting to see if any violations are mentioned a lot in this column and inform us on what we can do to inform the community/food establishments on how to provide better service while passing health inspections

11/22-11/30 \-\> Thanksgiving Break, any extra work that needs to be done from the past week should be finished during Thanksgiving by Sam

12/1-12/8 \-\> Relate our project to one of the lifecycle models we discussed in lecture, address ethical data handling, transparency, add metadata, and document everything in the final report

12/9-12/10 \-\> Finish cleaning up any final artifacts and the final report to turn in by 11:59 PM 12/10

**Contributions:**

**Samantha Sy \-\>** Cleaned the New York City dataset in OpenRefine, making the dataset more fit for use in Python, integrated the Chicago and New York City datasets using an append method in Python, and discussed the respective steps in the report

**Andres Gomez:** Cleaned Chicago Food Inspection dataset using OpenRefine and made a clean folder structure for better workflow and intuitive Data Management. Wrote a notebook that lays out how the reduced data files were made for reproducibility and updated the [README.md](http://README.md) file to include the Google Drive folder where the full datasets are stored.

**Both:** Upkeep on the Google Drive filesystem and writing our Status Report  
