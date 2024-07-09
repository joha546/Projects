from flask import render_template, render_template_string, request, redirect, session, url_for, flash
from . import auth
from .forms import LoginForm, SignupForm, TeacherSignupForm
from .models import User, Teacher
from .. import db

'''@auth.route('/')
def index():
    return "Hello, World!"

'''

@auth.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password')
            return redirect(url_for('auth.login'))
        session['user_id'] = user.id
        return redirect(url_for('dashboard'))  # Replace 'dashboard' with your desired route

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Attendance System</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    </head>
    <body>
        <div class="main">
            <div class="navbar">
                <div class="icon">
                    <h2 class="logo">BAIUST</h2>
                </div>
                <div class="menu">
                    <ul>
                        <li><a href="#">HOME</a></li>
                        <li><a href="#">ABOUT</a></li>
                        <li><a href="#">CONTACT</a></li>
                    </ul>
                </div>
            </div> 
            <div class="content">
                <h1>Students <br><span>Attendance</span> <br>System</h1>
                <div class="form">
                    <h2>Login Here</h2>
                    <form method="POST">
                        {{ form.hidden_tag() }}
                        {{ form.email(placeholder="Enter Email Here") }}
                        {{ form.password(placeholder="Enter Password Here") }}
                        {{ form.submit(class="btnn") }}
                    </form>
                    <p class="link">Don't have an account<br>
                        <a href="{{ url_for('auth.signup') }}">Sign up </a> for Students</a><br>
                        <a href="{{ url_for('auth.t_signup') }}">Sign up </a> for Teachers</a>
                    </p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html, form=form)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None:
            flash('Email is already registered. Please use a different email.')
            return redirect(url_for('auth.signup'))

        new_user = User(
            email=form.email.data,
            student_id=form.student_id.data,
            name=form.name.data
        )
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully. You can now log in.')
        return redirect(url_for('auth.login'))

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Attendance System</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    </head>
    <body>
        <div class="main">
            <div class="navbar">
                <div class="icon">
                    <h2 class="logo">BAIUST</h2>
                </div>
                <div class="menu">
                    <ul>
                        <li><a href="#">HOME</a></li>
                        <li><a href="#">ABOUT</a></li>
                        <li><a href="#">CONTACT</a></li>
                    </ul>
                </div>
            </div> 
            <div class="content">
                <h1>Students <br><span>Attendance</span> <br>System</h1>
                <div class="form">
                    <h2>Sign up for Students</h2>
                    <form method="POST">
                        {{ form.hidden_tag() }}
                        {{ form.name(placeholder="Enter Your Name") }}
                        {{ form.email(placeholder="Enter Email Here") }}
                        {{ form.student_id(placeholder="Enter ID") }}
                        {{ form.password(placeholder="Create New Password") }}
                        {{ form.confirm_password(placeholder="Confirm Password") }}
                        {{ form.submit(class="btnn") }}
                    </form>
                    <p class="link">Already have an account<br>
                    <a href="{{ url_for('auth.login') }}">Log in</a> here</a></p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html, form=form)

@auth.route('/t_signup', methods=['GET', 'POST'])
def t_signup():
    form = TeacherSignupForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None:
            flash('Email is already registered. Please use a different email.')
            return redirect(url_for('auth.t_signup'))

        new_user = Teacher(
            email=form.email.data,
            teacher_id=form.teacher_id.data,
            name=form.name.data
        )
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully. You can now log in.')
        return redirect(url_for('auth.login'))

    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>Attendance System</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    </head>
    <body>
        <div class="tmain">
            <div class="navbar">
                <div class="icon">
                    <h2 class="logo">BAIUST</h2>
                </div>
                <div class="menu">
                    <ul>
                        <li><a href="#">HOME</a></li>
                        <li><a href="#">ABOUT</a></li>
                        <li><a href="#">CONTACT</a></li>
                    </ul>
                </div>
            </div> 
            <div class="content">
                <h1>Students <br><span>Attendance</span> <br>System</h1>
                <div class="form">
                    <h2>Sign up for Teachers</h2>
                    <form method="POST">
                        {{ form.hidden_tag() }}
                        {{ form.name(placeholder="Enter Your Name") }}
                        {{ form.email(placeholder="Enter Email Here") }}
                        {{ form.teacher_id(placeholder="Enter ID") }}
                        {{ form.password(placeholder="Create New Password") }}
                        {{ form.confirm_password(placeholder="Confirm Password") }}
                        {{ form.submit(class="btnn") }}
                    </form>
                    <p class="link">Already have an account<br>
                    <a href="{{ url_for('auth.login') }}">Log in</a> here</a></p>
                </div>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html, form=form)

@auth.route('/db_content')
def db_content():
    students = User.query.all()
    teachers = Teacher.query.all()
    return render_template('db_content.html', students=students, teachers=teachers)