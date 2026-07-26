import sqlite3
from pathlib import Path

DB_PATH = Path('data') / 'ecolens.db'


def _ensure_parent():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)


def get_connection():
    _ensure_parent()
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def set_setting(key: str, value: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO settings(key, value) VALUES (?, ?) ON CONFLICT(key) DO UPDATE SET value=excluded.value',
        (key, value),
    )
    conn.commit()
    conn.close()


def get_setting(key: str, default=None):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT value FROM settings WHERE key = ?', (key,))
    row = cur.fetchone()
    conn.close()
    return row['value'] if row else default
