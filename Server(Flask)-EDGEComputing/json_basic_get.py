from flask import jsonify,Flask

app=Flask(__name__)
"json durumu"
durum=[
    {'name':'Merhaba'},
    {'name':'Nasılsın'},
    {'name':'Hayat Nasıl Gidiyor'},
    ]
"ilgili url e istek atıldığında"
@app.route('/',methods=['GET'])
def main():
    "bir return işlemi olsun"
    return jsonify({'durum':durum})

if __name__ == '__main__':
    "hani url den erişeceğimiz..."
    app.run(debug=True,host='localhost',port=9875)