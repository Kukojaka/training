import pandas as pd
import numpy as np

import matplotlib.pyplot as plt # some imports to set up plotting
import seaborn as sns # pip install seaborn

import warnings
warnings.filterwarnings('ignore')

# Graphics in retina format are more sharp and legible
%config InlineBackend.figure_format = 'retina'


# считываем 2 строчки, чтобы понять разделитель колонок 
pd.read_csv('my_file.csv', nrows=2)

# забираем таблицу из csv файла с нужным разделителем
df = pd.read_csv('my_file.csv', sep=';')
df.head()
