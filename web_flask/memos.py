from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__) #flask 객체 생성, 웹서버 역할

db_config={'host':'localhost', 'port':3306,
           'user':'madang', 'password':'madang', 'db':'madangdb'}
def get_db_connection():
    return pymysql.connect(**db_config) #언패킹

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM memos ORDER BY created_at DESC")
    memos = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('memos/index.html', memos=memos)
                  #템프릿에서 사용할 변수 = 파이썬에서 DB결과를 담은 변수
@app.route('/add', methods=['GET','POST'])
def add():
    if request.method =='POST':
        title = request.form['title']
        content = request.form['content']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("insert into memos (title, content) values (%s,%s)", (title, content))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('memos/add.html')

@app.route('/edit/<int:memo_id>', methods=['GET','POST'])
def edit(memo_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method =="POST":
        title = request.form['title']
        content = request.form['content']
        cursor.execute("update memos set title=%s, content=%s where id=%s", (title, content, memo_id))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))
    
    cursor.execute("select * from memos where id=%s", (memo_id,))
    memo = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('memos/edit.html', memo=memo)

#메모 삭제
@app.route('/delete/<int:memo_id>')
def delete(memo_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('delete from memos where id=%s', (memo_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect(url_for('index'))

if __name__ == "__main__" :
    app.run(debug=True)