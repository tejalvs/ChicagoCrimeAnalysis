# ChicagoCrimeAnalysis
# jupyter notebook is required for running all the *.ipynb file

Final Files:

DataCleaning_1.ipynb
DataCleaning_2.ipynb
Visualisations.ipynb
Mining.ipynb
dbCredentials.txt

# Steps to follow:


**1.Download the following datasets from the given link** :
Crime.csv: https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2
Census.csv: https://data.cityofchicago.org/Health-Human-Services/hardship-index/792q-4jtu
CommAreas.csv: https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-Community-Areas-current-/cauq-8yn6

**Kindly rename the files as Crime.csv , Census.csv and CommAreas.csv respectively.**
This file contains the dataset in a csv format. 

**2.Store the csv files in same directory as the .ipynb file**

**3.Go to the directory where the files are stored**: 
   cd filepath

**4. Change the dbCredentials.txt file to enter the mySQL db crentials of the user**
    The values that can be changed are below:
    host=localhost
    uname=root
    password=password
    dbName=ChicagoData
    dbName2=ChicagoDataForMining
    
    Please change uname and password field. Do NOT put spaces between or after the values when changing.

**5. Run the .ipynb file using the following command in jupter notebook** :
    Run in this order:
        DataCleaning_1.ipynb
        DataCleaning_2.ipynb
        Visualisations.ipynb
        Mining.ipynb

**6. The average execution time for the files is as below:
    DataCleaning_1.ipynb - 5-6 hrs ***
    DataCleaning_2.ipynb - 20-30 mins ***
    Visualisations.ipynb - 7-8 hrs ***
    Mining.ipynb         - 3-4 hrs ***
    
    ***As tested on machine with specs 
    2015 Macbook pro
    i5 7th gen
    mac OS X
    8 gb RAM
    256 GB SSD