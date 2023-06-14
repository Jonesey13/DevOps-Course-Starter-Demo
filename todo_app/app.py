from flask import Flask, redirect, render_template, request
from todo_app.data.session_items import add_item, get_items

from todo_app.flask_config import Config

app = Flask(__name__)
app.config.from_object(Config())


@app.route('/')
def index():
    items = get_items()
    return render_template("index.html", items_list = items)


@app.route('/add-todo', methods = ["POST"])
def add_todo():
    todo_name = request.form.get('todo-title')
    add_item(todo_name)
    return redirect('/')