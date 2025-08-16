import matplotlib
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['ps.fonttype'] = 42   # Use TrueType fonts in EPS

# X-axis categories
x_labels = ["15,15", "25,25", "30,30", "15,30", "30,15"]
x = np.arange(len(x_labels))
bar_width = 0.12

# Data
nru = {
    'BruteForce': [5.009, 7.562, 7.797, 4.616, 9.255],
    'COTO': [4.999, 7.570, 7.826, 4.581, 9.209],
    'QEE': [4.554, 2.017, 2.069, 1.912, 7.431]
}

wifi = {
    'BruteForce': [18.884, 27.153, 30.627, 35.975, 18.424],
    'COTO': [18.848, 27.317, 30.666, 36.055, 18.267],
    'QEE': [18.924, 31.595, 37.773, 37.780, 18.923]
}

# Color definitions
colors = {
    'BruteForce_NRU': '#1f77b4',  # Blue (NRU - solid)
    'BruteForce_WiFi': '#6baed6',  # Light Blue (WiFi - soft blue)

    'COTO_NRU': '#e76f51',  # Burnt orange
    'COTO_WiFi': '#f4a261',  # Light orange

    'QEE_NRU': '#6a4c93',  # Purple
    'QEE_WiFi': '#b48eae'   # Light purple
}

# Create plot
fig, ax = plt.subplots(figsize=(12, 6))

# Plot NRU bars
ax.bar(x - 1.5 * bar_width, nru['BruteForce'], width=bar_width,
       label='NR-U - BruteForce', color=colors['BruteForce_NRU'])
ax.bar(x - 0.5 * bar_width, nru['COTO'], width=bar_width,
       label='NR-U - COTO', color=colors['COTO_NRU'])
ax.bar(x + 0.5 * bar_width, nru['QEE'], width=bar_width,
       label='NR-U - QEE', color=colors['QEE_NRU'])

# Plot WiFi bars
ax.bar(x + 1.5 * bar_width, wifi['BruteForce'], width=bar_width,
       label='WiFi - BruteForce', color=colors['BruteForce_WiFi'])
ax.bar(x + 2.5 * bar_width, wifi['COTO'], width=bar_width,
       label='WiFi - COTO', color=colors['COTO_WiFi'])
ax.bar(x + 3.5 * bar_width, wifi['QEE'], width=bar_width,
       label='WiFi - QEE', color=colors['QEE_WiFi'])

# Customize
ax.set_xlabel('Number of users (NR-U, WiFi)', fontsize=18)
ax.set_ylabel('Throughput (Mbps)', fontsize=18)
ax.set_xticks(x)
ax.set_xticklabels(x_labels)

# Formatting
ax.tick_params(axis='x', labelsize=18)
ax.tick_params(axis='y', labelsize=18)
ax.legend(fontsize=14, loc='upper left', bbox_to_anchor=(1, 1))
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
