from database import Base
import sqlalchemy as db

class Transaction(Base):
    __tablename__ = "transactions"
    
    id = db.Column(db.Integer, primary_key=True, index=True)
    date = db.Column(db.String)
    amount = db.Column(db.Float)
    category = db.Column(db.String)
    is_income = db.Column(db.Boolean)
    description = db.Column(db.String)
    