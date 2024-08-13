import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd

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

def plot_distribution_fit(ax, data, dist_name, dist, params, p_value):
    """
    Vykreslení histogramu dat a fitnuté distribuce na dané osy.
    Anotace p-hodnoty na grafu.
    """
    # Vykreslení histogramu
    ax.hist(data, bins=30, density=True, alpha=0.6, color='g', edgecolor='k')
    
    # Vykreslení fitnuté distribuce
    x = np.linspace(min(data), max(data), 100)
    y = dist.pdf(x, *params)
    ax.plot(x, y, 'k', linewidth=2)
    
    # Anotace p-hodnoty
    ax.text(0.95, 0.95, f'p-hodnota: {p_value:.4f}', transform=ax.transAxes,
            fontsize=12, verticalalignment='top', horizontalalignment='right',
            bbox=dict(facecolor='white', alpha=0.7))
    
    ax.set_title(f'Fit distribuce {dist_name}')
    ax.set_xlabel('Hodnota')
    ax.set_ylabel('Hustota')

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
    fig = plt.figure(figsize=(18, 16))
    gs = gridspec.GridSpec(4, 3, height_ratios=[1, 0.05, 1, 1])  # 4 rows: 3 for plots, 1 empty row, 1 for the last row

    axes = [plt.subplot(gs[i]) for i in range(3)]  # Upper row
    empty_axes = [plt.subplot(gs[3])]  # Empty row
    axes += [plt.subplot(gs[i]) for i in range(4, 7)]  # Lower row

    for ax, (name, dist) in zip(axes, distributions.items()):
        fit_success, p_value, params = fit_and_test_distribution(data, name, dist)
        print(f"{name} - p-hodnota: {p_value:.4f}")
        plot_distribution_fit(ax, data, name, dist, params, p_value)
    
    # Remove the empty row
    for ax in empty_axes:
        ax.axis('off')  # Hide the empty subplot

    plt.tight_layout()
    plt.show()

# Generování vzorových dat
np.random.seed(0)
data = np.random.weibull(a=1.5, size=1000)  # Generování dat z Weibullovy distribuce pro testování


# Identifikace nejlepší distribuční shody
identify_distribution(data)
