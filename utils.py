import os
import pandas as pd
from sqlalchemy import create_engine

DB_PATH = "./db/test.db"

def setup_db():
    df = pd.read_csv("./data/all-states-history.csv").fillna(value = 0)
    database_file_path = DB_PATH
    os.makedirs(os.path.dirname(database_file_path), exist_ok=True)
    db_uri = f'sqlite:///{database_file_path}'
    engine = create_engine(db_uri)

    df.to_sql(
    'all_states_history',
    con=engine,
    if_exists='replace',
    index=False
    )
    print("DATABASE INITIALIZATION SUCCESSFULL")
    return db_uri