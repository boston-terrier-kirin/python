import sqlite3


class DatabaseConnection:
    def __init__(self, host):
        self.host = host
        self.conn = None

    def __enter__(self) -> sqlite3.Connection:
        self.conn = sqlite3.connect(self.host)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            self.conn.close()
        else:
            self.conn.commit()
            self.conn.close()
