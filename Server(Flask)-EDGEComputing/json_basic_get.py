from flask import jsonify,Flask

app=Flask(__name__)
"json durumu"
durum=[
    {'name':'Merhokopkaba'},
    {'name':'Nasışpkpğllsın'},
    {'name':'Hayat Nasıl Gidiyor'},
    ]
"ilgili url e istek atıldığında"
@app.route('/',methods=['GET'])
def main():
    "bir return işlemi olsun"
    return jsonify({'durum':durum})

@app.route('/api',methods=['GET'])
def api():
    "bir return işlemi olsun"
    return jsonify({'durum':durum})

if __name__ == '__main__':
    "hani url den erişeceğimiz..."
    app.run(debug=True,host='0.0.0.0',port=9875)