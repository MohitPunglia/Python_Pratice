import seaborn as sns
from matplotlib import pyplot as plt
import numpy as num
import pandas as pd

plt.style.use("fivethirtyeight")

data = sns.load_dataset("tips")

print(data.head())

sns.relplot(x="total_bill", y="tip", data=data)


sns.relplot(x='total_bill', y='tip',hue='smoker',data=data)

plt.show()
