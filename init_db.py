from ext import app, db
from models import Project, Org_User, User

with app.app_context():

    db.drop_all()
    db.create_all()

    #admin_user = User(FullName = "admin", password="adminpass", role="Admin")
    #admin_user.create()
