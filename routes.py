from flask import Flask, render_template, redirect
from forms import SignUpForm, SignInForm, Project_detailsForm, ProjectForm, SignUp_orgForm
from flask_login import login_user, logout_user, login_required

from models import Project, User, Org_User
from os import path
from ext import app, db

profiles = []

@app.route("/")
def home():
    return render_template("EVRICA_guest_page.html")


@app.route("/projects")
def projects():
    projects = Project.query.all()
    return render_template("projects.html", projects=projects)

@app.route("/project/<int:project_id>")
def project(project_id):
    project = Project.query.get(project_id)
    return render_template("project_details.html", project=project, role="Admin")

@app.route("/create_project", methods=["GET", "POST"])
#@login_required
def create_project():
    form = ProjectForm()
    if form.validate_on_submit():
        new_project = Project(title=form.title.data, deadline=form.deadline.data, detailed_description=form.detailed_description.data)
        image = form.project_img.data
        directory = path.join(app.root_path, "static", "images", image.filename)
        image.save(directory)

        project.project_img = image.filename
        new_project.create()
        return redirect("/projects")
    return render_template("create_project.html", form=form)


@app.route("/edit_project/<int:project_id>", methods=["GET", "POST"])
#@login_required
def edit_project(project_id):
    project = Project.query.get(project_id)
    form = ProjectForm(title=project.title, deadline=project.deadline, detailed_description=project.detailed_description, project_img=project.project_img)
    if form.validate_on_submit():
        project.title = form.title.data
        project.deadline = form.deadline.data
        project.detailed_description = form.detailed_description.data

        project.project_img = form.project_img.data
        project.save()
        return redirect("/projects")

    return render_template("create_project.html", form=form)

@app.route("/delete_project/<int:project_id>")
#@login_required
def delete_project(project_id):
    project = Project.query.get(project_id)

    project.delete()
    return redirect("/projects")


@app.route("/SignUp", methods=["POST", "GET"])
def SignUp():
    form = SignUpForm()
    if form.validate_on_submit():
        if form.Sign_Up.data:
            new_user = User(FullName=form.FullName.data, Birthday=form.Birthday.data, Gender=form.Gender.data, Region=form.Region.data, Email=form.Email.data, Password=form.Password.data)
            image = form.profile_img.data
            directory = path.join(app.root_path, "static", "images", image.filename)
            image.save(directory)

            new_user.profile_img = image.filename
            new_user.create()
            pass
        return redirect("/")
    return render_template("SignUp.html", form=form)

@app.route("/SignUp_org", methods=["POST", "GET"])
def SignUp_org():
    form = SignUp_orgForm()
    if form.validate_on_submit():
        if form.Sign_Up.data:
            new_user = Org_User(OrgName=form.OrgName.data, Email=form.Email.data, Password=form.Password.data)
            image = form.org_profile_img.data
            directory = path.join(app.root_path, "static", "images", image.filename)
            image.save(directory)

            new_user.org_profile_img = image.filename
            new_user.create()
            pass
        return redirect("/")
    return render_template("SignUp_org.html", form=form)

@app.route("/Signin", methods=["POST", "GET"])
def Signin():
    form = SignInForm()
    if form.validate_on_submit():
        user = User.query.filter(User.Email == form.Email.data).first()
        if user:
            login_user(user)
        return redirect("/") #hmmmmm

    return render_template("Signin.html", form=form)

@app.route("/Logout")
def Logout():
    logout_user()
    return redirect("/")









@app.route("/profile/<int:profile_id>")
def profile(profile_id):
    print("Received profile id", profile_id)
    return render_template("profile.html", user=profiles[profile_id])

@app.route("/Project_details", methods=["GET", "POST"])
def Project_details():
    form = Project_detailsForm()
    if form.validate_on_submit():
        return render_template("project_details.html", form=form, project=projects[0], role="Guest")


@app.route("/communities")
def communities():
    return render_template("communities.html")


@app.route("/people")
def people():
    return render_template("people.html")

#if __name__ == "__main__":
 #   app.run(debug=True)