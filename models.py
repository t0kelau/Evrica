from flask_login import UserMixin

from ext import db, login_manager

class BaseModel:
    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def save(self):
        db.session.commit()


class Project(db.Model, BaseModel):

    __tablename__ = "projects"

    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(), nullable=False)
    deadline = db.Column(db.DateTime(), nullable=False)
    detailed_description = db.Column(db.String(), nullable=False)
    project_img = db.Column(db.String(), nullable=False, default="default_photo.jpg")



class User(db.Model, BaseModel):

    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    FullName = db.Column(db.String(), nullable=False)
    Birthday = db.Column(db.DateTime(), nullable=False)
    Gender = db.Column(db.String(), nullable=False)
    Region = db.Column(db.String(), nullable=False)
    Email = db.Column(db.String(), nullable=False)
    Password = db.Column(db.String(), nullable=False)
    profile_img = db.Column(db.String(), nullable=False, default="default_photo.jpg")
    role = db.Column(db.String())


class Org_User(db.Model, BaseModel, UserMixin):

    __tablename__ = "org_users"

    id = db.Column(db.Integer(), primary_key=True)
    OrgName = db.Column(db.String(), nullable=False)
    Email = db.Column(db.String(), nullable=False)
    Password = db.Column(db.String(), nullable=False)
    org_profile_img = db.Column(db.String(), nullable=False, default="default_photo.jpg")
    role = db.Column(db.String())


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



def load_user(user_id):
    return User.query.get(user_id)





