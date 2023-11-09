import psycopg2
import yaml
from sqlalchemy import create_engine
import pandas as pd

class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.credentials = credentials
        self.engine = create_engine(f"postgresql://{self.credentials['RDS_USER']}:{self.credentials['RDS_PASSWORD']}@{self.credentials['RDS_HOST']}:{self.credentials['RDS_PORT']}/{self.credentials['RDS_DATABASE']}")

    def connect(self):
        self.connection = psycopg2.connect(
            host=self.credentials['RDS_HOST'],
            port=self.credentials['RDS_PORT'],
            database=self.credentials['RDS_DATABASE'],
            user=self.credentials['RDS_USER'],
            password=self.credentials['RDS_PASSWORD']
        )
    
    def extract_data_to_dataframe(self, table_name):
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql(query, con=self.engine)
        return df    
    
    def save_data_to_csv(self, df, file_path):
        df.to_csv(file_path, index=False)

# Load credentials from YAML file
with open('credentials.yaml', 'r') as f:
    credentials = yaml.safe_load(f)
    print(credentials)

rds_connector = RDSDatabaseConnector(credentials)
rds_connector.connect()
loan_df = rds_connector.extract_data_to_dataframe('loan_payments')
rds_connector.save_data_to_csv(loan_df, 'loan.csv')
print(loan_df)
print(loan_df.shape)
