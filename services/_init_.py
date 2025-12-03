import sqlite3

CONN = sqlite3.connect('attendance.db')
CURSOR = CONN.cursor()
