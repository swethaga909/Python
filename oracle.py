import cx_Oracle
import sqlalchemy
import pandas as pd
 
# Use your database credentials below
DATABASE = "orclpdb"
SCHEMA   = "hr"
PASSWORD = "hr"
 
# Generating connection string
connstr  = "oracle://{}:{}@{}".format(SCHEMA, PASSWORD, DATABASE)
conn     = sqlalchemy.create_engine(connstr)
 
# Fetching the data from the selected table using SQL query
RawData= pd.read_sql_query("select * from [HR].[Employees] where id=90", conn)
RawData.head()