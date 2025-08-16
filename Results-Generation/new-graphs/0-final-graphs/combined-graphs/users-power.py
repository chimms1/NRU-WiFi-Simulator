import matplotlib
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['ps.fonttype'] = 42   # Use TrueType fonts in EPS

matplotlib.rcParams['ps.fonttype'] = 42   # Use TrueType fonts in EPS

# X-axis categories
x_labels = ["15,15", "25,25", "30,30", "15,30", "30,15"]
x = np.arange(len(x_labels))
bar_width = 0.2

# Updated Power Consumed data for NR-U
nru = {
    'BruteForce': [0.617234, 0.9046375, 0.873183, 0.551152, 1.086344],
    'COTO': [0.614946576700022, 0.902504408000026, 0.876706618400025, 0.54755200730002, 1.08023303380004],
    'QEE': [0.515601661211471, 0.196819863750635, 0.195721840890678, 0.186337777928343, 0.817395064211681]
}

# Color definitions for NR-U
colors = {
    'BruteForce_NRU': '#1f77b4',  # Blue
    'COTO_NRU': '#e76f51',        # Burnt orange
    'QEE_NRU': '#6a4c93'          # Purple
}

# Create plot
fig, ax = plt.subplots(figsize=(12, 6))

# Plot NR-U bars
ax.bar(x - bar_width, nru['BruteForce'], width=bar_width,
       label='BruteForce', color=colors['BruteForce_NRU'])
ax.bar(x, nru['COTO'], width=bar_width,
       label='COTO', color=colors['COTO_NRU'])
ax.bar(x + bar_width, nru['QEE'], width=bar_width,
       label='QEE', color=colors['QEE_NRU'])

# Customize
ax.set_xlabel('Number of users (NR-U, WiFi)', fontsize=18)
ax.set_ylabel("Power consumed (mWatt)", fontsize=18)
ax.set_xticks(x)
ax.set_xticklabels(x_labels)

# Formatting
ax.tick_params(axis='x', labelsize=16)
ax.tick_params(axis='y', labelsize=16)
ax.legend(fontsize=12, loc='upper left', bbox_to_anchor=(1, 1))
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
