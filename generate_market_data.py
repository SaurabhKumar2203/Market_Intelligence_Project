import pandas as pd
import numpy as np
import random

# CONFIGURATION
NUM_RESTAURANTS = 2000
LOCATIONS = ['Koramangala', 'Indiranagar', 'HSR Layout', 'Whitefield', 'Electronic City', 'Jayanagar']
CUISINES = ['North Indian', 'South Indian', 'Chinese', 'Continental', 'Healthy/Salad', 'Biryani']

def generate_market_data():
    data = []
    
    for i in range(NUM_RESTAURANTS):
        rest_id = f"REST-{1000+i}"
        
        # 1. Location Logic (Skewed distribution)
        # Koramangala is overcrowded (30% of data)
        location = np.random.choice(LOCATIONS, p=[0.3, 0.2, 0.15, 0.15, 0.1, 0.1])
        
        # 2. Cuisine Logic
        # HSR Layout has fewer 'Healthy' options (Simulating the Gap)
        if location == 'HSR Layout':
            cuisine = np.random.choice(CUISINES, p=[0.3, 0.2, 0.2, 0.1, 0.05, 0.15]) # Only 5% Healthy
        else:
            cuisine = np.random.choice(CUISINES)
            
        # 3. Business Metrics
        # Cost for Two (Correlated with location)
        base_cost = 400
        if location in ['Indiranagar', 'Koramangala']: base_cost = 800
        cost_for_two = int(np.random.normal(base_cost, 200))
        cost_for_two = max(200, cost_for_two)
        
        # Rating (1.0 to 5.0)
        rating = round(np.random.normal(3.8, 0.5), 1)
        rating = min(4.9, max(2.1, rating))
        
        # Demand (Votes) - Proxy for Footfall
        # Higher ratings usually get more votes
        base_votes = 100
        if rating > 4.0: base_votes = 1000
        votes = int(np.random.exponential(base_votes))
        
        # 4. Sentiment / Review Keywords (Simulated NLP)
        # We simulate "Pain Points"
        keywords = []
        if votes > 500: keywords.append("Crowded")
        if rating < 3.5: keywords.append("Bad Service")
        if location == 'HSR Layout' and cuisine == 'North Indian': keywords.append("Oily")
        if location == 'Whitefield': keywords.append("Slow Delivery")
        
        # The "Opportunity" Signal
        if location == 'HSR Layout' and np.random.random() > 0.8:
            keywords.append("Searching for Healthy") # Latent Demand
            
        review_summary = ", ".join(keywords) if keywords else "Average Experience"
        
        data.append({
            'Restaurant_ID': rest_id,
            'Location': location,
            'Cuisine': cuisine,
            'Cost_for_Two': cost_for_two,
            'Rating': rating,
            'Votes': votes,
            'Review_Keywords': review_summary
        })
        
    return pd.DataFrame(data)

# GENERATE & SAVE
df = generate_market_data()
print(f"Generated Market Data for {NUM_RESTAURANTS} Restaurants.")
print(df.head())
df.to_csv('bangalore_market_data.csv', index=False)