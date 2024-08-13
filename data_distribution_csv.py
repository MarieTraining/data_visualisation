import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

def fit_and_test_distribution(data, dist_name, dist):
    """
    Fitnutí distribuce na data a provedení testu shody.
    Vrací n-tici (fit_success, p_value, params), kde fit_success označuje, zda je fit úspěšný.
    """
    # Fitnutí distribuce
    params = dist.fit(data)
    
    # Provedení Kolmogorov-Smirnov testu shody
    D, p_value = stats.kstest(data, dist.cdf, args=params)
    
    return p_value > 0.05, p_value, params

def plot_distribution_fit(ax, data, dist_name, dist, params, p_value, y_limits):
    """
    Vykreslení histogramu dat a fitnuté distribuce na dané osy.
    Anotace p-hodnoty na grafu.
    """
    # Vykreslení histogramu
    ax.hist(data, bins=30, density=True, alpha=0.6, color='g', edgecolor='k')
    
    # Vykreslení fitnuté distribuce
    x = np.linspace(min(data), max(data), 100)
    if dist_name == 'Weibull':
        # Weibull distribution uses shape and scale parameters
        y = dist.pdf(x, *params)
    else:
        y = dist.pdf(x, *params)
        
    ax.plot(x, y, 'k', linewidth=2)
    
    # Anotace p-hodnoty
    ax.text(0.95, 0.95, f'p-hodnota: {p_value:.4f}', transform=ax.transAxes,
            fontsize=12, verticalalignment='top', horizontalalignment='right',
            bbox=dict(facecolor='white', alpha=0.7))
    
    ax.set_title(f'Fit distribuce {dist_name}')
    ax.set_xlabel('Hodnota')
    ax.set_ylabel('Hustota')
    ax.set_ylim(y_limits)  # Set the y-axis limits for consistency

def identify_distribution(data):
    distributions = {
        'Normal': stats.norm,
        'Exponential': stats.expon,
        'Gamma': stats.gamma,
        'Beta': stats.beta,
        'Uniform': stats.uniform,
        'Weibull': stats.weibull_min
    }
    
    num_distributions = len(distributions)
    
    # Define subplot layout: 3 rows and 2 columns
    fig, axes = plt.subplots(3, 2, figsize=(14, 18))  # Adjust size for better visibility
    
    # Flatten the axes array for easy indexing
    axes = axes.flatten()
    
    # Determine global y-axis limits
    y_limits = [0, 0]  # Initialize y_limits with min and max values
    for dist_name, dist in distributions.items():
        params = dist.fit(data)
        x = np.linspace(min(data), max(data), 100)
        if dist_name == 'Weibull':
            y = dist.pdf(x, *params)
        else:
            y = dist.pdf(x, *params)
        y_max = max(y)
        if y_max > y_limits[1]:
            y_limits[1] = y_max
    
    # Plot each distribution
    for ax, (name, dist) in zip(axes, distributions.items()):
        fit_success, p_value, params = fit_and_test_distribution(data, name, dist)
        print(f"{name} - p-hodnota: {p_value:.4f}")
        plot_distribution_fit(ax, data, name, dist, params, p_value, y_limits)
    
    # Hide any unused subplots
    for i in range(len(distributions), len(axes)):
        axes[i].axis('off')
    
    plt.tight_layout()
    plt.show()

# Read data from CSV file
csv_file = 'normal_distribution_data.csv'  # Path to your CSV file
df = pd.read_csv(csv_file)

# Assuming the data you want is in the first column; adjust as needed
data = df.iloc[:, 0].values

# Identifikace nejlepší distribuční shody
identify_distribution(data)
