import sys
import sqlalchemy
import pandas as pd
import os


#dist da tabela de dados
file_dir =  os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
data_dir =  os.path.join(file_dir, 'data')
db_one = os.path.join(data_dir, 'project-house.csv')

#segunda forma da compreensão de listas 
file_names =  [i for i in os.listdir( data_dir ) if i.endswith('.csv')]

#criando o conector de banco de dados
str_connection = 'sqlite:///{path}'
str_connection = str_connection.format(  path=os.path.join( data_dir, 'house.db' ) )
conection = sqlalchemy.create_engine( str_connection )

"""
    fazendo a iteração com o dist,
    mudando a string com para o nome table,
    e salvando o novo banco de dados,
    e isolando a connection com o sqlalchemy, 
"""
for f in file_names:
    df_tmp = pd.read_csv( os.path.join( data_dir, f ) )
    table_name = "tb_house" +  f.replace('project-', 'house').replace('house', '').strip(".csv")
    df_tmp.to_sql( table_name, conection )      
    
    

    
    
    
    
    