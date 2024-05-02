import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
# print(sns.get_dataset_names())
df=sns.load_dataset('titanic')
df.head()
sns.set_style('whitegrid')
sns.displot(df['fare'],kde=True)
plt.show()
sns.displot(df['fare'],kde=False)
plt.show()
sns.displot(df['fare'],kde=False,bins=10)
plt.show()
