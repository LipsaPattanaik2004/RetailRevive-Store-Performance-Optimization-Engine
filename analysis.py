import pandas as pd

def analyze_data(df):
    df['profit'] = df['revenue'] - df['cost']
    df['profit_margin'] = (df['profit'] / df['revenue']) * 100

    underperforming = df[df['profit'] < 0]

    insights = []

    for _, row in df.iterrows():
        if row['profit'] < 0:
            insights.append(f"Store {row['store_id']} in {row['city']} is loss-making.")
        elif row['profit_margin'] < 10:
            insights.append(f"Store {row['store_id']} has low margin.")

    return df, underperforming, insights
