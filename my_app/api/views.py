from flask import Blueprint, flash, redirect, render_template, request, jsonify, abort, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, current_user
from datetime import datetime
from my_app import db
from my_app.api.model import User, Client, DoctorRoom
from my_app.api.forms import RegisterForm, LoginForm, RegisterClientForm, FolderForm, SearchForm

ehealth = Blueprint('ehealth', __name__)

@ehealth.route('/dashboard', methods = ['POST', 'GET'])
def home():
    form = SearchForm()
    user = User.query.filter_by(id = current_user.id)
    if  request.method == "POST":
        print("entered post")
        search_term = form.search.data
        print("entered search")
        if search_term:
            patient = [client.to_dict() for client in Client.query.filter((Client.opd_number.contains(search_term)) | (Client.insurance_number.contains(search_term))).all()]
            print("entered")
            if patient:
                deed=None
                for p in patient:
                    deed = p['id']
                record = [client.to_dict() for client in DoctorRoom.query.filter(DoctorRoom.client_id.contains(deed)).all()]
                print(patient)
                print(record)
                return render_template ("search.html", patient=patient, record=record, user=user)
            else:
                return render_template ("search.html", user=user)                
        else:
            return render_template ("search.html", user=user)

    return render_template("home.html" , user=user, form=form)

@ehealth.route('/', methods = ['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit:
        user = User.query.filter_by(email = form.email.data).first()
        print("yeah test one1")
        if user and check_password_hash(user.password, form.password.data):
            print("checking if entered")
            login_user(user)
            print("done and dusted")
            return redirect('/dashboard')
        else:
            print("invalid details")
            flash("Invalid details...")

    return render_template("login.html", form=form)

@ehealth.route('/register', methods = ['POST', 'GET'])
def register():
    form = RegisterForm()
    if request.method == 'GET':
        return render_template('register.html', form=form)
    
    if request.method == 'POST':
        user = User(first_name=form.first_name.data,
                    last_name=form.last_name.data,
                    email=form.email.data,
                    password=generate_password_hash(form.password.data)
        )
        db.session.add(user)
        db.session.commit()
        return redirect ('/')

@ehealth.route('/client', methods = ['POST', 'GET'])
def clienr():
    form = RegisterClientForm()
    if request.method =="GET":
        return render_template("client.html", form=form)
    
    if request.method == 'POST':
        client = Client(first_name = form.first_name.data,
                            last_name = form.last_name.data,
                            opd_number = form.opd_number.data,
                            date_of_birth = form.date_of_birth.data,
                            nearest_relative = form.nearest_relative.data,
                            emergency_contact = form.emergency_contact.data,
                            insurance_status =form.insurance_status.data, 
                            insurance_type = form.insurance_type.data,
                            insurance_number = form.insurance_number.data
        )
        db.session.add(client)
        db.session.commit()
        return redirect('/dashboard')
    
@ehealth.route('/folder', methods = ['POST', 'GET'])
def search():
    form= FolderForm()
    wasNow = datetime.now()
    
    if request.method == 'GET':
        return render_template('folder.html', wasNow=wasNow, form=form)
    
    if form.validate_on_submit:
       client = Client.query.filter_by(opd_number=form.opd_number.data).first()
       if client:
            folder = DoctorRoom(client_id = client.id,
                                    note =  form.note.data,
                                    principal_didnose = form.principal_didnose.data,
                                    created_at =  form.created_at.data,
                                    drug =  form.drug.data,
                                    drug_collection_status =  form.drug_collection_status.data,
                                    admission_status = form.admission_status.data,
                                    admission_date = form.admission_date.data,
                                    discharge_date = form.discharge_date.data
                                ) 
            db.session.add(folder)
            db.session.commit()
            return redirect('/dashboard')
       else:
           flash("Client with this OPD number does not exist", "danger")
           return render_template("folder.html")

@ehealth.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    return redirect('/')    