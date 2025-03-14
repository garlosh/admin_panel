from classes.sqlHandler import Client
from sqlalchemy import update


class WalletService:
    def __init__(self):
        self.sql_con = Client('mysql', 'pymysql', 'adm',
                              'cabeca0213', '192.168.0.134', '3306', 'projeto_onix')
        self.sql_con.get_table_metadata("jogadores")

    def add_recursos(self, player_id: str, cristais: int = 0, onix: int = 0) -> bool:
        try:
            if cristais:
                query = update(self.sql_con.TABLES['jogadores']).where(
                    self.sql_con.TABLES['jogadores'].c.id_alderon == player_id
                ).values(cristais=self.sql_con.TABLES['jogadores'].c.cristais + cristais)
                self.sql_con.execute_query(query)

            if onix:
                query = update(self.sql_con.TABLES['jogadores']).where(
                    self.sql_con.TABLES['jogadores'].c.id_alderon == player_id
                ).values(onix=self.sql_con.TABLES['jogadores'].c.onix + onix)
                self.sql_con.execute_query(query)
            return True
        except Exception:
            return False
