import sqlite3
import os
import Config


def CheckSteamInfo(id):
    conn = sqlite3.connect(Config.DBPath)
    c = conn.cursor()
    t = (id,)
    c.execute('SELECT * FROM Steam WHERE ID=?', t)
    return c.fetchone()

