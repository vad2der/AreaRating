from model.model import School, Rank, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import func

# db config
engine = create_engine('sqlite:///school_ranks.db') # for windows create_engine('sqlite:///C:\\app\\db\\school_ranks.db')
session = sessionmaker()
session.configure(bind=engine)
s = session()

def create_tables():
    # table drop and creation
    try:
        Base.metadata.drop_all(engine)
    except:
        pass
    Base.metadata.create_all(engine)

def get_all_schools():
    pass

def get_all_rank_for_school(school_id):
    pass