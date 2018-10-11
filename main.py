from flask import Flask, request, redirect, render_template
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('form.html')
    return template.render()


@app.route("/", methods=['POST'])
def validate_form():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''


    if len(username) < 3 or len(username) > 20 or " " in username:
        username_error = "That's not a valid username"
        username = ""

    if len(password) < 3 or len(password) > 20 or " " in password:
        password_error = "That's not a valid password"
        password = ""

    if verify != password:
        verify_error = "Passwords are not the same"
        verify = ""

    if "@" and "." not in email:
        email_error = "That's not a valid email"
        email = ""

    if username_error or password_error or verify_error or email_error:
        template = jinja_env.get_template('form.html')
        return template.render(username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error, username=username, password=password, verify=verify, email=email) 

    else: 
        return redirect('/greeting?username={}'.format(username))


@app.route("/greeting", methods=['POST', 'GET'])
def greeting():
    name = request.args.get('username')
    template = jinja_env.get_template('greeting.html')
    return render_template(template, name=name)



app.run()   