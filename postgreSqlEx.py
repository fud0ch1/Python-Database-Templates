import psycopg2


def create_table():
    # Establish connection and database
    conn = psycopg2.connect("dbname='[Database Name]' user='[username]' password='[password]' host='[hostname ex. localhost]' port='[Port Number, ex 5432]'")
    cur = conn.cursor()
    # Create a table named '[table name]', and add '3' columns ([variable1] [TYPE1], [variable2] [TYPE2], [variable3] [TYPE3])
    cur.execute("CREATE TABLE IF NOT EXISTS [table name] ([variable1] [Type, ex. TEXT], [variable2] [Type ex. INTEGER], [variable3] [Type, ex. REAL])")
    conn.commit()
    conn.close()


def insert(variable1, variable2, variable3):
    conn = psycopg2.connect("dbname='[Database Name]' user='[username]' password='[password]' host='[hostname ex. localhost]' port='[Port Number, ex 5432]'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (variable1, variable2, variable3))
    conn.commit()
    conn.close()


def delete(variable1):
    conn = psycopg2.connect("dbname='[Database Name]' user='[username]' password='[password]' host='[hostname ex. localhost]' port='[Port Number, ex 5432]'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = %s", (variable1,))
    conn.commit()
    conn.close()


def update(variable1, variable2="", variable3=""):
    conn = psycopg2.connect("dbname='[Database Name]' user='[username]' password='[password]' host='[hostname ex. localhost]' port='[Port Number, ex 5432]'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET variable2 = %s, variable3 = %s WHERE variable1 = %s",(variable2, variable3, variable1))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect("dbname='[Database Name]' user='[username]' password='[password]' host='[hostname ex. localhost]' port='[Port Number, ex 5432]'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM [table name]")
    rows = cur.fetchall()
    conn.close()
    return rows


print(view())
