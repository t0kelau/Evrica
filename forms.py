from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, RadioField, SelectField, SubmitField
from wtforms.validators import DataRequired, EqualTo, length, Email
from flask_wtf.file import FileField, FileRequired, FileSize, FileAllowed

class SignUpForm(FlaskForm):
    profile_img = FileField("Profile Image", validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!'), FileSize(1024 * 1024 * 2)])

    Student = SubmitField()
    Organisation = SubmitField()

    FullName = StringField(validators=[DataRequired()])
    Birthday = DateField(validators=[DataRequired()])
    Gender = SelectField(choices=["Male", "Female", "Other"], validators=[DataRequired()])
    Region = SelectField(choices=["Tbilisi", "Batumi", "Kutaisi"], validators=[DataRequired()])
    Email = StringField(validators=[DataRequired()])
    Password = PasswordField(validators=[DataRequired(), length(min=8, max=64, message="Password must be 8 characters or more")])
    ConfirmPassword = PasswordField(validators=[DataRequired(), EqualTo("Password", message="The passwords you entered do not match")])

    Sign_Up = SubmitField("Sign Up")
    Sign_Up_as_an_organization = SubmitField("Sign Up As An Organization")


class SignUp_orgForm(FlaskForm):
    org_profile_img = FileField("Organisanion profile image", validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!'), FileSize(1024 * 1024 * 2)])

    Student = SubmitField()
    Organisation = SubmitField()

    OrgName = StringField(validators=[DataRequired()])
    Email = StringField(validators=[DataRequired()])
    Password = PasswordField(validators=[DataRequired(), length(min=8, max=64, message="Password must be 8 characters or more")])
    ConfirmPassword = PasswordField(validators=[DataRequired(), EqualTo("Password", message="The passwords you entered do not match")])

    Sign_Up = SubmitField("Sign Up")
    #Sign_Up_as_an_organization = SubmitField("Sign Up As An Organization")


class SignInForm(FlaskForm):
    Email = StringField(validators=[DataRequired()])
    Password = PasswordField(validators=[DataRequired()])

    Sign_In = SubmitField("Sign In")

class Project_detailsForm(FlaskForm):
    project_img = FileField("Project Image", validators=[FileRequired(), FileAllowed(['jpg', 'png', 'jpeg'], 'Images only!')])

class ProjectForm(FlaskForm):
    title = StringField("Project Title", validators=[DataRequired()])
    deadline = DateField("Deadline", validators=[DataRequired()])
    detailed_description = StringField("Detailed Description", validators=[DataRequired()])
    project_img = FileField("Project Image", validators=[DataRequired()])
    submit = SubmitField("Upload Project")



