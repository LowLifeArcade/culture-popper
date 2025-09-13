from fastapi import FastAPI
import sqlite3
import os

app = FastAPI()

@app.get("/")
async def root():
    print("get function called.")
    conn = sqlite3.connect('culture-popper.db')
    cur = conn.cursor()

    try:
        msg = cur.execute('SELECT reference FROM pc_references ORDER BY RANDOM() LIMIT 1').fetchone()
    
    except Exception as e:
        msg = f"An error occured during a call to the 'get' function: {e}"
    
    return msg