from flask import Flask, abort, jsonify, make_response, request, render_template
from app.nfa_parser import NFA_Parser
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
@app.route('/index', methods=['POST'])
def convert():
    parser = NFA_Parser()
    input_regex = request.form['input_regex']
    try:
        nfa = parser.compile(input_regex)
    except:
        return render_template('index.html',
                            badGrammar=True)
    return render_template('index.html')
