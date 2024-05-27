from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, PasswordField, EmailField, SubmitField,SelectField,DateField, IntegerField,TextAreaField, DateTimeField

class RegisterForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class RegisterClientForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    opd_number = IntegerField('OPD Number', validators=[DataRequired()])
    date_of_birth = DateField('Date Of Birth', validators=[DataRequired()])
    nearest_relative = StringField('Nearest Relative', validators=[DataRequired()])
    emergency_contact = IntegerField('Emergency Contact', validators=[DataRequired()])
    insurance_status = SelectField('Insurance Status', choices=[('YES', 'YES'), ('NO', 'NO')])
    insurance_type = StringField('Insurance Type')
    insurance_number = IntegerField('Insurance Number')
    submit = SubmitField('Save',  render_kw={"class":"butsave"})

class FolderForm(FlaskForm):
    opd_number = IntegerField('OPD Number', validators=[DataRequired()])
    note =  TextAreaField('Physician Note', validators=[DataRequired()])
    principal_didnose = StringField('Principal Diagnose', validators=[DataRequired()])
    created_at =  DateTimeField("Date", validators=[DataRequired()])
    drug =  StringField('Drug', validators=[DataRequired()])
    drug_collection_status =  SelectField('Drug Collection Status', choices=[('YES', 'YES'), ('NO', 'NO')])
    admission_status = SelectField('Admission Status', choices=[('YES', 'YES'), ('NO', 'NO')])
    admission_date =  DateTimeField("Admission Date")
    discharge_date =  DateTimeField("Discharge Date")
    submit = SubmitField('Save', render_kw={"class":"butsave"})


class SearchForm(FlaskForm):
    search = IntegerField('search term', validators=[DataRequired()], render_kw={"placeholder" : "Enter OPD Number or  Insurace Number","class": "search"})
    submit = SubmitField('Search', render_kw={"class": "searhbuttton"})