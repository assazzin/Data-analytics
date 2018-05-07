import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
df=df.drop(['DATE'], 1)

# Plot 2 graps for correlation comparing
'''
stock1 = 'CPF'
stock2 = 'TISCO'

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ax1.plot(df[stock1], 'blue')
ax1.set_ylabel(stock1, color='blue')

ax2 = ax1.twinx()
ax2.plot(df[stock2], 'coral')
ax2.set_ylabel(stock2, color='coral')

plt.show()
exit()
'''

sns.set(style="white")

# Compute the correlation matrix
corr = df.corr()
corr.to_csv('correlation.csv')
print corr

# Generate a mask for the upper triangle
mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(220, 10, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
sns.heatmap(corr, cmap=cmap, center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5})
plt.title('Correlation table')
plt.show()
