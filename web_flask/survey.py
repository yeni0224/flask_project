from flask import Flask, render_template,request, redirect, url_for, jsonify

app = Flask(__name__)
app.secret_key = 'secret123' #세션/쿠키 데이터 암호화할때 사용하는 키

#설문 데이터
survey = {
    "question":"가장 좋아하는 과일은 무엇인가요?",
    "choices":['사과','바나나','포도'],
    "votes":[0,0,0]}

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == "POST":
        choice_index = int(request.form["choice"])
        print(choice_index)
        survey["votes"][choice_index] += 1
        
        return redirect(url_for('result')) #해당 함수 이름을 찾아서 URL 만들어줌
    return render_template("survey/index.html", survey=survey)
    
@app.route("/result")
def result():
    return render_template("survey/result.html", survey=survey)

#AJAX용 엔드포인트 : 투표데이터 반환
@app.route('/votes')
def votes():
    total = sum(survey['votes'])
    percentages = [round(v/total*100, 1) if total > 0 else 0 for v in survey['votes']]
    return jsonify({"votes":survey["votes"], "percentages":percentages})

if __name__ == "__main__":
    app.run(debug=True)