from keras.models import Sequential,load_model
from keras.layers import Dense, Dropout, Activation
import keras
from keras.layers import Input, Dense
from keras.optimizers import SGD

from sklearn.impute import SimpleImputer as Imputer
import numpy as np
import pandas as pd

from flask import jsonify,Flask,request

"yaptıgımız işlem rest api de get işlemine göre yapılmakta..."

app=Flask(__name__)


app.route("/",methods=["GET"])
def api():
    # tahmini yapılacak veri
    #model=egit()
    # g0=request.args.get("g0")
    # g1=request.args.get("g1")
    # g2=request.args.get("g2")
    # g3=request.args.get("g3")
    # g4=request.args.get("g4")
    # g5=request.args.get("g5")
    # g6=request.args.get("g6")
    # g7=request.args.get("g7")
    # tahmin = np.array([g0, g1, g2, g3, g4, g5, g6, g7]).reshape(1, 8)
    # # tahmin edilecek öğrenilen verilere göre çıktı ver...
    return "merhaba" #jsonify({"kanser_durum_cikti":"merhaba"})

def egit():
    veri = pd.read_csv("breast-cancer-wisconsin.data")

    veri.replace('?', -99999, inplace=True)
    # veri.drop(['id'], axis=1)
    veriyeni = veri.drop(['1000025'], axis=1)

    imp = Imputer(missing_values=np.nan, strategy="mean")
    veriyeni = imp.fit_transform(veriyeni)

    giris = veriyeni[:, 0:8]
    cikis = veriyeni[:, 9]

    model = Sequential()
    """modelimizdir biz bu model üzerine eklemeler yapmaktayız her .add() dediğimiz de 
    hidden layerlarımız eklemenmektedir ancak"""
    model.add(Dense(256, input_dim=8))
    '''input_dim dediğmiz girişte ne kadar bilgimiz var ise onu belirtiyoruz 
        256 dediğimiz ise hidden layerlara bağlantı sayılarıdır...
        '''
    model.add(Activation("relu"))
    model.add(Dropout(0.5))
    """Activiation() fonksiyonları ise bizim hesaplama fonklarımızdır eğer ki bu nerual
        networklardan """
    model.add(Dense(256))
    model.add(Activation("relu"))
    model.add(Dropout(0.6))
    model.add(Dense(256))
    model.add(Activation("softmax"))
    # modelimizi oturt
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    # modelimizi eğit
    #model.fit(giris, cikis, nb_epoch=50, batch_size=32, validation_split=0.13)
    model.load_model("breast-cancer-wisconsin.data")

    return model

if __name__ == '__main__':
    #egit() # modeli eğitir.
    app.run(debug=True,host='0.0.0.0',port=9876)# serveri başlatır