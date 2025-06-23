from sqlalchemy.orm import Session
from database.database_table_models import Transaction, PositionEnum

def insert_transaction(session: Session, trader_id: int, purchase_date: str, sell_date: str, purchase_price: int, 
                       sell_price: int, ticker: str, quantity: int, position: str):
    """
    Inserts a new transaction into the database.

    Args:
        session (Session): SQLAlchemy session object.
        trader_id (int): ID of the trader.
        purchase_date (str): Date of purchase (YYYY-MM-DD).
        sell_date (str): Date of sale (YYYY-MM-DD).
        purchase_price (int): Price at purchase.
        sell_price (int): Price at sale.
        ticker (str): Stock ticker symbol.
        quantity (int): Quantity of stocks.
        position (str): Position type (CALL, SHORT, HOLD).

    Returns:
        Transaction: The newly created transaction object.
    """
    new_transaction = Transaction(
        trader_id=trader_id,
        purchase_date=purchase_date,
        sell_date=sell_date,
        purchase_price=purchase_price,
        sell_price=sell_price,
        Ticker=ticker,
        quantity=quantity,
        position=PositionEnum[position.lower()]
    )
    session.add(new_transaction)
    session.commit()
    return new_transaction

def create_sample_transactions(session: Session):
    """
    Creates sample transactions for trader ID 1.

    Args:
        session (Session): SQLAlchemy session object.
    """
    sample_transactions = [
        {
            "trader_id": 1,
            "purchase_date": "2023-01-01",
            "sell_date": "2023-01-10",
            "purchase_price": 100,
            "sell_price": 120,
            "ticker": "XYZ",
            "quantity": 50,
            "position": "CALL"
        },
        {
            "trader_id": 1,
            "purchase_date": "2023-02-01",
            "sell_date": "2023-02-15",
            "purchase_price": 200,
            "sell_price": 250,
            "ticker": "ABC",
            "quantity": 30,
            "position": "SHORT"
        },
        {
            "trader_id": 1,
            "purchase_date": "2023-03-01",
            "sell_date": "2023-03-20",
            "purchase_price": 150,
            "sell_price": 180,
            "ticker": "DEF",
            "quantity": 40,
            "position": "HOLD"
        }
    ]

    for transaction in sample_transactions:
        insert_transaction(
            session=session,
            trader_id=transaction["trader_id"],
            purchase_date=transaction["purchase_date"],
            sell_date=transaction["sell_date"],
            purchase_price=transaction["purchase_price"],
            sell_price=transaction["sell_price"],
            ticker=transaction["ticker"],
            quantity=transaction["quantity"],
            position=transaction["position"]
        )