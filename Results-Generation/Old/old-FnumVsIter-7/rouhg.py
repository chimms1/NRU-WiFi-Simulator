import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("FnumVsIters-10-10-merged.csv")


sns.set_style('darkgrid')

fig, ax = plt.subplots(1, 1, figsize=(20, 10))
# df = pd.DataFrame()
df[['15,15', '25,25','30,30']][7000:].plot(ax=ax)
# df[['loss', 'val_loss']].plot(ax=ax[1])
# df[['acc', 'val_acc']].plot(ax=ax[2])
# ax.set_title('Model MAE', fontsize=12)
ax.set_xlabel('Iteration',fontsize = 12)
ax.set_ylabel('State Number',fontsize = 12)
# ax[1].set_title('Model Loss', fontsize=12)
# ax[2].set_title('Model Acc', fontsize=12)
# fig.title('Model Metrics', fontsize=18)
plt.show()
# print(df[['10']]) 
