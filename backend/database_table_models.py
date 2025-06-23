from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from datetime import datetime
from enum import Enum
from sqlalchemy.types import Enum as SQLAlchemyEnum
Base = declarative_base()

class Trader(Base):
    __tablename__ = 'traders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fname = Column(String)
    lname = Column(String)
    score = Column(Integer)
    manager_id = Column(Integer, ForeignKey('managers.id'))
    
    transactions = relationship("Transaction", back_populates="trader")
    manager = relationship("Manager", back_populates="traders")
    
    def __repr__(self):
        return f"<Trader(id={self.id}, fname={self.fname}, lname={self.lname}, score={self.score}, manager_id={self.manager_id})>"

class Manager(Base):
    __tablename__ = 'managers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fname = Column(String)
    lname = Column(String)
    score = Column(Integer)
    trading_level = Column(Integer)

    traders = relationship("Trader", back_populates="manager")
    
    def __repr__(self):
        return f"<Manager(id={self.id}, fname={self.fname}, lname={self.lname}, score={self.score}, trading_level={self.trading_level})>"

class PositionEnum(Enum):
    CALL = "call"
    SHORT = "short"
    HOLD = "hold"

class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    trader_id = Column(Integer, ForeignKey('traders.id'))
    purchase_date = Column(DateTime, default=datetime.now())
    sell_date = Column(DateTime, default=None)
    purchase_price = Column(Integer)
    sell_price = Column(Integer, default=None)
    Ticker = Column(String(6))
    quantity = Column(Integer)
    position = Column(SQLAlchemyEnum(PositionEnum), nullable=False)

    trader = relationship("Trader", back_populates="transactions")
    
    def __repr__(self):
        return (f"<Transaction(id={self.id}, trader_id={self.trader_id}, purchase_date={self.purchase_date}, "
                f"sell_date={self.sell_date}, purchase_price={self.purchase_price}, sell_price={self.sell_price}, "
                f"Ticker={self.Ticker}, quantity={self.quantity}, position={self.position})>")

class Login(Base):
    __tablename__ = 'logins'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)  # Store hashed passwords
    role = Column(String(20), nullable=False)  # e.g., 'trader', 'manager', 'admin'
    
    def __repr__(self):
        return f"<Login(username={self.username}, role={self.role})>"