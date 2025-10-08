# **Project Plan**

# **Overview**

Food service is an essential part of modern society. With the rise of delivery apps like DoorDash, Uber Eats, Fantuan, etc., the restaurant business is more popular than ever. Many people use it as a convenient way to eat their meals, spend time with friends/family, celebrate events, etc. It is important for restaurants to make sure that their customers are happy and healthy. This includes keeping their food safe for consumption. Health inspections are a way to make sure that restaurants are up to code and continue to keep their customers safe. Our goal for this project is to gain a better understanding of food safety and health violations so we can better recommend practices/raise awareness for businesses and consumers so they can continue using these services.

# **Research Question(s)**

Some of the questions we have ideated include the following, sorted by topics:

**Comparison Questions**

1. How do restaurant inspection outcomes (NYC’s grades vs. Chicago’s results) compare in terms of failure rate across years?  
2. How have average inspection scores (NYC) and pass rates (Chicago) changed from 2010–2025?

**Model Building Question**

1. Does the time since the last inspection increase the likelihood of a negative outcome?

# **Team**

## ***Andres Gomez***

Responsible for the end-to-end analysis of the City of Chicago Dataset. This includes initial data acquisition, cleaning, exploration, visualization, and modeling. Andres will also assist in aligning the Chicago dataset’s structure and terminology with that of the NYC dataset to enable cross-city comparison.

## ***Samantha Sy***

Responsible for the end-to-end analysis of the New York City Dataset. This includes initial data acquisition, cleaning, exploration, visualization, and modeling. Samantha will also assist in aligning the Chicago dataset’s structure and terminology with that of the New York City dataset to enable in-depth comparison.

## ***Overall***

We will be splitting up the work as evenly as possible throughout the course of the project development. Both members will work together to answer the research questions and will communicate when work has progressed so that we are on the same page. We will both have responsibilities at each sub-phase of the project and will have different responsibilities week by week, depending on the needs/quality of our datasets. All code and analysis will be version-controlled through GitHub, where individual contributions will be tracked through commits. This will ensure transparency for work distribution. Team members will maintain active communication through weekly check-ins and shared documentation. Any major changes in workflow or analysis will be discussed and approved jointly to prevent overlap or redundant work.

# **Datasets**

## ***Food Safety***

* [https://catalog.data.gov/dataset/dohmh-new-york-city-restaurant-inspection-results](https://catalog.data.gov/dataset/dohmh-new-york-city-restaurant-inspection-results)  
  * This dataset contains every sustained or not yet adjudicated violation citation from every full or special program inspection conducted up to three years prior to the most recent inspection for restaurants and college cafeterias in an active status on the date of the data pull. This contains all inspected restaurants; ones that pass inspections have one entry, while sustained violations have multiple entries.  
* [https://data.cityofchicago.org/Health-Human-Services/Food-Inspections/4ijn-s7e5/about\_data](https://data.cityofchicago.org/Health-Human-Services/Food-Inspections/4ijn-s7e5/about_data)  
  * This information is derived from inspections of restaurants and other food establishments in Chicago from January 1, 2010, to the present. Inspections are performed by staff from the Chicago Department of Public Health’s Food Protection Program using a standardized procedure. The results of the inspection are inputted into a database, then reviewed and approved by a State of Illinois Licensed Environmental Health Practitioner (LEHP).

One of these datasets was retrieved from the [Data.gov](http://Data.gov) website, and the other from the [cityofchicago.org](https://data.cityofchicago.org/d/4ijn-s7e5) website. These datasets have information about region-specific inspections from New York City and the City of Chicago. Using this information, we will be able to analyze patterns in violations, which can help us recommend better practices for restaurants across the country. 

# **Timeline**

We will work together on all these steps over the next month. As of today, we have two distinct datasets from well-known public databases ([nyc.gov](http://nyc.gov) and [cityofchicago.org](http://cityofchicago.org)). These datasets have different points of data/schemas for analysis based on our Module 3 lecture. Using these datasets, we will create an organizational strategy and organize our data according to what we learned in Modules 4 and 5\. After that, we will get to the analysis and dive deeper into our data. This will involve using Python/Pandas and SQL to clean data and ensure consistency within our schema, documenting the methods used to manipulate the data. 

In November, we will focus on finishing and cleaning up the rest of our project.

* **Workflow automation and provenance**  
  * Here, we will develop an automated end-to-end workflow   
* **Reproducibility and transparency**   
  * Here, we will ensure that whatever steps we take, we will document them in a way so that anyone can reproduce our workflow and analysis  
* **Metadata and data documentation**  
  * Here we will build on our previous step and continue to ensure that metadata documentation is held to the standard of discovery, understandability, and reuse.

At the end, we will also tie everything back to the data lifecycle of our project as well as the legal implications of our analysis. These datasets do not provide licenses; both datasets provide their Terms of Use, highlighting that their data should be used in compliance with the law and not wrongfully reproduced/violate copyright. This will all be collected for the Final Project Submission, which will consist of all the steps above and their related artifacts (Scripts, Documentation, Licenses, etc.).

# **Constraints**

These datasets limit us to two specific regions in the United States. Although New York City and Chicago are large and diversely populated, they will not provide the full scope and be fully generalizable to the greater U.S. population. Another limitation is the inconsistency between the two datasets. Since these two datasets were made from separate organizations, different variables were collected, and therefore, there is a case where one dataset has a certain column, whereas the other does not. For example, New York City uses a numeric and letter grade, whereas Chicago categorizes results as “Pass”, “Fail”, etc. Key missing values seem apparent in each dataset, like violation descriptions and inspection results, which limit our ability to accurately use each observation in each dataset. 

# **Gaps**

Given our position and time in the course, we would need more information on the later modules. Things like automated workflow are something that our team has limited information on. This is something we plan to implement after Modules 11/12 and the status report. Another thing that will be interesting to learn is part of Module 15: Metadata and data documentation. It is a new topic to learn to purposely add metadata to our GitHub repository. 

