import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px


# Sample data for expenditures
# Replace with actual data as needed

data = {
    'Category': ['Education', 'Health', 'Infrastructure', 'Defense', 'Social Services'],
    'Expenditure': [50000, 30000, 25000, 15000, 20000]
}
df = pd.DataFrame(data)

def plot_expenditure_trends():
    # Line plot for spending trends over months
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
    expenditure_trends = [10000, 15000, 20000, 25000, 30000]  # Replace with actual monthly data

    plt.figure(figsize=(10, 6))
    plt.plot(months, expenditure_trends, marker='o')
    plt.title('Expenditure Trends Over Months')
    plt.xlabel('Months')
    plt.ylabel('Expenditure')
    plt.grid()
    plt.show()


def plot_expenditure_by_category():
    # Bar chart for expenditure by category
    plt.figure(figsize=(10, 6))
    plt.bar(df['Category'], df['Expenditure'], color='skyblue')
    plt.title('Expenditure by Category')
    plt.xlabel('Category')
    plt.ylabel('Expenditure')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.show()


def plot_time_series():
    # Time series plot example
    date_rng = pd.date_range(start='2026-01-01', end='2026-12-31', freq='M')
    ts_data = pd.DataFrame(date_rng, columns=['date'])
    ts_data['Expenditure'] = [x * 100 for x in range(1, 13)]  # Mock data

    plt.figure(figsize=(10, 6))
    plt.plot(ts_data['date'], ts_data['Expenditure'], marker='o')
    plt.title('Expenditure Time Series')
    plt.xlabel('Date')
    plt.ylabel('Expenditure')
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()


def forecast_expenditure():
    # Forecasting example using plotly
    forecast_data = {
        'Month': ['2026-01', '2026-02', '2026-03', '2026-04', '2026-05'],
        'Forecast': [12000, 15000, 18000, 21000, 24000]
    }
    forecast_df = pd.DataFrame(forecast_data)

    fig = px.line(forecast_df, x='Month', y='Forecast', title='Expenditure Forecast')
    fig.show()

# Example usage
# plot_expenditure_trends()
# plot_expenditure_by_category()
# plot_time_series()
# forecast_expenditure()