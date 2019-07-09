import numpy as np
import pandas as pd
'''
Go to https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
for a better version of this. Everything in here is me playing around with
this reasource.
'''

# series data
# -----------------------------------------------------------------
series_a = pd.Series([1,2,3,4,5])
series_b = pd.Series([5,7,9,11])
print(series_a + series_b)  # can preform operation on series objects

# Dataframes
# -----------------------------------------------------------------
dates = pd.date_range(start='19971231', end='20191231', periods=10)
# creates a list of 10 dates between start and end
print(dates)

letters = 'ABCD'
data_frame = pd.DataFrame(np.random.rand(10, 4), index = dates, columns = list(letters))
# generates three random numbers for each date (row)
# the index and columns are used to label the data created by np.random.rand
print('Random timeseries dataframe')
print(data_frame)

# Dataframe using dictionary of objects
data_frame2 = pd.DataFrame({'Dog': 'Cat',
                            'Eagle': ['Bird', 'Eggs', 'Nest'],
                            'Cow': ('Beef', 'Farm', 100)
                            })

print('Dataframe from dictionary')
print(data_frame2)
# indexes are automatically set from 0 -> number rows
print(data_frame2.dtypes)  # datatypes are all objects, works as length are compatable
                           # Dog -> Cat has one cat and so cat is replicated

# Visualization and Converting
# ----------------------------------------------------------------

# Heads or Tails?

print('Showing from head')
print(data_frame2.head(3))
print('Showing from tail')
print(data_frame2.tail(3))

print('Get a description of the data (using DF1 here)')
print(data_frame.describe())

# converting to other representations
print(data_frame2.to_latex())  # print as latex code
print(data_frame2.to_json())  # print as json

# Data Selection
# -----------------------------------------------------------------
# using the time series data frame

print(data_frame['B'])  # slice by column name
print(data_frame.loc[:, ['A', 'B']])  # by label (loc) and multi-axis

# Gerneral Operations and Appling Functions
# ------------------------------------------------------------------

# pandas includes basic descriptive operations like mean and can specify the
# dimension in the arguements of these methods

print(data_frame.apply(np.cumsum))
print(data_frame.apply(lambda x: x.min() * x.max()))
