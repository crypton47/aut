import sqlite3

def insert(name,email,message,publickey):
    try:
        sqliteConnection = sqlite3.connect('LightCourrier.db')
        sqlite_insert_query = """INSERT INTO `clients`
                          ('name','email', 'message', 'publickey')  VALUES  (?,?,?,?)"""
        data_tuple = (name, email,message , publickey)
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute(sqlite_insert_query, data_tuple)
        sqliteConnection.commit()
        print("Data inserted!")
        cursor.close()
    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed")
if __name__ == '__main__':
    try:
        sqliteConnection = sqlite3.connect('LightCourrier.db')
        sqlite_create_table_query = '''CREATE TABLE clients (
                                name TEXT PRIMARY KEY,
                                email TEXT NOT NULL UNIQUE,
                                message TEXT NOT NULL,
                                publickey text NOT NULL);'''
        cursor = sqliteConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute(sqlite_create_table_query)
        print("SQLite table created")
        sqliteConnection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Error while creating a sqlite table", error)
    finally:
        if (sqliteConnection):
            sqliteConnection.close()
            print("sqlite connection is closed the main")

    insert('device1','device1@gmail.com','Salut les amis','AAAAAAAAaa')
    insert('device2','device2@gmail.com', 'salut Batali','BBBBBBBBBBB')
    insert('device3','device3@gmail.com', 'salut simo, batali','CCCCCCCCCcc')
    insert('device4','device4@gmail.com', 'salut a tous !','DDDDDDDDDDDDd')



