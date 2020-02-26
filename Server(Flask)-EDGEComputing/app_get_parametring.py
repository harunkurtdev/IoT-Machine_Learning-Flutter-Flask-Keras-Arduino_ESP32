from flask import Flask,request,jsonify

""" Flask ı başlatmak için app e atıyoruz"""
app=Flask(__name__)

"""app.route diyerek url üzerinde ki istekleri yakalıyoruz"""
@app.route('/api',methods=['GET'])# methodumuzun ne oldugunu anlıyoruz
def api():
    jsonolustur={} #bir list map olusturduk json için
    jsonolustur['APİ']=str(request.args['APİ']) #url üzerinden get işlemi ile gelen parametreler
    return jsonify(jsonolustur)# json olarak geri döndürüyoruz

#ilgili sayfa için başlatıcı
if __name__ =='__main__':
    """app run diyerek flask ın çalışmasını başlatıyoruz localhost ve portumuzu giriyoruz"""
    app.run(debug=True,host='0.0.0.0',port=9874)