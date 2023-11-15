import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame
df = pd.read_csv('loan.csv')

# Class for transforming data
class DataTransform:
    def __init__(self, df):
        self.df = df

    def convert_to_date(self, column):
        # Convert the specified column to datetime format
        self.df[column] = pd.to_datetime(self.df[column])

    def convert_to_float(self, column):
        # Extract digits and convert the specified column to float
        self.df[column] = self.df[column].str.extract('(\d+)').astype(float)

    def change_column_name(self, column, new_name):
        # Rename the specified column
        self.df = self.df.rename(columns={f'{column}': f'{new_name}'})

# Uncomment to display the head of the DataFrame
# print(df.head(3))

# Instantiate DataTransform class
# transformer = DataTransform(df)

# Uncomment to apply various transformations
# transformer.convert_to_date('last_payment_date')
# transformer.convert_to_date('next_payment_date')
# transformer.convert_to_date('last_credit_pull_date')
# transformer.convert_to_date('issue_date')
# transformer.convert_to_date('earliest_credit_line')
# transformer.convert_to_date('last_credit_pull_date')
# transformer.convert_to_float('term')

# Uncomment to display specific columns after transformations
# print(df['term'])
# print(df['last_credit_pull_date'])

# Class for obtaining information about the DataFrame
class DataFrameInfo:
    def __init__(self, df):
        self.df = df

    def describe_columns(self):
        # Display data types of columns
        return self.df.dtypes

    def extract_statistical_values(self):
        # Display basic statistical values
        return self.df.describe()

    def count_distinct_values(self, column):
        # Count distinct values in the specified column
        return self.df[column].nunique()

    def print_shape(self):
        # Display the number of rows and columns
        print(f"Number of rows: {self.df.shape[0]}")
        print(f"Number of columns: {self.df.shape[1]}")

    def count_null_values(self):
        # Count null values and calculate null percentage
        null_values = self.df.isnull().sum()
        total_rows = self.df.shape[0]
        null_percentage = (null_values / total_rows) * 100
        null_info = pd.DataFrame({
            'Null Count': null_values,
            'Null Percentage': null_percentage
        })
        return null_info

# Class for creating plots
class Plotter:
    @staticmethod
    def plot_null_distribution(df):
        # Plot null value distribution using a heatmap
        plt.figure(figsize=(10, 6))
        sns.heatmap(df.isnull(), cmap='viridis', cbar=False, yticklabels=False)
        plt.title('NULL Values Distribution')
        plt.show()

    @staticmethod
    def plot_skewness(df, columns):
        # Plot skewness analysis for specified columns
        plt.figure(figsize=(12, 6))
        for column in columns:
            sns.histplot(df[column], kde=True, label=column)
        plt.title('Skewness Analysis')
        plt.legend()
        plt.show()

# Class for transforming the DataFrame
class DataFrameTransform:
    def __init__(self, df):
        self.df = df

    def check_null_values(self):
        # Check and display null values
        return self.df.isnull().sum()

    def drop_columns(self, columns_to_drop):
        # Drop specified columns
        self.df = self.df.drop(columns=columns_to_drop, axis=1)

    def impute_null_values(self, column, method='median'):
        # Impute null values in the specified column using median or mean
        if method == 'median':
            self.df[column].fillna(self.df[column].median(), inplace=True)
        elif method == 'mean':
            self.df[column].fillna(self.df[column].mean(), inplace=True)

    def identify_skewed_columns(self, threshold=0.5):
        # Identify columns with skewness above a threshold
        numeric_columns = self.df.select_dtypes(include=[np.number]).columns
        skewness = self.df[numeric_columns].apply(lambda x: x.skew())
        skewed_columns = skewness[abs(skewness) > threshold].index.tolist()
        return skewed_columns

    def log_transformation(self, column):
        # Perform log transformation on the specified column
        log_transformed = np.log1p(self.df[column])
        log_skewness = log_transformed.skew()
        return log_transformed

    def transform_skewed_columns(self, threshold=0.5):
        # Transform skewed columns using log transformation
        skewed_columns = self.identify_skewed_columns(threshold)

        for column in skewed_columns:
            transformed_column = self.log_transformation(column)
            if transformed_column is not None:
                self.df[column] = transformed_column

# Instantiate DataFrameTransform class
df_transformer = DataFrameTransform(df)
# Instantiate Plotter class
plotter = Plotter()

# Uncomment to display null values before handling
# print("Before NULL Value Handling:")
# print(df_transformer.check_null_values())

# Columns to drop
columns_drop = ['mths_since_last_major_derog', 'next_payment_date', 'mths_since_last_record', 'mths_since_last_delinq']
# Drop specified columns
df_transformer.drop_columns(columns_drop)

# Columns to impute null values
impute_columns = ['funded_amount', 'int_rate', 'collections_12_mths_ex_med']
for column in impute_columns:
    # Impute null values using median
    df_transformer.impute_null_values(column, method='median')

# Uncomment to display null values after handling
# print("\nAfter NULL Value Handling:")
# print(df_transformer.check_null_values())
# Plot null distribution
# plotter.plot_null_distribution(df)

# Uncomment to display specific columns after transformations
# print(df_transformer.df['funded_amount'].head(3))

# Uncomment to plot skewness analysis before and after transformations
# plotter.plot_skewness(df, df.columns)
df_transformer.transform_skewed_columns()
# plotter.plot_skewness(df_transformer.df, df_transformer.df.columns)

# Create a copy of the transformed DataFrame
transformed_df = df_transformer.df.copy()

# Display information about the transformed DataFrame
print(transformed_df.info())
