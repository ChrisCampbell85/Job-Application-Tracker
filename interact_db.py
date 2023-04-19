import sqlite3


DB_NAME = 'applications.db'
columns = ['company','contact_details','position','hiring_platform','misc_details','date_applied']
table = 'job_applications'

def get_database_connection():
    """
    this function should create a connection
    to the database and return the connection
    """

    con = sqlite3.connect(DB_NAME)
    # con = sqlite3.connect(':memory:')
    return con

def create_db(create=True):
    """
    Creates a table ready to accept our data.
    write code that will execute the given sql statment
    on the database
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
    write code that will use the given sql statement to populate
    the new table with the contract_list data
    """   

    to_execute = [entry_variables]

    add_data_stmt = f''' INSERT INTO {table} ({columns[0]},{columns[1]},{columns[2]},{columns[3]},{columns[4]},{columns[5]}) VALUES(?,?,?,?,?,?); '''
    con = get_database_connection()
    con.executemany(add_data_stmt, to_execute)
    con.commit()
    con.close()


def read_data_from_db(read_all=True, label=None, query=None):
    """
    Read all data from database.
    """
    if read_all:
        sql_query = f''' SELECT {columns[0]}, {columns[1]}, {columns[2]}, {columns[3]}, {columns[4]}, {columns[5]} FROM {table}; '''
    else:
        sql_query = f''' SELECT {columns[0]}, {columns[1]}, {columns[2]}, {columns[3]}, {columns[4]}, {columns[5]} FROM {table} WHERE {label} LIKE "{query}%"; '''

    con = get_database_connection()
    cur = con.cursor()

    cur.execute(sql_query)
    results = cur.fetchall()

    cur.close()
    con.close()

    return results