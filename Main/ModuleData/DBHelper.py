import sqlite3

DBName = 'GameSaveInfo.db'


def CheckSteamInfo(id):
    conn = sqlite3.connect(DBName)
    c = conn.cursor()
    t = (id,)
    c.execute('SELECT * FROM Steam WHERE ID=?', t)
    return c.fetchone()

