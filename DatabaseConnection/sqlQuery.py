from dbConnect import *

contact = []
row = ''
def SelectSQL(what, where):
    cursor.execute("SELECT" + what + "FROM" + where)
    row = cursor.fetchall()
    for j in row:
        contact.append(j)