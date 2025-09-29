import sqlite3 as sqlite

def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = sqlite.connect('holas.db')
    try:
        conn = sqlite.connect(db_file)
        return conn
    except sqlite.Error as e:
        print(e)

    return conn
def create_table(conn):
    """ create a table from the create_table_sql statement """
    try:
        sql_create_table = """ CREATE TABLE IF NOT EXISTS firefighters (
                                    id integer PRIMARY KEY,
                                    nombre text NOT NULL,
                                    rango text NOT NULL,
                                    years_of_service integer
                                ); """
        c = conn.cursor()
        c.execute(sql_create_table)
    except sqlite.Error as e:
        print(e)
def base_de_datos(conn, firefighter):
    """
    Create a new firefighter into the firefighters table
    :param conn:
    :param firefighter:
    :return: firefighter id
    """
    sql = ''' INSERT INTO firefighters(name,rank,years_of_service)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, firefighter)
    conn.commit()
    return cur.lastrowid
def main():
    database = r"firefighters.db"

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        create_table(conn)

        # insert sample data
        firefighter_1 = ('John Doe', 'Captain', 10)
        firefighter_2 = ('Jane Smith', 'Lieutenant', 5)

        base_de_datos(conn, firefighter_1)
        base_de_datos(conn, firefighter_2)

        conn.close()
    else:
        print("Error! cannot create the database connection.")
if __name__ == '__main__':
    main()