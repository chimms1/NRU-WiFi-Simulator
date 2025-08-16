import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.rcParams['ps.fonttype'] = 42   # Use TrueType fonts in EPS

# X-axis categories
x_labels = ["15,15", "25,25", "30,30", "15,30", "30,15"]
x = np.arange(len(x_labels))
bar_width = 0.12

# Updated Utilization Data
nru = {
    'BruteForce': [0.631499642857143, 0.931388452380952, 0.96810130952381, 0.870252380952381, 0.89155880952381],
    'COTO': [0.633484953, 0.93075544719048, 0.97306105690476, 0.873017238880954, 0.891276056119047],
    'QEE': [0.646165191, 0.991995391964285, 0.997125139535714, 0.977860161559522, 0.906290887607134]
}

wifi = {
    'BruteForce': [0.63006006006006, 0.899466323466323, 0.943260403260402, 0.870069962819963, 0.829558558558558],
    'COTO': [0.626870841984837, 0.902277115379659, 0.944435377112821, 0.868567569705412, 0.82494771923352],
    'QEE': [0.592886613863867, 0.579013344801953, 0.687463246081796, 0.688999435213786, 0.699467883308307]
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
