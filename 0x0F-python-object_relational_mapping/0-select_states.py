#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

try:
    conn = MySQLdb.connect(host="localhost",
                           user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

except Exception:
    print("ERROR")
