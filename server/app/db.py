from flask_sqlalchemy import SQLAchemy 
from flask_migrate import Migrate 
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
db=SQLAlchemy(model_class=Base)
migrate=Migrate()