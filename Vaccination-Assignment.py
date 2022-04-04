import numpy as np
import pandas as pd

pd.set_option('display.width', 500)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Reading Data

df = pd.read_csv("datasets/country_vaccination_stats.csv")

# Exploration Data
df.head(20)

df.info()

df.isnull().sum()

# Imputing daily_vaccinations with minimum daily vaccination number of relevant countries.

min_vals = df.groupby("country")["daily_vaccinations"].agg("count") # identify countries with no vaccination records
no_vac = min_vals[min_vals == 0].index.to_list()

df.loc[df.country.isin(no_vac), "daily_vaccinations"] = 0 # Assigning 0 to the variable daily vaccinations for countries without vaccination records

df.groupby("country")["daily_vaccinations"].transform("min")  # Getting min value by countries
df["daily_vaccinations"].fillna(df.groupby("country")["daily_vaccinations"].transform("min"), inplace=True) # fill in the missing values with the min value of the countries

df.isnull().sum()

# Top 3 countries with the highest median daily vaccination numbers

df.groupby("country")["daily_vaccinations"].agg("median").sort_values(ascending=False)[:3]

# total number of vaccinations done on 1/6/2021
df[df["date"] == "1/6/2021"]["daily_vaccinations"].sum()



