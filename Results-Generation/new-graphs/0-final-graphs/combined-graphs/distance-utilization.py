import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['ps.fonttype'] = 42   # Use TrueType fonts in EPS

# X-axis categories
x_labels = ["20", "30", "40", "50"]
x = np.arange(len(x_labels))
bar_width = 0.12

# New Utilization Data
nru = {
    'BruteForce': [0.966596428571429, 0.840465833333333, 0.710895833333334, 0.656958333333334],
    'COTO': [0.9678749925, 0.845163491857143, 0.716939606404761, 0.658219329357143],
    'QEE': [0.997853348666667, 0.976310922166667, 0.901715592869047, 0.78616717395238]
}

wifi = {
    'BruteForce': [0.932548691548691, 0.850029172029173, 0.707605105105105, 0.656013871013871],
    'COTO': [0.932819461826112, 0.849175308058059, 0.705316093364793, 0.656698118318318],
    'QEE': [0.576608912769913, 0.583881812630488, 0.597487606578006, 0.611001845524095]
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
ax.set_ylabel('Utilization', fontsize=18)
ax.set_xticks(x)
ax.set_xticklabels(x_labels)

# Formatting
ax.tick_params(axis='x', labelsize=16)
ax.tick_params(axis='y', labelsize=16)
ax.legend(fontsize=12, loc='upper left', bbox_to_anchor=(1, 1))
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
