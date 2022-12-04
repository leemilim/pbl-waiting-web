from flask import Flask, request, render_template, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.hsitcgg.mongodb.net/test')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/massplate')
def massplate():
    return render_template('massplate.html')

@app.route('/hyo2dang')
def hyo2dang():
    return render_template('hyo2dang.html')

@app.route('/korea')
def korea():
    return render_template('korea.html')

@app.route('/ktmurijib')
def ktmurijib():
    return render_template('ktmurijib.html')

@app.route('/china')
def china():
    return render_template('china.html')

@app.route('/japan')
def japan():
    return render_template('japan.html')

@app.route('/west')
def west():
    return render_template('west.html')

@app.route('/etc')
def etc():
    return render_template('etc.html')

@app.route('/my_restaurant')
def my_restaurant():
    return render_template('my_restaurant.html')


@app.route('/waiting/fixing', methods=['POST'])
def waiting_fixing():
    name_receive = request.form['name_give']
    db.waiting.update_one({'num': int(name_receive)},{'$set':{'fixed': 0}})

    return jsonify({'msg': 'fixed!'})

@app.route('/waiting/unfixing', methods=['POST'])
def waiting_unfixing():
    name_receive = request.form['name_give']
    db.waiting.update_one({'num': int(name_receive)},{'$set':{'fixed': 1}})

    return jsonify({'msg': 'unfixed!'})


@app.route('/waiting', methods=['POST'])
def waiting_post():
    waiting_receive = request.form['waiting_give']

    db.waiting.update_one({'name':'끄트머리집'},{'$set':{'wait': waiting_receive}})

    return jsonify({'msg':'success!'})


@app.route('/waiting', methods=['GET'])
def waiting_get():
    waiting_list = list(db.waiting.find({},{'_id':False}))

    return jsonify({'waiting': waiting_list})


if __name__ == '__main__':
    app.run('0.0.0.0',port=5000,debug=True)
