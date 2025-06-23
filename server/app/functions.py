from .__init__ import db

class Trader(db.Model):
    __tablename__ = 'traders'
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Float, nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey('managers.id'), nullable=False)

    manager = db.relationship('Manager', backref=db.backref('traders', lazy=True))

class Manager(db.Model):
    __tablename__ = 'managers'
    id = db.Column(db.Integer, primary_key=True)
    trading_level = db.Column(db.String(50), nullable=False)
    fname = db.Column(db.String(50), nullable=False)
    lname = db.Column(db.String(50), nullable=False)
    score = db.Column(db.Float, nullable=False)

def get_all_traders():
    """Fetch all traders from the database."""
    return Trader.query.all()

def get_trader_by_id(trader_id):
    """Fetch a trader by their ID."""
    return Trader.query.get(trader_id)

def get_all_managers():
    """Fetch all managers from the database."""
    return Manager.query.all()

def get_manager_by_id(manager_id):
    """Fetch a manager by their ID."""
    return Manager.query.get(manager_id)

def get_traders_by_manager(manager_id):
    """Fetch all traders assigned to a specific manager."""
    return Trader.query.filter_by(manager_id=manager_id).all()

def get_trader_count_by_manager(manager_id):
    """Fetch the number of traders assigned to a specific manager."""
    return Trader.query.filter_by(manager_id=manager_id).count()


