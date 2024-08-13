import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from scipy.special import gamma  # Import gamma function

def fit_and_test_distribution(data, dist_name, dist):
    """
    Fitnutí distribuce na data a provedení testu shody.
    Vrací n-tici (fit_success, p_value, params, std_dev), kde fit_success označuje, zda je fit úspěšný.
    """
    # Fitnutí distribuce
    params = dist.fit(data)
    
    # Provedení Kolmogorov-Smirnov testu shody
    D, p_value = stats.kstest(data, dist.cdf, args=params)
    
    # Výpočet standardní odchylky
    if dist_name == 'Normal':
        std_dev = params[1]  # Standardní odchylka pro normální distribuci
    elif dist_name == 'Exponential':
        std_dev = params[0]  # Parametr lambda je inverzní standardní odchylka
    elif dist_name == 'Uniform':
        std_dev = (params[1] - params[0]) / np.sqrt(12)  # Uniformní distribuce
    elif dist_name == 'Weibull':
        # Výpočet standardní odchylky pro Weibullovu distribuci
        shape, scale = params[1], params[2]  # Weibull distribution returns: location, scale, shape
        std_dev = scale * np.sqrt(gamma(1 + 2 / shape) - (gamma(1 + 1 / shape))**2)
    else:
        std_dev = np.nan  # Pokud distribuce není zpracována

    return p_value > 0.05, p_value, params, std_dev

def plot_distribution_fit(ax, data, dist_name, dist, params, p_value, std_dev, y_limits):
    """
    Vykreslení histogramu dat a fitnuté distribuce na dané osy.
    Anotace p-hodnoty na grafu.
    """
    # Vykreslení histogramu
    ax.hist(data, bins=30, density=True, alpha=0.6, color='g', edgecolor='k')
    
    # Vykreslení fitnuté distribuce
    x = np.linspace(min(data), max(data), 100)
    y = dist.pdf(x, *params)  # Vypočítání hustoty podle fitnuté distribuce
    ax.plot(x, y, 'k', linewidth=2)
    
    # Anotace p-hodnoty
    text = f'p-hodnota: {p_value:.4f}'
    if not np.isnan(std_dev):
        text += f'\nStandardní odchylka: {std_dev:.4f}'
    
    ax.text(0.95, 0.95, text, transform=ax.transAxes,
            fontsize=12, verticalalignment='top', horizontalalignment='right',
            bbox=dict(facecolor='white', alpha=0.7))
    
    ax.set_title(f'Fit distribuce {dist_name}')
    ax.set_xlabel('Hodnota')
    ax.set_ylabel('Hustota')
    ax.set_ylim(y_limits)  # Nastavení limitů y-osi pro konzistenci

def identify_distribution(data):
    distributions = {
        'Normal': stats.norm,
        'Exponential': stats.expon,
        'Uniform': stats.uniform,
        'Weibull': stats.weibull_min
    }
    
    num_distributions = len(distributions)
    
    # Definování rozložení subplotů: 2 řádky a 2 sloupce
    fig, axes = plt.subplots(2, 2, figsize=(14, 12))  # Úprava velikosti pro lepší viditelnost
    
    # Flatten the axes array for easy indexing
    axes = axes.flatten()
    
    # Určení globálních limitů y-osi
    y_limits = [0, 0]  # Inicializace limitů y-osi
    for dist_name, dist in distributions.items():
        params = dist.fit(data)
        x = np.linspace(min(data), max(data), 100)
        y = dist.pdf(x, *params)
        y_max = max(y)
        if y_max > y_limits[1]:
            y_limits[1] = y_max
    
    for ax, (name, dist) in zip(axes, distributions.items()):
        fit_success, p_value, params, std_dev = fit_and_test_distribution(data, name, dist)
        print(f"{name} - p-hodnota: {p_value:.4f}")
        plot_distribution_fit(ax, data, name, dist, params, p_value, std_dev, y_limits)
    
    plt.tight_layout()
    plt.subplots_adjust(hspace=0.4, wspace=0.4)  # Úprava mezery mezi subploty
    plt.show()

# Čtení dat z CSV souboru
csv_file = 'normal_distribution_data.csv'  # Cesta k vašemu CSV souboru
df = pd.read_csv(csv_file)

# Předpokládáme, že data jsou v prvním sloupci; upravte podle potřeby
data = df.iloc[:, 0].values

# Identifikace nejlepší distribuční shody
identify_distribution(data)
