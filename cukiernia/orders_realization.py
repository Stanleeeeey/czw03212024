from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *


class DataBase:

    def __init__(self):
        engine = create_engine('sqlite:///cukiernia.db', echo=True if __name__ == "__main__" else False)
        db.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)

    def get_by_id(self, id:int) -> Order:
        session = self.Session()

        ans = session.query(Order).filter_by(id = id).first()
        session.close()

        return ans
    
    def update_status(self, id:int, status: int):
        session = self.Session()

        ans = session.query(Order).filter_by(id = id).first()

        if ans== None: return "Error: no order with that id"
        ans.order_status = str(Status(status).name)

        session.commit()
        session.close()

    def add_new_order(self, order:Order):
        session = self.Session()

        session.add(order)
        session.commit()
        session.close()


