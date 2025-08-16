import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['ps.fonttype'] = 42   # Use TrueType fonts in EPS

# X-axis categories
x_labels = ["20", "30", "40", "50"]
x = np.arange(len(x_labels))
bar_width = 0.2

# Updated power consumed data (mWatt)
nru = {
    'BruteForce': [1.0321275, 0.6911345, 0.369664, 0.2712155],
    'COTO': [1.0234850726, 0.6864481082, 0.3686745484, 0.278260416140014],
    'QEE': [0.196894164764069, 0.196233004441991, 0.201112851832035, 0.201054512780303]
}

# Color definitions
colors = {
    'BruteForce_NRU': '#1f77b4',  # Blue
    'COTO_NRU': '#e76f51',        # Burnt orange
    'QEE_NRU': '#6a4c93'          # Purple
}

# Create plot
fig, ax = plt.subplots(figsize=(12, 6))

# Plot bars
ax.bar(x - bar_width, nru['BruteForce'], width=bar_width,
       label='BruteForce', color=colors['BruteForce_NRU'])
ax.bar(x, nru['COTO'], width=bar_width,
       label='COTO', color=colors['COTO_NRU'])
ax.bar(x + bar_width, nru['QEE'], width=bar_width,
       label='QEE', color=colors['QEE_NRU'])

# Customize
ax.set_xlabel('Distance between NR-U BS and WiFi AP', fontsize=18)
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
