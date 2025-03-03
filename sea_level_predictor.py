import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('./epa-sea-level.csv')

    # Create scatter plot
    x1 = df['Year']
    y1 = df['CSIRO Adjusted Sea Level']
    plt.scatter(x1, y1)

    # Create first line of best fit
    first_line = linregress(x1, y1)
    first_intercept = first_line.intercept
    first_slope = first_line.slope
    years = np.arange(1880, 2051)
    plt.plot(years, first_slope * years + first_intercept, '-r', label = 'prediction line (1880 onwards)')
    plt.xlim(1850,2075)
    plt.legend()

    # Create second line of best fit
    df_2 = df[120:]
    x2 = df_2['Year']
    y2 = df_2['CSIRO Adjusted Sea Level']
    second_line = linregress(x2, y2)
    second_intercept = second_line.intercept
    second_slope = second_line.slope
    years = np.arange(2000, 2051)
    plt.plot(years, second_slope * years + second_intercept, '-g', label = 'prediction line (2000 onwards)')
    plt.xlim(1850,2075)
    plt.legend()

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()