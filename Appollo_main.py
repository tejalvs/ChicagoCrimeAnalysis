'''Import necessary packages '''
import time
import numpy as np
import pandas as pd
from pandas import *
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")



def Main():
    Crimes=read_files('Crimes.csv')
    '''Understanding the shape of data'''
    print("-----Understanding the shape of data----")
    Crimes.info()
    Census=read_files('Census.csv')
    Census.info()

    print("-----Sample records from the Census dataset-----")
    print(Census.head(10))
    print("-----Sample records from the Crime dataset-----")
    print(Crimes.head(10))

    '''Create a copy of original dataset'''
    Crimes_copy = Crimes.copy()
    Census_copy = Census.copy()

    '''Removing Duplicate columns of Longitude and Latitude as separate Location column is present'''
    print('----Removing Duplicate columns of Longitude and Latitude as separate Location column is present-----')
    Crimes_copy.drop(['Latitude', 'Longitude'], axis=1, inplace=True)
    print(Crimes_copy.head(5))

    '''Replacing spaces in the column headers for easy of access'''
    Crimes_copy.columns = Crimes_copy.columns.str.replace(' ', '')
    print("Columns are: ",Crimes_copy.columns)

    '''Conversion of Date Time to python's DateTime format'''
    Crimes_copy.Date = pd.to_datetime(Crimes_copy.Date, format='%m/%d/%Y %I:%M:%S %p')
    Crimes_copy.index = pd.DatetimeIndex(Crimes_copy.Date)

    print("----Checking for missing values in the data----")
    missingValues(Census_copy,"census")
    missingValues(Crimes_copy,"crime")
    print("Missing data has been removed")
    visualisation(Crimes_copy)

def visualisation(dataset):
    '''various visualisation of our data to answer some questions'''
    '''Which crimes happen the most ?'''
    plt.figure(figsize=(15, 10))
    sns.countplot(y='PrimaryType', data=dataset, order=dataset['PrimaryType'].value_counts().iloc[:10].index)
    plt.savefig("Most_occuring_crimes")
    '''Which locations do the crimes mostly occur ?'''
    plt.figure(figsize=(15, 10))
    sns.countplot(y='LocationDescription', data=dataset,
                  order=dataset['LocationDescription'].value_counts().iloc[:10].index)
    plt.savefig("Crimes_Occur_at_location")

    '''trend of all the crimes'''
    crime_data_for_trend = dataset.pivot_table('ID', aggfunc=np.size, columns='PrimaryType',
                                                   index=dataset.index.date, fill_value=0)
    crime_data_for_trend.index = pd.DatetimeIndex(crime_data_for_trend.index)
    plot_trend = crime_data_for_trend.rolling(365).sum().plot(figsize=(12, 24), subplots=True, layout=(-1, 3), sharex=False,
                                                        sharey=False)

    '''Trend of Crimes occurring over the years'''
    plt.figure(figsize=(13, 8))
    dataset.resample('M').size().plot(legend=False)
    plt.title('Trend of Crimes occurring over the years')
    plt.xlabel('Months')
    plt.ylabel('Number of crimes')
    plt.savefig("AllCrimeTrend")

    "Crimes happening month wise"
    months = ['Jan', 'Feb', 'Mar', 'April', 'May', 'June', 'July','Aug',"Sep",'Oct','Nov',"Dec"]
    dataset.groupby([dataset.index.month]).size().plot(kind='barh')
    plt.ylabel('Months of the year')
    plt.xlabel('Number of crimes')
    plt.yticks(np.arange(12), months)
    plt.title('Number of crimes by month of the year')
    plt.savefig("Crimes_monthwise_count")

    """Crimes happening day-wise"""
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    dataset.groupby([dataset.index.dayofweek]).size().plot(kind='barh')
    plt.ylabel('Days of the week')
    plt.yticks(np.arange(7), days_of_week)
    plt.xlabel('Number of crimes')
    plt.title('Number of crimes by day of the week')
    plt.savefig("Crimes_daywise_count")

    '''Crime dristribution as per district'''
    plt.figure(figsize=(13, 8))
    Crimes = dataset.loc[(dataset['XCoordinate'] != 0)]
    sns.lmplot('XCoordinate',
               'YCoordinate',
               data=Crimes[:],
               fit_reg=False,
               hue="District",
               palette='Dark2',
               size=14,
               ci=2,
               scatter_kws={"marker": "D",
                            "s": 10})
    ax = plt.gca()
    ax.set_title("All Crime Distribution per District")
    plt.savefig("district.png")

def missingValues(dataset,name):
    plt.figure(figsize=(10, 10))
    sns.color_palette("magma", as_cmap=True)
    sns.heatmap(dataset.isnull(), cbar=False, cmap="viridis")
    plt.savefig("missing.png")
    pd.isnull(dataset).any(axis=1)
    plt.savefig("missingvalues_"+name)

    '''Removing missing values'''
    dataset = dataset.dropna()
    plt.figure(figsize=(10, 7))
    sns.color_palette("magma", as_cmap=True)
    sns.heatmap(dataset.isnull(), cbar=False, cmap="viridis")
    pd.isnull(dataset).any(axis=1)
    plt.savefig("missing_data_"+ name+"_removed")

def read_files(file):
    start = time.time()
    Crimes=pd.read_csv(file, engine = 'c')
    end = time.time()
    print("Read csv with pandas: ",(end-start),"sec")
    Crimes.shape
    return Crimes

Main()
