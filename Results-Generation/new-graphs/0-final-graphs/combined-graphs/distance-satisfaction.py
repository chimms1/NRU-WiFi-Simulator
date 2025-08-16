import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['ps.fonttype'] = 42   # Use TrueType fonts in EPS

# X-axis categories
x_labels = ["20", "30", "40", "50"]
x = np.arange(len(x_labels))
bar_width = 0.12

# Updated Request Satisfaction Data
nru = {
    'BruteForce': [0.7724946723381, 0.972222615890924, 1, 0.994674796747967],
    'COTO': [0.768493222575188, 0.967535290697277, 0.997272757945233, 0.994297909274795],
    'QEE': [0.170808578816598, 0.344070784003372, 0.636577204654612, 0.838091964642917]
}

wifi = {
    'BruteForce': [0.800634571674957, 0.941556958208067, 0.999880952380952, 1],
    'COTO': [0.809548569503368, 0.948630082379808, 0.999610338723002, 0.999758118441401],
    'QEE': [0.990850539459091, 0.991090338159986, 0.992516208711077, 0.995197095732771]
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
ax.set_xlabel('Distance between NR-U BS and WiFi AP', fontsize=18)
ax.set_ylabel('Request satisfaction', fontsize=18)
ax.set_xticks(x)
ax.set_xticklabels(x_labels)

# Formatting
ax.tick_params(axis='x', labelsize=16)
ax.tick_params(axis='y', labelsize=16)
ax.legend(fontsize=12, loc='upper left', bbox_to_anchor=(1, 1))
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
