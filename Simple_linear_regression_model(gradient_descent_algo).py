import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import seaborn as sns
plt.rcParams['figure.figsize']=(12,8)
data=pd.read_csv('bike_sharing_data.txt')
ax = sns.scatterplot(x='Population', y='Profit', data=data)
ax.set_title('Profit in $1000 vs Population in 1000s')

