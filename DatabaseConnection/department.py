from dbConnect import DatabaseConnector
from sqlalchemy import Column, String, Integer, ForeignKey


class Department(DatabaseConnector.Base):
    __tablename__ = "Department"
    ID = Column(Integer, primary_key=True, autoincrement=True)
    DepName = Column(String, nullable=False)

    def __init__(self, dep_name):
        self.DepName = dep_name

DatabaseConnector.Base.metadata.create_all(DatabaseConnector.engine)

