from knit import db

class TblProducts(db.Model):
    __tablename__ = 'tblprod'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    desc = db.Column(db.String(2000))
    price = db.Column(db.Float(12))
    category = db.Column(db.String(50))
    enable = db.Column(db.Integer)
    picture = db.Column(db.String(50))