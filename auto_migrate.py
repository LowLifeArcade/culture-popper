import sqlite3


def auto_migrate():
    with (sqlite3.connect('culture-popper.db')) as conn:
        curr = conn.cursor()

        with open('./schema.sql', 'r') as file:
            try:
                # check if the database is current
                curr.execute(file.readline())

            except Exception as e:
                return False    # database is already up-to-date
            
            try:
                curr.executescript(file.read())

            except Exception as e:
                raise RuntimeError('schema.sql could not be executed.')
    
    return True    # database has been updated