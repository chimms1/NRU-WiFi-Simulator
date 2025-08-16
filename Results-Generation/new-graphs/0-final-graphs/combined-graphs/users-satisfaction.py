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
    'BruteForce': [0.995057280463959, 0.881327741550399, 0.753678552855544, 0.92217712391988, 0.903048781955119],
    'COTO': [0.993082006339548, 0.882386470807796, 0.752940108384857, 0.918013593973798, 0.898382353567351],
    'QEE': [0.942420051648897, 0.234648867840036, 0.192775243492089, 0.410076398327289, 0.756437831595332]
}

wifi = {
    'BruteForce': [0.991439204623738, 0.85740599324102, 0.804285229279803, 0.944415432654881, 0.968829881023621],
    'COTO': [0.990556583553723, 0.861510333676442, 0.806570342777184, 0.946567380701902, 0.96186927124686],
    'QEE': [0.993575238633429, 0.99091560907067, 0.988996992124588, 0.989225627639758, 0.993174703396605]
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
