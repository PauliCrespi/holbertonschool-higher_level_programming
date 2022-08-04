#!/usr/bin/python3

if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    namearg = argv[4]

try:
    conn = MySQLdb.connect(host="localhost",
                           user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    txt = "SELECT cities.name FROM cities JOIN "
    txt1 = "states ON cities.state_id = states.id WHERE"
    txt2 = " states.name LIKE '" + namearg + "'"
    cur.execute(txt + txt1 + txt2)
    query_rows = cur.fetchall()
    lo = ""
    for row in query_rows:
        for wen in row:
            lo = lo + wen + ", "
    print(lo[:-2])
    cur.close()
    conn.close()

except Exception:
    print("ERROR")
