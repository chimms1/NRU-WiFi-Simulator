# Library Import(numpy and matplotlib)
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plot 
 
# Make a data definition
_data=[["Increasing epsilon", 48000 , 46000, 45000, 45000],
      ["0.1", 47000,47000,46000,45000],
      ["0.3", 52000,45000,48000,48000],
      ["0.5", 65000,62000,61000,50000],
      ["0.9", 113000,200001,200001,200001]
     ]
 
# Plotting multiple groups
_df=pd.DataFrame(_data, columns=["Epsilon", "Q-learning", "Dyna-Q(k=0.1)", "Dyna-Q(k=0.2)", "Dyna-Q(k=0.05)"])
ax=_df.plot(x="Epsilon", y=["Q-learning", "Dyna-Q(k=0.1)", "Dyna-Q(k=0.2)", "Dyna-Q(k=0.05)"], kind="bar",rot=0,
 figsize=(5,5))

plot.title('EPSILON VS NUMBER OF ITERATIONS',fontsize=22)
ax.set_ylabel('No. of Iterations',fontsize=21)
ax.set_xlabel('Epsilon', fontsize=21)
ax.set_ylim([25000,200001])
ax.yaxis.set_ticks([i for i in range(25000, 200001, 20000)])

ax.tick_params(axis='x', labelsize=19)
ax.tick_params(axis='y', labelsize=17)

for label in ax.get_legend().get_texts():
    label.set_fontsize(18)

# Display the plot
plot.show()
