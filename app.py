from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
import pandas as pd
import numpy as np
import warnings
from flask import Flask, request, render_template
import pickle
from sklearn import *
# from Model import scaler

from xgboost import XGBClassifier
warnings.filterwarnings("ignore")


test=pd.read_csv("test_lTY72QC.csv")
test = test.drop(["ID"], axis = 1)
test=test.apply(LabelEncoder().fit_transform)
filename = 'finalxgbmodel.sav'



app = Flask(__name__)

model = pickle.load(open(filename, 'rb'))

@app.route("/")
def main():
    return render_template("index2.html")

@app.route("/predict", methods = ["POST"])
def home():
    Age =int(request.form["age"])
    Gender = int(request.form["gender"])
    Income = int(request.form["income"])
    Balance = int(request.form["balance"])
    Vintage = int(request.form["vintage"])
    Transaction_Status = int(request.form["ts"])
    Product_Holdings = int(request.form["ph"])
    Credit_Card = int(request.form["ccard"])
    Credit_Category = int(request.form["ccategory"])             
    X = np.array([[Age,Gender, Income, Balance, Vintage, Transaction_Status, Product_Holdings,Credit_Card,Credit_Category]])
    X = X.reshape(1,-1)
    scaler = StandardScaler().fit(test)
    X = scaler.transform(X)    
    pred = model.predict(X)
    return render_template("index.html", data = pred)
  


if __name__ == "__main__":
    #app.run(debug = True, use_reloader = False)
    port = int(os.environ.get("PORT", 5000)) # <-----
    app.run(host='0.0.0.0', port=port)  
    
    

# scaler = StandardScaler().fit(test)
 # X = scaler.transform(test)   
#X = np.array([[29,0, 3, 1889, 2, 1, 1,1,0]])
##X = X.reshape(1,-1)
# X = scaler.transform(X)    
# pred = model.predict(X)
