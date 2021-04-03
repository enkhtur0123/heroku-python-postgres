import psycopg2
import os
rows = 0
def rowcount():
    try:
        DATABASE_URL = os.environ['DATABASE_URL']

        conn = psycopg2.connect(DATABASE_URL, sslmode='require')
        print("Successfully connected!")
        cur = conn.cursor()
        cur.execute('select * from "XPObjectType"')
        print("The number of parts: ", cur.rowcount)
        rows = cur.fetchall()

        #for row in rows:
        print(rows)

        cur.close()
        

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return cur.rowcount
