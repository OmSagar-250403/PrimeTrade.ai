import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load the feature-enhanced dataset
df = pd.read_csv("features_data.csv")

# Random Forest feature importances (example values)
rf_importances = np.array([0.1145, 0.1052, 0.1007, 0.1085, 0.1006, 0.1024, 0.1008, 0.1124, 0.0795, 0.0749])

# Normalize metrics and calculate composite scores
def rank_accounts(df, importances):
    scaler = StandardScaler()
    metrics = ['total_trade_volume', 'avg_realized_profit', 'active_buy_count', 'avg_fee_percentage',
               'position_side_long', 'position_side_short']
    df[metrics] = scaler.fit_transform(df[metrics])

    normalized_weights = importances / importances.sum()
    df['composite_score'] = sum(df[metric] * weight for metric, weight in zip(metrics, normalized_weights))
    df['rank'] = df['composite_score'].rank(ascending=False)

    return df[['Port_IDs', 'composite_score', 'rank']].sort_values('rank')

ranked_df = rank_accounts(df, rf_importances)
ranked_df.to_csv("ranked_accounts.csv", index=False)

print("Ranking complete. Results saved to 'ranked_accounts.csv'.")
