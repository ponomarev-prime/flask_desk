from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Включение режима отладки
app.debug = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_command', methods=['POST'])
def run_command():
    hostname = request.form['hostname']
    command = 'ping ' + hostname + ' -c 5'
    result = os.popen(command).read()
    return render_template('index.html', results=[result])

if __name__ == '__main__':
    app.run()
