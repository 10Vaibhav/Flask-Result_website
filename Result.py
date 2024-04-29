# integrating html with flask
# http verb like get and post

# jinja2 template engine

"""
{%...%} for statements,conditions,loops
{{  }}  expressions to print output
{#....#} this is for comments
"""

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "pass"
    else:
        res = "fail"
    exp = {'score': score, 'res': res}
    return render_template('result.html', result=exp)


# Result checker submit html page
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        DAA = float(request.form['DAA'])
        TFCS = float(request.form['TFCS'])
        BDA = float(request.form['BDA'])
        DBMS = float(request.form['DBMS'])
        LA = float(request.form['LA'])

        total_score = (DAA + TFCS + BDA + DBMS + LA) / 5
    return redirect(url_for("success", score=total_score))


if __name__ == '__main__':
    app.run(debug=True)
