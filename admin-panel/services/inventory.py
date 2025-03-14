from classes.sqlHandler import Client
from sqlalchemy import insert


class InventoryService:
    def __init__(self):
        self.sql_con = Client('mysql', 'pymysql', 'adm',
                              'cabeca0213', '192.168.0.134', '3306', 'projeto_onix')
        self.sql_con.get_table_metadata("inventario_jogador")

    def add_item(self, player_id: str, item_id: int, quantidade: int) -> bool:
        try:
            query = insert(self.sql_con.TABLES['inventario_jogador']).values(
                id_alderon=player_id,
                id_item=item_id,
                quantidade=quantidade
            )
            self.sql_con.execute_query(query)
            return True
        except Exception:
            return False
