from flask import render_template
from flask import Flask
import os

sajto = Flask(__name__) 
@sajto.route('/listo/')
def index():
    variablo = 'testa mesaĝo numero 1'
    return render_template('listo.html',teksto=variablo)
sajto.run(host='0.0.0.0', port=443,debug=True)