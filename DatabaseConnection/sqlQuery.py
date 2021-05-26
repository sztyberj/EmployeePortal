from main import *
from dbConnect import conn

class SqlQuery:

    def SelectContacts(self):
        cursor.execute('SELECT Person.ID, Person.FirstName, Person.LastName, Person.Email, Person.PhoneNumber, Department.DepName '
                       'FROM Person '
                       'INNER JOIN Department ON Person.DepID=Department.ID')
        cont = cursor.fetchall()
        return cont


    def Select(self, query, condition):
        cursor.execute(query +"'"+condition+"'")
        results = cursor.fetchall()
        return results

    def Update(self, query):
        cursor.execute(query)
        cursor.commit()
        print('udało się')
