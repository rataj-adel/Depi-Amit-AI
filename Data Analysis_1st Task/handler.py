import pandas as pd 
import numpy as np
import warnings
warnings.filterwarnings('ignore')
import pandas as pd, os 
from sqlalchemy import create_engine
def read_file(path, query="SELECT * FROM students", db_url=None):
    
    """ this function reads the data we have with various looks.  
    """
    ext = os.path.splitext(path)[-1].lower()
    if ext == ".csv": df = pd.read_csv(path)
    elif ext in [".xls", ".xlsx"]: df = pd.read_excel(path)
    elif ext == ".json": df = pd.read_json(path)
    elif ext == ".sql":
        if not db_url:
            raise ValueError("db_url")
        engine = create_engine(db_url)
        df = pd.read_sql(query, engine)
    else: raise ValueError("unsupported")
    return df.head()

print(read_file("Student_performance.csv"))
# print(read_file("Student_performance.xlsx"))
# print(read_file("Student_performance.json"))
#db_url = "postgresql://postgres:rataj@localhost:5432/mydb"
#print(read_file("Data.sql", query="SELECT * FROM students", db_url=db_url))

