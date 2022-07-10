from sqlalchemy.engine import create_engine
from sqlalchemy.orm import declarative_base



engine = create_engine('postgresql://postgres:Larry@localhost:5432/sqlalchemy') 

Base = declarative_base()

