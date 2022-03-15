### calculate correlation coefficient
import numpy as np
import pandas as pd
from numpy.random import seed
from numpy.random import randn
from scipy.stats import pearsonr
# seed random number generator
seed(1)
# prepare data
data1 = 20 * randn(1000) + 100
data2 = data1 + (10 * randn(1000) + 50)

# calculate Pearson correlation
corr, p = pearsonr(data1, data2)

print(f'Pearson correlation: {round(corr, 3)}')


### Loading white wine (schmeckt) dataset
# https://archive.ics.uci.edu/ml/datasets/Wine+Quality

data = pd.read_csv('./winequality-white.csv', sep=';') # .convert_objects(convert_numeric=True)
print('\nData:')
print(data.head())
print(f'\nNaN Statistic : \n {data.isnull().sum()}\n')
data = data.fillna(value=0)

# Pearson correlation quality vs all other features
df_corr = pd.DataFrame(index=[col for col in data.columns], columns=[col for col in data.columns])
for row in df_corr.index:
    for col in df_corr.columns:
        if row == col:
            df_corr.loc[row, col] = 0
        else:
            corr, p = pearsonr(data[row], data[col])
            print(corr)
            df_corr.loc[row, col] = round(corr, 3)

print(f'Correlation Quality vs all Features : \n{df_corr}\n')


