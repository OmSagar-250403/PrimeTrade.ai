import pandas as pd
import ast

# Load the data
df = pd.read_csv("TRADES_CopyTr_90D_ROI.csv")

# Forward fill missing Trade_History based on the previous row
df['Trade_History'].fillna(method='ffill', inplace=True)

# Convert string representations of lists/dictionaries to actual Python objects
df['Trade_History'] = df['Trade_History'].apply(
    lambda x: ast.literal_eval(x) if isinstance(x, str) else x
)

# Shuffle the dataset
df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Save the shuffled data to a CSV
df_shuffled.to_csv("shuffled_data.csv", index=False)

print("Data preparation complete. Shuffled data saved to 'shuffled_data.csv'.")
