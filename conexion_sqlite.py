# -*- coding: utf-8 -*-
import sqlite3


class sqlite(object):
    conn = None

    def __init__(self, base):
        self.conn = sqlite3.connect(base)

    def limpia(self, SQLquery):
        c = self.conn.cursor()
        c.execute(SQLquery)
        self.conn.commit()

    def inserta(self, data):
        c = self.conn.cursor()
        c.execute(data)
        self.conn.commit()

    def query2(self, SQLCommand):
        cursor = self.conn.cursor()
        data = []
        for row in cursor.execute(SQLCommand):
            data.append(row)
        return data
    def cerrar(self):
        self.conn.close()
    def select(self):
        for row in self.conn.execute('SELECT * FROM carrera'):
            print row,8

if __name__ == '__main__':
    obj = sqlite('fam.db')
    obj2 = sqlite('tese_db.db')

    results1 = obj.query2('select * from persona')

    print results1

    obj.inserta("insert into persona values (5, 'Luis' )")

    results2 = obj.query2('select * from persona')

    print results2



    print '*' * 50

    select1 = obj2.query2("select * from carrera")

    print select1

