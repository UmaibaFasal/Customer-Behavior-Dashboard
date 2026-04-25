from Main import get_cleaned_data
from sqlalchemy import create_engine
from urllib.parse import quote_plus
#Fetch Data
df=get_cleaned_data()
#Connect to mySQL
username = "root"
password = quote_plus("hAmd@2021")
host = "localhost"
port = "3306"  # MySQL default port
database = "customer_behavior"
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")
#Load DataFrame into MySQL
table_name = "customers"
df.to_sql("customers", engine, if_exists="replace", index=False)
print(f"Data successfully loaded into table '{table_name}' in database '{database}'.")