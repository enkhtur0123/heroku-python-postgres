import psycopg2
try:
    conn = psycopg2.connect(user="zbesclbnhnygje", password="70a93a1c2ee52958831f418c458768f6ea234caf5473909133798f5f2d0e40b5", database="d9c261lskckdkd", host="ec2-54-216-48-43.eu-west-1.compute.amazonaws.com", port="5432", sslmode='require')
    print("Successfully connected!")
    cur = conn.cursor()
    cur.execute('select * from "XPObjectType"')
    print("The number of parts: ", cur.rowcount)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()