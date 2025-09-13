from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get("/")
async def root():
    conn = sqlite3.connect('culture-popper.db')
    cur = conn.cursor()

    try:
        msg = cur.execute('SELECT reference FROM pc_references ORDER BY RANDOM() LIMIT 1').fetchone()
    
    except Exception as e:
        msg = f"An error occured during a call to the 'get' function: {e}"
    
    return msg