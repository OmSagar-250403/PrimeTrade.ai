# Account Ranking and Classification Project

## Overview

This project processes a dataset of trading accounts and uses machine learning techniques to rank and classify these accounts based on their trade history. The steps involve data preprocessing, feature extraction, model training, and ranking based on composite scores influenced by feature importances derived from a Random Forest model.

## Project Structure

- **Data Preprocessing**: Handle missing values, convert string representations of lists/dictionaries into Python objects, and shuffle the dataset.
- **Feature Extraction**: Extract meaningful trade features from the 'Trade_History' column and create new columns with these features.
- **Modeling**: Train multiple machine learning models (Random Forest, Logistic Regression, and Support Vector Classifier) to predict and classify accounts based on their features.
- **Ranking**: Use feature importances from Random Forest to compute composite scores and rank the accounts.

## Installation and Setup

1. Clone the repository or download the necessary script files.
2. Install the required Python libraries by running:

```bash
pip install pandas numpy scikit-learn matplotlib
