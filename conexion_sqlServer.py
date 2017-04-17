# -*- coding: utf-8 -*-
import pypyodbc
class sql(object):
    connection = None
    def __init__ (self, base, user, password):
        cadena_conn = 'Driver={SQL Server};Server=DESKTOP-EAUDH3P\ENRIQUE;Database=%s;uid=%s;pwd=%s' % (base, user, password)
        self.connection = pypyodbc.connect(cadena_conn)
        
    def conexion(self):
        connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-EAUDH3P\ENRIQUE;'
                              'Database=tese;'
                              'uid=sa;pwd=sasa')
        return connection
    def query(self, connection, SQLCommand):
        cursor = connection.cursor()
        cursor.execute(SQLCommand)
        results = cursor.fetchone()
        return results

    def query2(self, SQLCommand):
        cursor = self.connection.cursor()
        cursor.execute(SQLCommand)
        results = cursor.fetchone()
        return results

'''
while results:
    print results[0],results[1],results[2]
    results = cursor.fetchone()
connection.close()
'''
if __name__ == '__main__':
    objeto = sql('tese', 'sa', 'sasa')
    resultado = objeto.query2('select * from alumno')
    print resultado
