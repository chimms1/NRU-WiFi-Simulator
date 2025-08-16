import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['ps.fonttype'] = 42   # Use TrueType fonts in EPSs

df = pd.read_csv("FnumVsIters7-30.csv")

sns.set_style('darkgrid')

fig, ax = plt.subplots(1, 1, figsize=(16, 6))

df[['30,15']][8000:].plot(ax=ax, label='30,15')

ax.set_xlabel('Iteration', fontsize=18)
ax.set_ylabel('State Number', fontsize=18)

ax.tick_params(axis='x', labelsize=19)
ax.tick_params(axis='y', labelsize=19)

# Increase legend font size
ax.legend(fontsize=17) # use a numerical font size, or 'x-large','large' etc.

plt.show()
