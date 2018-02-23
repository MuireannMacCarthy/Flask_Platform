from flask import Flask, render_template
from app import app


from systeminfo.main import get_platform


@app.route('/')
def index():
    returnDict = {}
    returnDict['user'] = 'Muireann'
    returnDict['title'] = 'Home'
    returnDict['platform'] = get_platform()
    return render_template("index.html", **returnDict)