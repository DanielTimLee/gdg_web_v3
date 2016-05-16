from app import app
from flask import render_template


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('pages/index.html')


@app.route("/group/about")
def about():
    return render_template('pages/group/about.html')


@app.route("/group/member")
def member():
    return render_template('pages/group/member.html')


@app.route("/group/recruit")
def recruit():
    return render_template('pages/group/recruit.html')


@app.route("/group/mission")
def mission():
    return render_template('pages/group/mission.html')
