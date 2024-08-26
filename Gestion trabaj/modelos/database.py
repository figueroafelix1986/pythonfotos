import os
from modelos.librery import create_engine,sessionmaker


class Database():
    def __init__(self, db_url, Base):
        self.engine = create_engine(db_url)
        if not os.path.exists(db_url.split('///')[-1]):
            Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()
