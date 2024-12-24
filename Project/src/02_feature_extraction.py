import numpy as np
import pandas as pd

# Load shuffled data
df = pd.read_csv("shuffled_data.csv")

# Feature extraction function
def extract_trade_features(trade_history):
    if isinstance(trade_history, list) and trade_history:
        prices = [trade['price'] for trade in trade_history if 'price' in trade]
        quantities = [trade['quantity'] for trade in trade_history if 'quantity' in trade]
        fees = [trade['fee'] for trade in trade_history if 'fee' in trade]
        realized_profits = [trade['realizedProfit'] for trade in trade_history if 'realizedProfit' in trade]
        active_buy = [trade['activeBuy'] for trade in trade_history if 'activeBuy' in trade]
        position_side = [trade['positionSide'] for trade in trade_history if 'positionSide' in trade]

        return {
            'mean_price': np.mean(prices) if prices else 0,
            'mean_quantity': np.mean(quantities) if quantities else 0,
            'total_trade_volume': np.sum(quantities),
            'total_fee_paid': np.sum(fees),
            'avg_fee_percentage': np.sum(fees) / np.sum(quantities) if quantities else 0,
            'avg_realized_profit': np.mean(realized_profits) if realized_profits else 0,
            'num_trades': len(trade_history),
            'active_buy_count': sum(active_buy),
            'position_side_long': sum(1 for pos in position_side if pos == 'LONG'),
            'position_side_short': sum(1 for pos in position_side if pos == 'SHORT')
        }
    return {key: 0 for key in ['mean_price', 'mean_quantity', 'total_trade_volume', 'total_fee_paid',
                               'avg_fee_percentage', 'avg_realized_profit', 'num_trades', 'active_buy_count',
                               'position_side_long', 'position_side_short']}

# Apply feature extraction
df['features'] = df['Trade_History'].apply(extract_trade_features)

# Expand extracted features into separate columns
df_features = pd.DataFrame(df['features'].tolist())
df = pd.concat([df, df_features], axis=1)

# Save the feature-enhanced dataset
df.to_csv("features_data.csv", index=False)

print("Feature extraction complete. Data saved to 'features_data.csv'.")
