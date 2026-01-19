# MSc Project 
## Data analysis and Predictive modelling on Career Trajectories

This is the source code and data used to complete the analysis for this Msc Report

### Data in repository
- UKHLS-6614-spss - this holds individual response files for Harmonised British Household Panel Survey (BHPS) Waves 1-18 1991 - 2009, Understanding Society: the UK Household Longitudinal Study (UKHLS) Waves 1-15 2009 - 2024
- combined_core_analysis.csv - hold the initial extracted file 
- BPHS_UKHLS_clean_renamed.csv - this holds the cleaned dataset for EDA
- UK Gender Pay Gap 2017 - 2025.csv dataset for EDA
- HR_Analytics for Predictive modelling

### Source code
It contains 4 files that are used in the following order:-

1. Data Pre-processing
- the UKHLS&BHPS_extraction python script is used to transform individual response files into one csv file.
- After the csv file has been created the UKHLS&BHPS_cleaning is used to clean and normalise the file
2. Exploratory data analysis
- For this step Rstudio is used
- The csv file for UKHLS&BHPS file along with Gender Pay Gap data is then pulled into Rstudio for Exploratory analysis
- The following files are used to conduct Exploratory Data Analysis with 
  - GPG EDA.Rmd 
  - UKHLS/BHPS EDA.Rmd
3. Univariate Analysis 
- A Python script 'Univariate Analysis.py' is then used to conduct Univariate analysis on key variables within the HR_Analytics Dataset
4. Predictive Model
- A Python script 'Predictive Model' is then used to conduct Predictive modelling on career trajectories.
