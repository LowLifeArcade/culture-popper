from contextlib import asynccontextmanager
from fastapi import FastAPI
import sqlite3

from auto_migrate import auto_migrate


@asynccontextmanager
async def lifespan(app: FastAPI):
    print('Checking for database updates...')
    
    try:
        if(auto_migrate()):
            print('Database was successfully updated.')
        else:
            print('The database is already up to date.')

    except RuntimeError as e:
        print('auto_migrate failed with the following error: ' + e)

    yield
    # Clean up the ML models and release the resources

app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root(title: str = None):
    with (sqlite3.connect('culture-popper.db')) as conn:
        curr = conn.cursor()

        if title == None:
            try:
                msg = curr.execute('SELECT quote FROM quotes ORDER BY RANDOM() LIMIT 1').fetchone()
            
            except Exception as e:
                msg = f"An error occured during a call to the 'get' function: {e}"

        else:
            # check if the movie is in the database
            print(title)

            title = title.upper()

            query = f'SELECT movieId FROM Movies WHERE Movies.movie = \'{title}\''

            print(curr.execute(query).fetchall())
            print(curr.execute('SELECT * FROM Movies').fetchall())

            if curr.execute(query).fetchall() == []:
                msg = f'Sorry, {title} is not in our database.'
            
            else:
                try:
                    query = f'SELECT quote FROM Quotes WHERE movieId = (SELECT movieId FROM Movies WHERE movie = \'{title}\')'
                    # query = f'SELECT quote FROM Quotes JOIN Movies ON Movies.movie = \'{title}\''
                    msg = curr.execute(query).fetchall()
                
                except Exception as e:
                    msg = f"An error occured during a call to the 'get' function: {e}"
        
        return msg