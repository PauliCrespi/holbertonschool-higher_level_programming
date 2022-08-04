#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

try:
    conn = MySQLdb.connect(host="localhost",
                           user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    txt = "SELECT city.id, city.name, state.name FROM cities city,"
    txt1 = " states state WHERE state.id = city.state_id ORDER BY city.id"
    cur.execute(txt + txt1)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

except Exception:
    print("ERROR")
