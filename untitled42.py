# -*- coding: utf-8 -*-
"""Untitled42.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nDpXZYprQ-G5ZwxLInShnbEZjHXxagrw
"""

"""
GitHub Repository URL:

Corporate Analytics Project


This script generates simulated weekly sales data and analytics for the following citites Corona, Bay Area, Seal Beach, Sacramento, Compton, Long Beach, Tampa, and Miami.

Instructions:
- Ensure that the required libraries pandas and altair are installed.
- Execute the script to generate weekly sales data and analyze annual variance.
"""
"""
 class WeeklySalesSimulator: Simulates weekly sales data for the cities above and stores it in a DataFrame.

    Attributes:
    - cities (list): List of cities to simulate sales for.
    - central_df (pd.DataFrame): Central DataFrame to store weekly sales statistics.
"""
"""
      def __init__(self, cities): Initialize the simulator with a list of cities.
"""
"""
     def simulate_sales(self, weeks=52):  Simulate weekly sales data for each city over a specified number of weeks.

        Args:
        - weeks (int): Number of weeks to simulate (default is 52).
"""
"""
 class SalesAnalytics:   Performs analytics on weekly sales data using Altair for visualization.

    Attributes:
    - central_df (pd.DataFrame): Central DataFrame containing weekly sales data.
"""
"""
    def __init__(self, central_df): Initialize the analytics with a DataFrame of weekly sales data.
"""
"""
     def analyze_annual_variance(self): Analyze the variance of weekly sales data for each store on an annual basis.

        Returns:
        - annual_variance (pd.DataFrame): DataFrame with store names and their annual variance.
"""
"""
     (def plot_sales_histogram(self): Plot a histogram of annual sales variance using Altair.

        Returns:
        - chart (alt.Chart): Altair chart object displaying the histogram.
"""



import pandas as pd
import random
from datetime import datetime, timedelta
import altair as alt

class WeeklySalesSimulator:


    def __init__(self, cities):

        self.cities = cities
        self.central_df = pd.DataFrame(columns=['week', 'Global Sports', 'weekly_sales_total'])

    def simulate_sales(self, weeks=52):

        for i in range(weeks):
            start_date = datetime(2024, 1, 1) + timedelta(weeks=i)
            end_date = start_date + timedelta(days=6)

            weekly_totals_per_week = []
            for city in self.cities:
                store_name = city
                weekly_sales_total = random.randint(100000, 1000000)
                store_dict = {'week': start_date, 'Global Sports': store_name, 'weekly_sales_total': weekly_sales_total}
                weekly_totals_per_week.append(store_dict)

            self.central_df = pd.concat([self.central_df, pd.DataFrame(weekly_totals_per_week)])


class SalesAnalytics:


    def __init__(self, central_df):

        self.central_df = central_df

    def analyze_annual_variance(self):

        annual_variance = self.central_df.groupby('Global Sports')['weekly_sales_total'].var().reset_index()
        annual_variance.columns = ['Global Sports', 'variance']
        return annual_variance

    def plot_sales_histogram(self):

        annual_variance = self.analyze_annual_variance()
        color_scale = alt.Scale(scheme='redblue', domainMid=0)
        histogram = alt.Chart(annual_variance).mark_bar().encode(
            x='Global Sports:N',
            y='variance:Q',
            color=alt.Color('variance:Q', scale=color_scale, legend=None),
            tooltip=['Global Sports:N', 'variance:Q']
        ).properties(
            width=700
        )
        return histogram

# List of cities
cities = ['Corona', 'Bay Area', 'Seal Beach ', 'Sacramento', 'Compton', 'Long Beach', 'Tampa', 'Miami']

# Simulate weekly sales
simulator = WeeklySalesSimulator(cities)
simulator.simulate_sales()

# Perform analytics
analytics = SalesAnalytics(simulator.central_df)
histogram = analytics.plot_sales_histogram()

# Display the histogram
histogram