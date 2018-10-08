from flask import Flask, request, redirect
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
    


@app.route("/greeting", methods=['POST'])
def greeting():
    user_name = request.form['user_name']
    template = jinja_env.get_template('greeting.html')
    return template.render(name=user_name)



app.run()   