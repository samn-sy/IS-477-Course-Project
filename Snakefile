rule run_all:
    input:
        "Visualizations/passing_inspections_year.png",
        "Visualizations/passing_inspections_yearmonth.png"


rule sha256:
    input:
        chicago="Data/Original Datasets/11.7_Chicago_Food_Inspections.csv",
        nyc="Data/Original Datasets/11.7_New_York_City_Inspections.csv"
    output:
        "Data/Data Acquisition/12.5_hashes.sha256"
    shell:
        "python Scripts/12.5_SHA256.py"


rule sample_chicago:
    input:
        "Data/Cleaned Datasets/Chicago_Inspections_Data/11.7_Chicago_Food_Inspections.csv"
    output:
        "Data/Cleaned Datasets/Chicago_Inspections_Data/11.7_Chicago_Food_Inspections_Cleaned_Reduced.csv"
    shell:
        "python Scripts/12.5_SampleChicago.py"


rule sample_nyc:
    input:
        "Data/Cleaned Datasets/NYC_Inspections_Data/11.12_NYC_Inspections_CLEANED.csv"
    output:
        "Data/Cleaned Datasets/NYC_Inspections_Data/11.16_NYC_Inspections_Cleaned_Reduced.csv"
    shell:
        "python Scripts/12.5_SampleNYC.py"


rule data_integration:
    input:
        chicago="Data/Cleaned Datasets/Chicago_Inspections_Data/11.7_Chicago_Food_Inspections_Cleaned_Reduced.csv",
        nyc="Data/Cleaned Datasets/NYC_Inspections_Data/11.16_NYC_Inspections_Cleaned_Reduced.csv"
    output:
        merged="Data/Data Integration/11.16_Inspections_Reduced.csv"
    shell:
        "python Scripts/12.5_DataIntegration.py"


rule visualization:
    input:
        merged="Data/Data Integration/11.16_Inspections_Reduced.csv"
    output:
        year="Visualizations/passing_inspections_year.png",
        month="Visualizations/passing_inspections_yearmonth.png"
    shell:
        "python Scripts/12.7_Visualizations.py"