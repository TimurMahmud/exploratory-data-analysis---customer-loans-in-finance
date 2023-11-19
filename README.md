# Customer Loans in Finance - Exploratory Data Analysis

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Key Findings](#key-findings)
- [File Structure](#file-structure)

## Description
This project undertakes an in-depth Exploratory Data Analysis (EDA) of customer loan data within the finance sector. The primary goal is to uncover insights, identify patterns, and prepare the dataset for advanced analytics. Our EDA focuses on understanding various aspects of the loan data, including loan recovery, customer payment behaviour, and risk assessment.

Key analyses include:
- Calculation of current recovery percentages and projections.
- Analysis of charged off loans and their impact on total revenue.
- Exploration of potential indicators for customers likely to default or fall behind on payments.

The insights gained from this analysis are instrumental in identifying factors that influence loan performance, customer reliability, and potential financial risks.

## Installation
To set up the environment and run the code for this project, follow these steps:

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/finance-loans-eda.git

2. Install required Python packages:
   ```bash
   pip install -r requirements.txt

## Usage      

After installing the required packages, run the Jupyter notebooks in the repository to explore the analyses and findings.

## Key Findings

- Loan Recovery and Projections: Detailed analysis of current loan recovery rates and future projections.

- Risk Assessment: Identification of key factors contributing to loan default risks, including loan grade, purpose, and Debt to Income Ratio (DTI).

- Comparative Analysis: Insights into different borrower behaviors between those who have defaulted and those currently behind on payments.

## File Structure

- `db_utils.py` - Python script with utility functions for database operations.
- `eda.ipynb` - Jupyter notebook containing the exploratory data analysis.
- `eda.py` - Python script version of the exploratory data analysis.
- `loan_data_dict.md` - Markdown file containing the data dictionary for the loan dataset.
- `loan.csv` - The original loan dataset in CSV format.
- `README.md` - Markdown file with the project description and instructions.
- `transformed_df.csv` - CSV file containing the transformed dataset after processing.
- `visualisations.ipynb` - Jupyter notebook dedicated to data visualisations.

