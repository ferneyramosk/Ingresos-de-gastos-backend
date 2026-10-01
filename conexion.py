import sqlite3

class Conexion:
    def __init__(self,sql_query,parametro=[]):
        self.con=sqlite3.connect("bd_ingresos_gastos.db")          # Conexion
        self.con.row_factory = sqlite3.Row                         # Formatear
        self.cur = self.con.cursor()                               # Cursor para consultar sql
        self.res = self.cur.execute(sql_query,parametro)           # Para pasar una lista vacia