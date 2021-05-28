from dbConnect import DatabaseConnector
from sqlalchemy import Column, String, Integer, ForeignKey

class Person(DatabaseConnector.Base):
    __tablename__ = "Person"
    ID = Column(Integer, primary_key=True, autoincrement=True)
    UserLogin = Column(String, nullable=False)
    UserPassword = Column(String, nullable=False)
    FirstName = Column(String, nullable=False)
    LastName = Column(String, nullable=False)
    Email = Column(String, nullable=False)
    Phone = Column(String, nullable=False)
    DepID = Column(Integer, nullable=False)

    def __init__(self, user_login, user_password, firstname, lastname, email, phone, dep_id):
        self.UserLogin = user_login
        self.UserPassword = user_password
        self.FirstName = firstname
        self.LastName = lastname
        self.Email = email
        self.Phone = phone
        self.DepID = dep_id

DatabaseConnector.Base.metadata.create_all(DatabaseConnector.engine)

