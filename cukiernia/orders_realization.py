from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *


class DataBase:

    def __init__(self):
        engine = create_engine('sqlite:///cukiernia.db', echo=True if __name__ == "__main__" else False)
        db.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)

    def get_by_id(self, id:int):
        session = self.Session()

