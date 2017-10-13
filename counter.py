from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "ThisIsSecret"

 

@app.route('/')
def makeCounter(): 
    session['counter']=0
    return render_template('index.html', counter=session['counter'])

@app.route('/count', methods=['post'])
def countEmUp():
    session['counter']=session['counter']+1
    return render_template('index.html', counter=session['counter'])

@app.route('/count2', methods=['post'])
def countByTwo():
    session['counter']=session['counter']+2
    return render_template('index.html', counter=session['counter'])

@app.route('/reset', methods=['post'])
def reset():
    session['counter']=0
    return render_template('index.html', counter=session['counter'])

app.run(debug=True)
