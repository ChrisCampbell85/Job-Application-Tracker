import sqlite3


DB_NAME = 'applications.db'
columns = ('company','contact_details','position','hiring_platform','misc_details','date_applied')
table = 'job_applications'

def get_database_connection():
    """
    this function creates a connection
    to the database and returns the connection
    """
    con = sqlite3.connect(DB_NAME)
    # con = sqlite3.connect(':memory:')
    return con

def create_db(create=True):
    """
    Creates a table ready to accept our data.
    """
    if create:
        create_table = f""" CREATE TABLE IF NOT EXISTS {table} (
            ID              INTEGER PRIMARY KEY AUTOINCREMENT,
            {columns[0]}    TEXT                NOT NULL,
            {columns[1]}    TEXT                NOT NULL,
            {columns[2]}    TEXT                NOT NULL,
            {columns[3]}    TEXT                NOT NULL,
            {columns[4]}    TEXT                NULL,
            {columns[5]}    CHAR(15)            NULL

        )   
        """
        con = get_database_connection()
        con.execute(create_table)
        con.close()

def populate_db(entry_variables):
    """
    Populate the table database.
    """   
    to_execute = [entry_variables]
    add_data_stmt = f''' INSERT INTO {table} ({columns[0]},{columns[1]},{columns[2]},{columns[3]},{columns[4]},{columns[5]}) VALUES(?,?,?,?,?,?); '''
    con = get_database_connection()
    con.executemany(add_data_stmt, to_execute)
    con.commit()
    con.close()


def read_data_from_db(read_all=True, param=None, query=None):
    """
    Read data from database.
    """
    statement = f'SELECT {columns[0]}, {columns[1]}, {columns[2]}, {columns[3]}, {columns[4]}, {columns[5]} FROM {table}'
    if read_all:
        sql_query = f''' {statement}; '''
    else:
        sql_query = f''' {statement} WHERE {param} LIKE "{query}%"; '''
        print(sql_query)

    con = get_database_connection()
    cur = con.cursor()

    cur.execute(sql_query)
    results = cur.fetchall()

    cur.close()
    con.close()
    print(results)
    return results

def sort_db_table(table, db_columns):
        """Matches each entry label with entry data. Returns list containing dict of database records"""
        sorted_database_list = []
        for item in table:
            entry = dict((zip(db_columns, item)))
            sorted_database_list.append(entry)
        
        return sorted_database_list

def delete_from_db(position):

    try:
        con = get_database_connection()
        statement = f'''DELETE FROM {table} WHERE position = ?;'''
        cur = con.cursor()
        cur.execute(statement, (position,))
        con.commit()
        print('Record deleted')
        cur.close()

    except sqlite3.Error as error:
        print('Failed to delete record', error)
    finally:
        if con:
            con.close()
            print('Connection closed')