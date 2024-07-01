from flask import Flask, render_template, url_for, request, redirect
from model import connectToDb, insertDB, viewData, updateData, view_todo, deleteData
from datetime import datetime

app = Flask(__name__)

# def __repr__(self) -> str:
#     return f"{self.sno} - {self.title}"

connectToDb()

@app.route('/', methods=["GET", "POST"])
def home():
    
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        insertDB(title, desc)
    todos = viewData()
    # return todos
    return render_template('index.html', todos=todos, todo_id=1)

@app.route('/todo', methods=["GET"])
def listtodo():
    test = viewData()
    print(test)
    return render_template('index.html', test=test)
    return redirect(url_for("home"))


@app.route('/todo/<int:todo_id>', methods=["GET"])
def single_todo(todo_id):
    todo = view_todo(todo_id)  
    print(todo)
    return render_template('index.html', todo=todo)



# @app.route('/todo/create', methods=["GET"])

@app.route('/edit/<int:todo_id>', methods=["GET", "POST"])
def edit(todo_id):
    if request.method == "GET":
        todo = view_todo(todo_id)
        if todo:
            return render_template('edit.html', todo=todo)
        else:
            return "Todo not found"
    else:
        new_title = request.form.get('title')
        new_desc = request.form.get('desc')
        updateData(new_title, new_desc, todo_id)
        
        return redirect(url_for('home'))

# @app.route('/update/<int:todo_id>', methods=["POST"])
# def update_todo(todo_id):
#     if request.method == "POST":
#         new_title = request.form('new_title')
#         new_desc = request.form('new_desc')
#         updateData(new_title, new_desc, todo_id)

#         return render_template('edit.html')

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "GET":
        todo = viewData()
        if todo:
            return render_template('add.html', todo=todo)
    if request.method == "POST":
        title = request.form.get("title")
        desc = request.form.get("desc")
        print(f"Adding title: {title}, desc: {desc}")
        insertDB(title, desc)
        return redirect(url_for('home'))
    else:
        return redirect(url_for('home'))


@app.route("/delete/<int:todo_id>",methods=["POST"])
def delete_todo(todo_id):
    # return str(todo_id)
    # todo_id=1
    d = deleteData(todo_id)
    
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)