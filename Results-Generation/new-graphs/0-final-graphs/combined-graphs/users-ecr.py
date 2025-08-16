import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['ps.fonttype'] = 42   # Use TrueType fonts in EPS

# X-axis categories
x_labels = ["15,15", "25,25", "30,30", "15,30", "30,15"]
x = np.arange(len(x_labels))
bar_width = 0.2

# Updated ECR data for NR-U
nru = {
    'BruteForce': [12.37, 12.26, 11.66, 12.29, 12.09],
    'COTO': [12.37, 12.23, 11.66, 12.29, 12.08],
    'QEE': [11.59, 10.43, 10.01, 11.20, 11.23]
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
ax.set_ylabel("ECR (mWatt/Mbps)", fontsize=18)
ax.set_xticks(x)
ax.set_xticklabels(x_labels)

# Formatting
ax.tick_params(axis='x', labelsize=16)
ax.tick_params(axis='y', labelsize=16)
ax.legend(fontsize=12, loc='upper left', bbox_to_anchor=(1, 1))
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
