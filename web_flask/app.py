from flask import Flask

app = Flask(__name__) #flask 객체 생성=>웹서버 역할을 함

#웹사이트 루트, 누가 해당 주소로 요청을 보내면 hello()실행해라 알려주는 역할
#데코레이터 : 라우팅을 정의함
@app.route("/") 
def hello():
    return "Hello Flask!"
if __name__ == "__main__" :
    app.run(debug=True)