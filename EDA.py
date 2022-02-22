import pandas as pd


# Read data
data = pd.read_csv('Global Terrorism - START data//globalterrorismdb_0718dist.csv')
print(data.head())

# Take important features from the dataset
new_data=data[['iyear','imonth','iday','country_txt','provstate',
                       'region_txt','attacktype1_txt','target1','nkill',
                       'nwound','summary','gname','targtype1_txt',
                       'weaptype1_txt','motive']]

# check for missing values
print("Percentage of null values\n",new_data.isnull().sum())
print("Shape of the data = ", new_data.shape)
new_data.to_csv('cleaned_data.csv')

# check for duplicates
print("Sum of duplicates = ",data.duplicated().sum())

# Statistical analysis view
print(new_data.corr())
print(data.describe())
