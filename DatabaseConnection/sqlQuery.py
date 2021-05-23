from dbConnect import *
from Backend.person import *

def SelectContacts():
    cursor.execute('SELECT Person.FirstName, Person.LastName, Person.Email, Person.PhoneNumber, Department.DepName '
                   'FROM Person '
                   'INNER JOIN Department ON Person.DepID=Department.ID')
    cont = cursor.fetchall()
    return cont

SelectContacts()

