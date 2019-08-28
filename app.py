from flask import Flask, jsonify, request, render_template
from flask import url_for
from werkzeug import secure_filename

app1 = Flask(__name__)

@app1.route('/')
def hello_world():
    return 'Hello World!'

@app1.route('/user/<int:id>/')
def user_id(id):
    ret = {}
    ret['method'] = request.method
    ret['type'] = str(type(id))
    ret['id'] = id
    ret['msg'] = request.args.get('msg', 'default message')
    return jsonify(ret)

@app1.route('/hello/')
@app1.route('/hello/<name>/')
def hello(name=None):
    return render_template('hello.html', name=name)

@app1.route('/upload/', methods=['POST'])
def upload():
    file1 = request.files['file']
    file1.save('upload/' + secure_filename(file1.filename))
    ret = {}
    ret['type'] = str(type(file1))
    ret['dir'] = dir(file1)
    return jsonify(ret)

if __name__ == '__main__':
    # url_for('static', filename='1.js')
    app1.run(debug=True)
