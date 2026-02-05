import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. LOAD DATA
df = pd.read_csv('bangalore_market_data.csv')

# 2. CHART 1: STRATEGIC LOCATION MATRIX
# Supply vs. Demand by Location
market_summary = df.groupby('Location').agg({
    'Restaurant_ID': 'count',
    'Votes': 'sum',
    'Cost_for_Two': 'mean'
}).reset_index()

market_summary.columns = ['Location', 'Supply', 'Demand', 'Avg_Cost']

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=market_summary, 
    x='Supply', 
    y='Demand', 
    size='Avg_Cost', 
    hue='Location',
    sizes=(100, 1000),
    alpha=0.7
)

# Quadrant Lines
plt.axvline(x=market_summary['Supply'].median(), color='grey', linestyle='--')
plt.axhline(y=market_summary['Demand'].median(), color='grey', linestyle='--')
plt.title('Strategic Matrix: Finding the "White Space"')
plt.xlabel('Competition (Number of Restaurants)')
plt.ylabel('Demand (Total Customer Votes)')
plt.text(x=market_summary['Supply'].min(), y=market_summary['Demand'].max(), 
         s="OPPORTUNITY ZONE\n(High Demand, Low Supply)", color='green', fontweight='bold')
plt.grid(True, alpha=0.3)
plt.show()

# 3. CHART 2: THE "CUISINE GAP" (HSR Layout Deep Dive)
# focus on HSR Layout to find what is missing
hsr_df = df[df['Location'] == 'HSR Layout']

# A. Supply Side (What exists?)
supply_counts = hsr_df['Cuisine'].value_counts(normalize=True) * 100

# B. Demand Side (What do people want?)
# We use "Review Keywords" to find hidden demand signals
# Count mentions of "Searching for Healthy" or specific complaints per cuisine
# For simplicity in this demo, we simulate the "Search Volume" based on our data generation logic
demand_proxies = {
    'North Indian': 30, # Saturated
    'South Indian': 20,
    'Chinese': 15,
    'Biryani': 10,
    'Healthy/Salad': 80, # High latent demand (from our "Searching for Healthy" tag)
    'Continental': 15
}
demand_series = pd.Series(demand_proxies)

# Combine into a DataFrame for plotting
gap_analysis = pd.DataFrame({
    'Current Supply (%)': supply_counts,
    'Search Interest Index': demand_series
}).fillna(0)

# Plotting the Gap
gap_analysis.plot(kind='bar', figsize=(10, 6), color=['#ff9999', '#66b3ff'])
plt.title('The "Healthy Food" Gap in HSR Layout')
plt.ylabel('Score')
plt.xlabel('Cuisine Type')
plt.xticks(rotation=45)
plt.legend(title='Metric')
plt.grid(axis='y', alpha=0.3)
plt.show()