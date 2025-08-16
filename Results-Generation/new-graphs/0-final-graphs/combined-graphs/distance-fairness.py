import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['ps.fonttype'] = 42   # Use TrueType fonts in EPS

# X-axis categories
x_labels = ["20", "30", "40", "50"]
x = np.arange(len(x_labels))
bar_width = 0.2

# Updated Jain's fairness index data (distance-based)
nru = {
    'BruteForce': [0.998451317606859, 0.995877342907185, 0.993269550270957, 0.993177557761844],
    'COTO': [0.998139585566702, 0.995603053706718, 0.992347023931666, 0.991379001487064],
    'QEE': [0.928583138430643, 0.931309878316888, 0.945989246547784, 0.966345347785346]
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
ax.set_ylabel("Jain's fairness index", fontsize=18)
ax.set_xticks(x)
ax.set_xticklabels(x_labels)

# Formatting
ax.tick_params(axis='x', labelsize=16)
ax.tick_params(axis='y', labelsize=16)
ax.legend(fontsize=12, loc='upper left', bbox_to_anchor=(1, 1))
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
