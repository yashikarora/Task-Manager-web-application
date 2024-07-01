import sqlite3

def connectToDb():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Todo
                   (title TEXT NOT NULL,
                   desc TEXT NOT NULL,
                   id INTEGER PRIMARY KEY AUTOINCREMENT)''')
    
    conn.commit()
    print('Table Todo has created')
    conn.close()

def viewData():
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute("Select title, desc, id from Todo")
    rows = cursor.fetchall()
    return rows

def view_todo(todo_id):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute("Select title, desc, id from Todo where id=?", (todo_id,))
    rows = cursor.fetchall()

    if len(rows) > 0:
        todo_tuple = rows[0]
        return { "title": todo_tuple[0], "desc": todo_tuple[1], "Id": todo_tuple[2] }
    else:
        return None

def insertDB(title, desc):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Todo (title, desc) VALUES (?, ?)",(title, desc))
    conn.commit()
    print('value is inserted')
    conn.close()


    
def updateData(new_title, new_desc, todo_id):
    conn = sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE Todo SET title=?, desc=? WHERE id=?", (new_title, new_desc, todo_id))
    conn.commit()
    conn.close()

def deleteData(todo_id):
    conn=sqlite3.connect('todo.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Todo WHERE id=?", (todo_id,))
    conn.commit()
    conn.close()