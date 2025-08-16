import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("FnumVsIters-10-10-merged.csv")


sns.set_style('darkgrid')

fig, ax = plt.subplots(1, 1, figsize=(20, 10))

df[['QEE', 'Dyna-Q+']][37500:50000].plot(ax=ax)

ax.set_xlabel('Iteration',fontsize = 18)
ax.set_ylabel('State Number',fontsize = 18)

# Change the font size of x and y-axis numbers
ax.tick_params(axis='x', labelsize=18)  # Change 12 to your desired font size
ax.tick_params(axis='y', labelsize=18)  # Change 12 to your desired font size

plt.show()
