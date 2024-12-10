# Future NBA Player Salary Prediction

This project predicts future NBA player salaries based on various player statistics and other relevant features using a Random Forest Regressor. The model is trained and tested on NBA data and allows users to input player statistics to estimate a player's salary.

![image](https://github.com/user-attachments/assets/9a187ba5-826c-40a0-8f20-477ee117ccff)

## Project Overview
### The project involves:
Data Preprocessing: Cleaning and merging datasets of NBA player contracts and statistics.
Feature Selection: Identifying the most relevant features influencing salaries.
Model Training: Building and testing a Random Forest Regressor model to predict player salaries.
User Interaction: Allowing users to input player statistics for salary predictions.

### Repository Contents
#### Files
nba.py: Contains the main code for data preprocessing, feature selection, model training, and salary prediction. Users can input player features to estimate salaries interactively.
preprocessing and model test.ipynb: Jupyter Notebook used for exploratory data analysis and evaluating the performance of various models to decide the best approach for salary prediction.

### Data Requirements
#### The project uses two CSV files: (source: https://www.basketball-reference.com/)
nba_contract.csv: Contains contract information, including player salaries.
player_stat.csv: Includes detailed player statistics and awards.

### Usage
#### Requirements
Python 3.7 or above
Required libraries: pandas, numpy, scikit-learn, seaborn, matplotlib
Running the Script
Clone the repository.
Ensure the nba_contract.csv and player_stat.csv files are in the same directory as the script.

### Example Input
Enter the following features to predict salary:
Age: 35
GS: 70
3P: 200
eFG%: .500
TRB: 300
AST: 600
BLK: 50
PTS: 2000
Awards: 1

### Example Output

Predicted Salary: $37,344,149.89

![image](https://github.com/user-attachments/assets/6aaff60f-26af-45c7-932e-9d2857491b85)

## Model Insights
### After comparing Linear Regression vs Random Forest: 
The Random Forest model was chosen based on its:
High accuracy on validation data.
Ability to handle complex feature interactions effectively.
Further analysis and comparison of models can be found in the Jupyter Notebook.
## Future Enhancements
Add a web-based user interface for easier interaction.
Expand the dataset with historical salary data for improved predictions.
Test additional machine learning models to further improve accuracy.

# Author
Dinh Dang Khoa Tran

