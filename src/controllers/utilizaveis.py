import sqlalchemy
import os 
import sys 



 


sys.path.append('..')
#dist dos arquivos 
def dist_files():
    file_dir = os.path.dirname( os.path.dirname( os.path.dirname( os.path.abspath(__file__)) ) )
    data_dir = os.path.join(file_dir, 'data')
    db_one =  os.path.join(data_dir, 'house.db')

    return db_one    

    
    
def conection_querys():
    dist_path =  dist_files()
    str_conection = f'sqlite///{dist_path}'
    conection = sqlalchemy.create_engine( str_conection )
    
    return conection