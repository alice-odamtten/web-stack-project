from my_app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String, unique = True)
    password = db.Column(db.String)

    '''client = db.relationship ('Client', backref ='owner')'''

    def __repr__(self):
        return f'User.{self.first_name} {self.last_name}'
    
class Client(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    opd_number = db.Column(db.Integer, unique= True)
    date_of_birth = db.Column(db.DateTime())
    nearest_relative = db.Column(db.String(255))
    emergency_contact = db.Column(db.Integer)
    insurance_status = db.Column(db.String)
    insurance_type = db.Column(db.String(255))
    insurance_number = db.Column(db.Integer)

    doctorroom = db.relationship ('DoctorRoom', backref ='owner')

    def to_dict(self):
        return {
            'id' : self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'opd_number': self.opd_number,
            'date_of_birth': self.date_of_birth,
            'nearest_relative': self.nearest_relative,
            'emergency_contact': self.emergency_contact,
            'insurance_status': self.insurance_status,
            'insurance_type': self.insurance_type,
            'insurance_number': self.insurance_number
        }

    

class DoctorRoom(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    note =  db.Column(db.Text)
    principal_didnose = db.Column(db.String(255))
    created_at =  db.Column(db.DateTime())
    drug =  db.Column(db.String(255))
    drug_collection_status =  db.Column(db.String)
    admission_status = db.Column(db.String)
    admission_date = db.Column(db.DateTime())
    discharge_date = db.Column(db.DateTime())
    
    def to_dict(self):
        return {
            'client_id': self.client_id,
            'note': self.note,
            'principal_didnose': self.principal_didnose,
            'created_at': self.created_at,
            'drug': self.drug,
            'drug_collection_status': self.drug_collection_status,
            'admission_status': self.admission_status,
            'admission_date': self.admission_date,
            'discharge_date': self.discharge_date
        }
    

