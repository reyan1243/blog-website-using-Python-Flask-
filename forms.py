from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired,Length,equal_to

class registeration_form(FlaskForm):
    user = StringField("Username", validators=[DataRequired(),Length(min=2,max=30)])
    email= StringField("Email",validators=[DataRequired(),Length(min=2,max=30)])
    password = PasswordField("Password", validators=[DataRequired()])
    confirm_password=PasswordField("Confirm-password",validators=[DataRequired(),equal_to(password)])
    remember=BooleanField("remenber me")
    submit=SubmitField("Sign In")



