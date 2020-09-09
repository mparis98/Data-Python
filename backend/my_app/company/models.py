from my_app import db


class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    siren = db.Column(db.String(255))
    denomination = db.Column(db.String(255))
    region = db.Column(db.String(255))
    ville = db.Column(db.String(255))
    code_postal = db.Column(db.String(255))
    num_dept = db.Column(db.String(255))
    date_immatriculation = db.Column(db.DateTime)

    def __init__(self, siren, denomination, region, ville, code_postal, num_dept, date_immatriculation):
        self.siren = siren
        self.denomination = denomination
        self.region = region
        self.ville = ville
        self.code_postal = code_postal
        self.num_dept = num_dept
        self.date_immatriculation = date_immatriculation

    def __repr__(self):
        return '<Company %d>' % self.id
