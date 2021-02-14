import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")
    extend_years1 = np.arange(1880, 2050, 1)
    extend_years2 = np.arange(2000, 2050, 1)

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x="Year", y="CSIRO Adjusted Sea Level", data=df)

    # Create first line of best fit
    best_fit1 = linregress(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])
    plt.plot(
        extend_years1,
        best_fit1.intercept + best_fit1.slope * extend_years1,
        "r",
        label="Fitted line using all years",
    )
    # Create second line of best fit
    best_fit2 = linregress(
        x=df[df["Year"] >= 2000]["Year"],
        y=df[df["Year"] >= 2000]["CSIRO Adjusted Sea Level"],
    )
    plt.plot(
        extend_years2,
        best_fit2.intercept + best_fit2.slope * extend_years2,
        "y",
        label="Fitted line using only the years after 2000",
    )

    # Add labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")
    ax.set_xticks(np.arange(1850.0, 2100.0, 25.0))
    plt.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig("sea_level_plot.png")
    return plt.gca()
