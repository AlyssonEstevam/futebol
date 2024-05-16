import pyodbc

conexao = pyodbc.connect('DRIVER={ODBC Driver 18 for SQL Server};'+
                         'SERVER=localhost;'+
                         'DATABASE=FUTDB;'+
                         'UID=usrMasterFut;'+
                         'PWD=My98MasterPa$$;'+
                         'Encrypt=Optional')

def executa_query(comando):
    cursor = conexao.cursor()
    cursor.execute(comando)
    conexao.commit()

def consulta_query(comando):
    cursor = conexao.cursor()
    cursor.execute(comando)

    return cursor.fetchall()
