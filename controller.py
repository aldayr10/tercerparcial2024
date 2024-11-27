import time
import sqlite3 as sql

def createDb():
    conn = sql.connect("autoconocimiento.db")
    print("Base de datos de autoconocimiento creada")
    conn.commit()
    conn.close();

def createTeable():
    conn=sql.connect("autoconocimiento.db")
    cursor= conn.cursor()

    cursor.execute("""
    CREATE TABLE strategic_impact (
    impact_id INTEGER PRIMARY KEY AUTOINCREMENT,
    plan_id INTEGER,
    impact_area TEXT,
    expected_outcome TEXT,
    actual_outcome TEXT,
    impact_score INTEGER CHECK (impact_score BETWEEN 1 AND 10),
    FOREIGN KEY (plan_id) REFERENCES strategic_plan(plan_id)
    );
    """)
    conn.commit()
    print("Tabla creada")
    conn.close()

if __name__=="__main__":
    createDb()
    createTeable()

