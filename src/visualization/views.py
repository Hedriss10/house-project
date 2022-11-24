import sys 
import os 
import pandas as pd 
import sqlalchemy


sys.path.append('..')
from controllers.utilizaveis import conection_querys


def views_querys():
    df = pd.read_sql_query( os.path.join( conection_querys() ) )
    print(df.head(10))
    
    
views_querys()