from sqlalchemy import Column, String, Integer, ForeignKey, Date
from DatabaseConnection.dbConnect import DatabaseConnector


class WorkHour(DatabaseConnector.Base):
    __tablename__ = "WorkHours"
    ID = Column(Integer, primary_key=True, autoincrement=True)
    WorkDate = Column(Date, nullable=False)
    WorkHours = Column(Integer, nullable=False)

    def __init__(self, id, work_date, work_hours):
        self.WorkDate = work_date
        self.WorkHour = work_hours

DatabaseConnector.Base.metadata.create_all(DatabaseConnector.engine)