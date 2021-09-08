import sqlite3


DB_NAME = 'applications.db'

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
        create_table = """ CREATE TABLE IF NOT EXISTS job_applications (
            ID          INTEGER PRIMARY KEY     AUTOINCREMENT,
            company             TEXT                NOT NULL,
            contact_details     TEXT                NOT NULL,
            position            TEXT                NOT NULL,
            hiring_platform     TEXT                NOT NULL,
            misc_details        TEXT                NULL,
            date_applied        CHAR(15)            NULL

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

    add_data_stmt = ''' INSERT INTO job_applications (company,contact_details,position,hiring_platform,misc_details,date_applied) VALUES(?,?,?,?,?); '''
    con = get_database_connection()
    con.executemany(add_data_stmt, to_execute)
    con.commit()
    con.close()


def read_data_from_db():
    """
    Read data from database.
    execute the given sql statement and return the results
    """
    sql_query = ''' SELECT company, contact_details, position, hiring_platform, date_applied FROM job_applications; '''
    
    con = get_database_connection()
    cur = con.cursor()

    cur.execute(sql_query)
    results = cur.fetchall()

    cur.close()
    con.close()

    return results