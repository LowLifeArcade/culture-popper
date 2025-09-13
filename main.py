from fastapi import FastAPI
import sqlite3
import os

app = FastAPI()
# run the following command in a Bash window: <uvicorn main:app --reload>

@app.get("/")
async def root():
    conn = sqlite3.connect('culture-popper.db')
    cur = conn.cursor()

    res= cur.execute('SELECT reference FROM pc_references ORDER BY RANDOM() LIMIT 1')

    return res.fetchone()