from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:1234@localhost:3306/ncnt"
engine = create_engine(DATABASE_URL,echo=True)
SessionFactory = sessionmaker(autoflush= False, bind= engine)

def get_db():
    session = SessionFactory()

    try:
        yield session

    finally:
        session.close()