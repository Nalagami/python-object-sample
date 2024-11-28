import abc
import sqlite3
from typing import Optional


# 抽象クラス
class UserRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def method(self):
        pass


# UserRepository を継承して、具象クラスを作成
class SqliteUserRepository(UserRepository):
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)

    def method(self, user_id: int) -> Optional[str]:
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM user WHERE id = ?", (1,))
        user = cursor.fetchone()
        cursor.close()
        return user[1] if user else None
