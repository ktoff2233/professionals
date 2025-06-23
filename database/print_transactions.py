from database.database import get_db_context
from database.database_table_models import Transaction

def print_all_transactions():
    with get_db_context() as session:
        transactions = session.query(Transaction).all()
        for transaction in transactions:
            print(f"Transaction ID: {transaction.id}, Trader ID: {transaction.trader_id}, "
                  f"Purchase Date: {transaction.purchase_date}, Sell Date: {transaction.sell_date}, "
                  f"Ticker: {transaction.Ticker}, Quantity: {transaction.quantity}, "
                  f"Purchase Price: {transaction.purchase_price}, Sell Price: {transaction.sell_price}, "
                  f"Position: {transaction.position}")
