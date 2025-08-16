import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("QFnumVsIters.csv")

sns.set_style('darkgrid')

fig, ax = plt.subplots(1, 1, figsize=(16, 6))

df[['QEE']][37500:50000].plot(ax=ax, label='QEE')

ax.set_xlabel('Iteration', fontsize=18)
ax.set_ylabel('State Number', fontsize=18)

ax.tick_params(axis='x', labelsize=19)
ax.tick_params(axis='y', labelsize=19)

# Set y-axis limits (0 to 20)
ax.set_ylim(0, 20)

# Increase legend font size
ax.legend(fontsize=17) # use a numerical font size, or 'x-large','large' etc.

# Format y-axis ticks to show integers without decimal places
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}'))

plt.show()




# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# df = pd.read_csv("FnumVsIters21-30.csv")
#
# sns.set_style('darkgrid')
#
# fig, ax = plt.subplots(1, 1, figsize=(16, 6))
# df[['30,15']][29000:35000].plot(ax=ax)
#
# # Set axis labels
# ax.set_xlabel('Iteration', fontsize=16.5)
# ax.set_ylabel('State Number', fontsize=16.5)
#
# # Change the font size of x and y-axis numbers
# ax.tick_params(axis='x', labelsize=15)  # Change to desired font size
# ax.tick_params(axis='y', labelsize=15)  # Change to desired font size
#
# # Set y-axis limits (0 to 20)
# ax.set_ylim(0, 20)
#
# # Format y-axis ticks to show integers without decimal places
# ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}'))
#
# plt.show()




