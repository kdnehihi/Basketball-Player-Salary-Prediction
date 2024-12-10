import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor


# Load Data
contract_df = pd.read_csv('Data/nba_contract.csv', index_col='Rk')
stat_df = pd.read_csv('Data/player_stat.csv', index_col='Rk')

# Data Cleaning
contract_df = contract_df.drop(columns=['2025-26', '2026-27', '2027-28', '2028-29', '2029-30', 'Guaranteed'])
contract_df = contract_df.rename(columns={'2024-25': '2024-25_Salary($)'})
contract_df['2024-25_Salary($)'] = contract_df['2024-25_Salary($)'].str.replace('$', '', regex=False).astype(float)

stat_df['Awards'] = stat_df['Awards'].fillna(0)
awards_list = stat_df['Awards'].to_list()
for i in range(len(awards_list)):
    if "NBA" in str(awards_list[i]):
        awards_list[i] = int(awards_list[i][-1])
    else:
        awards_list[i] = 0
stat_df['Awards'] = awards_list
stat_df['FT%'] = stat_df['FT%'].fillna(0)
stat_df = stat_df.fillna(0)
stat_df = stat_df.drop_duplicates(subset='Player', keep='first')

# Merge Data
df = pd.merge(contract_df, stat_df, on='Player-additional', how='inner')
df = df.drop(['Team', 'Player_y'], axis=1)



# Feature Selection
X = df.drop(columns=['2024-25_Salary($)', 'Player_x', 'Player-additional', 'ORB', 'DRB', 'G', 'MP', 
                     'FGA', 'FG%', '3P%', '3PA', '2PA', '2P%', 'FT', 'FT%', '2P', 'FG', 'FTA', 
                     'TOV', 'STL', 'PF', 'Trp-Dbl','Tm', 'Pos'])
Y = df['2024-25_Salary($)']

# Train-Test Split
X_train, X_val, Y_train, Y_val = train_test_split(X, Y, test_size=0.2, random_state=42, shuffle=True)

# Model Training
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, Y_train)

# Function to Predict Salary
def predict_salary(user_input):
    """
    Predicts the NBA player's salary based on the input features.
        user_input (dict): A dictionary containing feature names and their respective values.
        float: Predicted salary.
    """
    try:
        input_array = np.array([user_input[feature] for feature in X_train.columns]).reshape(1, -1)
        predicted_salary = rf_model.predict(input_array)[0]
        return f"Predicted Salary: ${predicted_salary:,.2f}"
    except KeyError as e:
        return f"Missing feature in input: {e}"

# Example usage
if __name__ == "__main__":
    print("Enter the following features to predict salary:")
    user_input = {}
    for feature in X_train.columns:
        value = input(f"{feature}: ")
        user_input[feature] = float(value) if feature not in ['Awards'] else int(value)
    
    print(predict_salary(user_input))
