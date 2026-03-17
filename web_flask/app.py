from flask import Flask, render_template, redirect,url_for,request

app = Flask(__name__) #flask 객체 생성=>웹서버 역할을 함

#웹사이트 루트, 누가 해당 주소로 요청을 보내면 hello()실행해라 알려주는 역할
#데코레이터 : 라우팅을 정의함
# @app.route("/") 
# def hello():
#     return "Hello Flask!"

users = {'kim':'1234'}
posts = [{'title':'첫번째 글', 'author':'작성자1'},{'title':'두번째 글', 'author':'작성자2'},{'title':'세번째 글', 'author':'kim'}]
dict_user = {'name':'kim', 'job':'student', 'age':10}
 
current_user = None

@app.route("/") #html문서를 지정해줄 것, 클라 브라우저로 결과값을 리턴해줄 것
#templates 폴더를 자동으로 찾아서 템플릿 로딩
def home() : 
    #데이터 여러개 보낼 경우 , value=값 이런식으로 작성하면 됨
    #return render_template('HTML문서 경로', user=current_users, value=값)
    return render_template('login/index.html', user=current_user)

@app.route("/logout")
def logout():
    global current_user
    current_user = None
    #url_for : 함수 이름으로 경로 생성
    return redirect(url_for('home'))#home이라는 함수 이름이 등록된 URL 찾아서 문자열로 변환

#/login : GET 로그인 form 화면 출력
#/login : POST 폼에서 전송된 id, pwd값으로 로그인 처리
@app.route('/login', methods=['GET','POST'])
def login():
    global current_user
    if request.method == 'POST':
        #form에서 전송한 값 꺼내오기
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password: #로그인 성공시
            current_user = username
            return redirect(url_for('home'))
        else: return render_template('login/login.html', error='로그인 실패')
    else : return render_template("login/login.html")

@app.route('/a')
def showApage():
    #return render_template('login/a.html') # 이렇게 a.html 생성해도 되지만
    return '<h1>A 페이지 입니다</h1>' #이렇게도 페이지 생성 가능

@app.route('/posts')
def post_list():
    return render_template('login/posts.html', posts=posts, user=current_user, dict_user = dict_user)


if __name__ == "__main__" :
    app.run(debug=True)